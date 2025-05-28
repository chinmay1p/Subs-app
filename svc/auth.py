import jwt
import os

def chk_jwt(tok):
    if not tok:
        raise Exception('no token')
    tok = tok.replace('Bearer ', '')
    try:
        out = jwt.decode(tok, os.getenv('JWT_KEY'), algorithms=['HS256'])
        return out['uid']
    except:
        raise Exception('bad token')
