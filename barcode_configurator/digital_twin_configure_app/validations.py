from django.conf import settings
import requests

def checkValidations(key,validateData):
    if key=="Organization":
        if validateData.get('id')=='' or validateData.get('name')=='':
            return False
        if type(validateData.get('id')) == str and validateData.get('id').isnumeric()==False:
            return False    
        return True

    if key=="BusinessUnit":
        if validateData.get('id')=='' or validateData.get('name')=='':
            return False
        if type(validateData.get('id')) == str and validateData.get('id').isnumeric()==False:
            return False    
        return True
    
    if key=="Plant":
        if validateData.get('id')=='' or validateData.get('name')=='' or validateData.get('city')=='' or validateData.get('state')=='' or validateData.get('country')=='':
            return False
        if type(validateData.get('id')) == str and validateData.get('id').isnumeric()==False:
            return False    
        return True 
    return True            
