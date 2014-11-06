import urllib
from xml.dom import minidom

wurl = 'http://xml.weather.yahoo.com/forecastrss?p=%s'
wser = 'http://xml.weather.yahoo.com/ns/rss/1.0'

def weather_for_zip(zip_code):
    url = wurl % zip_code +'&u=c'
    dom = minidom.parse(urllib.urlopen(url))
    forecasts = []
    for node in dom.getElementsByTagNameNS(wser, 'forecast'):
        forecasts.append({
            'date': node.getAttribute('date'),
            'low': node.getAttribute('low'),
            'high': node.getAttribute('high'),
            'condition': node.getAttribute('text')
        })
    ycondition = dom.getElementsByTagNameNS(wser, 'condition')[0]
    return {
        'current_condition': ycondition.getAttribute('text'),
        'current_temp': ycondition.getAttribute('temp'),
        'forecasts': forecasts ,
        'title': dom.getElementsByTagName('title')[0].firstChild.data
    }

def make_http_request_with_temp(data):
	import httplib
	conn = httplib.HTTPConnection("10.1.1.19", 80)
	conn.request("GET", "http://www.python.org/index.html", headers={'temp':data})

def main():
    a=weather_for_zip("USCT0135")
    print a['current_temp']
    make_http_request_with_temp(a['current_temp'])


main()
