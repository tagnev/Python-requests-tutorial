import requests

GOOGLE_API_KEY = 'YOUR API KEY'


def extract_lat_lon(address_or_zip_code):

    # https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY

    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    # key = GOOGLE_API_KEY
    payload = {'address':address_or_zip_code, 'key':GOOGLE_API_KEY}
    r = requests.get(url, params=payload)
    if r.status_code not in range(200, 299):
        return 'Some Failrue'
    try:
        result = r.json()['results'][0]
        lat = result['geometry']['location']['lat']
        lng = result['geometry']['location']['lng']
    except:
        pass
    return lat, lng


