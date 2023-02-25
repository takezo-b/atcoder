# -*- coding: utf-8 -*-

# https://atcoder.jp/contests/abc285/tasks/abc285_a
#

def setup():
    data_dict_local = {}

    list_element = [2, 3]
    data_dict_local[1] = list_element

    list_element = [1, 4, 5]
    data_dict_local[2] = list_element

    list_element = [1, 6, 7]
    data_dict_local[3] = list_element

    list_element = [2, 8, 9]
    data_dict_local[4] = list_element

    list_element = [2, 10, 11]
    data_dict_local[5] = list_element

    list_element = [3, 12, 13]
    data_dict_local[6] = list_element

    list_element = [3, 14, 15]
    data_dict_local[7] = list_element

    list_element = [4]
    data_dict_local[8] = list_element

    list_element = [4]
    data_dict_local[9] = list_element

    list_element = [5]
    data_dict_local[10] = list_element

    list_element = [5]
    data_dict_local[11] = list_element

    list_element = [6]
    data_dict_local[12] = list_element

    list_element = [6]
    data_dict_local[13] = list_element

    list_element = [7]
    data_dict_local[14] = list_element

    list_element = [7]
    data_dict_local[15] = list_element

    return data_dict_local


def is_line(param_data_dict, param_point_a, param_point_b):
    line_data = param_data_dict[param_point_a]
    b_result_line: bool = param_point_b in line_data
    return b_result_line


if __name__ == "__main__":
    point_a, point_b = map(int, input().split())

    data_dict = setup()
    b_line = is_line(data_dict, point_a, point_b)

    print("Yes" if b_line else "No")

# EOF
