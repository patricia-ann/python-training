# REQUESTS
# In order to interact with data and files from a website, we need to send http requests using a given API url
# In Python, we can use requests library to send HTTP requests easily.
#
# In this Tutorial, we'll use public apis from https://thedogapi.com/ to use http methods to send requests to download an image
# of a particular dog breed using GET method, mark a particular dog image as one of the favourites using POST method and also try
# removing a previously marked favourite image from the list of favourites using DELETE method.
#
# For an overview of the various HTTP request methods refer to this link: https://www.w3schools.in/http-tutorial/http-request-methods/
#
# Pre-Requisites:
# 1. Install the requests package using - pip install requests
# 2. Import the requests package
# 3. Sign up on https://thedogapi.com/signup to get an API Key
# Note that in here, we are referring to this api documentation -> https://docs.thedogapi.com/
#
# References:
# https://www.w3schools.in/http-tutorial/http-request-methods/
# https://realpython.com/python-requests/
# https://docs.thedogapi.com/

import requests
import os
os.system('cls')

# Assign the header part on variable
# This will be used for Authentication
headers = {'x-api-key': '9eb2efa2-c0ca-469a-9db8-bee4ee8fd3d6'}

# Using GET method and query parameter 'q' on breeds api, we are searching for an image for a 'Pug' breed
response = requests.get(
    'https://api.thedogapi.com/v1/breeds/search?q=Pug', headers=headers)


if response.status_code == 200:
    # Inspect the Content-Type of the response, in this case it is json
    print(response.headers['Content-Type'])
    # Fetch the response as json object
    dog = response.json()
    # Parse the json response, get the first array and get the reference_image_id key to be used later for downloading the image.
    image_id = dog[0]['reference_image_id']
    # Using GET method on images api to search the image url
    image_search = requests.get(
        f"https://api.thedogapi.com/v1/images/{image_id}", headers=headers).json()

    if image_search:
        # Using GET method, we'll download the image using the image url
        dog_image = requests.get(image_search['url'])

        # Since the dog_image response is in bytes,
        # Now we will save the downloaded file as dog.jpg
        # wb means we're able to write bytes data on file
        with open("dog.jpg", 'wb') as f:
            f.write(dog_image.content)
    else:
        print("Image not found!")

    print("Successful")
else:
    print("Failed to connect")

# POST
# Using post method, we mark a dog image as favourite
response = requests.get('https://api.thedogapi.com/v1/favourites',
                        headers=headers)
print(response.json())

body = {
    "image_id": image_id,
    "sub_id": "my-sub-id"
}

response = requests.post('https://api.thedogapi.com/v1/favourites',
                         headers=headers, json=body)
print(response)

# DELETE
# Using delete method, we remove a record as one of our favourites
response = requests.delete('https://api.thedogapi.com/v1/favourites/9094',
                           headers=headers)
print(response)
