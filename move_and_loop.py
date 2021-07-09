import sys
import math


# 将x填充成n位
def fill_to_n_digits(x, n) -> int:
    add_digit = n - len(str(x))  # 需要补充0的位数
    x = int(str(x) + '0' * add_digit)
    return x


# 存储x到list中
def store_x_into_list(x, x_list) -> list:
    x_list.append(x)
    return x_list


# 将x按升序排列成x1
def increase_x(x) -> int:
    temp_str = str(x)
    temp_list = list(temp_str)
    temp_list.sort()
    temp_str = "".join(temp_list).zfill(5)
    x1 = int(temp_str)
    return x1


# 将x按降序排列成x2
def decrease_x(x) -> int:
    temp_str = str(x)
    temp_list = list(temp_str)
    temp_list.sort()
    temp_list.reverse()
    temp_str = "".join(temp_list).zfill(5)
    x2 = int(temp_str)
    return x2


# 计算x2 - x1
def new_x(x1, x2) -> int:
    x = x2 - x1
    return x


# 判断x是否和之前的x相同，返回(相同x的index, 循环周期)
def is_x_loop(x, x_list):
    for i in x_list:
        if x == i:
            return x_list.index(i), len(x_list) - x_list.index(i)
    return -1, -1


# 返回F的结果
def F_output(x, n):
    x = fill_to_n_digits(x, n)
    F1, F2 = -1, -1
    x_list = []
    while F1 == -1 and F2 == -1:
        x_list = store_x_into_list(x, x_list)
        x1 = increase_x(x)
        x2 = decrease_x(x)
        x = new_x(x1, x2)
        F1, F2 = is_x_loop(x, x_list)
    return F1, F2


# 主函数
def move_and_loop(n) -> list:
    F_list = list()
    for i in range(int(math.pow(10, n))):
        temp_F1, temp_F2 = F_output(i, n)
        F_list.append((temp_F1, temp_F2))
    return F_list

