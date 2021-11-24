import hashlib
from Cryptodome.Cipher import AES

Foo = '\\xDE\\xAD\\xBE\\xEF'
Bar = '\\x4\\xL\\x1\\xC\\x3\\x1\\xS\\xN\\x0\\xT\\x4\\xS\\xL\\x3\\x3\\xP\\xS\\x4\\xV\\x3\\xH\\x3\\xR'
iv = hashlib.md5(Foo.encode()).digest()
key = hashlib.sha256(Bar.encode()).digest()

cipher = AES.new(key, AES.MODE_CBC, iv)

f = open('./AliceInCeptiondream.txt', 'rb')
b = f.read()

pt = cipher.decrypt(b)
open('another.exe', 'wb').write(pt)
