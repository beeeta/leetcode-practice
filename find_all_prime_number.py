# find all prime number
def _odd_gene():
    n = 1
    while True:
        n = n+2
        yield n

def _filter_prime(num):
    return lambda x:x % num >0

def prime(n):
    odd = _odd_gene()
    while True:
        item = next(odd)
        if n>item:
            yield item
            odd = filter(_filter_prime(item),odd)
        else:
            break

if __name__ == '__main__':
    for i in prime(1000):
        print(i)

