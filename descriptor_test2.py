import time

class cache_property(object):

    def __init__(self,func):
        self.func = func

    def __get__(self, instance, owner):
        print(instance)
        value = instance.__dict__[self.func.__name__] = self.func(instance)
        return value

    # def __set__(self, instance, value):
    #     pass

class Master(object):

    @cache_property
    def cal(self):
        print(time.sleep(1))
        print('sleep finish')
        return 'ss'


if __name__ == '__main__':
    m = Master()
    print(m.cal)
    print('again')
    del m.cal # delete the key-value in dict
    print(m.cal)