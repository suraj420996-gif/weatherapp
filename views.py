from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    data = {}
    if request.method=="POST":
       city = request.POST.get("city")
       url = f"http://api.weatherapi.com/v1/current.json?key=d6e72d25920046efbfe91142252009&q={city}&aqi=yes"
       response = requests.get(url)
       if response.status_code == 200:
           home= response.json()
           data = {
                "city": home["location"][ "name"],
                "country":home["location"]["country"],
                "temp_c": home["current"]["temp_c"],
                "temp_f": home["current"]["temp_f"],
                "condition":home["current"]["condition"]["text"],
                "air_quality":home["current"]["air_quality"]["co"],
                "wind_degree":home["current"]["wind_degree"],
                "pressure_in":home["current"]["pressure_in"]
            }
       else:
          data = {"error": "City not found!"}
    return render(request, "home.html", {"data": data})

    
    return render(request, "home.html")