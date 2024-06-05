import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

response1 = response.status_code

if response1 == 200:
    print("yes, we are in")
else:
    print("Response not okay, please recheck your api")

longitude = response.json()["iss_position"]["longitude"]
longitude

latitude = response.json()["iss_position"]["latitude"]
latitude

iss_position = (f"The position of the current satelite is longitude of: {longitude} and latitude of: {latitude}")

iss_position
