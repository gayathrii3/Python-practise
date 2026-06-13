import requests

url = "https://dog.ceo/api/breed/pug/images/random"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("Breed: pug")
    print("Image URL:", data["message"])

else:
    print(f"Failed to retrieve data: {response.status_code}")