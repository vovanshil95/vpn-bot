import os

from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.environ.get('API_TOKEN')
USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')

SERVICE_HOST = '159.69.75.46'
VPN_PORT = '13425'
VPN_MANAGER_PORT = '64651'
SERVICE_PORT = 8000
TRIAL_PERIOD = 10
VPN_PUBLIC_KEY = '4fLXRHYmi2ue0q3AtulgOmDWuPMIw3jKaRmk5UD9axw'