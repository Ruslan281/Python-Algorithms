class List_Numbers:  # List_numbers adinda class yaradiriq


    def addTwoNumbers(self, List_1: list[int], List_2: list[int]):
    
        output = []
        sum_1 = ''
        sum_2 = ''
        
        convert_1 =[str(i) for i in List_1[::-1]]
        
        convert_2 = [str(i_1) for i_1 in List_2[::-1]]

        sum_1 = ''.join(convert_1)
        
        sum_2 = ''.join(convert_2)


        
        sum_total = int(sum_1) + int(sum_2)


        for m in str(sum_total):
                      output.append(int(m))


        return output[::-1]
        

        
                    
