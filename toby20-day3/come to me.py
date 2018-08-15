Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: /home/student/toby20-day3/grretingpt2.py =============
What is your name?toby
Hello theretoby
>>> 
============= RESTART: /home/student/toby20-day3/grretingpt2.py =============
What is your name?tboy
Traceback (most recent call last):
  File "/home/student/toby20-day3/grretingpt2.py", line 2, in <module>
    print("Hello there " + capitalize(name))
NameError: name 'capitalize' is not defined
>>> 
============= RESTART: /home/student/toby20-day3/grretingpt2.py =============
What is your name?toby
Hello there Toby
>>> 
============= RESTART: /home/student/toby20-day3/grretingpt2.py =============
What is your name?tobias
Hello there Tobias
Traceback (most recent call last):
  File "/home/student/toby20-day3/grretingpt2.py", line 4, in <module>
    print("Your name is" + llen(name) + "letters long!")
NameError: name 'llen' is not defined
>>> 
============= RESTART: /home/student/toby20-day3/grretingpt2.py =============
What is your name?tobias
Hello there Tobias
Traceback (most recent call last):
  File "/home/student/toby20-day3/grretingpt2.py", line 4, in <module>
    print("Your name is" + len(name) + "letters long!")
TypeError: must be str, not int
>>> 
============= RESTART: /home/student/toby20-day3/grretingpt2.py =============
What is your name?tobias
Hello there Tobias
Your name is6letters long!
>>> 
============= RESTART: /home/student/toby20-day3/grretingpt2.py =============
What is your name?aviv
Hello there Aviv
Your name is 4 letters long!
>>> 
============= RESTART: /home/student/toby20-day3/grretingpt2.py =============
What is your name?toby
Hello there Toby
Your name is 4 letters long!
The first letter of your name is t
>>> 
============= RESTART: /home/student/toby20-day3/grretingpt2.py =============
What is your name?toby
Hello there Toby
Your name is 4 letters long!
Traceback (most recent call last):
  File "/home/student/toby20-day3/grretingpt2.py", line 5, in <module>
    print("The first letter of your name is " + name[0].capitalize)
TypeError: must be str, not builtin_function_or_method
>>> 
============= RESTART: /home/student/toby20-day3/grretingpt2.py =============
What is your name?toby
Hello there Toby
Your name is 4 letters long!
The first letter of your name is T
>>> var='hi, there'
>>> var[0:9]
'hi, there'
>>> var[9]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    var[9]
IndexError: string index out of range
>>> var[8]
'e'
>>> var[len(var) - 1]
'e'
>>> 
============= RESTART: /home/student/toby20-day3/grretingpt2.py =============
What is your name?toby
Hello there Toby
Your name is 4 letters long!
Traceback (most recent call last):
  File "/home/student/toby20-day3/grretingpt2.py", line 5, in <module>
    print("The first letter of your name is " + name[0].capitalize() + "and the last letter in your name is " + name[len(name) - 1].capitalize)
TypeError: must be str, not builtin_function_or_method
>>> 
============= RESTART: /home/student/toby20-day3/grretingpt2.py =============
What is your name?tobia
Hello there Tobia
Your name is 5 letters long!
The first letter of your name is Tand the last letter in your name is A
>>> mystring = "Hi there, my name is Claire. Nice to meet you!"
>>> mystring[20]
' '
>>> mystring[21]
'C'
>>> mystring[21:27]
'Claire'
>>> 
