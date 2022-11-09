from django.http import JsonResponse

def GenrateResponse(status,status_code,message,data):
    response = JsonResponse({
                    "STATUS": status,
                    "RESPONSE":
                        {
                            "STATUS_CODE": status_code,
                            "MESSAGE": message,
                            "DATA": data
                        }
                },status=status_code)
    return response
 
def badRequest(message):
    data=[]
    return GenrateResponse("BAD REQUEST",500,message,data)

def successResponse(message,data):
    return GenrateResponse("SUCCESS",200,message,data)

def errorResponse(message):
    data=[]
    data.append(message)
    return GenrateResponse("error",500,message,data)
