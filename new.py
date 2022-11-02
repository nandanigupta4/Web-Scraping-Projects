player_names=['sachin','ashwin','kohli']
scores_per_ball=[[1,3,4,5,5,6],[3,4,3,6,5],[2,4,2,3,4]]
max_score=0
strike_rate=0
max_player=None
zip_list=zip(player_names,scores_per_ball)
for player in zip_list:
    sum_scores=0
    count=len(player[1])
    for j in player[1]:
        sum_scores+=j
    strike_ind= sum_scores/count
    if strike_ind>=strike_rate:
        strike_rate=strike_ind
        max_player=player[0]

print(max_player)
print(strike_rate)



    

