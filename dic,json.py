Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

===== RESTART: C:/Users/write/AppData/Local/Programs/Python/Python310/y.py =====
{"Tom": {"name": "Tom", "address": "1 tom street", "phone": 43563767}, "bob": {"name": "bob", "address": "1 bob street", "phone": 463573767}}

===== RESTART: C:/Users/write/AppData/Local/Programs/Python/Python310/y.py =====
{"Tom": {"name": "Tom", "address": "1 tom street", "phone": 43563767}, "bob": {"name": "bob", "address": "1 bob street", "phone": 463573767}}
Traceback (most recent call last):
  File "C:/Users/write/AppData/Local/Programs/Python/Python310/y.py", line 16, in <module>
    with open("f://pythonjson//book.txt","w") as f:
FileNotFoundError: [Errno 2] No such file or directory: 'f://pythonjson//book.txt'

===== RESTART: C:/Users/write/AppData/Local/Programs/Python/Python310/y.py =====
{"Tom": {"name": "Tom", "address": "1 tom street", "phone": 43563767}, "bob": {"name": "bob", "address": "1 bob street", "phone": 463573767}}

===== RESTART: C:/Users/write/AppData/Local/Programs/Python/Python310/y.py =====
f=open("f://pythonjson//book.txt","r")
s=f.read()
s
'{"Tom": {"name": "Tom", "address": "1 tom street", "phone": 43563767}, "bob": {"name": "bob", "address": "1 bob street", "phone": 463573767}}'
import json
book=json.load(s)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    book=json.load(s)
  File "C:\Users\write\AppData\Local\Programs\Python\Python310\lib\json\__init__.py", line 293, in load
    return loads(fp.read(),
AttributeError: 'str' object has no attribute 'read'
book=json.loads(s)
                 
book
                 
{'Tom': {'name': 'Tom', 'address': '1 tom street', 'phone': 43563767}, 'bob': {'name': 'bob', 'address': '1 bob street', 'phone': 463573767}}
type(book)
                 
<class 'dict'>
\
book['bob']
                 
{'name': 'bob', 'address': '1 bob street', 'phone': 463573767}
book['bob']['phone']
                 
463573767
for person in book
                 
SyntaxError: expected ':'
for person in book:
                 print(book[person])

                 
{'name': 'Tom', 'address': '1 tom street', 'phone': 43563767}
{'name': 'bob', 'address': '1 bob street', 'phone': 463573767}
