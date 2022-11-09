from django.http import JsonResponse
from django.conf import settings
import requests

def fetch_token(token_type):
    try:
        host=settings.DIGITAL_TWINS_URLS[settings.PRODUCTION_TYPE]['dev_keycloak']
        client_id=settings.DIGITAL_TWINS_URLS[settings.PRODUCTION_TYPE]['client_id']
        client_secret=settings.DIGITAL_TWINS_URLS[settings.PRODUCTION_TYPE]['client_secret']
        grant_type=settings.DIGITAL_TWINS_URLS[settings.PRODUCTION_TYPE]['grant_type']
        username = settings.DIGITAL_TWINS_URLS[settings.PRODUCTION_TYPE]['username']
        password = settings.DIGITAL_TWINS_URLS[settings.PRODUCTION_TYPE]['password']
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        for x in range(int(settings.DIGITAL_TWIN_TOKEN_ITERATION)):
            if token_type=="access_token":
                payload = {
                        "grant_type":grant_type,
                        "client_id":client_id,
                        "username":username,
                        "password":password,
                        "client_secret":client_secret
                        }
            elif token_type=="refresh_token":
                payload = {
                            'grant_type': 'refresh_token',
                            'client_id': client_id,
                            'client_secret': client_secret,
                            'refresh_token': settings.DIGITAL_TWIN_REFRESH_TOKEN
                            }
            response_data = requests.post(host+"/auth/realms/enterprise/protocol/openid-connect/token",
                                    data=payload, headers=headers)
            if response_data.status_code == 200:
                break
            if response_data.status_code != 200:
                token_type="access_token"                      
        if response_data.status_code == 200:
            return True,response_data
        else:
            return False,response_data
    except Exception as e:
        return False,[]

def get_api_data(endpoint):
    try:
        host=settings.DIGITAL_TWINS_URLS[settings.PRODUCTION_TYPE]['host']
        host = host + endpoint
        apiHeaders={
                "Authorization":"Bearer "+settings.DIGITAL_TWIN_ACCESS_TOKEN,
                "Content-Type": "application/json"
                }        
        response_data = requests.get(url=host,headers=apiHeaders)
        return True,response_data
    except Exception as e:
        return False,[]  
