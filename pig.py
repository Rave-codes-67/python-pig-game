import random
import time
import pyfiglet

CONFIG = {
    "roll_limit": 4, # How many times a player can roll consecutively with holding
    
    "max_dice": 6, # Maximum number any player can roll

    'withdrawal-point': 5, # How much points to deduct from a player's score if they roll '1'

    'default_goal': 100, # Target score if player selects default goal

    'goal': None, # Set by get_goal(); used by check_win() to manage the game's target score

    'max_players': 5, # Maximum number of players allowed by the code

    '1-point-word': 'unlocky' # Message displayed when a player rolls a 1
}

class PigGame:
    def __init__(self):
        self.get_goal()
        self.roll_limit = CONFIG['roll_limit']
        self.withdraw = CONFIG['withdrawal-point']
        self.score = {}
        self.choice = None
        self.retry = None

    def get_goal(self):
        while True:
            print('- - - - - - - - - - - - - - - - - - ')

            goal_input = input("Enter Goal (d -> default): ")
            goal_input = goal_input.lower().strip()

            if goal_input == 'd' or goal_input == 'default':
                CONFIG['goal'] = CONFIG['default_goal']
                break
            elif goal_input.isdigit() and (2 <= int(goal_input) < 1000):
                CONFIG['goal'] = int(goal_input)
                break
            else:
                print('Invalid Goal...')
                continue
        return

    def player_count(self) -> int:
        while True:
            print('- - - - - - - - - - - - - - - - - - ')
            players = input(f"Enter the number of players (2-{CONFIG['max_players']}): ")
            if players.isdigit():
                players = int(players)
                if players < 2 or players > CONFIG['max_players']:
                    print(f"There can only be 2 to {CONFIG['max_players']} players")
                else:
                    break
            else:
                print(f"Please enter a digit between 2 and {CONFIG['max_players']} which is the valid players required")
        return int(players)

    def roll(self) -> int | bool:
        roll = random.randint(1, CONFIG['max_dice'])

        if roll == 1:
            return False
        return roll


    def roll_setup(self) -> list | int:
        roll_value = 0
        roll_count = 0

        while True:
            roll_result = 0
            print('- - - - - - - - - - - - - - - - - - ')
            self.choice = input("Roll or Hold (r or h) - ")
            time.sleep(1)
            if self.choice.lower() == 'roll' or self.choice.lower() == 'r':
                roll_result = self.roll()
                if not roll_result:
                    if roll_value >= 1:
                        print('- - - - - - - - - - - - - - - - - - ')
                        print(f"{CONFIG['1-point-word']}... You got a 1. You've lost all ({roll_value}) points you got this round")
                        print(f'{self.withdraw} Points has also been removed from your total point')
                        return [0]
                    else:
                        print('- - - - - - - - - - - - - - - - - - ')
                        print(f"{CONFIG['1-point-word']}... You got a 1. Therefore you dont get any point this round")
                        print(f'{self.withdraw} Points has also been removed from your total point')
                        return [0]
                #roll_count += 1
                roll_value += roll_result
                
                print('- - - - - - - - - - - - - - - - - - ')
                if roll_result == 6:
                    print(f'You have just rolled a Freaking {roll_result}!, OPPORTUNITY: {roll_value}, do you want go with this or risk adding another roll?')
                else:
                    print(f'You have just rolled a {roll_result}, OPPORTUNITY: {roll_value}, do you want go with this or risk adding another roll?')
                
                print(f'You could lose {roll_value} points if you roll and get 1')

                # else:
                #     print('- - - - - - - - - - - - - - - - - - ')
                #     print(f'You have just rolled a {roll_result}, OPPORTUNITY: {roll_value}, do you want go with this or risk adding another roll?')
                #     print(f'You could lose {roll_value} points if you roll again and get 1')
            elif self.choice.lower() == 'hold' or self.choice.lower() == 'h':
                if isinstance(roll_value, int) and roll_value > 0:
                    print('- - - - - - - - - - - - - - - - - - ')
                    print(f'{roll_value} has been added to your points')
                    print('- - - - - - - - - - - - - - - - - - ')
                    return roll_value
                elif roll_value == 0:
                    print('- - - - - - - - - - - - - - - - - - ')
                    print('Turn Skipped')
                    print('- - - - - - - - - - - - - - - - - - ')
                    return 0
            else:
                print("please type either 'roll' or 'r' to role and 'hold' or 'h' to hold and continue with current point")
            roll_count += 1
            if roll_count == self.roll_limit:
                return roll_value or 0

    def check_win(self, point_to_check: int) -> bool:
        goal = CONFIG['goal']
        if point_to_check >= goal:
            return True
        else:
            return False

    def game(self) -> None:
        goal = CONFIG['goal']
        players_score = self.score
        player_count = self.player_count()
        apt = 1 # active_players_turn
        for i in range(player_count):
            self.score[f'player{i+1}'] = 0
        print('- - - - - - - - - - - - - - - - - - ')
        print(f'First to get to {goal}')
        for i, v in enumerate(players_score.values()):
            print(f'player-{i+1}: {v}')
        print('- - - - - - - - - - - - - - - - - - ')

        while True:
            if apt > player_count:
                apt = 1 
            print(f"Player-{apt}'s Turn")
            setup = self.roll_setup()
            #for i in range(len(players_score)):
            
            if isinstance(setup, list):
                players_score[f'player{apt}'] -= self.withdraw
            else:
                players_score[f'player{apt}'] += setup
            indiv_score = players_score[f'player{apt}'] #Individual Score
            if self.check_win(point_to_check=indiv_score) is True:
                print('- - - - - - - - - - - - - - - - - - ')
                print(f'Overall Goal: {goal}') 
                print('Current Score:') 
                for i, v in enumerate(players_score.values()):
                    print(f'player-{i+1}: {v}')
                print('|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|')
                print(f'player-{apt} has just won. Congratulations.')
                print('|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|')
                print('- - - - - - - - - - - - - - - - - - ')
                break

            print('- - - - - - - - - - - - - - - - - - ')
            print(f'Overall Goal: {goal}') 
            print('Current Score:') 
            time.sleep(0.5)
            for i, v in enumerate(players_score.values()):
                print(f'player-{i+1}: {v}')
            print('- - - - - - - - - - - - - - - - - - ')
            apt += 1
                    

def retry():
    print('\nDo you want to play again?')
    retry = input('Yes - 1 | No - 2 :- ')
    retry = retry.strip().lower()
    if retry == '1' or (retry == 'y' or retry == 'yes'):
        return True
    else:
        return False



if __name__ == '__main__':
    f = pyfiglet.Figlet(font='merlin1', width=150)
    print(f.renderText("Rave's Python Pig Game"))
    while True:
        run = PigGame().game()
        if retry() == True:
            continue
        else:
            break
