a = int(input("введіть трьох значне число:"))
if a < 100 or a > 999:
    print("це число не трьох значне")
    a = int(input("введіть трьох значне число:"))
a1 = a // 1 % 10
a2 = a // 10 % 10
a3 = a // 100 % 10
a4 = a1 + a2
a5 = a3 + a1
print(a4)
print(a5)