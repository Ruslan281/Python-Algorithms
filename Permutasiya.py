# Find all permutation s of string

def permutasiya(w):
    if len(w) <= 1:
        return set(w)

    smaller = permutasiya([1:])
    perms = set()

    for x in smaller:
        for post in range(0,len(x)+1):
            perm = x[:post] + w[0] + x[post:]
            perms.add(perm)


    return perms

print(permutasiya("Rus"))

# Output : ('Rsu','usR','Rus')
