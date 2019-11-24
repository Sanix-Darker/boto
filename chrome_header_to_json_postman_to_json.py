import json

to_threat = [{"key":"Origin","value":"https://www.leboncoin.fr","description":""},{"key":"Upgrade-Insecure-Requests","value":"1","description":""},{"key":"Content-Type","value":"application/x-www-form-urlencoded","description":""},{"key":"User-Agent","value":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36","description":""},{"key":"Sec-Fetch-User","value":"?1","description":""},{"key":"Accept","value":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3","description":""}]

result = {}
for t in to_threat:
    result[t["key"]] = t["value"]

print(json.dumps(result, indent=4, sort_keys=True))