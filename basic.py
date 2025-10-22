import requests

endpoint = "https://jsonplaceholder.typicode.com/posts"
#endpoint = "https://openweathermap.org/api"

get_response = requests.get(endpoint)

data =get_response.json() 
print(data[:2])
