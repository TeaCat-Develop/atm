#프로젝트 시작하기

# balance : 초기 잔액을 설정하는 변수를 초기화 = 할당
# 금액은 자유

balance = 10000 # 잔액 초기화 = 사용하기 위해 미리 만드는 것. 특정값을 넣어서 만들거나 빈 값을 넣어 만듦.
receipts = []

# 사용자로부터 atm 기기의 사용 목적에 맞는 기능을 선택할 수 있도록
# 기능 입력을 받는 기능을 구현

# 무한루프=> while (조건을 만족할때까지) vs for in (횟수 제한)

# a = 1
# while a<10: # 조건 : 
        # 조건 만족 시키는 중...
        # True인 경우 진행
        # False인 경우 멈춤

while True : # 무한반복
    num = input('사용하실 기능의 번호를 선택해주세요 (1.입금 2.출금 3.영수증 4.종료): ')

    if num == '4': # 문자형으로 비교
        break # 반복문 종료
    
    if num == '1': # 입금 기능 구현 -> feat/deposit 브랜치에서 작업
        deposit_amount = int(input('입금할 금액을 입력해주세요.')) # str:5000 -> int -> int:5000
        balance += deposit_amount
        print(f'입금하신 금액은{deposit_amount}원이고, 현재 잔액은 {balance}원 입니다.')
        receipts.append( ('입금하신 금액', deposit_amount, balance) )
        #.append()에 소괄호 또 넣은 이유: 튜플(보안을 위해)
        print(receipts)

    
    if num == '2': # 출금 기능 구현 -> feat/withdraw 브랜치에서 작업
        withdraw_amount = int(input('출금할 금액을 입력해주세요.')) # str:5000 -> int -> int:5000
        withdraw_amount = min(balance,withdraw_amount) # 내장함수 min
        balance -= withdraw_amount
        print(f'{withdraw_amount}원 출금되었습니다. 현재 잔액은 {balance}원 입니다.')
        receipts.append( ('출금하신 금액', withdraw_amount, balance) )
                  # min=가벼움 if=시인성
            # if balance>0:
            #     print(f'출금하신 금액은{withdraw_amount}원이고, 현재 잔액은 {balance}원 입니다.')
            # else:
            #     balance+=withdraw_amount
            #     print('잔액이 부족합니다.')
    
    if num == '3':
        if receipts: # 값이 존재하면 true로 인식

            # [('입금'),3000,13000),출금()...]
            for i in receipts:
                # i = ('입금',3000,13000)
                # i[0]=>'입금'
                print(f'{i[0]}:{i[1]}원 | 잔액 {i[2]}')
            #   print(receipts)
        # elif가 아니라 if를 사용하는 이유 -> 시인성
        # 전부 if 사용이 가능한 이유: 코드는 절차적으로 실행되므로...
        else:
            print('영수증 내역이 없습니다')

print(f'서비스를 종료합니다. 현재 잔액은 {balance} ₩ 입니다.')