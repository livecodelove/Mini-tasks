n, k = int(input()), (int(input()) - 1)
num_list = [i for i in range(1, n + 1)]
i = 0
while len(num_list) > 1:
    i = (i + k) % (len(num_list))
    num_list.remove(num_list[i])
    
print(*num_list)