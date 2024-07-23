import requests

r = requests.get("https://www.isepclub.com")
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)