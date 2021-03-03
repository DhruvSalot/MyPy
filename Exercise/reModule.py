import re
x = "My phone no. is 985-938-9876 and (987) 098-9883."

compiling = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d|\(\d\d\d\) \d\d\d-\d\d\d\d')

y = compiling.findall(x)

print (y)


# Output:
# ['985-938-9876', '(987) 098-9883']
