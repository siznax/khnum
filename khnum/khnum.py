'''
Khnum functions
~~~~~~~~~~~~~~~
'''

import json

UNITS = ['decimal', 'bytes', 'si']


def cnum(num):
    '''
    returns str with thousands separated by commas

    >>> khnum.cnum(123456789)
    '123,456,789'
    '''
    return "{:,}".format(num)


def hnum(num, units='decimal'):
    '''
    returns rounded human readable str with units suffix

    >>> khnum.hnum(123456789)  # decimal
    '123.5M'  # million

    >>> khnum.hnum(123456789, 'b')  # bytes
    '123.5MB'  # megabytes

    >>> khnum.hnum(123456789, 's')  # SI
    '117.7MiB'  # mebibytes

    >>> khnum.hnum(123456789e24, 'si')
    '102121062.3YiB'  # yobibytes

    raises ValueError for un-supported units

    Power  Decimal   Bytes      SI (binary)
    ---------------------------------------------
    10^3   Kilo (K)  Kilo (KB)  1024^1 Kibi (KiB)
    10^6   Mill (M)  Mega (MB)  1024^2 Mebi (MiB)
    10^9   Bill (B)  Giga (GB)  1024^3 Gibi (GiB)
    10^12  Tril (T)  Tera (TB)  1024^4 Tebi (TiB)
    10^15  Quad (Q)  Peta (PB)  1024^5 Pebi (PiB)
    10^18  Quin (Qn) Exa- (EB)  1024^6 Exbi (EiB)
    10^21  Sext (S)  Zeta (ZB)  1024^7 Zebi (ZiB)
    10^24  Sept (Sp) Yota (YB)  1024^8 Yobi (YiB)
    '''

    if units.lower().startswith('d'):  # decimal
        units = ['', 'K', 'M', 'B', 'T', 'Q', 'Qn', 'S']
        boundary = 1000.0
        last_unit = 'Sp'
        suffix = ''
    elif units.lower().startswith('b'):  # bytes
        units = ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']
        boundary = 1000.0
        last_unit = 'Y'
        suffix = 'B'
    elif units.lower().startswith('s'):  # SI
        units = ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']
        boundary = 1024.0
        last_unit = 'Yi'
        suffix = 'B'
    else:
        raise ValueError('unsupported units: %s' % units)

    for unit in units:
        if abs(num) < boundary:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= boundary

    return "%.1f%s%s" % (num, last_unit, suffix)


def pretty(data):
    '''
    returns prettified JSON from data
    '''
    return json.dumps(data,
                      indent=4,
                      sort_keys=True,
                      separators=(',', ': '))
