def del_dict():
    ak_dict = {"a": 1, "b": 2, "c": 3}

    del ak_dict["cc"]
    print(ak_dict)


def del_list():
    list_int = [1, 2, 3, 4, 5]

    del list_int[0]
    print(list_int)

    dict_del= {'accessId': 22,'csp': 'aliyun', 'companyId': '2V7tReeFv6GYHh5Gjr5KpO',
                  'clientId': '3AxO9eTYV1ciGdRdDafA9L', 'accessKey': 'LTAI5CjxNp0TTRiL', 'available': 2,
                  'updateTime': '2018-07-04 10:51:30.0', 'accessSecret': 'q6lW8WRGWT0x5Mhxwu4GysBtg29dPR',
                  'check': True, 'accessType': 'rw'}

    info_list = [{'accessId': 21, 'accessType': 'rw', 'csp': 'aliyun', 'companyId': 'abc',
                  'clientId': '3AxO9eTYV1ciGdRdDafA9L', 'accessKey': 'LTAI5CjxNp0TTRiL',
                  'available': 2, 'updateTime': '2018-07-04 10:51:30.0',
                  'accessSecret': 'q6lW8WRGWT0x5Mhxwu4GysBtg29dPR'},
                {'accessId': 22, 'accessType': 'rw', 'csp': 'aliyun', 'companyId': '2V7tReeFv6GYHh5Gjr5KpO',
                  'clientId': '3AxO9eTYV1ciGdRdDafA9L', 'accessKey': 'LTAI5CjxNp0TTRiL', 'available': 2,
                  'updateTime': '2018-07-04 10:51:30.0', 'accessSecret': 'q6lW8WRGWT0x5Mhxwu4GysBtg29dPR',
                  'check': True}
                 ]

    filter_ele = list(filter(lambda x: x["accessKey"] == dict_del["accessKey"] and x["accessSecret"] == dict_del["accessSecret"] , info_list))
    print(filter_ele[0])

    print(info_list.index(dict_del))


if __name__ == '__main__':
    # del_dict()
    del_list()
