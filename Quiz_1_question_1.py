def string_sum(dig1, dig2):
    import sys
    if len(dig1) > 1 or len(dig2) > 1:
        raise RuntimeError("Only digits")
    if int(dig1) + int(dig2) >= 10:
        return ["1", str(int(dig1) + int(dig2) - 10)]
    else:
        return ["0", str(int(dig1) + int(dig2))]


def string_op(str1, str2):
    if len(str1) == 1: str1 = "00{}".format(str1)
    elif len(str1) == 2: str1 = "0{}".format(str1)
    if len(str2) == 1: str2 = "00{}".format(str2)
    elif len(str2) == 2: str2 = "0{}".format(str2)

    first_digit = string_sum(str1[2], str2[2])[1]
    carry_1 = (string_sum(str1[2], str2[2])[0])

    second_digit = string_sum(carry_1[0], string_sum(str1[1], str2[1])[1])[1]

    if string_sum(carry_1, string_sum(str1[1], str2[1])[1]) == ["1","0"]:
        carry_2 = string_sum(carry_1, string_sum(str1[1], str2[1])[1])
    else:
        carry_2 = string_sum(str1[1], str2[1])
    third_digit = string_sum(carry_2[0], string_sum(str1[0], str2[0])[0])[1]

    if third_digit != "0":
        return "{}{}{}".format(third_digit, second_digit, first_digit)
    elif second_digit != "0":
        return "{}{}".format(second_digit, first_digit)
    else:
        return first_digit