import jwt
import os
import datetime
from dotenv import load_dotenv
load_dotenv()

from .models import CustomUser, CustomToken

def get_object(token):
    try:
        token = token.split(" ")
        payload = jwt.decode(token[1], os.getenv('JWT_SECRET'), algorithms=['HS256'])
        if payload['user_type']==0:
            # General User            
            required_object = CustomUser.objects.get(id=payload['id'])
        else:
            # Organisation
            pass
        token = CustomToken.objects.get(object_id=required_object.id, user_type=payload['user_type'])
        return required_object
    except Exception as error:
        print(error)
        return None

def get_token(object_id, user_type):
    payload = {
        'user_type':user_type,
        'id':object_id,
        'time_stamp':str(datetime.datetime.today())
    }
    encoded_jwt = jwt.encode(payload, os.getenv('JWT_SECRET'), algorithm='HS256')
    result = (encoded_jwt.decode("utf-8"))
    return result
