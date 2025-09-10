import requests
apiUrl="https://dummyjson.com/products"
response=requests.get(apiUrl)
if response.status_code == 200:
    content=response.json()
    # print(content)
    # print(type(content))
    mainData=content["products"]
    # print(mainData)
    for i in mainData:
        if i["rating"]>4.0:
            print(i["rating"])