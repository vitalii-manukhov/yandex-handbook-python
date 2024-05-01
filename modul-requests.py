# # Static API
# from requests import get
# # first variant to create request
# # response = get("https://static-maps.yandex.ru/1.x/?"
# #                "ll=37.677751,55.757718&"
# #                "spn=0.016457,0.00619&"
# #                "l=map")

# # second variant to create request
# params = {"ll": "37.677751,55.757718",
#           "spn": "0.016457,0.00619",
#           "l": "map"}

# response = get("https://static-maps.yandex.ru/1.x/",
#                params=params)

# print(response)

# try:
#     response = get("https://static-maps.yandex.ru/1.x/", params=params)
# except ConnectionError:
#     print("Проверьте подключение к сети.")
# else:
#     with open("map.png", "wb") as file:
#         file.write(response.content)

# # Yandex Disk API
# from requests_oauthlib import OAuth2Session
# from requests import get, post, put, delete

# client_id = "f0fa854f3a8e43a5b0cd872e0e2b0337"
# client_secret = "d23380eeecb64cdba9b55750779f0d6e"
# auth_url = "https://oauth.yandex.ru/authorize"
# token_url = "https://oauth.yandex.ru/token"
# oauth = OAuth2Session(client_id=client_id)
# authorization_url, state = oauth.authorization_url(auth_url, force_confirm="true")
# print("Перейдите по ссылке, авторизуйтесь и скопируйте код:", authorization_url)
# code = input("Вставьте одноразовый код: ")
# token = oauth.fetch_token(token_url=token_url,
#                           code=code,
#                           client_secret=client_secret)
# access_token = token["access_token"]
# print(access_token)

# headers = {"Authorization": f"OAuth {access_token}"}
# r = get("https://cloud-api.yandex.net/v1/disk", headers=headers)
# print(r.json())

# params = {"path": "Тест API"}
# r = put("https://cloud-api.yandex.net/v1/disk/resources", headers=headers, params=params)
# print(r)

# A. Check system
# Some server: 127.0.0.1.
# Port of server: 5000.

from requests import get

r = get("http://127.0.0.1:5000")
print(r.text)