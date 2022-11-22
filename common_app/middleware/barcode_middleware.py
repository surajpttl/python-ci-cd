import json

from django.utils.deprecation import MiddlewareMixin
import jwt
from django.http import JsonResponse
from datetime import datetime

class CheckUserSession(MiddlewareMixin):

    def process_request(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        #return self.get_response(request)
        if "digital_twin" not in request.path:
            if request.headers.get('Authorization')==None:
                return send_response("Token not found testing in docker ")
            if request.headers.get('Authorization'):
                auth_type, auth = request.headers.get('Authorization').split(' ', 1)
                if not auth_type.lower() == 'bearer':
                    return send_response("Your authorization type is not matching")
                user_data = jwt.decode(auth, options={"verify_signature": False})
                user_session_time = datetime.fromtimestamp(user_data.get("exp"))
                current_time  = datetime.now()
                difference = user_session_time - current_time
                if difference.total_seconds() <= 0:
                    return send_response("Your session has been expired...!")
                else:
                    request.META['user_name']=user_data.get("preferred_username")
        response = self.get_response(request)
        return response
def send_response(message):
        return JsonResponse({
                    "STATUS": False,
                    "RESPONSE":
                        {
                            "STATUS_CODE": 401,
                            "MESSAGE": message,
                            "DATA": []
                        }
                },status=401)
