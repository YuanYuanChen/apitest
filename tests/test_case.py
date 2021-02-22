# def test_version():
#     from apitesting import __version__
#     assert isinstance(__version__,str)

import requests
from tests.api.httpbin import *

def test_httpbin_get():
    resp=requests.get("http://httpbin.org/get",headers={"accept":"application/json"})
    assert resp.status_code == 200
    assert resp.headers["server"] == "gunicorn/19.9.0"




def test_httpbin_get():
    ApiHttpbinGet().run().validate("status_code",200)\
        .validate("headers.server","gunicorn/19.9.0")\
        .validate("json().url","http://httpbin.org/get")\
        .validate("json().args",{})\
        .validate("json().headers.Accept",'application/json')

def test_httpbin_get_withparams():
    ApiHttpbinGet().set_params(abc=123,xyz=456)\
        .run()\
        .validate("status_code",200)\
        # .validate("header.server","nginx")\
        # .validate("json().url","https://httpbin.org/get?abc=123&xyz=456")\
        # .validate("json().headers.Accept",'application/json')


def test_httpbin_post():
    ApiHttpbinPost().set_json({"abc":456})\
        .run()\
        .validate("status_code",405)\
        # .validate("json().url","http://httpbin.org/post")\
        # .validate("json().headers.Accept",'application/json')


