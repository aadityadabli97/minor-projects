import art,random
from game_data import data
print(art.logo)
end_of_game=False
score=0
choice1=random.choice(data)
def compare():
    global end_of_game,score,choice1
    choice2=random.choice(data)
    print(f"Compare A: {choice1['name']} a {choice1['description']} from {choice1['country']}")
    print(art.vs)
    print(f"Against B: {choice2['name']} a {choice2['description']} from {choice2['country']}")
    comparison=input("Who has more followers ? Type 'A' or 'B' : ")
    if comparison=='A' and choice1['follower_count']>choice2['follower_count']:
        score+=1
        print(f"You are right !, current score : {score}")
        choice1=choice2
    elif comparison=='B' and choice1['follower_count']<choice2['follower_count']:
        score+=1
        print(f"You are right !, current score : {score}")
        choice1=choice2
    else:
        print(f"Sorry, that's wrong. Final score : {score} ")
        end_of_game=True
while not end_of_game:
    compare()
