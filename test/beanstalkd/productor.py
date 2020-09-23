"""
Created by hu-jinwen on 2020/9/23
"""
import greenstalk

client = greenstalk.Client(('10.0.2.55', 11300), use="tube_1")

# client.use("tube_1")

status = client.put("Hello tube1")
print(status)

client.close()

