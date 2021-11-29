while True:
    password = int(input('방탈출을 진행하던 중, 세 개의 자물쇠를 해결하지 못해서 탈출하지 못하고 있습니다. 첫 번째 자물쇠입니다. '
                         '힌트를 보고, 네 자의 숫자 비밀번호를 맞춰보세요. '
                         '힌트 : RYOB. 오답 시 새로운 힌트가 주어집니다. '))
    if password == 1325:
        print('정답입니다! 두 개의 자물쇠가 더 남았습니다.')
        break
    elif password >= 1326:
        print('오답이 정답보다 큽니다. RED, YELLOW, ORANGE, BLUE. 해당 색을 무지개 색의 순서로 나열해보세요')
    elif password <= 1324:
        print('오답이 정답보다 작습니다. RED, YELLOW, ORANGE, BLUE. 해당 색을 무지개 색의 순서로 나열해보세요.')
        
while True:
    password2 = int(input('두 번째 자물쇠입니다. 다섯 자의 숫자 비밀번호를 맞춰주시면 됩니다. 힌트 : ㅏㅗㅣㅡ.'
                          '오답 시 새로운 힌트가 주어집니다. '))
    if password2 == 15109:
        print('정답입니다! 마지막 자물쇠만이 남았습니다.')
        break
    elif password2 >= 15110:
        print('오답이 정답보다 큽니다. 기본 모음 순서에 따라 해당 문자를 나열해보세요.')
    elif password2 <= 15108:
        print('오답이 정답보다 작습니다. 기본 모음 순서에 따라 해당 문자를 나열해보세요.')


while True:
    password3 = int(input('마지막 자물쇠입니다. 오직  한 번의 기회만이 주어집니다. 지금은 2022년 1월 1일, 토요일입니다. '
                          '주인공의 생일은 3월 2일, 수요일입니다. 며칠을 더 기다려야, 생일날이 되는지 계산해보세요. '
                          '1월은 31일로 구성되어 있고, 2월은 28일로 구성되어 있습니다.'))
    if password3 == 60:
        print('정답입니다! 탈출을 진심으로 축하드립니다.')
        break

    else:
        print('탈출에 실패하셨습니다.')
        break
    


    
  
