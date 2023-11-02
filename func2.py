'''def start_adventure():
    hero_name=input("enter your hero's name")
    print(f"welcome,{hero_name}! you embark on an epic adventure.")
start_adventure()'''


high_score=0  #global score
def update_high_score(score):
    global high_score
    if score>high_score:
        high_score=score
update_high_score(50)
print(high_score)
