# Compute the Intersection of two lists

def intersect(lst1,lst2):
    res,lst2_copy =[],lst2[:]
    for i in lst1:
        if i in lst2_copy:
            res.append(i)
            lst2_copy.remove(i)

    return res
