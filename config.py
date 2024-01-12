import os

from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.environ.get('API_TOKEN')
USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')

SERVICE_HOST = 'mega-prod.ru'
VPN_PORT = '27799'
VPN_MANAGER_PORT = '2053'
TRIAL_PERIOD = 10
VPN_PUBLIC_KEY = 'Ah8ZBwEB2jT3SiaSuBV3U3p21_VuNS3WtcC4qNRZgAs'