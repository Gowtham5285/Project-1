import requests
apiUrl="https://fakestoreapi.in/api/products"
response=requests.get(apiUrl)
if response.status_code == 200:
    content = response.json()
    # print(type(content))
    print(content)
    # for i in content:
    #     if i["category"] == "electronics":
    #         print(i["title"])