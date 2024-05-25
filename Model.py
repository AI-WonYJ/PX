def generate_pattern(n, arr, target):
    while True:
        # 뒤에서부터 조건을 확인하면서 늘려나감
        i = n - 1
        while i >= 0 and arr[i][1]*arr[i][2] < target:
            pattern[i] = 1
            i -= 1

        if i < 0:
            break

        pattern[i] += 1

# 예제로 n을 5로 설정하여 패턴 생성


def main():
    # 예산 입력
    budget = float(input("예산을 입력하세요: "))

    # 제품 정보 입력
    products = []
    while True:
        product_input = input("제품명/가격을 입력하세요 (종료를 원하면 0 입력): ")
        if product_input == '0':
            break
        product_info = product_input.split('/')
        if len(product_info) != 2:
            print("올바른 형식으로 입력하세요.")
            continue
        product_name, product_price = product_info
        product_price = float(product_price)
        products.append((product_name, product_price, 1))
    
    print(products)
    
    generate_pattern(len(product), products, budget)
    for i in range(0, len(products)):
        sum += products[i][1]*products[i][2]
    print(sum)
    
    
if __name__ == "__main__":
    main()
