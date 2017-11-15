class T:
    def __get__(self, instance, owner):
        print('T get ')
        return 'ttt'

class M:
    t = T()

    @classmethod
    def get_t(cls):
        cls.__dict__['t'] = 'dict_value'


M.get_t()
M.t