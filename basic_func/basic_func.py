def add(a, b):
      ## pass부분을 코드로 넣어서 pytest로 확인하기
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def power(base, pow):
    return base**pow


def square(base):
    return power(base,2)


def greet(이름="낯선자", 나이=20):
    if 나이 >= 50:
        return str (f"안녕하십니까 {이름}!")
    elif 나이 <= 4:
        return str (f"안녕 {이름}!")
    else:
        return str (f"안녕하신가 {이름}!")