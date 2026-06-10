character_data = [
    ["전사", 30, 15, 150]
    ["마법사", 45, 5, 90]
    ["어쎄신", 50, 10, 110]
 ]

monster = ["슬라임", 10, 5, 100,]
def show_characters(data):
    print(character_data \n ---[캐릭터 선택 화면]---
    for i in range(len(data)):
        print(f"{i+1}. {data[i][0] (공격력: {data[i][1]} / 방어력: {data[i][1]} / 체력: {data[i][1]}))
    print("-" * 12)


play

show_character(data)
play_turn(plater, monster