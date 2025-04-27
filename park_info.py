import requests
import bs4
# import ssl
url = ('https://opendata.tycg.gov.tw/api/v1/dataset.api_access?rid=99a8b764-8407-4c00-9e6c-57dc8452ecce&format=json')
# ssl._create_default_https_context = ssl._create_unverified_context

results = requests.get(url,verify=False)
results = results.json()
# print(results)

for result in results:
    # print(result)
    print(f'{result['description']}:{result['faredescription']}')
