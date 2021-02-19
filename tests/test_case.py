def test_version():
    from apitesting import __version__
    assert isinstance(__version__,str)

import requests
from apitesting.api import BaseApi
def test_httpbin_get():
    resp=requests.get("http://httpbin.org/get",headers={"accept":"application/json"})
    assert resp.status_code == 200
    assert resp.headers["server"] == "gunicorn/19.9.0"




class ApiHttpbinGet(BaseApi):
    url="http://httpbin.org/get"
    method = "GET"
    headers = {"accept":"application/json"}



def test_httpbin_get():
    ApiHttpbinGet().run().validate("status_code",200)

def test_httpbin_get_withparams():
    ApiHttpbinGet().set_params(abc=123,xyz=456).run().validate("status_code",200)





class ApiHttpbinPost(BaseApi):
    url = "http://httpbin.org/get"
    method = "POST"
    params={}
    headers = {"accept": "application/json"}
    data="abc=123"
    json={"abc":123}

def test_httpbin_post():
    ApiHttpbinPost().setjson({"abc":123}).run().validate("status_code",200)