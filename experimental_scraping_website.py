from time import sleep
import requests
import json
import sys
import uuid
from bs4 import BeautifulSoup

# I got these from sniffing api request by making my computer a MITM proxy for the mobile app
MID = '8955034345447357862108201902748063122'
MCORGID = 'AF963DE55A38EC390A495CD5@AdobeOrg'

def generate_headers():
        config_js = requests.get('https://ikonpass.com/js/config.js')
        with open('output.txt', 'w') as f:
	        if config_js.status_code == requests.codes.ok:
	        	print(config_js.text)
	        	soup = BeautifulSoup(config_js.text, 'html.parser')
	        	f.write(soup.prettify())
        #     modded = config_js.text[config_js.text.index("API_KEY"):]
        #     API_KEY = modded[modded.index(':') + 1:modded.index(',')].strip('"')
        # else:
        #     print("Couldn't get API_KEY")
        #     sys.exit(1)

        # USER_EXPERIENCE_KEY = str(uuid.uuid1()).upper()
        # # Pulled from proxying the Southwest iOS App
        # return {'Host': 'mobile.southwest.com', 'Content-Type': 'application/json', 'X-API-Key': API_KEY, 'X-User-Experience-Id': USER_EXPERIENCE_KEY, 'Accept': '*/*', 'X-Channel-ID': 'MWEB'}

print(generate_headers())