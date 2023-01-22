import requests
import requests
import os
import glob
import json

folder_path = './Job_Bulletins/'


for file_path in glob.glob(os.path.join(folder_path, '*.txt')):
    with open(file_path, 'r') as file:
        text = file.read()
        response = requests.get(f"http://localhost:8000/jobapi",params = {"text":text})
        if response.status_code == 200:
            result = response.json()["Result"]
            print(result)
        else:
            print(f"Request failed with status code {response.status_code}")


