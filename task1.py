import requests
response=requests.get("https://jsonplaceholder.typicode.com/posts/")
# print(response)
class jsonPlaceHolder:
    def __init__(self,i,t):
        self.id=i
        self.title=t
    def jsonPlaceHodlerdetails(self):
        print(f"The id is {self.id} & title is {self.title}")
if response.status_code==200:
    data=response.json()
    # print(data)
    for i in data:
        id=i["id"]
        title=i["title"]
        abc=jsonPlaceHolder(id,title)
        abc.jsonPlaceHodlerdetails()