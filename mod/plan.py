from db import pln

def get_all_plans():
    res = pln.find({}, {'_id': 0})
    return list(res)