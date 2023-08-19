from requests import Response


class BaseCase:
    """Base class for basic methods"""
    def get_cookies(self, response:Response, cookie_name):
        assert cookie_name in response.cookies, f"Wrong cookie name. Expected: {cookie_name}"
        return response.cookies[cookie_name]

    def get_headers(self, response: Response, header_name):
        assert header_name in response.headers, f"Wrong header name. Expected: {header_name}"
        return response.headers[header_name]

