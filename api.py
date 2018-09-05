#WEB API'S
#ques1:
import requests
response=requests.get('https://api.forismatic.com/api/1.0/? method=getQuote&format =json& lang=en')
d=response.json()
print(d["quoteText"])

                      
