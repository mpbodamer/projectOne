import json
import requests
import csv
import pandas as pd
from citipy import citipy
from pprint import pprint

def findDistrict(lat, lng, googleApiKey): #Outputs a district name in the form of a string.
    endpointURL = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={googleApiKey}"
    try:
        response = requests.get(endpointURL).json()
        addressComponents = response["results"][0]['address_components']
        for i in range(len(addressComponents)):
            if (addressComponents[i]['types'][0] == 'neighborhood'):
                return addressComponents[i]['long_name']
    except (KeyError, ValueError):
        print("KeyError or ValueError occured, district name was not retrivable.")
    return "null"

def districtDataframe(df, googleApiKey):
    latitude = df['latitude'].tolist()
    longitude = df['longitude'].tolist()
    district = []
    for i in range(len(latitude)):
        district.append(findDistrict(latitude[i], longitude[i], googleApiKey))
    df['district'] = district
    pprint(df)
    return df

def citipyDistrict(df):
    latitude = df['latitude'].tolist()
    longitude = df['longitude'].tolist()
    district = []
    for i in range(len(latitude)):
        city = citipy.nearest_city(latitude[i],longitude[i])
        district.append(city.city_name)
    df['district'] = district
    pprint(df)
    return df

def updateCsvDistrict(csvPath, newFileName):
    newCSV = citipyDistrict(pd.read_csv(csvpath))
    newCSV.to_csv(f"{newFileName}.csv")
    
def districtCoords(districtName):
    districtList = {
        'los angeles' : {
            'districtLat' : 34.0522 ,
            'districtLng' : -118.2437
        },
        'west hollywood' : {
            'districtLat' : 34.0900 ,
            'districtLng' : -118.3617
        },
        'beverly hills' : {
            'districtLat' : 34.0736 ,
            'districtLng' : -118.4004
        },
        'santa monica' : {
            'districtLat' : 34.0195 ,
            'districtLng' : -118.4912
        },
        'san fernando' : {
            'districtLat' : 34.2819 ,
            'districtLng' : -118.4390
        },
        'culver city' : {
            'districtLat' : 34.0211 ,
            'districtLng' : -118.3965
        },
        'glendale' : {
            'districtLat' : 34.1425 ,
            'districtLng' : -118.2551
        },
        'burbank' : {
            'districtLat' : 34.1808 ,
            'districtLng' : -118.3090
        },
        'calabasas' : {
            'districtLat' : 34.1367 ,
            'districtLng' : -118.6615
        },
        'westmont' : {
            'districtLat' : 41.7959 ,
            'districtLng' : -118.3047
        },
        'inglewood' : {
            'districtLat' : 33.9617 ,
            'districtLng' : -118.3531
        },
        'lomita' : {
            'districtLat' : 33.7922 ,
            'districtLng' : -118.3151
        },
        'south pasadena' : {
            'districtLat' : 34.1161 ,
            'districtLng' : -118.1503
        },
        'el segundo' : {
            'districtLat' : 33.9192 ,
            'districtLng' : -118.4165
        },
        'east los angeles' : {
            'districtLat' : 34.0224 ,
            'districtLng' : -118.1670
        },
        'willowbrook' : {
            'districtLat' : 33.9170 ,
            'districtLng' : -118.2551
        },
        'west carson' : {
            'districtLat' : 33.8217 ,
            'districtLng' : -118.2926
        },
        'walnut park' : {
            'districtLat' : 33.9689 ,
            'districtLng' : -118.2224
        },
        'lennox' : {
            'districtLat' : 33.9381 ,
            'districtLng' : -118.3526
        },
        'west athens' : {
            'districtLat' : 33.9240 ,
            'districtLng' : -118.3004
        },
        'lynwood' : {
            'districtLat' : 33.9303 ,
            'districtLng' : -118.2115
        },
        'gardena' : {
            'districtLat' : 33.8883 ,
            'districtLng' : -118.3090
        },
        'carson' : {
            'districtLat' : 33.8317 ,
            'districtLng' : -118.2817
        },
        'monterey park' : {
            'districtLat' : 34.0625 ,
            'districtLng' : -118.1228
        },
        'south gate' : {
            'districtLat' : 33.9547 ,
            'districtLng' : -118.2120
        },
        'long beach' : {
            'districtLat' : 33.7701 ,
            'districtLng' : -118.1937
        },
        'pasadena' : {
            'districtLat' : 34.1478 ,
            'districtLng' : -118.1445
        },
        'santa clarita' : {
            'districtLat' : 34.3917 ,
            'districtLng' : -118.5426
        },
        'rancho palos verdes' : {
            'districtLat' : 33.7445 ,
            'districtLng' : -118.3870
        },
        'alhambra' : {
            'districtLat' : 34.0953 ,
            'districtLng' : -118.1270
        },
        'maywood' : {
            'districtLat' : 33.9867 ,
            'districtLng' : -118.1853
        }
    }
    
    lat = districtList[districtName]['districtLat']
    lng = districtList[districtName]['districtLng']
    return lat, lng