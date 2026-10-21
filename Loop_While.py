'''
Q.1 Print numbers from 1 to 10 using for loop.
'''
------------------------------------------------------------------------------
for i in range(1,11):
	print(i)


OUTPUT
----------
C:\Users\SHINDE FAMILY\pythonfile\Loop_While.py>python3 While1.py
1
2
3
4
5
6
7
8
9
10


'''
Q.2 Print numbers from 10 to 1 using for loop.
'''
---------------------------------------------------------------------------------
for i in range(10,0,-1):
	print(i)


OUTPUT
------------
C:\Users\SHINDE FAMILY\pythonfile\Loop_While.py>python3 While2.py
10
9
8
7
6
5
4
3
2
1


'''
Q.3 Print all even numbers between 1 and 50.
'''
------------------------------------------------------------------------------------
for i in range(2,51,2):
    print(i)


OUTPUT
----------
C:\Users\SHINDE FAMILY\pythonfile\Loop_While.py>python3 While3.py
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50


'''
Q.4 Print all odd numbers between 1 and 50.
'''
-----------------------------------------------------------------------------
for i in range(1,51,2):
    print(i)


OUTPUT
----------
C:\Users\SHINDE FAMILY\pythonfile\Loop_While.py>python3 While4.py
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49


'''
Q.5 Print multiplication table of a given number.
'''
----------------------------------------------------------------------------
num=int(input("Enter a number:"))

for i in range(1,11):
	print(num,"x",i,"=",num)


OUTPUT
---------------
C:\Users\SHINDE FAMILY\pythonfile\Loop_While.py>python3 While5.py
Enter a number:7
7 x 1 = 7
7 x 2 = 7
7 x 3 = 7
7 x 4 = 7
7 x 5 = 7
7 x 6 = 7
7 x 7 = 7
7 x 8 = 7
7 x 9 = 7
7 x 10 = 7


'''
Q.6 Calculate sum of first 10 natural numbers.
'''
----------------------------------------------------------------------------
sum=0

for i in range(1,11):
    sum=sum+i

print("Sum =",sum)


OUTPUT
------------
C:\Users\SHINDE FAMILY\pythonfile\Loop_While.py>python3 While6.py
Sum = 55


'''
Q.7 Calculate factorial of a number using for loop.
'''
----------------------------------------------------------------------------
num=int(input("Enter a number:"))

factorial=1

for i in range(1,num+1):
    factorial=factorial*i

print("Factorial=",factorial)


OUTPUT
------------
C:\Users\SHINDE FAMILY\pythonfile\Loop_While.py>python3 While7.py
Enter a number:8
Factorial= 40320


'''
Q.8 Print all characters of a string.
'''
------------------------------------------------------------------------------
text=input("Enter a string:")

for ch in text:
    print(ch)


OUTPUT
-------------
C:\Users\SHINDE FAMILY\pythonfile\Loop_While.py>python3 While8.py
Enter a string:Nandini
N
a
n
d
i
n
i


'''
Q.9 Print square of numbers from 1 to 10.
'''
-------------------------------------------------------------------------------
for i in range(1,11):
    print(i,"=",i**2)


OUTPUT
------------
C:\Users\SHINDE FAMILY\pythonfile\Loop_While.py>python3 While9.py
1 = 1
2 = 4
3 = 9
4 = 16
5 = 25
6 = 36
7 = 49
8 = 64
9 = 81
10 = 100


'''
Q.10  Print cube of numbers from 1 to 10.
'''
--------------------------------------------------------------------------------
for i in range(1,11):
    print(i,"=",i**3)


OUTPUT
-----------
C:\Users\SHINDE FAMILY\pythonfile\Loop_While.py>python3 While10.py
1 = 1
2 = 8
3 = 27
4 = 64
5 = 125
6 = 216
7 = 343
8 = 512
9 = 729
10 = 1000