# -*- coding: utf-8 -*-

# https://atcoder.jp/contests/abc285/tasks/abc285_b
#

def get_uncommon_by_diff(length, target_string, diff
                         ) -> int:
    """
    比較する文字 インデックスの差を与え、文字比較が連続して異なる回数を返す

    Args:
        length (int):  文字数 (target_stringの)
        target_string (basestring):  文字列
        diff (int):  比較する文字 インデックスの差

    Returns:
        文字比較が連続して異なる回数
    """

    result = 0

    for index in range(length):
        if length <= index + diff:
            break

        # print("[{}, {}] : {} {}".
        #       format(index, index + diff, target_string[index], target_string[index + diff]))

        if target_string[index] == target_string[index + diff]:
            break
        else:
            result = index + 1

    return result


def get_uncommon(length, target_string
                 ) -> list[int]:
    """
　　 比較する文字 全範囲のインデックスの差での、それぞれの文字比較が連続して異なる回数

    Args:
        length (int):  文字数 (target_stringの)
        target_string (basestring):  文字列

    Returns:
        比較する文字 インデックスの差 1..length それぞれの文字比較が連続して異なる回数
    """
    result: list[int] = []

    for diff in range(1, length):
        uncommon_length = get_uncommon_by_diff(length, target_string, diff)
        result.append(uncommon_length)

    return result


if __name__ == "__main__":
    string_length = int(input())
    string = input()

    result_list = get_uncommon(string_length, string)

    for elm in result_list:
        print(elm)


# EOF
