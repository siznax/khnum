Khnum
=====

[_Khnum_](https://en.wikipedia.org/wiki/Khnum) is the god of human readable numbers


Usage
-----

```
>>> import khnum

>>> khnum.human_number(123456789)
'123.5M'

>>> khnum.human_number(123456789, 'b')
'123.5MB'

>>> khnum.human_number(123456789, 's')
'117.7MiB'

>>> khnum.human_number(123456789e24, 's')
'102121062.3YiB'
```


Help
----

```
$ pydoc khnum.human_number

Help on function human_number in khnum:

khnum.human_number = human_number(num, units='decimal')
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
```


Contributors
------------

* [Fred Cirera](https://stackoverflow.com/questions/1094841/reusable-library-to-get-human-readable-version-of-file-size)



@siznax
