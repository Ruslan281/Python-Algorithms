class Two_Sum:
    def twoSum(self, lst: list[int], target: int) -> list[int]:
        b=list()
        for  i in lst:
            if i not in b:
                b.append(i)
        for i in b:
            n = target - i
            if i in b and n != i:
                liste = [b.index(n),b.index(i)]
                return liste
            
