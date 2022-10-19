# 응용문제 7. 로또 맞춰보기 예제 

# 1. 6개의 숫자 입력받기 

# 6개의 숫자를 담을 list를 생성

from random import random


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

        # 무한 반복 종료 조건 2. 이미 등록한 번호가 아니어야함.
        # 중복인가 ? 내 로또 번호에 이미, 입력값이 들어 있는가?
        # input_num이 my_lotto_num 안에 포함되어 있는가?
        is_duplicated = input_num in my_lotto_numbers

        if is_range_ok and (not is_duplicated):
            # 검사 통과 시 무한반복 종료
            # 입력 값을 내 로또 번호로 등록 > 중복검사에도 활용 가능 
            my_lotto_numbers.append(input_num)
            break
        elif is_duplicated :
            # 중복검사에서 탈락됨
            print('이미 등록된 숫자 입니다.')
        else : 
            # 범위 검사 탈락 시 안내문구
            print('1~45의 값만 입력 가능합니다.')
            # 다시 입력 시킨다 > 무한박복 유지 > break x


# 입력한 숫자 목록 확인
print(f'내 숫자 목록 : {my_lotto_numbers}')


# 숫자 목록을 작은 수 ~ 큰 수로 정렬. (sort)

# bubble sort 구현해보기

# 2개씩 짝지어 비교 > 순서가 잘못 됐으면 서로 위치 변경 > 통째로 6번 반복

# 총 6개의 숫자를 모두 뽑아서 확인
for idx,val in enumerate(my_lotto_numbers):
    #2개씩 뽑아서 비교
    for j in range(5) :
    # 6회 반복 시 : 0, 1번 비교 > 1, 2 비교 > 2, 3 비교 > 3, 4 비교 > 4, 5비교 > 5, 6비교(여기서 오류 그래서 5로 지정)

    #순서가 잘못 되었나? > 앞의 숫자가 더 큰가?
        if my_lotto_numbers[j] > my_lotto_numbers[j+1]:
            #두 자료의 위치를 변경
            backup = my_lotto_numbers[j]
            my_lotto_numbers[j] = my_lotto_numbers[j+1]
            my_lotto_numbers[j+1] = backup

print(my_lotto_numbers)


# cpu가 숫자 6개 당첨 작업 진행
# 6개의 숫자가 1~45의 범위, 중복 없어야 함

# 당첨 번호 목록 
win_number_list = list()

for i in range(6):
    # 사용할 수 있는 번호가 나올때 까지 무한 반복
    while True :# random.random() > 0.0 ~ 0.9999의 랜덤값 출현

        # 0<= 랜덤값 < 1 1~45의 값으로 바꾸자. >랜덤값에 * 45로 > 0 * 45+1 <= 랜덤값 * 45 +1< 1*45 +1
        rand_number = int(random()*45+1)

        # 뽑을 때 부터 범위지정해서 에러처리 x
        # 당첨범호 목록에 있는지? > 중복인가?
        is_duplicated = rand_number in win_number_list

        # 중보이 아니면 목록에 등록, 다음 숫자 뽑으러.
        if not is_duplicated :
            win_number_list.append(rand_number)
            break

print(f'당첨본호 : {win_number_list}')






        
    