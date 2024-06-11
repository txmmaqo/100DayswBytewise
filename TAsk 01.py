Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #ex 1
>>> var1= int(input("Enter first number: "))
Enter first number: 3
>>> var2=int(input("Enter second number: "))
Enter second number: 4
>>> sum=var1+var2
>>> print(sum)
7
>>> #ex2
>>> r = int(input("Enter radius of circle: "))
Enter radius of circle: 5
>>> area = (22/7)*r*r
>>> print(area)
78.57142857142857
>>> #ex3
>>> num=int(input("Enter a number: "))
Enter a number: 7
>>> if(num/2 !=0):
...     print(num, " is odd")
... else:
...     print(num, " is even.")
... 
7  is odd
>>> num1 = int(input("Enter fisrt number: "))
Enter fisrt number: 10
>>> num2 = int(input("Enter second number: "))
Enter second number: 3
>>> opr = intput("Enter operation(:
...              
SyntaxError: unterminated string literal (detected at line 1)
>>> opr = intput("Enter operation(+,-,*,/): ")
...              
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    opr = intput("Enter operation(+,-,*,/): ")
NameError: name 'intput' is not defined. Did you mean: 'input'?
>>> opr = intput("Enter operation(+,-,*,/): "))
SyntaxError: unmatched ')'
opr = input("Enter operation(+,-,*,/): ")
Enter operation(+,-,*,/): /
if(opr == '+'):
    print(num1+num2)
elif(opr == '-'):
    print(num1-num2)
elif(opr == '*')
SyntaxError: expected ':'
if(opr == '+'):
    print(num1+num2)
elif(opr == '-'):
    print(num1-num2)
elif(opr == '*'):
    print(num1*num2)
elif(opr == '/'):
    print(num1/num2)
else:
    print("Erroe")

    
3.3333333333333335
#ex5
n1 = int(input("Enter first number: " ))
Enter first number: 7
n2 = int(input("Enter second number: "))
Enter second number: 15
n3 = int(input("Enter third number: "))
Enter third number: 10
list = [n1, n2, n3]
print(max(list))
15
#ex6
word = input("Enter a word: ")
Enter a word: hello
reversed_word=[::-1]
SyntaxError: invalid syntax
reversed_word=word[::-1]
print(reversed_word)
olleh
#ex7
word = input("Enter a word: ")
Enter a word: Euouae
vowels = "aeiouAEIOU"
vowel_count= 0
for char in word:
    if char in vowels:
        vowel_count +=1

        
print("The number of vowels in ", word," is "," vowel_count.")
The number of vowels in  Euouae  is   vowel_count.
print("The number of vowels in ", word," is ", vowel_count)
The number of vowels in  Euouae  is  6
#ex7 
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Example usage:
n = 10  # Number of terms in the Fibonacci series
fib_series = fibonacci(n)
print(f"Fibonacci series up to {n} terms: {fib_series}")


