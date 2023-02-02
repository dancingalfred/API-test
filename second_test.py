import requests
import os
import glob

folder_path = './Job_Bulletins/'

link = "https://jobdescrimination.azurewebsites.net/jobapi/"
link2 = "http://localhost:8000/jobapi/"

results = []
for file_path in glob.glob(os.path.join(folder_path, '*.txt')):
    with open(file_path, 'r') as file:
        text = file.read()
        try:
            response = requests.get(f"{link}",params = {"text":text})
            if response.status_code == 200:
                result = response.json()["Result"]
                print(result)
                if result not in results:
                    results.append(result)
                else:
                    continue
            else:
                print(f"Request failed with status code {response.status_code}")
        except:
            print("crash")
    
    
print(results)
