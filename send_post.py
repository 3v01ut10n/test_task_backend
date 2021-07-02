import requests


# r_login = requests.post("http://127.0.0.1:5000/login", json={"phone": "+71111111111", "code": "QWDCR4"})
# print(r_login.text)

r_check_structure = requests.post(
    "http://127.0.0.1:5000/check_structure",
    json={
        "link": "https://freestylo.ru/",
        "structure": {
            "html": 1, "head": 1, "body": 1, "p": 10, "img": 2
        }
    }
)
print(r_check_structure.text)
