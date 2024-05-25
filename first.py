def generate_pattern(arr):
    n = len(arr)
    
    setting = []
    for k in range(0, len(arr)):
        setting.append(arr[k][1])

    while True:
        
        sum = 0
        answer = []
        for j in range(0, len(arr)):
            sum += arr[j][0]*(arr[j][1]*arr[j][2])
        if sum == 600000:
            answer.append(arr)
            print(arr)
        print(arr, sum)
        
        i = n - 1
        while i >= 0 and sum > 600000:
            arr[i][1] = 1
            i -= 1

        if i < 0:
            break
        
        arr[i][1] += 1
    
    print("\n\nanswer\n\n")
    print(answer)

# 예제로 배열을 [4, 3, 2, 1]로 설정하여 패턴 생성
generate_pattern([[1250, 1, 12], [1030, 1, 20], [520, 1, 10], [680, 1, 40], [2150, 1, 10], [1030, 1, 24], [720, 1, 24], [790, 1, 24], [710, 1, 24], [680, 1, 24], [300, 1, 24]])
