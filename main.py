character_data = [
    ["전사", 30, 15, 150],
    ["마법사", 45, 5, 90],
    ["어쎄신", 50, 10, 110]
 ]

monster = ["슬라임", 10, 5, 100,]

def show_characters(data):
    print("\n ---[캐릭터 선택 화면]---")
    for i in range(len(data)):
        print(f"{i+1}. {data[i][0]} (공격력: {data[i][1]} / 방어력: {data[i][2]} / 체력: {data[i][3]}")
    print("--------------------------")

def player_turn(player, monster_target):
    print(f"\n⚔️ {player[0]}의 턴!")
    print("1. 일반 공격  2. 방어하기")
    choice = input("행동을 선택하세요: ")
    if choice =="1":
        damage = player[1] - monster_target[2]
        if damage < 0:
            damage = 0  
        monster_target[3] -= damage
        print(f"💥 {player[0]}의 공격! {monster_target[0]}에게 {damage}의 데미지를 입혔습니다.")
    else:
        print("🛡️ 방어 자세를 취했습니다.")


def monster_turn(player, monster_target):
    print(f"\n😈 {monster_target[0]}의 턴!")

    monster_damage = monster_target[1] - player[2]
    if monster_damage < 0:
        monster_damage = 0

    player[3] -= monster_damage
    print(f"🐾 {monster_target[0]}의 반격! {player[0]}에게 {monster_damage}의 데미지를 입혔습니다.")

show_characters(character_data)
selected_num = int(input("플래이할 캐릭터의 번호를 선택해주세요:")) - 1
player = character_data[selected_num]

print(f"\n▶ [{player[0]}]을(를) 선택하셨습니다! 건투를 시작합니다.")

while player[3] > 0 and monster[3] > 0:
    print(f"\n--- 현재 상태 ---")
    print(f"👤 {player[0]} HP: {player[3]}")
    print(f"👾 {monster[0]} HP: {monster[3]}")
    print(f"-----------------")

    player_turn(player, monster)

    if monster[3] <= 0:
        break
        
    monster_turn(player, monster)

print("\n=== 전투 종료 ===")
if player[3] > 0:
    print(f"🎉 승리했습니다! {monster[0]}를 물리쳤습니다.")
else:
    print("💀 패배했습니다... 다시 시도해보세요...")