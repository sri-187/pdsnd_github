#!/usr/bin/env python3
import random

"""This is a dummy program of bikeshare with code of rock paper scissors """

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

# This player only plays rock
class AllRockPlayer(Player):
    pass


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.human_last_move = None

    def learn(self, my_move, their_move):
        self.human_last_move = their_move

    def move(self):
        if self.human_last_move is None:
            return random.choice(moves)
        else:
            return self.human_last_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.last_move = random.randint(0, 2)

# learn the last move
    def learn(self, my_move, their_move):
        self.last_move = moves.index(my_move)

    def move(self):
        self.last_move = (self.last_move + 1) % 3
        return moves[self.last_move]


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            Human_move = input("choose your option :"
                               "from rock, Paper, scissors :").lower()
            if Human_move in moves:
                return Human_move
            else:
                print(f"The move {Human_move} is invalid try again!!")


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2} \n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if move1 == move2:
            print("it's a tie")
        elif beats(move1, move2):
            print("Player1 win's")
            self.p1_score += 1
        else:
            print("Player2 win's")
            self.p2_score += 1
        print("##############################")
        print("Current round scores :")
        print(f"Player1 : {self.p1_score}")
        print(f"Player2 : {self.p2_score}")
        print("##############################")

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        if self.p1_score > self.p2_score:
            print("##############################")
            print("overall/General score:")
            print(f"Player1 : {self.p1_score}")
            print(f"Player2 : {self.p2_score}")
            print("##############################")
            print("Player 1 wins the game")
        elif self.p1_score < self.p2_score:
            print("##############################")
            print("overall/General score:")
            print(f"Player1 : {self.p1_score}")
            print(f"Player2 : {self.p2_score}")
            print("##############################")
            print("player 2 wins the game")
        else:
            print("##############################")
            print("overall/General score:")
            print(f"Player1 : {self.p1_score}")
            print(f"Player2 : {self.p2_score}")
            print("##############################")
            print("The Game is a tie")
        print("Game over!")


if __name__ == '__main__':
    while True:
        print("welcome to the Game")
        print("please choose the game level")
        game_type = input("starter, easy, Medium, Hard : ").lower()

        if 'starter' in game_type:
            # starter code
            player1 = HumanPlayer()
            player2 = AllRockPlayer()
            game = Game(player1, player2)
            game.play_game()
        elif 'easy' in game_type:
            # this chooses a random choice
            player1 = HumanPlayer()
            player2 = RandomPlayer()
            game = Game(player1, player2)
            game.play_game()
        elif 'medium' in game_type:
            # code block to test reflect player
            player1 = HumanPlayer()
            player2 = ReflectPlayer()
            game = Game(player1, player2)
            game.play_game()
        elif 'hard' in game_type:
            # code block to test cycle player
            player1 = HumanPlayer()
            player2 = CyclePlayer()
            game = Game(player1, player2)
            game.play_game()

        play_again = input("would you like to play again (Yes/No) :").lower()
        if play_again != 'yes':
            print("Thank you for playing...see you soon")
            break

