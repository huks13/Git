# main.py
def print_gugudan():
    try:
        dan = int(input("출력할 구구단 단수를 입력하세요 (2~9): "))
        if 2 <= dan <= 9:
            print(f"--- {dan}단 ---")
            for i in range(1, 10):
                print(f"{dan} x {i} = {dan * i}")
        else:
            print("2에서 9 사이의 숫자만 입력해 주세요.")
    except ValueError:
        print("올바른 숫자를 입력해 주세요.")

if __name__ == "__main__":
    print_gugudan()