def get_code(phone, CODES):
    """Возвращает 6-значный код по номеру телефона."""
    code = CODES.get(delete_plus_and_space(phone))

    if code is None:
        return {"code": None}
    else:
        return {"code": code}


def delete_plus_and_space(phone):
    """

    Удаляет символ + и пробел из номера телефона.
    """
    return phone.replace("+", "", 1).replace(" ", "", 1)


def check_code(data, CODES):
    phone = delete_plus_and_space(data.get("phone"))
    code = data.get("code")

    if phone in CODES:
        if code == CODES.get(phone):
            return {"status": "OK"}
        else:
            return {"status": "Fail"}
    else:
        return {"status": "Fail"}


CODES = {
    "71111111111": "QWDCR4",
}
