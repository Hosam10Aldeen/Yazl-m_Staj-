# stackoverflow
import requests
import json

response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
# print(response) # attığımız istek yanıtı görebilmek için
# print(response.json()) # yanıtın verisiyle görmek için
# print(response.json()['items']) # item'leri (öğeleri) almak için

for question in response.json()['items']:
    if question['answer_count'] == 0 :  # sadece cevaplanmayan soruları görebilmemiz için
        print(question['title']) # cevaplanmayan sorunun başlığını yazdır
        print(question['link']) # cevaplanmayan sorunun linkini de yazdır
    else:
        print("Answered")
    print()


# Kendi API’mi kurabilmek için flask framework’u kullandım
from flask import Flask, render_template

app = Flask(__name__) #serveri calistiracak

@app.route("/") # ilk rotamizi yaptik(ana sayfa rotasi)
def home():
    #return "<h1>Home Page, Welcome from flask</h1>"
    return render_template('home.html')
@app.route("/about/") #burada 2.rotamizi yaptik (about sayfasi)
def about(): #sayfa ve fonksiyon ayni ada sahip olmasina gerek yok
    return "About me Page"

@app.route("/dashboard/")
def dashboard():
    return "Dashboard Page"
app.run(debug=True) #bunu yazdigimizda kodda herhangi bir degisiklik yaptigimizda bunun yansimasi icin serveri kapatip yine kaldirmadan sadace sayfaya yenileme yaparak degisiklikler sayfaya yansar,bu secenek de sadece gelistirme ve test etme sirasina kullanilir, yayinladigimizda kesinlikle false olamli

