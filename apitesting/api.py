import requests

class BaseApi(object):
    method="GET"
    url=""
    params={}
    headers={}
    data={}
    json={}

    def set_params(self,**params):
        self.params=params
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
            headers=self.headers,
            data=self.data,
            json=self.json
        )
        return self

    def validate(self,key,expected_value):
        value = self.response
        for _key in key.split("."):
            # print("++++++",_key,value,type(value))
            if isinstance(value,requests.Response):
                if _key=="json()":
                    value = self.response.json()
                else:
                    value = getattr(value,_key)
            elif isinstance(value,(requests.structures.CaseInsensitiveDict,dict)):
                value = value[_key]
        # print("=====222",_key,value,expected_value)
        assert value == expected_value
        return self