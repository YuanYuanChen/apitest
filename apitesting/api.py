import requests

class BaseApi(object):
    method="GET"
    url=""
    params={}
    headers={}
    cookies={}
    data={}
    json={}

    def set_params(self,**params):
        self.params=params
        return self

    def set_cookie(self,key,value):
        self.cookies.update({key:value})
        return self

    def set_data(self,data):
        self.data=data
        return self

    def set_json(self,json):
        self.json=json
        return self

    def run(self):
        self.response = requests.request(
            self.method,
            self.url,
            params=self.params,
            cookies=self.cookies,
            headers=self.headers,
            data=self.data,
            json=self.json
        )
        return self


    def extract(self,field):
        value = self.response
        for _key in field.split("."):
            print("++++++", _key, value, type(value))
            if isinstance(value, requests.Response):
                if _key == "json()":
                    value = self.response.json()
                else:
                    value = getattr(value, _key)
            elif isinstance(value, (requests.structures.CaseInsensitiveDict, dict)):
                print("value++++",value[_key])
                value = value[_key]
        return value

    def validate(self,key,expected_value):
        actual_value = self.extract(key)
        assert actual_value == expected_value
        return self