"""
方法是通过描述器来实现的,通过__get__定义绑定的和非绑定的方法

"""
class Te(object):

    def a(self):
        print('a print it')

    b = 'c'

if __name__ == '__main__':
    t = Te()
    print(dir(t.a))
    print(dir(Te.a))
    print('--------------')
    print(dir(t.b))
    print(dir(Te.b))