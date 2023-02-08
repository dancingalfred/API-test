import requests

#choose link in your response depending on if you want to try the local api or the one online
link = "https://jobdescrimination.azurewebsites.net/jobapi/"
link2 = "http://localhost:8000/jobapi/"

#Insert you job advert as a string
text = ""


#Run the client, will return the result, status code or a crash msg
try:
    response = requests.get(f"{link}",params = {"text":text})
    if response.status_code == 200:
        result = response.json()["Result"]
        print(result)
    else:
        print(f"Request failed with status code {response.status_code}")
except:
    print("crash")