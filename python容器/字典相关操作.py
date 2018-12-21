# coding:utf-8

import json

# def mfunc():
#     mdict = {"a": "aa", "b": "bb", "c": "cc"}
#     # Python 3.X 里不包含 has_key() 函数，被 __contains__(key) 替代
#     if mdict. has_key("a"):
#         print( "yes")
#     '''
#     if mdict. __contains__("a"):
#         print("yes")
#     '''


def func4():
    a = [None]
    report_dict = {}
    if a:
        report_dict['INSTALL_PATH'] = a[0]
        print report_dict

def func3():
    data1 = {"a": "b"}
    data11 = json.dumps(data1)
    # data111 = json.loads(data1),报错
    print type(data1)
    print type(data11)
    print data11
    # print type(data111)

    data2 = '{"a":"b"}'
    data22 = json.loads(data2)
    data222 = json.dumps(data2)
    print type(data2)
    print type(data22)
    print type(data222)


def mfunc2():
    mdict = {"a":"b"}
    flag = "a"
    print mdict[flag]



if __name__ == '__main__':
    # mfunc2()
    func3()
