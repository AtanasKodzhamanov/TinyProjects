import random
from BoardSetup import assign_positions

# Set up the board, place properties and special locations.
assign_positions()

board_size=len(positions)
#initialize the players
num_players = 2
players = [{"name": "Player 1", "position": 0, "money": 1000, "properties": []},
{"name": "Player 2", "position": 0, "money": 1000, "properties": []}]


#initialize the dice
dice = [1, 2, 3, 4, 5]

 #start the game
for player in players:
# roll the dice
    roll = random[dice]
    player["position"] = (player["position"] + roll) 


    # pay rent 
    # if player["position"] is equal to foreign owned property
        # reduce this player's money
        # have another player's money go up

    #                 owner = properties[player["position"]]["owner"]
#                     if owner != player["name"]:
#                     rent = properties[player["position"]]["rent"]
#                     player["money"] -= rent
#                     owner_index = [i for i in range(len(players)) if players[i]["name"] == owner][0]
#                     players[owner_index]["money"] += rent
#                     print(f"{player['name']} has paid {rent} to {owner}.")

    # if its a special property
    # activate choices/effects    
        # set up random choices for the AI 

    # if the property is free
        # option to buy

#         elif properties[player["position"]]["owner"] is None:
#             property_name = properties[player["position"]]["name"]
#             property_price = properties[player["position"]]["price"]
#             if player["money"] >= property_price:
#                 buy_property = input(f"{player['name']}, do you want to buy {property_name} for {property_price}? (y/n) ")
#                 if buy_property.lower() == "y":
#                     player["properties"].append(player["position"])
#                         player["money"] -= property_price
#                         properties[player["position"]]["owner"] = player["name"]
#                         print(f"{player['name']} has bought {property_name}.")



    # have an exit condition where a player runs out of money and they are kicked out

    # AI variables - mixture of the below 0-1 effects
        # Given immoral choices more likely to take them
        # Aggressive buyer
        # Aggresive builder
        # 

    # Random events at the end of the turn
        # Higher taxes from rents
        # Lower taxes from rents 
        # Other stuff