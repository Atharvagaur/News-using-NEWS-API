# Using request module to get news
import requests
APIKEY="Enter your api key"
url="Enter the website used for getting the news"
a=input("Enter the country for news:")
b=input("Enter the type of news:")
print("")
print("")
# Getting specific news form the news api
d={}
d["country"]=a
d["category"]=b
d["apikey"]=APIKEY


# Getting the news
a=requests.get(url,d)
# Using json module to get data from the web application
data=a.json()
cnt=1
if data['status'] == 'ok':
    print(f"Top News Headlines of {a}:")
    # Displayinig in an organised format using for loop
    for articles in data['articles']:
        print(f"NEWS {cnt}")
        print(f"Title: {articles['title']}\n")
        print(f"Source: {articles['source']['name']}\n")
        # print(f"Published At: {articles['publishedAt']}\n")
        # print(f"URL: {articles['url']}\n")
        cnt+=1
else:
    print("Error Occured")