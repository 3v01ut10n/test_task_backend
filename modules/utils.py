def get_code(phone, CODES):
    """Возвращает 6-значный код по номеру телефона."""
    code = CODES.get(phone)

    if code is None:
        return {"code": None}
    else:
        return {"code": code}


CODES = {
    "71111111111": "QWDCR4",
}
