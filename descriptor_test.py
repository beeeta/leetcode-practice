
class Dec(object):
    def __init__(self):
        self.name = ''

    def __get__(self, instance, owner):
        return self.name

    def __set__(self, instance, value):
        self.name = value.title()

class Owner(object):
        d = Dec()

if __name__ == '__main__':
    owner = Owner()
    print(owner.d)
    owner.d = 'abc'
    print(owner.d)

