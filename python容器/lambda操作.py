def list_oprate():
    list_int = [1, 2, 3, 4, 5, 6, 7, 11, 7, 8, 9, 10, 1, 2, 3, 4, 5]
    old_list = list(map(lambda x: x + 1, list_int))
    old_list2 = list(x+1 for x in list_int)

    print(old_list)

    sort_list = [{'accessId': 22, 'accessType': 'rw', 'csp': 'aliyun', 'companyId': '2V7tReeFv6GYHh5Gjr5KpO',
                  'clientId': '3AxO9eTYV1ciGdRdDafA9L', 'accessKey': 'LTAI5CjxNp0TTRiL', 'available': 2,
                  'updateTime': '2018-07-04 10:51:30.0', 'accessSecret': 'q6lW8WRGWT0x5Mhxwu4GysBtg29dPR',
                  'check': True}, {'accessId': 21, 'accessType': 'rw', 'csp': 'aliyun', 'companyId': 'abc',
                                   'clientId': '3AxO9eTYV1ciGdRdDafA9L', 'accessKey': 'LTAI5CjxNp0TTRiL',
                                   'available': 2, 'updateTime': '2018-07-04 10:51:30.0',
                                   'accessSecret': 'q6lW8WRGWT0x5Mhxwu4GysBtg29dPR'}]
    sort_list.sort(key=lambda x: x["accessId"])
    print(sort_list)

    filter_list = list(filter(lambda x: x["accessId"] == 21 and x["csp"] == "aliyun",sort_list))
    print(filter_list)

    s = lambda x: x + 2, list_int
    print(s)


def def_for_list():
    f = ["a", "b", "c"]
    fx = (item + "x" for item in f)
    print fx, ",".join(fx)

    fxl = list(item + "x" for item in f)
    print fxl, ",".join(fxl)

def def_map_list():
    f = ["a", "b", "c"]
    fx = list(map(lambda x:x+"x",f))
    print fx


if __name__ == '__main__':
    list_oprate()
