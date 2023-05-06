players = []

for i in range(5):
    input_str = input()
    
    name, height_str = input_str.split()
    
    height = int(height_str)
    
    player_tuple = (height, name)
    players.append(player_tuple)

sorted_players = sorted(players)

for player in sorted_players:
    print(f"{player[0]} - {player[1]}")