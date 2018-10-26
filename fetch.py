import urllib
import urllib.request
# If you are using Python 3+, import urllib instead of urllib

import json 


data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["ADDRESS", "TYPE"],
                    "Values": [   ["48th Street, East, New York, NY","RELIEF-CENTER"],
                                    ["43rd Street, West, New York, NY","RELIEF-CENTER"],
                                    ["52nd Street, East, New York, NY","RELIEF-CENTER"],
                                    ["44th Street, West, New York, NY","RELIEF-CENTER"], 
                                    ["54th Street, East, New York, NY","RELIEF-CENTER"],
                                    ["37th Street, West, New York, NY","RELIEF-CENTER"],
                                    ["47th Street, West, New York, NY","RELIEF-CENTER"],
                                    ["46th Street, East, New York, NY","RELIEF-CENTER"], 
                                    ["67th Street, East, New York, NY","RELIEF-CENTER"],
                                    ["26th Street, East, New York, NY","RELIEF-CENTER"],
                                    ["25th Street, East, New York, NY","RESOURCE-BASE"],
                                    ["13th Street, East, New York, NY","RESOURCE-BASE"] ]
                },        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/7b29ce0246cc4317be6de8371704b609/services/b09f2a519dab4d06a73dda0aac017726/execute?api-version=2.0&details=true'
api_key = 'RO+Dj+iBZx/p2NTx+bBc8DsZHDWDdsAROk4LWkW2onKLbfNjA+77t2SU5sHY4fzkVfdEfKpsyTPw2gtnJUXQew=='
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

# req = urllib.Request(url, body, headers) 
req = urllib.request.Request(url, body, headers) 
try:
    # response = urllib.urlopen(req)
    response = urllib.request.urlopen(req)

    # If you are using Python 3+, replace urllib with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers) 
    # response = urllib.request.urlopen(req)

    result = response.read()
    parsed_json = json.loads(result)
    # print the final output
    print(json.dumps(parsed_json, indent = 4,sort_keys=False))
except urllib.request.HTTPError :
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))                 