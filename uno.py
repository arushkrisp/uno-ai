from random import randint
cards = ["red0", "red1", "red2", "red3", "red4", "red5", "red6", "red7", "red8", "red9", "redrev", "redskip", "redplus2", "yellow0", "yellow1", "yellow2", "yellow3", "yellow4", "yellow5", "yellow6", "yellow7", "yellow8", "yellow9", "yellowrev", "yellowskip", "yellowplus2", "green0", "green1", "green2", "green3", "green4", "green5", "green6", "green7", "green8", "green9", "greenrev", "greenskip", "greenplus2", "blue0", "blue1", "blue2", "blue3", "blue4", "blue5", "blue6", "blue7", "blue8", "blue9", "bluerev", "blueskip", "blueplus2", "wild", "wild", "wild", "wild", "plus4", "plus4", "plus4", "plus4"]
user_cards = []
computer_cards = []
shuffled_cards = []
colors = ["red", "yellow", "green", "blue"]
def decideColor(computer_cards):
    color_list = [0, 0, 0, 0]
    for card in computer_cards:
        if card != "wild" and card != "plus4":
            if card[:3] == "red":
                color_list[0] += 1
            elif card[:4] == "blue":
                color_list[1] += 1
            elif card[:5] == "green":
                color_list[2] += 1
            elif card[:6] == "yellow":
                color_list[3] += 1
    maximum = max(color_list)
    indices = []
    for i in range(len(color_list)):
        if color_list[i] == maximum:
            indices.append(i)
    index = randint(0, len(indices)-1)
    col_index = indices[index]
    if col_index == 0:
        return "red"
    elif col_index == 1:
        return "blue"
    elif col_index == 2:
        return "green"
    else:
        return "yellow"
def shuffle(deck, cards, num):
    for i in range(num):
        index = randint(0, len(deck)-1)
        cards.append(deck[index])
        deck.pop(index)
def plus(deck, cards, num):
    for i in range(num):
        cards.append(deck[-1])
        deck.pop(-1)
def placeCard1C(color):
    leng = len(color)
    have_card = False
    for card in computer_cards:
        if card[:leng] == color:
            have_card = True
            break
    if have_card:
        if (color + "plus2") in computer_cards:
            play_card = color+"plus2"
            print("The computer played a " + color + "plus2")
            computer_cards.remove(play_card)
            return play_card
        elif (color + "skip") in computer_cards:
            play_card = color+"skip"
            print("The computer played a " + color + "skip")
            computer_cards.remove(play_card)
            return play_card
        elif (color + "rev") in computer_cards:
            play_card = color+"rev"
            print("The computer played a " + color+"rev")
            computer_cards.remove(play_card)
            return play_card
        else:
            for card in computer_cards:
                if card[:leng] == color:
                    play_card = card
                    print("The computer played a " + card)
                    computer_cards.remove(card)
                    return card
                    break
    else:
        if "plus4" in computer_cards:
            play_card = "plus4"
            print("The computer played a plus 4.")
            col = decideColor(computer_cards)
            print("The color is " + col)
            computer_cards.remove("plus4")
            return [play_card, col]
        elif "wild" in computer_cards:
            play_card = "wild"
            print("The computer played a wild card.")
            col = decideColor(computer_cards)
            print("The color is " + col)
            computer_cards.remove("wild")
            return [play_card, col]
        else:
            print("The computer took a card from the deck.")
            plus(cards, computer_cards, 1)
            return "HelloWorld..."
def placeCard2C(color, number):
    leng = len(color)
    have_color = False
    for card in computer_cards:
        if card[:leng] == color:
            have_color = True
            break
    have_number = False
    for card in computer_cards:
        if number == 2:
            if card[-1] == "2" and card[-2:] != "s2":
                have_number = True
        elif number == 4:
            if card[-1] == "4" and card[-2:] != "s4":
                have_number = True
        else:
            if card[-1] == str(number):
                have_number = True
    if have_color:
        if (color + "plus2") in computer_cards:
            play_card = color + "plus2"
            print("The computer played a " + color + "plus2")
            computer_cards.remove(play_card)
            return play_card
        elif (color + "skip") in computer_cards:
            play_card = color + "skip"
            print("The computer played a " + color + "skip")
            computer_cards.remove(play_card)
            return play_card
        elif (color + "rev") in computer_cards:
            play_card = color + "rev"
            print("The computer played a " + color + "rev")
            computer_cards.remove(play_card)
            return play_card
        else:
            for card in computer_cards:
                if card[:leng] == color:
                    play_card = card
                    print("The computer played a " + card)
                    computer_cards.remove(card)
                    return card
                    break
    elif have_number:
        for card in computer_cards:
            if number == 2 or number == 4:
                if card[-1] == str(number) and card[-2:] != "s" + str(number):
                    play_card = card
                    print("The computer played a " + card)
                    computer_cards.remove(card)
                    return [play_card, play_card[:-1]]
                    break
            else:
                if card[-1] == str(number):
                    play_card = card
                    print("The computer played a " + card)
                    computer_cards.remove(card)
                    return [play_card, play_card[:-1]]
                    break
    else:
        if "plus4" in computer_cards:
            play_card = "plus4"
            print("The computer played a plus 4.")
            col = decideColor(computer_cards)
            print("The color is " + col)
            computer_cards.remove("plus4")
            return [play_card, col]
        elif "wild" in computer_cards:
            play_card = "wild"
            print("The computer played a wild card.")
            col = decideColor(computer_cards)
            print("The color is " + col)
            computer_cards.remove("wild")
            return [play_card, col]
        else:
            print("The computer took a card from the deck.")
            plus(cards, computer_cards, 1)
            return "HelloWorld..."
def placeCardSkipC(color):
    leng = len(color)
    have_card = False
    for card in computer_cards:
        if card[:leng] == color:
            have_card = True
            break
    if have_card:
        if (color + "plus2") in computer_cards:
            play_card = color + "plus2"
            print("The computer played a " + color + "plus2")
            computer_cards.remove(play_card)
            return play_card
        elif (color + "skip") in computer_cards:
            play_card = color + "skip"
            print("The computer played a " + color + "skip")
            computer_cards.remove(play_card)
            return play_card
        elif (color + "rev") in computer_cards:
            play_card = color + "rev"
            print("The computer played a " + color + "rev")
            computer_cards.remove(play_card)
            return play_card
        else:
            for card in computer_cards:
                if card[:leng] == color:
                    play_card = card
                    print("The computer played a " + card)
                    computer_cards.remove(card)
                    return card
                    break
    else:
        for card in computer_cards:
            if card[-4:] == "skip":
                play_card = card
                print("The computer played a " + card)
                col = card[:-4]
                computer_cards.remove(card)
                return [card, col]
        if "plus4" in computer_cards:
            play_card = "plus4"
            print("The computer played a plus 4.")
            col = decideColor(computer_cards)
            print("The color is " + color)
            computer_cards.remove("plus4")
            return [play_card, col]
        elif "wild" in computer_cards:
            play_card = "wild"
            print("The computer played a wild card.")
            col = decideColor(computer_cards)
            print("The color is " + color)
            computer_cards.remove("wild")
            return [play_card, col]
        else:
            print("The computer took a card from the deck.")
            user_skip = False
            plus(cards, computer_cards, 1)
            return "HelloWorld..."
def placeCardReverseC(color):
    leng = len(color)
    have_card = False
    for card in computer_cards:
        if card[:leng] == color:
            have_card = True
            break
    if have_card:
        if (color + "plus2") in computer_cards:
            play_card = color + "plus2"
            print("The computer played a " + color + "plus2")
            computer_cards.remove(play_card)
            return play_card
        elif (color + "skip") in computer_cards:
            play_card = color + "skip"
            print("The computer played a " + color + "skip")
            computer_cards.remove(play_card)
            return play_card
        elif (color + "rev") in computer_cards:
            play_card = color + "rev"
            print("The computer played a " + color + "rev")
            computer_cards.remove(play_card)
            return play_card
        else:
            for card in computer_cards:
                if card[:leng] == color:
                    play_card = card
                    print("The computer played a " + card)
                    computer_cards.remove(card)
                    return card
                    break
    else:
        for card in computer_cards:
            if card[-3:] == "rev":
                play_card = card
                print("The computer played a " + card)
                col = card[:-3]
                computer_cards.remove(card)
                return [card, col]
        if "plus4" in computer_cards:
            play_card = "plus4"
            print("The computer played a plus 4.")
            col = decideColor(computer_cards)
            print("The color is " + color)
            computer_cards.remove("plus4")
            return [play_card, col]
        elif "wild" in computer_cards:
            play_card = "wild"
            print("The computer played a wild card.")
            col = decideColor(computer_cards)
            print("The color is " + color)
            computer_cards.remove("wild")
            return [play_card, col]
        else:
            print("The computer took a card from the deck.")
            plus(cards, computer_cards, 1)
            user_skip = False
            return "HelloWorld..."
def placeCardPlus2C(color):
    leng = len(color)
    have_card = False
    for card in computer_cards:
        if card[:leng] == color:
            have_card = True
            break
    if have_card:
        if (color + "plus2") in computer_cards:
            play_card = color + "plus2"
            print("The computer played a " + color + "plus2")
            computer_cards.remove(play_card)
            return play_card
        elif (color + "skip") in computer_cards:
            play_card = color + "skip"
            print("The computer played a " + color + "skip")
            computer_cards.remove(play_card)
            return play_card
        elif (color + "rev") in computer_cards:
            play_card = color + "rev"
            print("The computer played a " + color + "rev")
            computer_cards.remove(play_card)
            return play_card
        else:
            for card in computer_cards:
                if card[:leng] == color:
                    play_card = card
                    print("The computer played a " + card)
                    computer_cards.remove(card)
                    return card
                    break
    else:
        for card in computer_cards:
            if card != "wild":
                if card[-5:] == "plus2":
                    play_card = card
                    print("The computer played a " + card)
                    col = card[:-5]
                    computer_cards.remove(card)
                    return [card, col]
        if "plus4" in computer_cards:
            play_card = "plus4"
            print("The computer played a plus 4.")
            col = decideColor(computer_cards)
            print("The color is " + color)
            computer_cards.remove("plus4")
            return [play_card, col]
        elif "wild" in computer_cards:
            play_card = "wild"
            print("The computer played a wild card.")
            col = decideColor(computer_cards)
            print("The color is " + color)
            computer_cards.remove("wild")
            return [play_card, col]
        else:
            print("The computer took a card from the deck.")
            plus(cards, computer_cards, 1)
            return "HelloWorld..."
def placeCardPlus4C(color):
    leng = len(color)
    have_card = False
    for card in computer_cards:
        if card[:leng] == color:
            have_card = True
            break
    if have_card:
        if (color + "plus2") in computer_cards:
            play_card = color + "plus2"
            print("The computer played a " + color + "plus2")
            computer_cards.remove(play_card)
            return play_card
        elif (color + "skip") in computer_cards:
            play_card = color + "skip"
            print("The computer played a " + color + "skip")
            computer_cards.remove(play_card)
            return play_card
        elif (color + "rev") in computer_cards:
            play_card = color + "rev"
            print("The computer played a " + color + "rev")
            computer_cards.remove(play_card)
            return play_card
        else:
            for card in computer_cards:
                if card[:leng] == color:
                    play_card = card
                    print("The computer played a " + card)
                    computer_cards.remove(card)
                    return card
                    break
    else:
        if "plus4" in computer_cards:
            play_card = "plus4"
            print("The computer played a plus 4.")
            col = decideColor(computer_cards)
            print("The color is " + col)
            computer_cards.remove("plus4")
            return [play_card, col]
        elif "wild" in computer_cards:
            play_card = "wild"
            print("The computer played a wild card.")
            col = decideColor(computer_cards)
            print("The color is " + col)
            computer_cards.remove("wild")
            return [play_card, col]
        else:
            print("The computer took a card from the deck.")
            plus(cards, computer_cards, 1)
            return "HelloWorld..."
def placeCard1(col):
    play_card = input("Type the name of the card you want to place (color is " + col + "). If you want to take a card, type \"take\": ")
    if (play_card == "plus4" or play_card == "wild") and play_card in user_cards:
        chosen_color = input("What do you want the color to be? ")
        user_cards.remove(play_card)
        return [play_card, chosen_color]
    elif play_card[:len(col)] == col and play_card in user_cards:
        user_cards.remove(play_card)
        return play_card
    else:
        plus(cards, user_cards, 1)
        return "HelloWorld..."
def placeCard2(col, number):
    play_card = input("Type the name of the card you want to place (color is " + col + "). If you want to take a card, type \"take\": ")
    if (play_card == "plus4" or play_card == "wild") and play_card in user_cards:
        color = input("What do you want the color to be? ")
        user_cards.remove(play_card)
        return [play_card, color]
    elif play_card[:len(col)] == col and play_card in user_cards:
        user_cards.remove(play_card)
        return play_card
    elif number == 2 or number == 4:
        if play_card[-1] == str(number) and play_card[-2:] != "s" + str(number):
            user_cards.remove(play_card)
            return [play_card, play_card[:-1]]
    elif play_card[-1] == str(number) and play_card in user_cards:
        user_cards.remove(play_card)
        return [play_card, play_card[:-1]]
    else:
        plus(cards, user_cards, 1)
        return "HelloWorld..."
def placeCardSkip(col):
    play_card = input("Type the name of the card you want to place (color is " + col + "). If you want to take a card, type \"take\": ")
    if (play_card == "plus4" or play_card == "wild") and play_card in user_cards:
        chosen_color = input("What do you want the color to be? ")
        user_cards.remove(play_card)
        return [play_card, chosen_color]
    elif play_card[:len(col)] == col and play_card in user_cards:
        user_cards.remove(play_card)
        return play_card
    elif play_card[-4:] == "skip" and play_card in user_cards:
        user_cards.remove(play_card)
        return [play_card, play_card[:-4]]
    elif play_card == "take":
        plus(cards, user_cards, 1)
        computer_skip = False
        return "HelloWorld..."
def placeCardReverse(col):
    play_card = input("Type the name of the card you want to place (color is " + col + "). If you want to take a card, type \"take\": ")
    if (play_card == "plus4" or play_card == "wild") and play_card in user_cards:
        chosen_color = input("What do you want the color to be? ")
        user_cards.remove(play_card)
        return [play_card, chosen_color]
    elif play_card[:len(col)] == col and play_card in user_cards:
        user_cards.remove(play_card)
        return play_card
    elif play_card[-3:] == "rev" and play_card in user_cards:
        user_cards.remove(play_card)
        return [play_card, play_card[:-3]]
    elif play_card == "take":
        plus(cards, user_cards, 1)
        return "HelloWorld..."
        computer_skip = False
def placeCardPlus2(col):
    play_card = input("Type the name of the card you want to place (color is " + col + "). If you want to take a card, type \"take\": ")
    if (play_card == "plus4" or play_card == "wild") and play_card in user_cards:
        chosen_color = input("What do you want the color to be? ")
        user_cards.remove(play_card)
        return [play_card, chosen_color]
    elif play_card[:len(col)] == col and play_card in user_cards:
        user_cards.remove(play_card)
        return play_card
    elif play_card == "take":
        plus(cards, user_cards, 1)
        computer_plus2 = True;
        return "HelloWorld..."
    elif play_card[-5:] == "plus2" and play_card in user_cards:
        user_cards.remove(play_card)
        return [play_card, play_card[:-5]]
def placeCardPlus4(col):
    play_card = input("Type the name of the card you want to place (color is " + col + "). If you want to take a card, type \"take\": ")
    if (play_card == "plus4" or play_card == "wild") and play_card in user_cards:
        chosen_color = input("What do you want the color to be? ")
        user_cards.remove(play_card)
        return [play_card, chosen_color]
    elif play_card[:len(col)] == col and play_card in user_cards:
        user_cards.remove(play_card)
        return play_card
    else:
        plus(cards, user_cards, 1)
        return "HelloWorld..."
index_open = randint(0, len(cards) - 1)
open_card = cards[index_open]
while open_card == "plus4" or open_card == "redplus2" or open_card == "greenplus2" or open_card == "yellowplus2" or open_card == "blueplus2":
    index_open = randint(0, len(cards) - 1)
    open_card = cards[index_open]
cards.pop(index_open)
shuffle(cards, shuffled_cards, len(cards))
cards = shuffled_cards
plus(cards, user_cards, 7)
plus(cards, computer_cards, 7)
print("---UNO---")
print("Your cards are: " + str(user_cards))
current_card = open_card
print("The opening card is a " + open_card)
turn = "user"
num_stack = 0;
color = "undefined";
if open_card == "wild":
    color = colors[randint(0, 3)]
user_protection = False
computer_protection = False
user_skip = False
computer_skip = False
user_plus2 = False
computer_plus2 = False
while(len(computer_cards) != 0 and len(user_cards) != 0):
    if len(cards) <= 3:
        cards = ["red0", "red1", "red2", "red3", "red4", "red5", "red6", "red7", "red8", "red9", "redrev", "redskip", "redplus2", "yellow0", "yellow1", "yellow2", "yellow3", "yellow4", "yellow5", "yellow6", "yellow7", "yellow8", "yellow9", "yellowrev", "yellowskip", "yellowplus2", "green0", "green1", "green2", "green3", "green4", "green5", "green6", "green7", "green8", "green9", "greenrev", "greenskip", "greenplus2", "blue0", "blue1", "blue2", "blue3", "blue4", "blue5", "blue6", "blue7", "blue8", "blue9", "bluerev", "blueskip", "blueplus2", "wild", "wild", "wild", "wild", "plus4", "plus4", "plus4", "plus4"]
        shuffle(cards, shuffled_cards, len(cards))
        cards = shuffled_cards
    if turn == "user":
        if current_card == "plus4" and user_protection == False:
            num_stack += 1
            if "plus4" in user_cards:
                decision = input("Would you like to place a plus 4? Type y for yes and n for no: ")
                if decision == "y":
                    user_cards.remove("plus4")
                    color = input("What is the color? ")
                    print(user_cards)
                    user_skip = False
                    user_protection = False
                    user_plus2 = False
                    turn = "computer"
                else:
                    print("You get " + str((4*num_stack)) + " cards.")
                    plus(cards, user_cards, 4*num_stack)
                    num_stack = 0
                    print(user_cards)
                    user_protection = False
                    user_plus2 = False
                    user_skip = False
                    computer_protection = True
                    turn = "computer"
            else:
                print("You get " + str((4 * num_stack)) + " cards.")
                plus(cards, user_cards, 4 * num_stack)
                num_stack = 0
                print(user_cards)
                computer_protection = True
                user_protection = False
                user_plus2 = False
                user_skip = False
                turn = "computer"
        elif current_card == "plus4" and user_protection == True:
            arr = placeCardPlus4(color)
            if arr != "HelloWorld...":
                if len(arr) == 2:
                    current_card = arr[0]
                    color = arr[1]
                else:
                    current_card = arr
            else:
                computer_protection = True
            print(user_cards)
            user_protection = False
            user_plus2 = False
            user_skip = False
            turn = "computer"
        elif current_card == "wild":
            arr = placeCard1(color)
            if arr != "HelloWorld...":
                if len(arr) == 2:
                    current_card = arr[0]
                    color = arr[1]
                else:
                    current_card = arr
            print(user_cards)
            user_protection = False
            user_plus2 = False
            user_skip = False
            turn = "computer"
        elif current_card[-5:] == "plus2" and user_plus2 == False:
            num_stack += 1
            if ("redplus2" in user_cards or "yellowplus2" in user_cards or "blueplus2" in user_cards or "greenplus2" in user_cards):
                decide = input("Would you like to place a plus 2? Type y for yes and n for no: ")
                if decide == "y":
                    card_name = input("Type the name of the card that you want to place on the plus 2: ")
                    user_cards.remove(card_name)
                    current_card = card_name
                    print(user_cards)
                    user_protection = False
                    user_plus2 = False
                    user_skip = False
                    turn = "computer"
                else:
                    print("You get " + str(2 * num_stack) + " cards.")
                    plus(cards, user_cards, 2*num_stack)
                    print(user_cards)
                    num_stack = 0;
                    computer_plus2 = True
                    user_protection = False
                    user_plus2 = False
                    user_skip = False
                    turn = "computer"
            else:
                print("You get " + str(2 * num_stack) + " cards.")
                plus(cards, user_cards, 2 * num_stack)
                print(user_cards)
                num_stack = 0;
                computer_plus2 = True
                user_protection = False
                user_plus2 = False
                user_skip = False
                turn = "computer"
            color = current_card[:-5]
        elif current_card[-5:] == "plus2" and user_plus2 == True:
            arr = placeCardPlus2(color)
            if arr != "HelloWorld...":
                if len(arr) == 2:
                    current_card = arr[0]
                    color = arr[1]
                else:
                    current_card = arr
            else:
                computer_plus2 = True
            user_protection = False
            user_plus2 = False
            user_skip = False
            print(user_cards)
            turn = "computer"
        elif (current_card[-4:] == "skip" or current_card[-3:] == "rev") and user_skip == False:
            computer_skip = True
            user_protection = False
            user_plus2 = False
            user_skip = False
            print(user_cards)
            turn = "computer"
        elif (current_card[-4:] == "skip") and user_skip == True:
            arr = placeCardSkip(color)
            if arr != "HelloWorld...":
                if len(arr) == 2:
                    current_card = arr[0]
                    color = arr[1]
                else:
                    current_card = arr
            else:
                computer_skip = True
            user_skip = False
            user_protection = False
            user_plus2 = False
            print(user_cards)
            turn = "computer"
        elif (current_card[-3:] == "rev") and user_skip == True:
            arr = placeCardReverse(color)
            if arr != "HelloWorld...":
                if len(arr) == 2:
                    current_card = arr[0]
                    color = arr[1]
                else:
                    current_card = arr
            else:
                computer_skip = True
            user_skip = False
            user_protection = False
            user_plus2 = False
            print(user_cards)
            turn = "computer"
        else:
            if current_card[0] == "r":
                color = "red"
            elif current_card[0] == "y":
                color = "yellow"
            elif current_card[0] == "b":
                color = "blue"
            elif current_card[0] == "g":
                color = "green"
            number = int(current_card[len(color):])
            arr = placeCard2(color, number)
            if arr != "HelloWorld...":
                if len(arr) == 2:
                    current_card = arr[0]
                    color = arr[1]
                else:
                    current_card = arr
            print(user_cards)
            user_protection = False
            user_plus2 = False
            user_skip = False
            turn = "computer"
    if len(user_cards) == 1:
        print("USER SAID UNO!")

    if turn == "computer":
        if current_card == "plus4" and computer_protection == False:
            num_stack += 1
            if "plus4" in computer_cards:
                computer_cards.remove("plus4")
                print("The computer placed a plus4")
                color = decideColor(computer_cards)
                print("The color is " + color)
                print(user_cards)
                computer_protection = False
                computer_plus2 = False
                computer_skip = False
                turn = "user"
            else:
                print("The computer gets " + str((4 * num_stack)) + " cards.")
                plus(cards, computer_cards, 4 * num_stack)
                num_stack = 0
                user_protection = True
                print(user_cards)
                computer_protection = False
                computer_plus2 = False
                computer_skip = False
                turn = "user"
        elif current_card == "plus4" and computer_protection == True:
            arr = placeCardPlus4C(color)
            if arr != "HelloWorld...":
                if len(arr) == 2:
                    current_card = arr[0]
                    color = arr[1]
                else:
                    current_card = arr
            else:
                user_protection = True
            computer_protection = False
            computer_plus2 = False
            computer_skip = False
            print(user_cards)
            turn = "user"
        elif current_card == "wild":
            arr = placeCard1C(color)
            if arr != "HelloWorld...":
                if len(arr) == 2:
                    current_card = arr[0]
                    color = arr[1]
                else:
                    current_card = arr
            print(user_cards)
            turn = "user"
        elif current_card[-5:] == "plus2" and computer_plus2 == False:
            num_stack += 1
            if "redplus2" in computer_cards or "yellowplus2" in computer_cards or "blueplus2" in computer_cards or "greenplus2" in computer_cards:
                for card in computer_cards:
                    if card[-5:] == "plus2":
                        computer_cards.remove(card)
                        print("The computer placed a " + card)
                        current_card = card
                        print(user_cards)
                        computer_protection = False
                        computer_plus2 = False
                        computer_skip = False
                        turn = "user"
            else:
                print("The computer gets " + str(2 * num_stack) + " cards.")
                plus(cards, computer_cards, 2 * num_stack)
                user_plus2 = True
                num_stack = 0;
                print(user_cards)
                computer_protection = False
                computer_plus2 = False
                computer_skip = False
                turn = "user"
            color = current_card[:-5]
        elif current_card[-5:] == "plus2" and computer_plus2 == True:
            arr = placeCardPlus2C(color)
            if arr != "HelloWorld...":
                if len(arr) == 2:
                    current_card = arr[0]
                    color = arr[1]
                else:
                    current_card = arr
            else:
                user_plus2 = True
            print(user_cards)
            computer_protection = False
            computer_plus2 = False
            computer_skip = False
            turn = "user"
        elif (current_card[-4:] == "skip" or current_card[-3:] == "rev") and computer_skip == False:
            user_skip = True
            computer_protection = False
            computer_plus2 = False
            computer_skip = False
            print(user_cards)
            turn = "user"
        elif (current_card[-4:] == "skip") and computer_skip == True:
            arr = placeCardSkipC(color)
            if arr != "HelloWorld...":
                if len(arr) == 2:
                    current_card = arr[0]
                    color = arr[1]
                else:
                    current_card = arr
            else:
                user_skip = True
            computer_skip = False
            computer_protection = False
            computer_plus2 = False
            print(user_cards)
            turn = "user"
        elif (current_card[-3:] == "rev") and computer_skip == True:
            arr = placeCardReverseC(color)
            if arr != "HelloWorld...":
                if len(arr) == 2:
                    current_card = arr[0]
                    color = arr[1]
                else:
                    current_card = arr
            else:
                user_skip = True
            computer_skip = False
            computer_protection = False
            computer_plus2 = False
            print(user_cards)
            turn = "user"
        else:
            if current_card[0] == "r":
                color = "red"
            elif current_card[0] == "y":
                color = "yellow"
            elif current_card[0] == "b":
                color = "blue"
            elif current_card[0] == "g":
                color = "green"
            number = int(current_card[-1])
            arr = placeCard2C(color, number)
            if arr != "HelloWorld...":
                if len(arr) == 2:
                    current_card = arr[0]
                    color = arr[1]
                else:
                    current_card = arr
            print(user_cards)
            computer_protection = False
            computer_plus2 = False
            computer_skip = False
            turn = "user"
        if len(computer_cards) == 1:
            print("COMPUTER SAID UNO!")

if len(user_cards) == 0:
    print("USER WINS!!")
else:
    print("COMPUTER WINS!!")


