Python 3.9.7 (default, Sep 16 2021, 16:59:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> a=np.array([5,6,9])
>>> a{0}
SyntaxError: invalid syntax
>>> a[0]
5
>>> a.ndim
1
>>> a=np.array([5,6,9])
>>> a=np.array([5,,9],[3,7])
SyntaxError: invalid syntax
>>> a.ndim
1
>>> a=np.array([5,9],[3,7])
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a=np.array([5,9],[3,7])
TypeError: Field elements must be 2- or 3-tuples, got '3'
>>> a=np.array([[5,,9],[3,7]])
SyntaxError: invalid syntax
>>> a=np.array([[5,9],[3,7]])
>>> a.ndim
2
>>> a.itemsize
4
>>> a.dtype
dtype('int32')
>>> a=np.array([[5,,9],[3,7]])
SyntaxError: invalid syntax
>>> a.itemsize
4
>>> a=np.array([[5,,9],[3,7]],dtype=np.float64)
SyntaxError: invalid syntax
>>> a=np.array([[5,9],[3,7]],dtype=np.float64)
>>> a.itemsize
8
>>> a
array([[5., 9.],
       [3., 7.]])
>>> a.size
4
>>> a.shape
(2, 2)
>>> a=np.array([[5,9],[3,7],[6,7]])
>>> a
array([[5, 9],
       [3, 7],
       [6, 7]])
>>> a=np.array([[5,9],[3,7],[6,7]],dtype=np.complex)

Warning (from warnings module):
  File "<pyshell#24>", line 1
DeprecationWarning: `np.complex` is a deprecated alias for the builtin `complex`. To silence this warning, use `complex` by itself. Doing this will not modify any behavior and is safe. If you specifically wanted the numpy scalar type, use `np.complex128` here.
Deprecated in NumPy 1.20; for more details and guidance: https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations
>>> np.zeros((3,4))
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
>>>  np.ones((3,4))
 
SyntaxError: unexpected indent
>>> np.ones((3,4))
array([[1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.]])
>>> l=range(5)
>>> l
range(0, 5)
>>> l[0]
0
>>> np.arange(1,5)
array([1, 2, 3, 4])
>>> np.arange(1,5,2)
array([1, 3])
>>> np.linspace(1.5.10)
SyntaxError: invalid syntax
>>> np.linspace(1,5,10)
array([1.        , 1.44444444, 1.88888889, 2.33333333, 2.77777778,
       3.22222222, 3.66666667, 4.11111111, 4.55555556, 5.        ])
>>> np.linspace(1,5,20)
array([1.        , 1.21052632, 1.42105263, 1.63157895, 1.84210526,
       2.05263158, 2.26315789, 2.47368421, 2.68421053, 2.89473684,
       3.10526316, 3.31578947, 3.52631579, 3.73684211, 3.94736842,
       4.15789474, 4.36842105, 4.57894737, 4.78947368, 5.        ])
>>> a=np.array([[5,9],[3,7],[6,7]])
>>> a.shape
(3, 2)
>>> a.reshape(2,3)
array([[5, 9, 3],
       [7, 6, 7]])
>>> a.reshape(6,1)
array([[5],
       [9],
       [3],
       [7],
       [6],
       [7]])
>>> a.ravel()
array([5, 9, 3, 7, 6, 7])
>>> a
array([[5, 9],
       [3, 7],
       [6, 7]])
>>> a.min()
3
>>> a.max()
9
>>> a.sum()
37
>>> #asda
>>> a.sum(axis=0)  #forrows
array([14, 23])
>>> a.sum(axis=1)
array([14, 10, 13])
>>> np.sqrt(a)
array([[2.23606798, 3.        ],
       [1.73205081, 2.64575131],
       [2.44948974, 2.64575131]])
>>> a
array([[5, 9],
       [3, 7],
       [6, 7]])
>>> np.std(a)
1.863389981249825
>>> a=np.array([[5,,9],[3,7]]
	   
SyntaxError: invalid syntax
>>> 
>>> 
>>> a=np.array([[5,9],[3,7]])
>>> b=np.array([[2,4],[8,3]])
>>> a+b
array([[ 7, 13],
       [11, 10]])
>>> a-b
array([[ 3,  5],
       [-5,  4]])
>>> a*b
array([[10, 36],
       [24, 21]])
>>> a/b
array([[2.5       , 2.25      ],
       [0.375     , 2.33333333]])
>>> a.dot(b)
array([[82, 47],
       [62, 33]])
>>> 