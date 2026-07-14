# 간단한 계산기

num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

print("\n연산을 선택하세요.")
print("1. 더하기 (+)")
print("2. 빼기 (-)")
print("3. 곱하기 (*)")
print("4. 나누기 (/)")

choice = input("번호를 입력하세요 (1~4): ")

if choice == "1":
    print("결과:", num1 + num2)
elif choice == "2":
    print("결과:", num1 - num2)
elif choice == "3":
    print("결과:", num1 * num2)
elif choice == "4":
    if num2 != 0:
        print("결과:", num1 / num2)
    else:
        print("0으로 나눌 수 없습니다.")
else:
    print("잘못된 입력입니다.")