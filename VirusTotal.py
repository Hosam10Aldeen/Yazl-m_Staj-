import requests
import json
import base64
import time

Siteler = [
    "https://www.hepsiburada.com/",
    "http://117.206.73.53:34129/Mozi.m",  # zararliiiiii
    "http://117.235.114.251:58197/bin.sh",  # zararliiiiii
    "https://app.letsdefend.io/homepage",
    "https://www.crowdwave.com/",
    "http://mogagrocol.ru/wp-content/plugins/akismet/fv/index.php?email=ellie@letsdefend.io"  # zararliiiiii
]

api_key = 'e6c020c613da1bb37249e79e7fd9f1ac1e14bfef209d33610ca8485b65317665'

url = "https://www.virustotal.com/api/v3/urls/"

headers = {
    'x-apikey': api_key
}

for site in Siteler:
    # taranmak istenilen url'lerin VirusTotal base64 encode edilmesini şart koyduğu için bütün url'lerimize encode yapıyoruz
    encoded_url = base64.urlsafe_b64encode(site.encode()).decode().strip('=')

    # rl tamamı için verdiğimiz url sonrasında encode url'ı de ekleriz sonunda, bunun için de f parametresi kullandım
    api_url = f"{url}{encoded_url}"

    response = requests.get(api_url, headers=headers)

    # eğer isteğe gelen yanıt 200 (başarılı ise)
    if response.status_code == 200:
        response_json = response.json()
        # çıkarmak istediğimiz parametreleri tanımladım (veri,özelliği ve son tarama tarihi)
        analiz_istatistikleri = response_json['data']['attributes']['last_analysis_stats']
        if analiz_istatistikleri['malicious'] <= 0:
            with open('vt_sonuc.txt', 'a') as vt:
                vt.write(f"{site} - Zararlı Değil\n")
        else:
            with open('vt_sonuc.txt', 'a') as vt:
                vt.write(f"{site} - Zararlı\n")
    else:
        print(f"Error: bu site için veri alınamadı {site}, status code: {response.status_code}")

    time.sleep(15) #virustotal sitesi 1 dakika icinde 4 istekten fazla engellemesi sebebiyle butun verdigimiz url'lere tarama yapabilmemiz icin 60/4= 15 s yani her 15 saniye bir istek atarsak butun url'leri tarayabiliriz
