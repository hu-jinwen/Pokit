"""
Created by hu-jinwen on 2020/9/27
"""
from pokit.tools.priority_blocking_queue import PriorityBlockingQueue

queue = PriorityBlockingQueue()

queue.put("Hello World")
queue.put("Hello World2")
queue.put("Hello World3")
poll = queue.poll()
queue_poll = queue.poll()
n = queue.poll()

print()
