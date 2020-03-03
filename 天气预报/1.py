# -*- coding: gbk -*-
d = {'a': 1, 'b': 2, 'c': 3}
# 遍历key
# for key in d:
# #     print(key)
# 遍历value
# for value in d.values():
#     print(value)
# for k,v in d.items():
#     print(k,v)
from collections.abc import Iterable

isinstance('abc', Iterable)
isinstance(123, Iterable)
