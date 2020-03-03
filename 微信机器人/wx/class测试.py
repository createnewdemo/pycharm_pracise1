class demo1(object):
    def func1(self):
        print('123')


class demo2(demo1):
    def func1(self):
        super(demo2, self).func1()
        print('456')


a = demo2()
a.func1()
