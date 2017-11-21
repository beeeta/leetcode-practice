
from flask import Flask,request,redirect,make_response
import hashlib
import random

import config
# from backend import Urlpool

app = Flask(__name__)
# urlpool = Urlpool(config.db)


@app.route('/register',methods=['POST'])
def register_url():
    # check request and heads

    srcuri = request.args.get('src')
    # check srcuri

    shorturl = gene_shorturl(srcuri)
    # save shorturl
    # urlpool.add(shorturl)
    return make_response('success',200)


def gene_shorturl(srcurl):
    srcurl = srcurl.encode('utf8')
    hexd = hashlib.md5(srcurl).hexdigest()
    # 对hex分4段并随机取其中一段



if __name__ == '__main__':
    gene_shorturl('http://abc/bbb')