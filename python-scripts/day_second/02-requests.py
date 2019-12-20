import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

# jsonplaceholder.typecode.com

user_list = response.json()

# user_list [0]['name']

# print(response.json())

print(user_list[0]['name'])

post_response = requests.post('https://jsonplaceholder.typicode.com/users', {
    'name': 'Andy'
})

print(post_response.json())