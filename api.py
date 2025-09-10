import requests

# Example 1: GET request
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())

# # Example 2: POST request
# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     "title": "My First Post",
#     "body": "This is a test post using requests library.",
#     "userId": 1
# }

# response = requests.post(url, json=data)

# print("\nStatus Code:", response.status_code)
# print("Response JSON:", response.json())
