import sys
from decimal import Decimal

pipe = "========================================================================"


def calc_ranges():
    _ranges = []
    tmp = 0.0
    for _i in range(len(p)):
        _ranges.append((tmp, tmp + p[_i]))
        tmp += p[_i]
    return _ranges


def calc_range(c_range, mode):
    global row, high
    for t in text if mode == 1 else symbols:
        _row = round(row + c_range * table[t][0], 15)
        _high = round(row + c_range * table[t][1], 15)
        c_range = round(_high - _row, 15)
        row = _row
        high = _high
    return c_range


def calc_value(g_code: list[bool]):
    rcode = float(0.0)
    for _gc in range(len(g_code)):
        if g_code[_gc]:
            rcode += 2 ** (-(1 + _gc))
    return rcode


def generate_code():
    _code = []
    while calc_value(_code) < row:
        if calc_value(_code + [True]) > high:
            _code.append(False)
            continue
        _code.append(True)
    return calc_value(_code), _code


def code_to_bin():
    c_bin = "0."
    for c in code:
        if c:
            c_bin += "1"
        else:
            c_bin += "0"
    length = len(c_bin) - 2
    for _ in range(roundup_to_eight(length) - length):
        c_bin += "0"
    return c_bin


def len_decimal(x):
    return len(str(x).split(".")[1])


def roundup_to_eight(number):
    remainder = number % 4
    if remainder == 0:
        return number
    else:
        return number + (4 - remainder)


def bin_to_value(bin_code):
    _value = 0.0
    for i in range(len(bin_code)):
        if bin_code[i] == '1':
            _value += 2 ** (-(i + 1))
    return _value


def get_decimal(_encoded_value):
    _decimal = 0.0
    for it, _enc in enumerate(_encoded_value):
        _decimal += int(_enc) * 2 ** (-(it + 1))
    return _decimal


def decode(_encoded_value):
    _decoded_text = ""
    _decimal = get_decimal(_encoded_value)
    while True:
        for symbol, (low, _high) in table.items():
            if low <= _decimal < _high:
                _decoded_text += symbol
                _decimal = round((_decimal - low) / (_high - low), 15)
                break
        if len(table) == 0 or symbol == "EOD":
            break
    return _decoded_text


def init():
    if sum(p) < 1.0:
        symbols.append("EOD")
        p.append(float(Decimal('1.0') - sum(Decimal(str(x)) for x in p)))
        if choice == 1: text.append("EOD")

    if len(symbols) != len(p):
        print("error")
        exit()


def welcome():
    print(pipe)
    print("Arithmetic Encoding / Decoding tool")
    print("@Author Jiyong Jung / github.com/clxxrlove")
    print(pipe)
    print("Enter symbols on one line without commas; ex) A B C")
    print("Enter probabilities on one line without commas; ex) 0.5 0.3 0.2")
    print(pipe)
    print("if the sum or probabilities is less than 1, EOD(End of Data) will added.")
    print(pipe)


def menu():
    print(pipe)
    print("1. Arithmetic Encoding")
    print("2. Arithmetic Decoding")
    _menu = int(input("Enter the number of the menu: "))
    print(pipe)
    if _menu == 1:
        _text = input("Enter the text to encode: ").rstrip().rstrip("EOD")
        _text = list(_text)
    elif _menu == 2:
        _text = input("Enter the encoded value to decode: ")
    else:
        print("Invalid input")
        exit()

    return _menu, _text


# Initialization #

table = dict()
welcome()

symbols = sys.stdin.readline().rstrip().split(" ")
p = list(map(float, sys.stdin.readline().rstrip().split()))

choice, text = menu()
init()

ranges = calc_ranges()
_range = float(1.0)
row = float(0.0)
high = float(1.0)

for i in range(len(symbols)):
    table[symbols[i]] = ranges[i]

_range = calc_range(_range, choice)

# Encoding / Decoding #

if choice == 1:
    value, code = generate_code()
    _bin = code_to_bin()

    print(f"code = {_bin}, value = {value}")
else:
    encoded_value = text[2:]
    decoded_text = decode(encoded_value)
    print(f"decoded text = {decoded_text.rstrip('EOD')}")
