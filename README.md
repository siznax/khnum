khnum 𓎹𓃝
==========

<a href="https://en.wikipedia.org/wiki/Khnum"><img
 alt="Khnum image" align="right"
 src="https://upload.wikimedia.org/wikipedia/commons/5/5e/Khnum.svg"></a>

the god of human readable numbers


Install
-------

```
pip install khnum
𓎹𓃝
```

Usage
-----

```
import khnum
```

Examples
--------

```
>>> khnum.cnum(1234567890)
'1,234,567,890'
```

```
>>> khnum.hnum(1234567890)
'1.2B'
```

```
>>> khnum.hnum(1234567890, 'bytes')
'1.2GB'
```

```
>>> khnum.hnum(1234567890, 'si')
'1.1GiB'
```

```
>>> num = khnum.num(1234567890, 'b')
>>> print(num)
{
    "_num": 1234567890,
    "cnum": "1,234,567,890",
    "hnum": "1.2GB",
    "line": "1.2GB (1,234,567,890)",
    "type": "<class 'int'>",
    "units": "b"
}
```


Help
----

```
$ pydoc khnum
```

```
>>> help(khnum)
```


Test
----

```
$ pytest
```


Contributors
------------

* [Fred Cirera](https://stackoverflow.com/questions/1094841/reusable-library-to-get-human-readable-version-of-file-size)


@siznax
