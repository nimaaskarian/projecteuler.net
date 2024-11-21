def is_pandigital(num_str):
    if (len(num_str) != 9 or
        "0" in num_str or
        any(ch for ch in "123456789" if num_str.count(ch) > 1)
        ):
        return False
    return True

def pandigital_multiples():
    for d in range(1, 10000):
        num_str = ""
        for n in range(1, 10):
            multiple_str = str(n*d)
            if len(num_str)+len(multiple_str) > 9:
                break
            num_str+=multiple_str
        if not is_pandigital(num_str):
            continue
        yield int(num_str)

print(max(pandigital_multiples()))
