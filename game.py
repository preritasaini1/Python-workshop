#non local variable in a game-
'''def game_round():
    score=0
    def increase_score(points):
        nonlocal score
        score+=points
    increase_score(10)
    return score
round_score=game_round()
print(round_score)'''

#global player stats in a game-
player_stats ={
    "name":"player1",
    "score":100,
    "level":5
}

def display_player_info():
    print(f"Name: {player_stats['name']}")
    print(f"Score: {player_stats['score']}")
    print(f"Level: {player_stats['level']}")

display_player_info()