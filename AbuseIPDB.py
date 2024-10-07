import requests # web istekleri yapmak ve API ile iletisimi kurabilmek icin gerekli
import json # gelen datalari json'a cevirmek icin
import pandas # csv dosyalari okumak icin
import csv # json formatinda gelen verileri dictionary'ye cevirip ardindan csv dosyasina yerlestirmek icin

dosya_yolu = str(input('Lutfen taramk istediginiz IP listesisi buluna dosyanin yolunu yaziniz (dosya CSV dosyasi olmali ve IP adli sutunu icermeli): ')) # taramak istedigimiz verilerin dosya yolu
IP_CSV = pandas.read_csv((dosya_yolu)) # yolu verilen dosyanin verisini cekip okuyacak

ip = IP_CSV['IP'].tolist() #  IP sutundan okudugu verileri pandas series python listesine cevirerek ve bu ip parametresine yazacak

API_KEY = '133ca269d3b4447b7123f31bdf2370e319bc765d744f7c3fd2a79cf4648031a02d7ebddb82fb3603' # abuseipdb sitesinden API anahtarimiz
url = 'https://api.abuseipdb.com/api/v2/check'  # api'mizi calistirmak icin baglanti kuracagimiz url baglantisi

csv_sutunlari = ['ipAddress','isPublic','ipVersion','isWhitelisted','abuseConfidenceScore','countryCode','countryName',
               'usageType','isp','domain','hostnames','isTor','totalReports','numDistinctUsers','lastReportedAt']
                # bu parametrede json formatinda gelen verilerin header'leri bulunur ve bu header'ler csv dosyanin header'leri olacak

headers = {
            'Accept': 'application/json', # yukarida verdigimiz anahtarimizla calisacagimizi ve cekilecek veriler json formatinda alacagimizi belirtiyoruz cunku gelecek veriler json'dan farkli formatta gelebilir (XML, plain text, vs.) gibi
            'Key': API_KEY # istege dogrulama yapilmasi gerekli oldugu icin yukarida verdigimiz kendi API anahtarimizi veriyoruz
          } # bu da sozluk sayilir (dictionary) , icinde de hem value hem de anahtar bulunur

with open("AbuseIP_results.csv","a",newline='') as dosyacsv: # with parametresi, acilan dosyadan isimiz bittiginde kapatacak. "w" parametresi yazilan verinin ustunde yazarken "a" parametresi en son satirdan sonra yazmaya baslar ve eger ki dosya yoksa olusturacak. newline='' ifadesi CSV dosyalarina ozeldir,yazilan satir sonrasinda bos satir yazmasini engeller. dosyacsv parametresi AbuseIP_results dosyasina isaretci olarak yerine gececek
    SutunDoldurma = csv.DictWriter(dosyacsv, fieldnames=csv_sutunlari) # csv.DictWriter CSV kutuphanesinin bir fonk. olup dosyacsv sutunlerin basliklari csv_columns dosyasindan cekecek
    if  dosyacsv.tell() == 0: # dosya ilk defa calistiriliyorsa sutunlarin basliklari yazacak,bu da sutun basliklarin tekrari onlemek icin
        SutunDoldurma.writeheader()  # sutunlerin basliklari basliklara yazacak

for i in ip:
    parameteres = {
                    'ipAddress' : i,
                    'EnSonBildiri' : '90'
                  }
    yanit = requests.get(url=url,headers=headers,params=parameteres) #istek icin, url, API_KEY, data formatini ve parametreleri belirledik
    json_data = json.loads(yanit.content) # json.loads, json kutuphanesinin bir fonk. olup respnse ile gelen json formatinda veriyi python objesine (python dictionary)'ye donusturur
    json_main = json_data["data"] # python formatindaki json_data parametresine bulunan data paramtresine cagirdik

    with open("AbuseIP_results.csv","a",newline='') as dosyacsv:
        SutunDoldurma = csv.DictWriter(dosyacsv,fieldnames=csv_sutunlari)
        SutunDoldurma.writerow(json_main)
