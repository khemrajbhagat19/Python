import sys

from Day5.Iterator import iter_obj


class my_range:
    def __init__(self,start=0,stop=None,step=1):
        self.start=start
        self.stop=stop
        self.step=step
    def __iter__(self):
        return my_range_iterator(self)

class my_range_iterator:
    def __init__(self,iterable_obj):
        self.iterable_obj=iterable_obj
    def __iter__(self):
        return self
    def __next__(self):
        if self.iterable_obj.start<=self.iterable_obj.stop:
            return self.iterable_obj.start
            self.iterable_obj.start=self.iterable_obj.start+self.iterable_obj.step
            return result
        else:
            raise StopIteration

num=my_range(1,10)
iter_obj=iter(num)
