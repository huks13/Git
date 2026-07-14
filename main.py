# main.py (수정된 버전)
def print_gugudan():
    while True:
        print("\n--- 구구단 프로그램 (종료하려면 'q' 입력) ---")
        user_input = input("출력할 구구단 단수를 입력하세요 (2~9): ")

        if user_input.lower() == 'q':
            print("프로그램을 종료합니다.")
            break

        try:
            dan = int(user_input)
            if 2 <= dan <= 9:
                print(f"--- {dan}단 ---")
                for i in range(1, 10):
                    print(f"{dan} x {i} = {dan * i}")
            else:
                print("2에서 9 사이의 숫자만 입력해 주세요.")
        except ValueError:
            print("올바른 숫자를 입력하거나 종료하려면 'q'를 입력하세요.")

if __name__ == "__main__":
    print_gugudan()