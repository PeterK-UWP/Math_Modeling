# question 9
# do question 8 with a while loop
print('calculating fibonacci sequence trial 1')
n = eval(input('enter n:'))
f1 = 1
f2 = 1
print(f1)
print(f2)
counter = 2
while counter <= n-1:
    (f1, f2) = (f2, (f1 + f2))
    print(f2)
    counter = counter  + 1