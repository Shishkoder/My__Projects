from random import shuffle

class Card:

	suits = [
			"пики",
			"черви",
			"буби",
			"крести"
			]

	values = [
			 '2', '3', '4', '5', '6', '7', '8', '9', '10',
			 "вальта", "даму", "короля", "туза"
			 ]

	def __init__( self, value, suit ):
		self.value = value
		self.suit = suit

	def __lt__( self, other_card ):

		'''
		Установление "меньше, чем...".
		'''

		if self.value < other_card.value:
			return True
		elif self.value == other_card.value:
			if self.suit < other_card.suit:
				return True
			else:
				return False
		else:
			return False

	def __gt__( self, other_card ):

		'''
		Установление "больше, чем...".
		'''

		if self.value > other_card.value:
			return True
		elif self.value == other_card.value:
			if self.suit > other_card.suit:
				return True
			else:
				return False
		else:
			return False

	def __str__( self ):
		string = self.values[ self.value - 2] + " " + self.suits[ self.suit ]
		return string

class Deck:

	def __init__( self ):

		'''
		Создание колоды карт.
		: deck_cards : Колода карт 
		'''

		self.deck_cards = []

		# Создание колоды карт путём добавления нового экземпляра класса через цикл
		for i in range( 2, 15 ):
			for j in range(4):
				self.deck_cards.append( Card( i, j ) )

		shuffle( self.deck_cards )

	def rm_card( self ):

		'''
		Удаление последней карты из колоды, если она непустая.
		'''

		if len( self.deck_cards ) == 0 :
			return None
		else:
			return self.deck_cards.pop()

class Player:

	def __init__( self, name ):

		'''
		Инициализация переменных экземпляра класса Игрок.
		: wins : Количество выигранных раундов игроком
		: card : Карта игрока
		: name : Имя игрока
		'''
		
		self.wins = 0
		self.card = None
		self.name = name

class Game:

	def __init__( self ):
		name_player_1 = input( "Введите имя игрока №1: " )
		name_player_2 = input( "Введите имя игрока №2: " )

		self.deck = Deck() #?

		self.player_1 = Player( name_player_1 )
		self.player_2 = Player( name_player_2 )

	def wins( self, winner ):
		print( f"{ winner } забирает карты" )

	def draw( self, player_name_1, player_card_1, player_name_2, player_card_2 ):
		print( f"{ player_name_1 } кладёт { player_card_1 }, " +\
			f"а { player_name_2 } кладёт { player_card_2 }" )

	def play_game( self ):
		cards = self.deck.deck_cards
		print( "Поехали!" )

		while len( cards ) >= 2:
			response = input( "Для того, чтобы выйти, нажмите 'X', " +\
				"для продолжения игры нажмите любую другую клавишу: " )

			if response.lower() == 'x':
				break
			
			player_name_1 = self.player_1.name
			player_card_1 = self.deck.rm_card()
			player_name_2 = self.player_2.name
			player_card_2 = self.deck.rm_card()

			self.draw( player_name_1, player_card_1, player_name_2, player_card_2 )

			if player_card_1 > player_card_2:
				self.player_1.wins += 1
				self.wins( self.player_1.name )
			else:
				self.player_2.wins += 1
				self.wins( self.player_2.name )

		win = self.winner( self.player_1, self.player_2 )
		print( f"Игра окончена. { win }" )

	def winner( self, player_1, player_2 ):
		if player_1.wins > player_2.wins:
			return f"{ player_1.name } выиграл!"
		elif player_1.wins < player_2.wins:
			return f"{ player_2.name } выиграл!"
		else:
			return "Ничья!"

game = Game()
game.play_game()