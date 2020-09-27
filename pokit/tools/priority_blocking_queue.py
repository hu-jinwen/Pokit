"""
Created by hu-jinwen on 2020/9/7
"""
import time

from gevent.queue import PriorityQueue


class PriorityBlockingQueue(object):
    """
    带优先级的阻塞队列。
    优先级数字越小，优先级越高。

    插入元素：
    * put: 向队列尾部插入一个元素，如果该队列已满，则一直阻塞。
    * offer: 向队列尾部插入一个元素，插入成功返回True。插入失败返回False。

    获取元素：
    * poll: 获取并移除队列的头元素，若队列为空，则返回null。
    * take: 获取并移除队列的头元素，若队列为空，则一直阻塞。
    * peek：获取但不移除队列的头元素，若队列为空，则返回null

    队列状态状态：
    * qsize：获取队列中当前元素数量
    * maxsize：获取队列的最大容量
    """

    def __init__(self, maxsize: int = None):
        """
        init
        :param maxsize: 队列的最大容量
        """
        self.__queue = PriorityQueue(maxsize=maxsize)

    def put(self, item, priority: int = 200) -> None:
        """
        向队列尾部插入一个元素，如果该队列已满，则一直阻塞。
        :param item:
        :param priority: 优先级
        :return:
        """
        while True:
            try:
                self.__queue.put((priority, item))
                break
            except Exception:
                pass
            time.sleep(0.5)

    def offer(self, item, priority: int = 200) -> bool:
        """
        向队列尾部插入一个元素，插入成功返回True。插入失败返回False。
        :param item: 元素
        :param priority: 优先级
        :return:
        """
        try:
            self.__queue.put((priority, item), block=False)
        except Exception:
            return False
        return True

    def poll(self):
        """
        获取并移除队列的头元素，若队列为空，则返回null。
        :return:
        """
        try:
            return self.__queue.get(block=False)[1]
        except Exception:
            pass
        return None

    def take(self):
        """
        获取并移除队列的头元素，若队列为空，则一直阻塞。
        :return:
        """
        while True:
            try:
                return self.__queue.get()[1]
            except Exception:
                pass
            time.sleep(0.5)

    def peek(self):
        """
        获取但不移除队列的头元素，若队列为空，则返回null
        :return:
        """
        try:
            return self.__queue.peek(block=False)[1]
        except Exception:
            pass
        return None

    def qsize(self) -> int:
        """
        获取队列中当前元素数量
        :return:
        """
        return self.__queue.qsize()

    def maxsize(self) -> int:
        """
        获取队列的最大容量
        :return:
        """
        return self.__queue.maxsize
