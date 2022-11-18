def myfunc(n):
    return len(n)

x = list(map(myfunc, ('apple', 'banana', 'cherry')))

print(x)

evens = list(map(int, ["2","4", "6", "8"]))
print(evens)

for i in evens:
    print(f' i : {i} , Data type: {type(i)}')