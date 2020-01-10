# coding: utf-8
import hashlib
a = "123456"
print (hashlib.md5(a).hexdigest())
print (hashlib.sha1(a).hexdigest())
print (hashlib.sha224(a).hexdigest())
print (hashlib.sha256(a).hexdigest())
print (hashlib.sha384(a).hexdigest())
print (hashlib.sha512(a).hexdigest())