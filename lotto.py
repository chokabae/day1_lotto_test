# 응용문제 7. 로또 맞춰보기 예제 

# 1. 6개의 숫자 입력받기 

# 6개의 숫자를 담을 list를 생성
my_lotto_numbers = list()

# 6번 숫자를 입력 : for
for i in range(6):
    # 정수 입력 : 조건에 맞는 숫자가 입력될 때 까지 반복 입력
    # 몇번 입력해야 ok인지 알 수 없다 -> while True : 사용

    while True :
        input_num = int(input(f'{i+1}번째 로또 번호 입력 : '))

        #받아낸 input_num가 제대로 되었다면? 무한반복 종료
        #반복 종료 조건 1~45 이내?
        # -> 1 <= 입력값 and 입력값 <=45

        is_range_ok = (1 <= input_num) and (input_num <= 45)

        if is_range_ok:
            # 검사 통과 시 무한반복 종료
            break
        else : 
            # 범위 검사 탈락 시 안내문구
            print('1~45의 값만 입력 가능합니다.')
            # 다시 입력 시킨다 > 무한박복 유지 > break x

        
    