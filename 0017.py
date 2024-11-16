import sys
from mymath import nth_digit, truncate

def main():
    print(sum(len(item) for item in strs()))

def strs():
    for num in range(1,1000):
        try:
            num_str = e1_teen[truncate(num, 2)]
        except:
            num_str = e0[truncate(num,1)]
            num_str = e1[nth_digit(num, 2)] + num_str

        e2_digit = nth_digit(num, 3)
        if e2_digit:
            if num_str:
                num_str = e0[e2_digit] + e2 + "and" + num_str
            else:
                num_str = e0[e2_digit] + e2

        yield num_str
    yield e0[1] + e3

            

e0 = {
        0:"",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        }

e1_teen = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        }

e1 = {
        0: "",
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"
        }
e2 = "hundred"
e3 = "thousand"

if __name__ == "__main__":
    main()
