import random
import os
import collections

# 가능한 카드 리스트를 반환


def getAvailable(hand, last_card, is_attack):
    available = []
    if not is_attack and last_card[0] == 'Joker':
        available.extend(hand)
        return available

    for card in hand:
        if card[0] == 'Joker':
            available.append(card)

        elif (card[0] != last_card[0]
              and card[1] != last_card[1]):
            continue    

        elif is_attack:
            if get_damage(card) >= get_damage(last_card):
                available.append(card)
        else:
            available.append(card)

    return available


is_attack = False
damage = 1


def is_attack_card(card):
    return card[0] == 'Joker' or card[1] in ['A', '2']


damage_map = {
    'colored': 15,
    'black': 10,
    'A': 3,
    '2': 2
}


def get_damage(card):
    global damage_map
    return damage_map.get(card[1], 0)


def draw(hand):

    global put, deck

    hand.append(deck.pop())

    if len(deck) == 0:
        print("카드를 다시 섞습니다!")
        last_card = put.pop()
        random.shuffle(put)
        put, deck = deck, put
        put.append(last_card)


def card_str(card):
    return f'[{card[0]}{card[1]}]'


def hand_str(hand):
    return " ".join(map(card_str, hand))


message_count = 0
messages = []



def print_message(message):
    global put, deck, is_attack, messages, message_count, people
    player = people[0].hand
    os.system("cls")

    output = []
    output.append(f":: last put card ::  [[[{card_str(put[-1])}")
    output.append(f":: player's hand ::  {hand_str(player)}")
    output.append(
        f"::   available   ::  {hand_str(getAvailable(player, put[-1], is_attack))}")
    output.append("-" * 30)

    message_count += 1
    messages.append(message)
    if len(messages) == 16:
        messages.pop(0)
    for i, m in enumerate(messages):
        output.append(f'[{message_count - len(messages) + i + 1:>3}] {m}')
    output.append("-" * 30)

    print("\n".join(output))


def turn(person):
    # 전역 변수 접근
    global put, deck, is_attack, damage

    name = person.name
    hand = person.hand
    isComputer = person.is_computer

    # 차례
    print_message(f'{name}의 차례입니다.')

    # ----------- 낼 수 있는 카드 고르기 ---------------
    available = getAvailable(hand, put[-1], is_attack)

    # ----------- 카드 선택하기 ---------------------
    selected = None
    is_available = len(available) > 0
    if is_available:
        if isComputer:
            selected = random.choice(available)
        else:
            while True:
                i = input("몇 번째 카드를 내시겠습니까? "
                          "카드를 먹고 싶다면 0을 눌러주세요.")
                if not i.isdigit():
                    print_message("숫자를 입력해주세요.")
                    continue
                i = int(i) - 1
                if i >= len(available):
                    print_message("범위 내 숫자를 입력해주세요.")
                    continue
                if i != -1:
                    selected = available[i]
                break
    else:
        print_message(f'{name}가 낼 수 있는 카드가 없습니다.')

    # ------------선택한 카드 내기 -----------------------
    if selected is not None:
        hand.remove(selected)
        put.append(selected)

        if is_attack_card(selected):
            if not is_attack:
                damage = get_damage(selected)
            else:
                damage += get_damage(selected)

            is_attack = True

        print_message(f'{name}가 {selected}를 냈습니다."')

    # ------------ 카드 먹기 -----------------------
    else:
        print_message(f'{name}가 {damage}장 먹습니다.')
        if not isComputer:
            input("계속 하려면 엔터를 누르세요")
        is_attack = False
        for i in range(damage):
            draw(hand)
        damage = 1


deck = []

# num과 shape 정의
shapes = '♥♣♠◆'
nums = []
for i in range(2, 11):
    nums.append(str(i))
for c in 'JQKA':
    nums.append(c)

# 덱 만들기
for shape in shapes:
    for num in nums:
        deck.append((shape, num))

deck.append(('Joker', 'black'))
deck.append(('Joker', 'colored'))
random.shuffle(deck)

# 플레이어 정보를 담는 namedtuple 생성
Person = collections.namedtuple('Person', 'name hand is_computer')
people = []

# 플레이어 설정
people.append(Person('플레이어', [], False))

# 컴퓨터 설정
com_count = int(input('컴퓨터의 수를 입력해주세요. --> '))
for i in range(com_count):
    people.append(Person(f'컴퓨터{i}', [], True))

# 플레이어에게 카드 나누기
for i in range(7):
    for person in people:
        person.hand.append(deck.pop())

# 낸 카드에 하나 올려놓기
put = []
put.append(deck.pop())

# 게임 시작
i = 0
while True:
    current_person = people[i % len(people)]
    turn(current_person)
    if len(current_person.hand) == 0:
        print_message(f"{current_person.name}가 이겼습니다!")
        break
    i += 1