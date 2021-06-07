from requests import *
from json import *

r = get("https://economia.awesomeapi.com.br/json/all").json()
p = dumps(r, indent = 4)
print(p['BTC'])