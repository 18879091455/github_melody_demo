# coding:utf-8
'''
查看列表元素在列表的什么位置
'''


def find_index():
    list_int = [1, 2, 3, 4, 5, 6, 7, 11, 7, 8, 9, 10, 1, 2, 3, 4, 5]

    # 查找index
    try:
        int_index = list_int.index(55)
    except ValueError:
        int_index = None
    print(int_index)

    # 去重
    new_list_int = list(set(list_int))
    print(new_list_int)


def count_list():
    mlist = [1, 2, 3, 4, 5, 6, 12, 2, 3, 5]

    print(mlist.count(5))
    print(mlist.index(5))
    mlist.remove(1)
    print(mlist)


def oprate_list():
    li = [1, 2, 3, 4, 5, 6]
    # 序列中的每个元素+1
    li1 = list(map(lambda x: x + 1, li))
    print("元素加一", li1)
    # 返回序列中的偶数
    li2 = list(filter(lambda x: x % 2 == 0, li))
    print("返回偶数", li2)
    li3 = list(filter(lambda x: li[::2], li))
    print("返回偶数", li3)
    print("创建列表", [i for i in range(len(li))])
    print(round(2.675, 6))


# 快捷遍历
def def_for_list():
    f = ["a", "b", "c"]
    fx = (item + "x" for item in f)
    print fx, ",".join(fx)

    fxl = list(item + "x" for item in f)
    print fxl, ",".join(fxl)


def def_map_list():
    f = ["a", "b", "c"]
    fx = list(map(lambda x: x + "x", f))
    print fx


if __name__ == '__main__':
    # find_index()
    # count_list()
    oprate_list()