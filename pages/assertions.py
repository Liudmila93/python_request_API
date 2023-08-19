from requests import Response
import json


class Assertions:
    def assert_status_code(self, response:Response, status_code):
        assert response.status_code == status_code, f"Wrong status code. Expected: {status_code}. Actual: {response.status_code}"

    @staticmethod
    def assert_json_has_key(self, response:Response, key_name):
        try:
            response_as_dictionary = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is {response.text}"

        assert key_name in response_as_dictionary, f"Response does not have key = '{key_name}'"

    @staticmethod
    def assert_json_has_value(self, response: Response, value_name, expected_value, error_message):
        try:
            response_as_dictionary = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is {response.text}"

        assert value_name in response_as_dictionary, f"Response does not have value = '{value_name}'"
        assert response_as_dictionary[value_name] == expected_value, error_message
