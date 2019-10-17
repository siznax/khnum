'''
Datapoint class
~~~~~~~~~~~~~~~
'''

from . import khnum


class Datapoint():

    '''
    represents a human readable number
    '''

    def __init__(self, num, units='d'):
        '''
        returns Datapoint instance
        '''
        self._num = num
        self.cnum = khnum.cnum(num)
        self.hnum = khnum.hnum(num, units)
        self.type = str(type(num))
        self.units = units

    def __str__(self):
        return khnum.pretty(dict(self.__dict__))

    def update(self, num, units='d'):
        '''
        update datapoint value with number and (optional) khnum units
        '''
        self.type = str(type(num))
        self._num = num
        self.cnum = khnum.cnum(num)
        self.hnum = khnum.hnum(num, units)
        self.units = units
