# -*- coding: utf-8 -*-
import hashlib
# from crypto.Cipher import AES
import base64
user = 'jointwisdom'
pwd ="8F, Block E, Dazhongsi Zhongkun Plaza, No. A18 West Beisanhuan Road, Haidian District, Beijing"
pw1 = bytes(pwd, encoding = "utf8")
print(type(pw1))
m2 = hashlib.md5()
m2.update(pw1)
print(m2.hexdigest())

