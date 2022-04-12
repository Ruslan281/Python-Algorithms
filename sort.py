# Sort list with Quicksort algorithm


def sort(L):
    if L ==[]: return []
    return sort([x for x in L[1:] if x < L[0]]) + L[0:1] +
    sort([x for x in L[1:] if x >= L[0]])


lst = [44,55,43,33,5,55,999]

print(sort(lst))

# Output : [5,33,43,44,55,999]


