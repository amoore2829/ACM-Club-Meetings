#Alice and Bob are playing a board game with a deck of nine cards. 
#For each digit between 1 to 9, there is one card with that digit on it. 
#Alice and Bob each draw two cards after shuffling the cards, and see the digits on their own cards without revealing the digits to each other. 
# Then Alice gives her two cards to Bob. Bob sees the digits on Alice’s cards and lays all the four cards on the table in increasing order by the digits. 
#Cards are laid facing down.
#Bob tells Alice the positions of her two cards. 
#The goal of Alice is to guess the digits on Bob’s two cards. 
#Can Alice uniquely determine these two digits and guess them correctly?


line = input().split()

alice_first = int(line[0])
alice_second = int(line[1])

position = input()

if position == "ABBA":
    if alice_second - alice_first == 3:
        bobs_cards = [alice_first + 1, alice_first + 2]
    else:
        bobs_cards = -1
elif position == "BAAB":
    if alice_first == 2 and alice_second == 8:
        bobs_cards = [1,9]
    else:
        bobs_cards = -1
elif position == "AABB":
    if alice_second == 7:
        bobs_cards = [8,9]
    else:
        bobs_cards = -1
elif position == "BBAA":
    if alice_first == 3:
        bobs_cards = [1,2]
    else:
        bobs_cards = -1
elif position == "ABAB":
    if alice_first == 6 and alice_second == 8:
        bobs_cards = [7,9]
    else:
        bobs_cards = -1
elif position == "BABA":
    if alice_first == 2 and alice_second == 4:
        bobs_cards = [1,3]
    else:
        bobs_cards = -1
    if bobs_cards == -1:
        print(-1)
    else:
        print(f"{bobs_cards[0]} {bobs_cards[1]}")


