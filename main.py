# 1
son = lambda x: x * 5

res = son(5)
print(res)

# 2
s = lambda son1, son2: son1 * son2

r = s(5, 5)
print(r)

# 3
s = lambda x: "jupt" if x % 2 == 0 else "toq"

r = s(9)
print(r)

# 4
katta = lambda a, b: max(a, b)

res = katta(45, 54)
print(res)

# 5
uzun = lambda ism: len(ism) > 7

res = uzun("Sayfiddin")
print(res)
