import requests
city_name="chennai"
api_key="7c00ea5e949cb91a732e1eb18799886c"
url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
response=requests.get(url)
if response.status_code == 200:
    data=response.json()
    print("wheather is ",data["weather"][0]["description"])
    print("current temparature is",data['main']['temp'])
    print("humidity",data["main"]["humidity"])