import requests
from sqlalchemy.dialects.mssql.information_schema import views

BASE = "http://127.0.0.1:5000/"
#
# data = [{"likes":100, "name":"API Olusturma", "views":10000},
#         {"likes":135, "name":"python ogren", "views":5000},
#         {"likes":10, "name":"REST Flask", "views":400}]
# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i),data[i])
#     print(response.json())

# response = requests.get(BASE + "video/2")
# response = requests.get(BASE + "video/6")
response = requests.patch(BASE + "video/2",{"views":99,"likes":101})
print(response.json())
