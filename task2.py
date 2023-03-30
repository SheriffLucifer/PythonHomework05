list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

mini = int(input('Min value: '))
maxi = int(input('Max value: '))
print(*[i for i in range(len(list)) if mini <= list[i] <= maxi])