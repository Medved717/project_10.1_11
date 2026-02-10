def up_first(msg):
    "Делвет первую букву строки заглавной."
    if msg:
        return msg[0].upper() + msg[1:]
    else:
        return msg


result = up_first("poetry_1")
print(result)