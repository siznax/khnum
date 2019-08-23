'''
Khnum
~~~~~
'''

def human_number(num, units='decimal'):
    '''
    returns a human readable number from num and units

    raises ValueError for un-supported units

    For example:  num = 123456789  (123,456,789)

        units = 'd[ecimal]' => 123.5M   (million)
        units = 'b[ytes]'   => 123.5MB  (megabytes)
        units = 's[i]'      => 117.7MiB (mebibytes)

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

    Based on Fred Cirera's solution:
    https://stackoverflow.com/questions/1094841/reusable-library-to-get-human-readable-version-of-file-size
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
