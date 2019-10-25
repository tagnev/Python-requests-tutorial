import requests

headers = {'Authorization': 'Basic cG9zdG1hbjpwYXNzd29yZA=='}

# r = requests.get('https://postman-echo.com/basic-auth', headers=headers)
# payload = {'foo1':'bar1',"foo2":'bar2'}

files = {'files':open('tetsing_file.txt','rb')}
r = requests.post('https://postman-echo.com/post',files=files)

print(r.text)
