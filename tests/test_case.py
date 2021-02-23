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

# 参数共享
def test_httpbin_parameters_share():
    user_id="adk129"
    ApiHttpbinGet().set_params(user_id=user_id) \
        .run() \
        .validate("status_code", 200) \
        .validate("json().headers.Accept", "application/json")\
        .validate("json().url","http://httpbin.org/get?user_id=adk129")\
        .validate("json().args.user_id","adk129")


    ApiHttpbinPost().set_json({"user_id": user_id}) \
        .run() \
        .validate("status_code", 405)\
        # .validate("json().url","http://httpbin.org/post?user_id=adk129")\
        # .validate("json().headers.Accept", "application/json")


def test_httpbib_extract():
    api_run=ApiHttpbinGet().run()
    status_code=api_run.extract("status_code")
    assert status_code==200
    accept_type=api_run.extract("json().headers.Accept")
    assert accept_type=="application/json"


def test_httpbin_setcookies():
    api_run = ApiHttpbinGetCookies()\
        .set_cookie("free_form1","123")\
        .set_cookie("free_form2", "456")\
        .run()
    freeform1=api_run\
        .extract("json().cookies.free_form1")
    freeform2 = api_run\
        .extract("json().cookies.free_form2")
    assert freeform1 == "123"
    assert freeform2 == "456"




# 第一个接口的返回作为第二个接口的输入
def test_httpbin_parameters_extract():
    #get value
    freeform = ApiHttpbinGetCookies()\
            .set_cookie("free_form","123")\
            .run()\
             .extract("json().cookies.free_form")
    assert freeform=="123"

    #user value as parameter
    ApiHttpbinGet().set_params(user_id=freeform)\
        .run().validate("json().args.user_id","123")





