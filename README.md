khnum
=====

<img alt="Khnum image" align="right"
 src="https://upload.wikimedia.org/wikipedia/commons/5/5e/Khnum.svg">

the god of human readable numbers

Install
-------

```
pip install khnum
```

Usage
-----

```
import khnum
```

Help
----

```
Help on module khnum.khnum in khnum:

NAME
    khnum.khnum

FUNCTIONS
    cnum(num)
        returns str with thousands separated by commas
        
        >>> khnum.cnum(123456789)
        '123,456,789'
    
    hnum(num, units='decimal')
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
```

Contributors
------------

* [Fred Cirera](https://stackoverflow.com/questions/1094841/reusable-library-to-get-human-readable-version-of-file-size)


@siznax
