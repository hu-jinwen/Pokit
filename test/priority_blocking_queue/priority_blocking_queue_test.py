"""
Created by hu-jinwen on 2020/9/27
"""
from pokit.tools.priority_blocking_queue import PriorityBlockingQueue

queue = PriorityBlockingQueue()

queue.put({"1": "sss"}, 23424234)
queue.put({"2": "ss"}, 234243)
queue.put({"3": "ssssss"}, 2)
poll = queue.poll()
queue_poll = queue.poll()
n = queue.poll()

print()
