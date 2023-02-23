# -*- coding: utf-8 -*-

# https://atcoder.jp/contests/abc001/tasks/abc001_2
#

def calc(distance_meter):
    distance_kilo_meter = distance_meter / 1000

    if distance_meter < 100:
        result = 0
    elif 100 <= distance_meter < 6000:
        result = distance_kilo_meter * 10
    elif 6000 <= distance_meter <= 30000:
        result = distance_kilo_meter + 50
    elif 35000 <= distance_meter <= 70000:
        result = (distance_kilo_meter - 30) / 5 + 80
    else:
        result = 89

    return result


if __name__ == "__main__":
    input_data = int(input())
    output_data = calc(input_data)
    print("{:02}".format(int(output_data)))

# EOF
