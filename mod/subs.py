from db import sub, pln
from datetime import datetime, timedelta

def add_sub(uid, dat):
    pid = dat.get('pid')
    plan = pln.find_one({'id': pid})
    if not plan:
        return {'err': 'plan'}
    now = datetime.utcnow()
    end = now + timedelta(days=plan['duration'])
    doc = {
        'uid': uid,
        'pid': pid,
        'sts': 'ACTIVE',
        'sta': now,
        'end': end
    }
    sub.insert_one(doc)
    return {'ok': 1}

def get_sub(uid):
    res = sub.find_one({'uid': uid}, {'_id': 0})
    return res or {}

def set_sub(uid, dat):
    pid = dat.get('pid')
    plan = pln.find_one({'id': pid})
    if not plan:
        return {'err': 'plan'}
    now = datetime.utcnow()
    end = now + timedelta(days=plan['duration'])
    res = sub.update_one(
        {'uid': uid},
        {'$set': {'pid': pid, 'sts': 'ACTIVE', 'sta': now, 'end': end}}
    )
    return {'mod': res.modified_count}

def del_sub(uid):
    res = sub.update_one(
        {'uid': uid},
        {'$set': {'sts': 'CANCELLED'}}
    )
    return {'mod': res.modified_count}
