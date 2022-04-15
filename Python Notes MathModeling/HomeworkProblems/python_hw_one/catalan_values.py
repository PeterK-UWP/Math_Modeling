n = 0
C = 1.
print('catalan values up to 10000 are:')
print(f' C1 = {C:0.1f}')
while C <= 10000:
    C = ((4*n+2) * C) / (n + 2)
    if C > 10000:
        break
    print(f'{C:2.1f}')   # reformat
    n = n + 1
