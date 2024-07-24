import time
def for_loop(n):
    result = []
    for i in range(n):
        result.append(i**2)
    return result

def list_comprehension(n):
    return [i**2 for i in range(n)]
# '''begin = time.time()
# for_loop(10*6)
# end = time.time()
# print('Time taken For_loop:', round(end-begin, 2))'''
# begin = time.time()
print(list_comprehension(10))
# end = time.time()
# print('Time taken By List_comprehension:', round(end-begin, 2))