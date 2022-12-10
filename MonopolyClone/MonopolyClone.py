import random
from BoardSetup import assign_positions

# Set up the board, place properties and special locations.
board=assign_positions()

board_size=len(board)
#initialize the players

players = [
    {"name": "Player 1", "position": 0, "money": 100000, "properties": [], "mortgage": 0, "rent": 0, "expenses": 0},
    {"name": "Player 2", "position": 0, "money": 100000, "properties": [], "mortgage": 0, "rent": 0, "expenses": 0},
    {"name": "Player 3", "position": 0, "money": 100000, "properties": [], "mortgage": 0, "rent": 0, "expenses": 0},
    {"name": "Player 4", "position": 0, "money": 100000, "properties": [], "mortgage": 0, "rent": 0, "expenses": 0},
]

#initialize the dice
dice = [0, 1, 2, 3, 4, 5]


# Start game loop    
while True:
    for player in players:

        # Prompt the user to enter a command to roll the die
        command = input("Press any key to throw the dice: ")
        
        # roll the dice
        dice_roll = random.choice(dice)
        print("You threw: " + str(dice_roll))

        # if the the player's current position + dice_roll exceeds the board_size, subtract the board size from the position
        if ( player["position"]+dice_roll > board_size-1 ):
            player["position"] = (player["position"] + dice_roll-board_size)
            player["money"] += 2500
        else:
            player["position"] = (player["position"] + dice_roll) 
        print( player["position"])
        
        # print the street they landed on
        street = board[player["position"]][0]
        print("You landed on " + str(street))

        # offer to buy the property if the owner is Public
        if board[player["position"]][1]["owner"] == "Public" and board[player["position"]][1]["type"] == "Real Estate":
            # Offer to buy the property
            price = board[player["position"]][1]["price"]
            response = input(f"Do you want to buy this property for ${price}? Y/N")

            if response == "Y":
                # Subtract the property's price from the player's money
                player["money"] -= price

                # Update the property's owner
                board[player["position"]][1]["owner"] = player["name"]

                # Add the property to the player's list of properties
                player["properties"].append(board[player["position"]][0])
                
        # Initialize the owner_player variable
        owner_player = None

        if board[player["position"]][1]["type"] == "Real Estate":
            if board[player["position"]][1]["owner"] != player["name"]:
                # Calculate the rent
                rent = board[player["position"]][1]["rent"]
                house_multiplier = board[player["position"]][1]["house_multiplier"]
                houses = board[player["position"]][1]["houses"]
                rent *= house_multiplier ** houses

                # Find the owner player
                for p in players:
                    if p["name"] == board[player["position"]][1]["owner"]:
                        owner_player = p
                        break
                if owner_player is not None:         
                    # Subtract the rent from the current player's money and add it to the owner player's money
                    player["money"] -= rent
                    owner_player["money"] += rent

                    print(f"You paid ${rent} in rent to {owner_player['name']}")

        # Build a house
        
        # Initialize the owner_player variable
        owner_player = "Public"

        if board[player["position"]][1]["owner"] == player["name"]:
            # Prompt the user to build a house
            response = input("Do you want to build a house on this property? Y/N")

            if response == "Y":
                # Check if the player has enough money to pay for the house
                house_cost = board[player["position"]][1]["price"] / 2
                if player["money"] >= house_cost:
                    # Subtract the cost of the house from the player's money and increment the number of houses on the property
                    player["money"] -= house_cost
                    board[player["position"]][1]["houses"] += 1

                    print("You built a house on {} for ${}".format(board[player["position"]][0], house_cost))
                else:
                    print("You don't have enough money to build a house")




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

    # Economics
        # Competition effects

    # The Monopoly Authority
    # The Oligopoly Bureau
    # The Cartel Commission
    # The Anti-Trust Agency
    # The Price Fixing Department
    # The Collusion Office
    # The Market Control Division
    # The Competition Council
    # The Corporate Regulation Agency
    # The Fair Trade Commission
    # The Oligopoly Enforcement Office
    # The Collusion Prevention Agency
    # The Market Power Division
    # The Dominance Regulation Office
    # The Predatory Pricing Task Force
    # The Monopolistic Practices Unit
    # The Oligopoly Observatory
    # The Price Fixing Bureau
    # The Cartel Countermeasures Committee
    # The Market Manipulation Monitoring Agency
    # The Collusion Detection Department
    # The Predatory Pricing Prevention Office
    # The Fair Trade Enforcement Agency