# main.py (노래 추가 기능 업그레이드 버전)
def music_playlist():
    playlist = ["Nell - Slip Away", "Oasis - Live Forever", "The Beatles - Yesterday"]
    
    while True:
        print("\n=== 내 플레이리스트 ===")
        for i, song in enumerate(playlist, 1):
            print(f"{i}. {song}")
            
        print("\n[1] 노래 추가  [2] 프로그램 종료")
        choice = input("원하는 메뉴 번호를 입력하세요: ")
        
        if choice == "1":
            new_song = input("추가할 가수와 노래 제목을 입력하세요 (예: 밴드이름 - 노래제목): ")
            if new_song.strip():
                playlist.append(new_song)
                print(f"🎵 '{new_song}'이(가) 추가되었습니다!")
        elif choice == "2":
            print("프로그램을 종료합니다. 즐거운 감상 되세요!")
            break
        else:
            print("올바른 번호를 선택해 주세요.")

if __name__ == "__main__":
    music_playlist()