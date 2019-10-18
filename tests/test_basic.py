'''
Khnum basic tests
'''

from khnum import khnum  # export PYTHONPATH=..


def test_datapoint():
    num = khnum.num(1234567890)
    assert num.cnum == '1,234,567,890'
    assert num.hnum == '1.2B'

def test_datapoint_bytes():
    num = khnum.num(1234567890, 'byte')
    assert num.cnum == '1,234,567,890'
    assert num.hnum == '1.2GB'

def test_datapoint_print():
    num = khnum.num(1234567890)
    print(num)

def test_datapoint_si():
    num = khnum.num(1234567890, 'si')
    assert num.cnum == '1,234,567,890'
    assert num.hnum == '1.1GiB'

def test_datapoint_update():
    num = khnum.num(1234567890)

    assert num.cnum == '1,234,567,890'
    assert num.hnum == '1.2B'

    num.update(987654321, 'b')

    assert num.cnum == '987,654,321'
    assert num.hnum == '987.7MB'

def test_datapoint_compact():
    num = khnum.num(1234567890, 'b')
    assert num.line == '1.2GB (1,234,567,890)'
