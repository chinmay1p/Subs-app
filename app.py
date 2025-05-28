from flask import Flask, request, jsonify
from svc.auth import chk_jwt
from mod.plan import get_all_plans
from mod.subs import add_sub, get_sub, set_sub, del_sub

app = Flask(__name__)

@app.route('/plans', methods=['GET'])
def r_pln():
    return jsonify(get_all_plans())

@app.route('/subscriptions', methods=['POST'])
def c_sub():
    tok = request.headers.get('Authorization')
    usr = chk_jwt(tok)
    dat = request.json
    return jsonify(add_sub(usr, dat))

@app.route('/subscriptions/<uid>', methods=['GET'])
def g_sub(uid):
    return jsonify(get_sub(uid))

@app.route('/subscriptions/<uid>', methods=['PUT'])
def u_sub(uid):
    dat = request.json
    return jsonify(set_sub(uid, dat))

@app.route('/subscriptions/<uid>', methods=['DELETE'])
def d_sub(uid):
    return jsonify(del_sub(uid))

if __name__ == '__main__':
    app.run()
