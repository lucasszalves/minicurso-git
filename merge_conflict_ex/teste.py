def fibas(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fibas(x-1) + fibas(x-2)

print("git é mol lesgal")

for i in range(0, 10):
    print(fibas(i))

print("blablabla")