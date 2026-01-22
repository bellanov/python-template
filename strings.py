# strings
a = "Hello, World!"
print("String:", a, "Type:", type(a))

# immutability of strings
a = "hello"
b = a
a = a + "world!"
print(a)  # Output: helloworld!
print(b)  # Output: hello

# slicing
s = "Hello, Python!"
print(s[0])  # Output: H
print(s[7:13])  # Output: Python
print(s[-1])  # Output: !
print(s[:5])  # Output: Hello
print(s[::2])  # Output: Hlo yhn
print(s[::-1])  # Output: !nohtyP ,olleH
