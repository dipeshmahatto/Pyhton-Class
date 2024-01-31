import requests
# api_url = "https://api.adviceslip.com/advice"
# response=requests.get(api_url)
# if (response.status_code==200):
#     data = response.json()
#     print(data['slip']['advice'])

api_url = "https://catfact.ninja/fact"
response=requests.get(api_url)
if (response.status_code==200):
    data = response.json()
    print(data['fact'])
