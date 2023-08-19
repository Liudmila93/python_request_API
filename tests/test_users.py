# import requests
# import pytest
# # https://petstore.swagger.io/
#
# class TestUserAuth:
#     def test_sign_user(self):
#         data = {
#             "id": 1,
#             "username": "string1",
#             "firstName": "string1",
#             "lastName": "string1",
#             "email": "string1@mail.ru",
#             "password": "string1",
#             "phone": "123456",
#             "userStatus": 1
#         }
#         headers = {"Content-Type": "application/json", "accept": "application/json"}  # Specify JSON content type
#
#         url_sign_up = "https://petstore.swagger.io/v2/user"
#         response = requests.post(url_sign_up, data=data, headers=headers)
#         print(response.status_code)
#         print(response.text)
#
#         print(response.json())
#        #
#        #  assert 'login' in response.json(), "There is no username"
#        #  assert 'password' in response.json(), "There is no password"
#        #  assert 'nickname' in response.json(), "There is no nickname"
#        #  assert 'email' in response.json(), "There is no email"
#
#         # username = response.json()['login']
#         # password = response.json()['password']
#         # nickname = response.json()['nickname']
#         # email = response.json()['email']
#         #
#         # url_get_data = "https://api.qanotes.info/api-docs/account"
#         # response2 = requests.get(url_get_data)
#         # assert username == response2.json()['login'], "User name is not correct"
#         # assert password == response2.json()['password'], "Password is not correct"
#
#
#     def test_login_user(self):
#         data = {
#             "login": "string",
#             "password": "string"
#         }
#       #  headers = {"Content-Type": "application/json; v = 1.0", "accept": "*/*"}  # Specify JSON content type
#
#         url_login = "https://api.qanotes.info/api-docs/login"
#         response = requests.post(url_login, data=data)
#
#         print(response.json())
#
#         assert 'login' in response.json(), "There is no username"
#         assert 'password' in response.json(), "There is no password"
#
#         username = response.json()['login']
#         password = response.json()['password']
#
#         url_get_data = "https://api.qanotes.info/api-docs/account"
#         response2 = requests.get(url_get_data)
#         assert username == response2.json()['login'], "User name is not correct"
#         assert password == response2.json()['password'], "Password is not correct"


