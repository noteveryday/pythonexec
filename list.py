import time
min_time = 1000
avg_time = 0.0
for num in range(1000):
    start_clock = time.clock()
    a = [(x,y) for x in range(100) for y in range(100)]
    end_clock = time.clock()
    avg_time = end_clock - start_clock
    if (end_clock - start_clock) < min_time:
        min_time = end_clock - start_clock
print("min_time = " , min_time)
print("avg_time= ", avg_time)
