import requests
test = ['https://img2.10bestmedia.com/Images/Photos/352450/GettyImages-913753556_55_660x440.jpg',
'https://img2.10bestmedia.com/Images/Photos/352450/GettyImages-913753556_55_660x440.jpg']
for download in test:
    r = requests.get(download)

    if r.status_code == 200:
        with open('test.jpg', 'wb') as f:
            f.write(r.content)
    else:
        print('Some failure')
