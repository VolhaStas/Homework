class Cart:
    def __init__(self, suit, number, weight=None):
        self.suit = suit
        self.number = number
        self.weight = weight if weight is not None else number

    def __repr__(self):
        return f"_________\n|{self.__get_number_string():<2}      {self.__get_suit_symbol()}|\n|         |\n|         |\n|{self.__get_suit_symbol():<2}       {self.__get_number_string()}|\n|_________|"

    def __get_suit_symbol(self):
        symbols = {
            'Hearts': '♥️',
            'Diamonds': '♦️',
            'Spades': '♠️',
            'Clubs': '♣️'
        }
        return symbols.get(self.suit, '')

    def __get_number_string(self):
        numbers = {
            1: 'A',
            11: 'J',
            12: 'Q',
            13: 'K',
            10: '10'
        }
        return numbers.get(self.number, str(self.number))


def create_deck():
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    numbers = range(1, 14)
    deck = [Cart(suit, number) for suit in suits for number in numbers]
    return deck


def interact_with_cards(deck):
    while True:
        print("Deck size:", len(deck))
        choice = input("Choose an action: (1) Draw a card, (2) Exit: ")
        if choice == '1':
            if len(deck) > 0:
                drawn_card = deck.pop()
                print("Drawn card:", drawn_card)
            else:
                print("No more cards in the deck!")
        elif choice == '2':
            print("Exit the program.")
            break
        else:
            print("Invalid choice. Try again.")


deck_of_cards = create_deck()
interact_with_cards(deck_of_cards)