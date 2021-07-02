import requests


r = requests.post("http://127.0.0.1:5000/login", json={"phone": "+71111111111", "code": "QWDCR4"})
print(r.text)
