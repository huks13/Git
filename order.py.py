def create_order(menu: dict) -> list:
    """사용자의 주문을 받아 장바구니 리스트를 반환한다."""
    
    # 1. 텅 빈 장바구니 리스트 생성
    cart = [] 
    
    # 2. 키오스크 무한 반복 시작
    while True:
        print("\n=== ☕ 메뉴판 ===")
        # 딕셔너리로 된 메뉴판을 예쁘게 출력
        for key, value in menu.items():
            print(f"{key}. {value['name']} ({value['price']}원)")
            
        print("=================")
        
        # 3. 사용자 입력받기
        choice = input("원하시는 메뉴 번호를 선택하세요 (결제 단계로 가려면 'q' 입력): ")
        
        # 4. 탈출구 (q를 누르면 반복문 종료)
        if choice.lower() == 'q':
            print("\n주문을 마칩니다. 장바구니를 확인합니다.")
            break
            
        # 5. 장바구니에 담는 로직
        if choice in menu:
            drink_name = menu[choice]['name']
            drink_price = menu[choice]['price']
            
            count_str = input(f"[{drink_name}] 몇 잔을 주문하시겠습니까? ")
            
            # 수량에 문자가 아닌 숫자를 쳤는지 확인
            if count_str.isdigit():
                count = int(count_str)
                
                # 리스트(cart) 안에 딕셔너리 형태로 묶어서 쏙(append) 담기!
                cart.append({
                    "name": drink_name, 
                    "count": count, 
                    "price": drink_price
                })
                print(f"👉 장바구니에 {drink_name} {count}잔이 담겼습니다!")
            else:
                print("❌ 수량은 숫자로만 입력해주세요.")
        else:
            print("❌ 잘못된 번호입니다. 메뉴판에 있는 번호를 입력해주세요.")
            
    # 6. 최종 장바구니 리스트 반환 (이게 결제 담당자에게 넘어갑니다!)
    return cart


# --- 혼자 테스트해보기 위한 실행 코드 (협업할 땐 지워도 됩니다) ---
if __name__ == "__main__":
    # 가상의 메뉴판 데이터
    sample_menu = {
        "1": {"name": "아메리카노", "price": 3000},
        "2": {"name": "카페라떼", "price": 3500}
    }
    
    # 내가 만든 함수 실행해보기
    my_cart = create_order(sample_menu)
    print("\n[최종 생성된 장바구니 데이터]")
    print(my_cart)