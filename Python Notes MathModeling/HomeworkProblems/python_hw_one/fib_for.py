# question 8
# given n output the first n terms of the fibonacci sequence with a for loop
print('calculating fibonacci sequence trial 1')
n = eval(input('enter n:'))
f1 = 1
f2 = 1
print(f1)
print(f2)
for i in range(1, n - 1):
    (f1, f2) = (f2, (f1 + f2))
    print(f2)
