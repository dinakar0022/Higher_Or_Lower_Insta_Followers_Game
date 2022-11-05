from game_data import data
from art_1 import logo, vs
import random
from replit import clear

print(logo)           #for the first time logo will be used from this line of code


def check_who_has_more_followers(first_id_followers, second_id_followers):   #checking which account is having more followers
    if first_id_followers > second_id_followers:
        return "A"
    else:
        return "B"

score = 0   #starting score
flag = True   #starting flag 

first_id = random.choice(data)   # first account
second_id = random.choice(data)  # second account

while second_id==first_id:       #making sure that first != second  because of random.choice module
        second_id=random.choice(data)

while flag:                      #if this breaks the game ends....the flag gets changed to False if the user guess it wrong

    first_id_name = first_id["name"]                #taking values from the dictionaries of first account
    first_id_description = first_id["description"]
    first_id_country = first_id["country"]
    first_id_followers = first_id["follower_count"]

    second_id_name = second_id["name"]              #taking values from the dictionaries of second account
    second_id_description = second_id["description"]
    second_id_country = second_id["country"]
    second_id_followers = second_id["follower_count"]
    
    #showing the user the choices he have
    print(
        f"Compare A: {first_id_name}, {first_id_description}, {first_id_country}."
    )
    print(vs)   #print(VS ASCII art)
    print(
        f"Compare B: {second_id_name}, {second_id_description}, {second_id_country}."
    )

    #Player Zone

    player_ans = input("Who has more followers A or B: Type A or B: ")
    #if user guesses it correct then increment the score and clean the screen and print his current score and show him the next round choices he have
    if player_ans == check_who_has_more_followers(first_id_followers,                                    second_id_followers):
      score = score + 1
      clear()
      print(logo)
      print(f"You're right! Current score: {score}.")
      #if he guesses it right give assign second_id to first_id for the next round for the second account take another one randomly from the data (a list of dictionaries).
      first_id = second_id     
      second_id = random.choice(data)      
      
      while second_id==first_id:
        second_id=random.choice(data)
        
    else:  #if he guesses it wrong claer the screen and show him his score before this round and turn the flag to False so that while loop gets broken
        clear()
        print(logo)
        print(f"Sorry that's wrong. Final Score: {score}")
        flag=False
