## 0x09. Python - Everything is object

Orlando Gomez Lopez

Holberton

Cohort 10

Cali Colombia

15 january 2020

# Requirements

Python Scripts
	Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
	All your files should end with a new line
	The first line of all your files should be exactly #!/usr/bin/python3
	A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style (version 1.7.*)
	All your files must be executable
	The length of your files will be tested using wc
	.txt Answer Files
	Only one line
	No Shebang
	All your files should end with a new line

# Tasks

# 0. Who am I? mandatory

	What function would you use to print the type of an object?

	Write the name of the function in the file, without ().

	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 0-answer.txt

# 1. Where are you? mandatory

	How do you get the variable identifier (which is the memory address in the CPython implementation)?

	Write the name of the function in the file, without ().

	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 1-answer.txt

# 2. Right count mandatory

	In the following code, do a and b point to the same object? Answer with Yes or No.

	>>> a = 89
	>>> b = 100
	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 2-answer.txt

# 3. Right count = mandatory

	In the following code, do a and b point to the same object? Answer with Yes or No.

	>>> a = 89
	>>> b = 89
	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 3-answer.txt

# 4. Right count = mandatory

	In the following code, do a and b point to the same object? Answer with Yes or No.

	>>> a = 89
	>>> b = a
	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 4-answer.txt

# 5. Right count =+ mandatory

	In the following code, do a and b point to the same object? Answer with Yes or No.

	>>> a = 89
	>>> b = a + 1
	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 5-answer.txt

# 6. Is equal mandatory

	What do these 3 lines print?

	>>> s1 = "Holberton"
	>>> s2 = s1
>>> print(s1 == s2)
	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 6-answer.txt

# 7. Is the same mandatory

	What do these 3 lines print?

	>>> s1 = "Holberton"
	>>> s2 = s1
>>> print(s1 is s2)
	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 7-answer.txt

# 8. Is really equal mandatory

	What do these 3 lines print?

	>>> s1 = "Holberton"
	>>> s2 = "Holberton"
>>> print(s1 == s2)
	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 8-answer.txt

# 9. Is really the same mandatory

	What do these 3 lines print?

	>>> s1 = "Holberton"
	>>> s2 = "Holberton"
>>> print(s1 is s2)
	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 9-answer.txt

# 10. And with a list, is it equal mandatory

	What do these 3 lines print?

	>>> l1 = [1, 2, 3]
	>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 10-answer.txt

# 11. And with a list, is it the same mandatory

	What do these 3 lines print?

	>>> l1 = [1, 2, 3]
	>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 11-answer.txt

# 12. And with a list, is it really equal mandatory

	What do these 3 lines print?

	>>> l1 = [1, 2, 3]
	>>> l2 = l1
>>> print(l1 == l2)
	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 12-answer.txt

# 13. And with a list, is it really the same mandatory

	What do these 3 lines print?

	>>> l1 = [1, 2, 3]
	>>> l2 = l1
>>> print(l1 is l2)
	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 13-answer.txt

# 14. List append mandatory

	What does this script print?

	l1 = [1, 2, 3]
	l2 = l1
	l1.append(4)
print(l2)
	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 14-answer.txt

# 15. List add mandatory

	What does this script print?

	l1 = [1, 2, 3]
	l2 = l1
	l1 = l1 + [4]
print(l2)
	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 15-answer.txt

# 16. Integer incrementation mandatory

	What does this script print?

	def increment(n):
		n += 1

	a = 1
	increment(a)
print(a)
	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 16-answer.txt

# 17. List incrementation mandatory

	What does this script print?

	def increment(n):
		n.append(4)

	l = [1, 2, 3]
	increment(l)
print(l)
	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 17-answer.txt

# 18. List assignation mandatory

	What does this script print?

	def assign_value(n, v):
		n = v

		l1 = [1, 2, 3]
	l2 = [4, 5, 6]
	assign_value(l1, l2)
print(l1)
	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 18-answer.txt

# 19. Copy a list object mandatory

	Write a function def copy_list(l): that returns a copy of a list.

	The input list can contain any type of objects
Your file should be maximum 3-line long (no documentation needed)
	You are not allowed to import any module
	guillaume@ubuntu:~/0x09$ cat 19-main.py
#!/usr/bin/python3
	copy_list = __import__('19-copy_list').copy_list

	my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

	print(my_list)
print(new_list)

	print(new_list == my_list)
print(new_list is my_list)

	guillaume@ubuntu:~/0x09$ ./19-main.py
	[1, 2, 3]
	[1, 2, 3]
	[1, 2, 3]
	True
	False
	guillaume@ubuntu:~/0x09$ wc -l 19-copy_list.py 
	3 19-copy_list.py
	guillaume@ubuntu:~/0x09$ 
	No test cases needed

	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 19-copy_list.py

# 20. Tuple or not? mandatory

a = ()
	Is a a tuple? Answer with Yes or No.

	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 20-answer.txt

# 21. Tuple or not? mandatory

a = (1, 2)
	Is a a tuple? Answer with Yes or No.

	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 21-answer.txt

# 22. Tuple or not? mandatory

a = (1)
	Is a a tuple? Answer with Yes or No.

	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 22-answer.txt

# 23. Tuple or not? mandatory

a = (1, )
	Is a a tuple? Answer with Yes or No.

	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 23-answer.txt

# 24. Richard Sim's special #0 mandatory

	What does this script print?

	a = (1)
b = (1)
	a is b
	Task created by Richard Sim from Cohort 1 - San Francisco

	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 24-answer.txt

# 25. Richard Sim's special #1 mandatory

	What does this script print?

	a = (1, 2)
b = (1, 2)
	a is b
	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 25-answer.txt

# 26. Richard Sim's special #2 mandatory

	What does this script print?

	a = ()
b = ()
	a is b
	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 26-answer.txt

# 27. Richard Sim's special #3 mandatory

>>> id(a)
	139926795932424
	>>> a
	[1, 2, 3, 4]
	>>> a = a + [5]
>>> id(a)
	Will the last line of this script print 139926795932424? Answer with Yes or No.

	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 27-answer.txt

# 28. Richard Sim's special #4 mandatory

	>>> a
	[1, 2, 3]
>>> id (a)
	139926795932424
	>>> a += [4]
>>> id(a)
	Will the last line of this script print 139926795932424? Answer with Yes or No.

	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 28-answer.txt

# 29. Python3: Mutable, Immutable... everything is object! mandatory

	Write a blog post about everything you just learned / this project is covering. Your blog post should be articulated this way (one paragraph per item):

		introduction
		id and type
		mutable objects
		immutable objects
		why does it matter and how differently does Python treat mutable and immutable objects
		how arguments are passed to functions and what does that imply for mutable and immutable objects
		If you worked on advanced tasks, please also include what you did learn in those tasks in the blog post.

		Your posts should have many code/output examples to illustrate what you are explaining, and at least one picture, at the top. Publish your blog post on Medium or LinkedIn, and share it at least on Twitter and LinkedIn.

When done, please add all urls below (blog post, tweet, etc.)

	Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.

	Add URLs here:


# 30. #pythonic #advanced

	Write a function magic_string() that returns a string Holberton n times the number of the iteration (see code):

	Format: see example
Your file should be maximum 4-line long (no documentation needed)
	You are not allowed to import any module
	guillaume@ubuntu:~/0x09$ cat 100-main.py
#!/usr/bin/python3
	magic_string = __import__('100-magic_string').magic_string

	for i in range(10):
		print(magic_string())

		guillaume@ubuntu:~/0x09$ ./100-main.py | cat -e
		Holberton$
		Holberton, Holberton$
		Holberton, Holberton, Holberton$
		Holberton, Holberton, Holberton, Holberton$
		Holberton, Holberton, Holberton, Holberton, Holberton$
		Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
		Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
		Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
		Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
		Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
		guillaume@ubuntu:~/0x09$ wc -l 100-magic_string.py 
		4 100-magic_string.py
		guillaume@ubuntu:~/0x09$ 
		No test cases needed

		Repo:

		GitHub repository: holbertonschool-higher_level_programming
		Directory: 0x09-python-everything_is_object
		File: 100-magic_string.py

# 31. Low memory cost #advanced

		Write a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.

		You are not allowed to import any module
		guillaume@ubuntu:~/0x09$ cat 101-main.py
#!/usr/bin/python3
		LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()
	lc.first_name = "John"
	try:
	lc.last_name = "Snow"
	except Exception as e:
	print("[{}] {}".format(e.__class__.__name__, e))

	guillaume@ubuntu:~/0x09$ ./101-main.py
	[AttributeError] 'LockedClass' object has no attribute 'last_name'
	guillaume@ubuntu:~/0x09$ 
	No test cases needed

	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 101-locked_class.py

# 32. int 1/3 #advanced

	julien@ubuntu:/python3$ cat int.py 
	a = 1
	b = 1
	julien@ubuntu:/python3$ 
	Assuming we are using a CPython implementation of Python3 with default options/configuration:

	How many int objects are created by the execution of the first line of the script? (103-line1.txt)
How many int objects are created by the execution of the second line of the script (103-line2.txt)
	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 103-line1.txt, 103-line2.txt

# 33. int 2/3 #advanced

	julien@ubuntu:/python3$ cat int.py 
	a = 1024
	b = 1024
	del a
	del b
	c = 1024
	julien@ubuntu:/python3$ 
	Assuming we are using a CPython implementation of Python3 with default options/configuration:

	How many int objects are created by the execution of the first line of the script? (104-line1.txt)
	How many int objects are created by the execution of the second line of the script (104-line2.txt)
	After the execution of line 3, is the int object pointed by a deleted? Answer with Yes or No (104-line3.txt)
	After the execution of line 4, is the int object pointed by b deleted? Answer with Yes or No (104-line4.txt)
How many int objects are created by the execution of the last line of the script (104-line5.txt)
	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 104-line1.txt, 104-line2.txt, 104-line3.txt, 104-line4.txt, 104-line5.txt

# 34. int 3/3 #advanced

	julien@twix:/tmp/so$ cat int.py 
	print("I")
	print("Love")
	print("Python")
	julien@ubuntu:/tmp/so$ 
	Assuming we are using a CPython implementation of Python3 with default options/configuration:

	Before the execution of line 2 (print("Love")), how many int objects have been created and are still in memory? (105-line1.txt)
Why? (optional blog post :))
	Hint: NSMALLPOSINTS, NSMALLNEGINTS



	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 105-line1.txt

# 35. Clear strings mandatory

	guillaume@ubuntu:/python3$ cat string.py 
	a = "HBTN"
	b = "HBTN"
	del a
	del b
	c = "HBTN"
	guillaume@ubuntu:/python3$ 
	Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, dont spell out the word):

	How many string objects are created by the execution of the first line of the script? (106-line1.txt)
	How many string objects are created by the execution of the second line of the script (106-line2.txt)
	After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No (106-line3.txt)
	After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No (106-line4.txt)
How many string objects are created by the execution of the last line of the script (106-line5.txt)
	Repo:

	GitHub repository: holbertonschool-higher_level_programming
	Directory: 0x09-python-everything_is_object
	File: 106-line1.txt, 106-line2.txt, 106-line3.txt, 106-line4.txt, 106-line5.txt

