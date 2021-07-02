from flask import Flask, request

from modules.utils import *


app = Flask(__name__)


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    GET /login?phone=<телефон> - возвращает 6-значный код.
    POST {"phone": "+71111111111", "code": "QWDCR4"} - возвращает статус в зависимости от корректности кода.
    """
    if request.method == "GET":
        phone = request.args.get("phone")
        return get_code(phone, CODES)
    elif request.method == "POST":
        data = request.get_json()
        return check_code(data, CODES)


if __name__ == "__main__":
    app.run(debug=True)
