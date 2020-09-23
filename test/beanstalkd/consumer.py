"""
Created by hu-jinwen on 2020/9/23
"""
import greenstalk

client = greenstalk.Client(('10.0.2.55', 11300), use="tube_1")

watching = client.watching()
using = client.using()

# client.use("tube_1")

client.watch("tube_1")

# client.put("Hello tube_1 1")
# # stats = client.stats()
job = client.reserve()
print(job)
#
# print()

client.close()

# job = client.reserve()
# print("拿到了job -> " + job)
# client.delete(job)
