#!/usr/bin/env python3

f = open("input.in", "r")
calibration_doc = f.read()
f.close()


def part_one(data):
    digits = []
    calibration_value_sum = 0

    for i, line in enumerate(data.split()):
        tmp = ''
        for char in line:
            if char.isdigit():
                tmp += char
        digits.append(tmp)

    for i, n in enumerate(digits):
        if len(n) == 1:
            digits[i] = n + n
        else:
            digits[i] = n[0] + n[len(n) - 1]

    for i in digits:
        calibration_value_sum += int(i)

    return calibration_value_sum


def part_two(data):
    pass


if __name__ == '__main__':
    print(part_one(calibration_doc))
    print(part_two(calibration_doc))
