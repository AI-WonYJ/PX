def total(arr):
    summ = 0
    for i in range(0, len(arr)):
        summ += arr[i][0]*arr[i][1]*arr[i][2]
    return summ

def increment_array(budget, arr):
    setting = []
    for j in arr:
        setting.append(j[1])
    while True:
        i = len(arr) - 1
        if total(arr) == budget:
            print(arr, total(arr))
        while i >= 0 and total(arr) >= budget:
            arr[i][1] = setting[i]
            i -= 1
        if i < 0:
            break
        arr[i][1] += 1

increment_array(700000, [[1250, 2, 12], 
[1030, 4, 20],
[520, 4, 20],
[680, 4, 30],
[2150, 1, 24],
[1030, 1, 16],
[720, 4, 16],
[790, 1, 16],
[710, 6, 24],
[680, 1, 30],
[300, 4, 30]])

print("END")
