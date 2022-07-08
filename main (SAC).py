num = input()

result = []
result.extend(num)
if len(num) > 3:
    for i in range(len(num) % 3, len(result) + len(num) // 3,4):        
            if len(num) % 3 == 0:
                if i + 3 == len(result):
                    break
                else:
                    result.insert(i + 3, ',')
            else: 
                result.insert(i, ',')
else:
    result = num 
print(*result, sep = '')