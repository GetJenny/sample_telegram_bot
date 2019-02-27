from urllib3 import PoolManager, Timeout, util
import json
import time


class ApiCallException(Exception):
    """
    Generic exception used to report problems
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class NoContentApiCallException(Exception):
    """
    Exception used to report problems no content
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class Starchat:
    def __init__(self):
        self.starchat_url = "http://localhost:8889"
        headers = util.make_headers(basic_auth='eremocafe:p4ssw0rd')
        headers['Content-Type']='application/json'
        self.post_headers = headers
        self.get_headers = headers
        print("FANCU", self.post_headers)

    @staticmethod
    def call_api_function(url, method, body=None, headers={'Content-Type': 'application/json'}):
        """
        call an API's function and return response

        exception: raise an exception if any error occur

        :param url: the url
        :param method: POST or GET, DELETE
        :param body: the body of the request if any
        :return: the data structure or None
        """
        try:
            with PoolManager(retries=5, timeout=Timeout(total=5.0)) as http:
                r = http.urlopen(method, url, headers=headers, body=body)
                ret_data = (r.status, r.data)
                r.close()
        except Exception as exc:
            e_message = "error getting response from url: " + url
            raise ApiCallException(e_message)
        else:
            if ret_data:
                if ret_data[0] == 204:
                    raise NoContentApiCallException("No content for the call")
                try:
                    structured_res = (ret_data[0], json.loads(ret_data[1].decode("utf-8")))
                except ValueError as exc:
                    e_message = "error parsing response from url: " + url + " : res(" + str(ret_data) + ")"
                    raise ApiCallException(e_message)
            else:
                structured_res = None
            return structured_res

    def get_next_response(self, body):
        url = self.starchat_url + "/get_next_response"
        headers = self.post_headers
        print("HEADERS......................", self.post_headers)
        body = body
        res = self.call_api_function(url=url, method="POST", body=json.dumps(body), headers=headers)
        if res[0] > 299 or res[0] < 200:
            print("Error: getting a response:", res)
        return res
