
from itertools import chain,islice
# combine multi list to one
a = [1,2,3,4,'a']
b = ['a','b','c','d']
c = set().union(a).union(b) # remove repeated
print('remove repeated')
print(c)

e = a + b
print('keep repeated')
print(e)

f = chain(a,b)
print('keep repeated')
print(list(f))

# combine multidimension list to one
h = [a,b]
g = [i for j in h for i in j]
print(h)
print('cut dimension ')
print(g)
print('cut dimension method two')
print(sum(h,[]))

# count fiblaqi number
def count_fblq():
    i,j = 0,1
    while True:
        yield j
        i,j = j,i+j
cfblq = count_fblq()
print(list(islice(cfblq,10)))

# 函数连续调用
class Count(object):
    def __init__(self,count):
        self.count = count

    def __call__(self, num):
        return Count(self.count + num)

c = Count(1)(2)(3)(4)
print(c.count)