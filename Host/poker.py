import random


class Poker_card:
    decor = 0
    number = 0

    def __init__(self, decor, number):
        self.decor = decor
        self.number = number

    def get_decor(self):
        return self.decor
    
    def get_number(self):
        return self.number
    
    def print_card_info(self):

        number = 0
        if(self.number == 11):
            number = "J"
        elif(self.number == 12):
            number = "Q"
        elif(self.number == 13):
            number = "K"
        else:
            number = self.number

        if(self.decor == 1):
            print("♠"+str(number))
        elif(self.decor == 2):
            print("♥"+str(number))
        elif(self.decor == 3):
            print("♣"+str(number))
        elif(self.decor == 4):
            print("♦"+str(number))
        
        
                


class Deck:
    cards = []
    
    def __init__(self):
        for i in range(1,5): 
            for j in range(1,14): 
                self.cards.append(Poker_card(i,j))
                
    
    def shuffleCard(self):
        random.shuffle(self.cards)

    def popCard(self):
        return self.cards.pop(1)
    
print("test")

deck = Deck()
deck.shuffleCard()
for num in deck.cards:
    card = deck.popCard()
    card.print_card_info()
