Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def isPalindrome(word):
    word = word.lower()
    if word == word[::-1]:
        return(word, " is Palindrome.")
    else:
        return(word, " is not Palindrome.")

    
print(isPalindrome("racecar"))
('racecar', ' is Palindrome.')
print(isPalindrome("python"))
('python', ' is not Palindrome.')
#ex2
def fizz_buss():
    for i range(1, 101):
        
SyntaxError: invalid syntax
def fizz_buss():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
fizz_buss()
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz
#ex3
def fib(n):
    a,b = b, a+b
    return a

def nth_fibonacci(n):
    a, b = 0., 1
    for _ in range(n):
        a, b = b ,a+b
    return a

def ordianl_suffix(n):
    if 10 <= n % 100 <=20:
        suffix = "th"
    else:
        suffix ={1: 'st', 2: 'nd', 3:'rd'}.get(n % 10, 'th')
    return suffix

n = 10
fib_number = nth_fibonacci(n)
print("The ", n, ordianl_suffix(n), " Fibonacci number is ", fib_number)
The  10 th  Fibonacci number is  55.0
#ex 4
def isPrime(num):
    if num<=1:
        return(num, " aint prime number")
    for i in range (2, int(number * 0.5) +1):
        if number % i ==0:
            return(num, "aint prime number.")
        else:
            return(num, " is prime number.")
def isPrime(num):
    if num<=1:
        return(num, " aint prime number")
    for i in range (2, int(num * 0.5) +1):
        if num % i ==0:
            return(num, "aint prime number.")
        else:
            return(num, " is prime number.")

        
print(isPrime(7))
(7, ' is prime number.')
print(isPrime(10))
(10, 'aint prime number.')
#ex5
import random
def guesssNum():
    number_to_guess = random.randint(1,100)
    attempts = 0
    print("Greeting! Guess what number im thinkinh of in between 1 to 100")
    while True:
        try:
            user_guess=int(input("Enter what you guessed: "))
            attempts +=1
            if user_guess <number_to_guess
            
SyntaxError: expected ':'
def guesssNum():
    number_to_guess = random.randint(1,100)
    attempts = 0
    print("Greeting! Guess what number im thinkinh of in between 1 to 100")
    while True:
        try:
            user_guess=int(input("Enter what you guessed: "))
            attempts +=1
            if user_guess <number_to_guess:
                return("Too low!ome again.")
            elis user_guess > number_to_guess:
                
SyntaxError: invalid syntax
def guesssNum():
    number_to_guess = random.randint(1,100)
    attempts = 0
    print("Greeting! Guess what number im thinkinh of in between 1 to 100")
    while True:
        try:
            user_guess=int(input("Enter what you guessed: "))
            attempts +=1
            if user_guess <number_to_guess:
                return("Too low!ome again.")
            elif user_guess > number_to_guess:
                return("Too High! Try again.")
            else:
                return("Aww, youve guessed it right :)", number_to_guess)
                break
        except ValueError:
            print("Invalid Iput. Enter a valid number.")

            
guesssNum()
Greeting! Guess what number im thinkinh of in between 1 to 100
Enter what you guessed: 2
'Too low!ome again.'
3
3
4
4
2
2
guesssNum()
Greeting! Guess what number im thinkinh of in between 1 to 100
Enter what you guessed: 6
'Too low!ome again.'

guesssNum()
Greeting! Guess what number im thinkinh of in between 1 to 100
Enter what you guessed: 3
'Too low!ome again.'
#ex6
def squaresList(n):
    squares = [i**2 for i in range (1, n+1)]
    return sqaures

squares_list=squaresList(10)
def squaresList(n):
    squares = [i**2 for i in range (1, n+1)]
    return squares

squares_list = suqaeesList(10)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    squares_list = suqaeesList(10)
NameError: name 'suqaeesList' is not defined. Did you mean: 'squaresList'?
squares_list = suqaresList(10)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    squares_list = suqaresList(10)
NameError: name 'suqaresList' is not defined. Did you mean: 'squaresList'?
squares_list = squaresList(10)
print(squares_list)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#ex7
import string
def isPalindrome(sentence):
    sentencesCleaned= ''.join(char.lower() for char in sentence if char.isalnum())
    if sentencesCleaned == sentencesCleaned[::-1]:
        return(sentence, "is palindrome")
    else:
        return(sentence," aint palindrome")

    
print(isPalindrome("A man, a plan, a canal: Panama"))
('A man, a plan, a canal: Panama', 'is palindrome')
print(isPalindrome("Hello World"))
('Hello World', ' aint palindrome')
#ex 8
>>> def anagrams(str1,str2):
...     cleanedStr1= ''.join(str1.split()).lower()
...     cleanedStr2=''.join(str1.split()).lower()
...     if sorted(cleanedStr1) == sorted(cleanedStr2):
...         return(str1, " and ", str2, " are anagrams")
...     else:
...         return(str1, " and ", str2,"are not anagrams.")
... 
...     
>>> print(anagrams("listen", "silent"))
('listen', ' and ', 'silent', ' are anagrams')
>>> print(anagrams("pythin", "java"))
('pythin', ' and ', 'java', ' are anagrams')
>>> #ex 9
>>> def reverse(sentece):
...     word = sentence.split()
...     reversed_words = word[::-1]
...     reversedSentence = ''.join(reversed_words)
...     return reversedSentence
... 
>>> sentence = "The quick brown fox jumps over lazy dog."
>>> reversedSentence = reverse(sentence)
>>> print(reversedSentence)
dog.lazyoverjumpsfoxbrownquickThe
>>> #ex10
>>> def celToF(cel):
...     return(cel*9/5)
... 
>>> def celToK
SyntaxError: expected '('
>>> def celToK(cel):
...     return cel+273.15
... 
>>> def tempConv(cel):
...     F = celToF(cel)
...     K = celToK(cel)
...     return(cel ," degrees Celsius = ", F " degrees F and ", K ," degrees K.")
SyntaxError: invalid syntax
>>> def tempConv(cel):
...     F = celToF(cel)
...     K = celToK(cel)
...     return(cel ," degrees Celsius = ", F ," degrees F and ", K ," degrees K.")
... 
>>> celTemp=20
>>> print(tempConv(celTemp))
(20, ' degrees Celsius = ', 36.0, ' degrees F and ', 293.15, ' degrees K.')
