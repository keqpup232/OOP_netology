import requests
from datetime import date
from datetime import timedelta
from pprint import pprint

two_days = date.today()-timedelta(1)
current_date = date.today()+timedelta(1)

i = 1
while i>0:
    resp = requests.get("https://api.stackexchange.com/2.3/questions",
                       params={
                           "tagged":"python",
                           "min":two_days,
                           "max":current_date,
                           "site":"ru.stackoverflow",
                           "sort":"creation",
                           "pagesize":100,
                           "page":i
                           }
                       )
    print(resp.text) 
    resp.raise_for_status()
    result=resp.json()["items"]
    for title in result:
        print(title["title"])
    i=i+1
    











