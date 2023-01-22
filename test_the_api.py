# import requests

# apiLink = "https://jobdescrimination.azurewebsites.net/jobapi"
# myText = "Hej på dig"

# def get_data(api,text):
#     response = requests.get(api,params={"text":text})


#     if response.status_code == 200:
#         print("sucessfully fetched the data")
#         response = response.json()
#         print(response)
#     else:
#         print(f"Hello person, there's a {response.status_code} error with your request")

# get_data(apiLink,myText)


import requests
import os
import glob
import json

apiLink = "http://127.0.0.1:8000/jobapi/{text}"



def get_data(api,text):
    #response = requests.get(api,params={"text":text})
    # response = requests.get(api.format(text=text))
    response = requests.get(api, params={'text':text})

    if response.status_code == 200:
        print("sucessfully fetched the data")
        response = json.loads(response.text)

        print(response)
    else:
        print(f"Hello person, there's a {response.status_code} error with your request")

#get_data(apiLink,myText)



folder_path = './Job_Bulletins/'


for file_path in glob.glob(os.path.join(folder_path, '*.txt')):
    with open(file_path, 'r') as file:
        myText = file.read()
        get_data(apiLink, myText)
