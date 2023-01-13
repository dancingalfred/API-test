import requests

apiLink = "https://jobdescrimination.azurewebsites.net/jobapi"
myText = "Hej på dig"

def get_data(api,text):
    response = requests.get(api,params={"text":text})


    if response.status_code == 200:
        print("sucessfully fetched the data")
        response = response.json()
        print(response)
    else:
        print(f"Hello person, there's a {response.status_code} error with your request")

get_data(apiLink,myText)



