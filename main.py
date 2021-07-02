from flask import Flask, request

from modules.code_manager import *
from modules.structure import *

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


@app.route("/structure", methods=["GET"])
def structure():
    if request.method == "GET":
        link = request.args.get("link")
        tags = request.args.get("tags")
        if link is None and tags is None:
            return get_structure()
        elif link is not None and tags is None:
            return get_structure(link=link)
        else:
            return {"status": "Fail"}


@app.route("/check_structure", methods=["POST"])  # TODO: Пункт 4
def check_structure():
    if request.method == "POST":
        pass


if __name__ == "__main__":
    app.run(debug=True)
