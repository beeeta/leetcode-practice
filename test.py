class Te(object):
    def __getattr__(self, item):
        print('get attr')
        return Te.__dict__[item]

    # def __getattribute__(self, item):
    #     print('get attribute')
    #     return Te.__dict__[item]

    name ='haha'

if __name__ == '__main__':
    te = Te()
    print(te.afa)