# Find dublicate number in integer list

def find_dublicate(e):
    dublicates,a = set(),set()
    for i in e:
        if i in a:
            dublicates.add(i)

        a.add(i)

    return list(dublicates)
