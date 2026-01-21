# 1)Palindrome
n = int(input("Enter a number: "))
original = n
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10
if original == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")
    
# 2) * Pattern
n = int(input("Enter a number: "))
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()
    
# 3) Number pattern 
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
    
# 4) Reverse string 
str1 = input("Enter a string: ")
reverse = str1[::-1]
print("Reversed string:", reverse)

# 5) Reverse Number 
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10     
    rev = rev * 10 + digit
    num = num // 10       
print("Reversed number:", rev)

# 6) Positive, Negative , Zero 
num = int(input("Enter a number: "))
if num > 0 and num != 0:
    print("Positive number")
elif num < 0 and num != 0:
    print("Negative number")
else:
    print("Zero")
    
 # 7) Bit in a number 
num = int(input("Enter a number: "))
pos = int(input("Enter bit position: "))
bit = (num >> pos) & 1
print("Bit at position", pos, "is:", bit)

# 8) Swap Numbers 
a = int(input("Enter a: "))
b = int(input("Enter b: "))
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)