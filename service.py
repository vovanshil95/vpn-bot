import base64
import string
import uuid
import random

import requests

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, Response
from ua_parser import user_agent_parser

from config import SERVICE_HOST, USERNAME, PASSWORD, VPN_PORT, TRIAL_PERIOD, VPN_MANAGER_PORT, VPN_PUBLIC_KEY

app = FastAPI()

@app.get("/app", response_class=RedirectResponse, status_code=301)
async def get_app(request: Request):
    device_brand = user_agent_parser.Parse(request.headers.get('User-Agent'))['device']['brand']
    if 'Apple' in device_brand:
        return 'https://apps.apple.com/us/app/streisand/id6450534064'
    else:
        return 'https://play.google.com/store/apps/details?id=com.v2ray.ang'

@app.get("/config/{chat_id}", response_class=RedirectResponse, status_code=301)
async def get_app(request: Request, chat_id: int):

    device_brand = user_agent_parser.Parse(request.headers.get('User-Agent'))['device']['brand']

    if 'Apple' in device_brand:

        return f'streisand://import/https://{SERVICE_HOST}/download/{chat_id} #fast vpn'
    else:
        return f'v2rayng://install-config?url=https://{SERVICE_HOST}/download/{chat_id}'

@app.get('/download/{chat_id}')
async def download_config(chat_id: str):
    chat_id = int(chat_id[:-1])

    # if chat_id is not in ids:
    #     return 403

    creds = {"username": USERNAME,
             "password": PASSWORD}

    login_resp = requests.post(f'http://{SERVICE_HOST}:{VPN_MANAGER_PORT}/login',
                         headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0'},
                         json=creds)

    session = login_resp.cookies['session']
    cookies = {'session': session}

    user_id = str(uuid.uuid4())
    sub_id = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(16))

    requests.post(f'http://{SERVICE_HOST}:{VPN_MANAGER_PORT}/panel/inbound/addClient',
                  cookies=cookies,
                  json={
                      "id": 1,
                      "settings": f"{{\"clients\": [{{\n  \"id\": \"{user_id}\",\n  \"flow\": \"xtls-rprx-vision\",\n  \"email\": \"{chat_id}\",\n  \"limitIp\": 0,\n  \"totalGB\": 0,\n  \"expiryTime\": {-24 * 3600 * 1000 * TRIAL_PERIOD},\n  \"enable\": true,\n  \"tgId\": \"\",\n  \"subId\": \"{sub_id}\",\n  \"reset\": 0\n}}]}}"
                  })

    config = f'vless://{user_id}@{SERVICE_HOST}:{VPN_PORT}?type=tcp&security=reality&pbk={VPN_PUBLIC_KEY}&fp=firefox&sni=google.com&sid=47edc4d9&spx=%2F&flow=xtls-rprx-vision#{chat_id}'

    return Response(base64.b64encode(config.encode('utf-8')))
