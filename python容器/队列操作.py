import queue
'''
队列的增加删除
'''


def queue_get():
    ak_queue = queue.Queue()
    ak_queue.put((1,2,3,4,4,5,6))
    ak_queue.put((1,2,3,4,4,5,6,7,8,9))

    # while True:
    #     print(ak_queue.get(timeout=1))

    while not ak_queue.empty():
        print(ak_queue.get())


if __name__ == '__main__':
    queue_get()