def num_to_str_modulo(num: int, mod: int, string: str) -> str:
    if num % mod == 0:
        return string
    else:
        return ""

def fizz(num: int) -> str:
    return num_to_str_modulo(num, 3, "fizz")

def buzz(num: int) -> str:
    return num_to_str_modulo(num, 5, "buzz")

def fizzbuzz(num: int) -> str:
    string = ""
    string += fizz(num)
    string += buzz(num)
    return string

def return_string_or_num(num: int, func):
    string = func(num)
    if string == "":
        return str(num)
    else:
        return string

def run_string_or_none_for_iterations(func, n: int):
    lst = []
    for i in range (n):
        lst.append(return_string_or_num(i+1, func))
    return lst


if __name__ == "__main__":
    lst = run_string_or_none_for_iterations(fizzbuzz, 100)

    for i in lst:
        print(i)
