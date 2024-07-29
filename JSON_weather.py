import json, requests
"""
معرفة الطقس حاليا عن طريق اتلاي بي اي
"""
#تجهيز الرابط
api_key = "###############################"
# الصيغة "https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}"
url1 = "https://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name: ")
# &units-metric لكي يطلع بيانات بالنظام المتري
complete_url = url1 + "q=" + city_name + "&units-metric" + "&appid=" + api_key
#احضار البيانات من الموقع
Data = requests.get(complete_url)
#يحول لجيسون
#البيانات الي من الموقع مخصصة لتكون جيسون
x = json.loads(Data.text)

if x["cod"] != "404":
    y = x["main"]
    temp = y["temp"]
    pressure = y["pressure"]
    humidity = y["humidity"]
    z = x["weather"]
    weather_desc = z[0]["description"]
    #حرارة بالكلفن
    print("Temperature (in metric unit) = " + str(temp))
    print("atmospheric pressure (in metric unit) = " + str(pressure))
    #بالمئة
    print("humidity (in metric) = " + str(humidity))
    print("description = " + str(weather_desc))
else:
    print("City Not Found")