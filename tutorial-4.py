import requests

url = 'https://httpbin.org/cookies/set'

jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')

r = requests.get(url, cookies=jar)

print(r.text)

