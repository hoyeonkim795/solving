
    # for i in range(len(total)):
    #     t = total[i] 
    #     new_numbers = deepcopy(numbers)
    #     new_op = deepcopy(op)
    #     for l in range(3):
    #         p = len(new_op)
    #         for j in range(p):
    #             if new_op[j] == t[l]:
    #                 c = calculate(new_op[j],new_numbers[j],new_numbers[j+1])
    #                 del new_numbers[j]
    #                 new_numbers.insert(j,c)
    #                 del new_numbers[j+1]
    #                 del new_op[j]
    #                 print(new_numbers)
    #                 break
                    
    #             if len(new_numbers) == 1:
    #                 print(new_numbers[0])
    #                 if answer < abs(new_numbers[0]):
    #                     answer = abs(new_numbers[0])

print(eval("100-200*(300-500)+20"))