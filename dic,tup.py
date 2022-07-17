Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d={'joe': 72314453,'rob': 89234557}
d
{'joe': 72314453, 'rob': 89234557}
d['joe']
72314453
d['umer']=23891479
d
{'joe': 72314453, 'rob': 89234557, 'umer': 23891479}
del d['joe']
d
{'rob': 89234557, 'umer': 23891479}
]
for key in d:
    print("key is: ",key,"value :",d{key})
    
SyntaxError: invalid syntax
for key in d:
    print("key is: ",key,"value :",d[key])

key is:  rob value : 89234557
key is:  umer value : 23891479
d
{'rob': 89234557, 'umer': 23891479}
'umer' in d
True
d.clear()
d
{}
