# Remove all dublicates from list

lst = list(range(10)) + list(range(10))

lst = list(set(lst))

print(lst)
