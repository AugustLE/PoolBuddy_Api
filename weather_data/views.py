from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import City, Forecast
from rest_framework import status, permissions
from django.http import HttpResponse
import requests
import xmltodict, json




def met(request, city):
    '''
    Retrive MET API weathercast for a spesifiv latlong

    Arguments: 
        lat: float; latitude coordinate 
        long: float; longitude coordinate 
    '''

    lat, long = city_to_latlong(city)
    # get MET API xml
    res = requests.get(
        f'https://api.met.no/weatherapi/locationforecastlts/1.3/?lat={lat}&lon={long}')
    # convert xml to json
    o = xml_to_dict(res.text)
    city = save_city(city)
    time_list = o["weatherdata"]["product"]["time"]
    for obj in time_list:
        try:
            save_temperature(obj, city)
        except:
            pass
    
    # dump to readable string
    user_response = json.dumps(time_list)

    return HttpResponse(user_response)

def xml_to_dict(xml):
    '''
    Convert xml to json dictinary 

    Arguments: 
        xml: str; xml string
    '''
    return xmltodict.parse(xml)

def save_city(city):
    ''' 
    Save city to database
        Arguments: 
            obj: json; obj containing forecast features
    '''
    obj, created = City.objects.get_or_create(
                        city_name = city)

    return obj

def save_temperature(obj, city):
    ''' 
    Save temperature reading to database
        Arguments: 
            lat: float; latitude coordinate 
            long: float; longitude coordinate 
    '''
    if "temperature" in obj["location"]:
        obj, created = Forecast.objects.get_or_create(city = city, 
                        temp_from = obj["@from"],
                        temp_to = obj["@to"],
                        temperature = obj["location"]["temperature"]["@value"],
                        windDirection = obj["location"]["windDirection"]["@deg"],
                        windSpeed = obj["location"]["windSpeed"]["@mps"],
                        humidity = obj["location"]["humidity"]["@value"],
                        pressure = obj["location"]["pressure"]["@value"],
                        cloudiness = obj["location"]["cloudiness"]["@percent"],
                        fog = obj["location"]["fog"]["@percent"],
                        lowClouds = obj["location"]["lowClouds"]["@percent"],
                        mediumClouds = obj["location"]["mediumClouds"]["@percent"],
                        highClouds = obj["location"]["highClouds"]["@percent"],
                        dewpointTemperature = obj["location"]["dewpointTemperature"]["@value"]
            )
        # removed the following because it is only in some api calls:
        #  windGust = obj["location"]["windGust"]["@mps"],
        #  areaMaxWindSpeed = obj["location"]["areaMaxWindSpeed"]["@mps"],
        


city_to_latlong_dict ={
    "sb": {
        "lat": 34.42,
        "long": -119.69
    },
    "hive": {
        "lat": 34.415088,
        "long": -119.861335
    },
}


def city_to_latlong(city):
    lat = city_to_latlong_dict[city]["lat"]
    long = city_to_latlong_dict[city]["long"]
    return lat, long