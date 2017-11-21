from multiprocessing.dummy import Pool as ThreadPool  # 这里是多线程 去掉dummy编程多进程
import time

urls=["http://www.sina.com.cn/"]*10
pool = ThreadPool(4)

print(time.time())
pool.map(requests.get,urls)
print(time.time())