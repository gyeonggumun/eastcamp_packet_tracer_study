import random

def number_guessing_game():
    print("=" * 40)
    print("   숫자 맞추기 게임에 오신 것을 환영합니다!   ")
    print("=" * 40)
    
    # 1부터 50 사이의 임의의 숫자 생성
    secret_number = random.randint(1, 50)
    attempts = 0
    
    print("컴퓨터가 1부터 50 사이의 숫자를 하나 골랐습니다.")
    print("제가 고른 숫자는 무엇일까요?")
    
    while True:
        try:
            # 사용자 입력 받기
            user_guess = int(input("\n숫자를 입력하세요: "))
            attempts += 1
            
            # 입력한 숫자와 정답 비교
            if user_guess < secret_number:
                print("🔼 그것보다는 큰 숫자입니다. (Up!)")
            elif user_guess > secret_number:
                print("🔽 그것보다는 작은 숫자입니다. (Down!)")
            else:
                print(f"🎉 정답입니다! 총 {attempts}번 만에 맞추셨네요!")
                break
                
        except ValueError:
            # 숫자가 아닌 문자를 입력했을 때의 예외 처리
            print("⚠️ 경고: 문자가 아닌 '숫자'로만 입력해주세요!")

# 게임 실행
if __name__ == "__main__":
    number_guessing_game()