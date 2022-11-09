from django.conf import settings
import requests
import jwt
import re

def get_user_name_from_token(request):
    #return True, "configurator-service"
    user_name = request.META['user_name']
    if not user_name:
        return False
    return True, "configurator-service"
    return True,user_name

def check_special_characters(check_special_characters):
    check_special_characters = check_special_characters.replace(" ", "")
    return bool(re.match('^[a-zA-Z0-9]*$', check_special_characters))


