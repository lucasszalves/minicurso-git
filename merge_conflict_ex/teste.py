def fibas(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fibas(x-1) + fibas(x-2)

print("git é mol lesgal")

for n in range(0, 20):
    print(fibas(n))