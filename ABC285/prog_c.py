# -*- coding: utf-8 -*-

# https://atcoder.jp/contests/abc285/tasks/abc285_c
#

def decode(string_id
           ) -> int:
    """
    文字列ID 先頭から何番目に変換する
    Args:
        string_id (basestring): 文字列ID

    Returns:
        先頭からのIDの順番
    """
    length = len(string_id)
    value_id = 0

    for index in range(length):
        char = string_id[index]
        value_id = value_id * 26 + ord(char) - ord('A') + 1
        # print("index : {}, char : {}, value_id : {}".format(index, char, value_id))
    return value_id


if __name__ == "__main__":
    string_id = input()
    value_id = decode(string_id)
    print(value_id)

# EOF
