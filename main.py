import requests
import json
import pandas as pd

def azureml_main(dataframe1 = None, dataframe2 = None):
     bing_key = "Av1VsBty8uPUxZbGda-gDgDAgWWJeaNQNDuXwLKKe6dXCh49sVKQPLMN27yXpty2"
     bing_out = "json"
     bing_url = "http://dev.virtualearth.net/REST/v1/Locations"
     latitude = []
     longitude = []
     for address in dataframe1["ADDRESS"]:
         url = bing_url + "?key=" + bing_key + "&o=" + bing_out + "&q=" + address
         req = requests.get(url)
         if req.status_code == 200:
             resp = json.loads(req.text)
             latitude.append(resp['resourceSets'][0]['resources'][0]['point']['coordinates'][0])
             longitude.append(resp['resourceSets'][0]['resources'][0]['point']['coordinates'][1])
             
     dataframe1["LATITUDE"] = latitude
     dataframe1["LONGITUDE"] = longitude
     return dataframe1