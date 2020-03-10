import queue

data_queue = queue.Queue() # 일반적인 FIFO 정책인 큐
data_queue.put(11)
data_queue.put(13)

print(data_queue.qsize())
print(data_queue.get())
print(data_queue.get())

print("----------------------")

data_queue2 = queue.LifoQueue()
data_queue2.put("asdf")
data_queue2.put(1)
print(data_queue2.qsize())
print(data_queue2.get())
print(data_queue2.get())

print("----------------------")

data_queue3 = queue.PriorityQueue()
data_queue3.put((10,"korea"))
data_queue3.put((5,1))
data_queue3.put((15,"china"))
print(data_queue3.qsize())