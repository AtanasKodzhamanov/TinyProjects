import random 
import math

#initialize the properties
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Brown", "Gray", "Black"]

street_names = ["Rouge Acacia Avenue", "Violet Willow Way", "Luminaire Boulevard", "Elysium Avenue", "Calle del Sol", "Rue des Étoiles", "Verde Alder Lane", "Indigo Birch Court", "Orion Road", "Nebula Place", "Crimson Maple Street", "Turquoise Oak Drive", "Lunar Crescent", "Eden Way", "Calle de la Luna", "Rue des Fleurs", "Verde Pine Path", "Indigo Cedar Avenue", "Orbit Drive", "Nebula Boulevard", "Scarlet Willow Lane", "Turquoise Birch Court", "Lunar Avenue", "Eden Place", "Calle del Mar", "Rue des Oiseaux", "Verde Cedar Way", "Indigo Oak Drive", "Orbit Road", "Nebula Way"]

streets = {}

for i, street_name in enumerate(street_names):
    color = random.choice(colors)
    stars = random.choices([1, 2, 3, 4, 5], weights=[0.1, 0.2, 0.5, 0.2, 0.1])  # Generate a list of star ratings with specific probabilities
    stars = round(sum(stars) / len(stars))  # Calculate the average of the star ratings, rounded up to the nearest integer and overwrite the stars variable
    price = 200000 * stars * random.uniform(0.7, 1.5)  # Calculate the price of the property add some noise
    monthly_rent = int(price * random.uniform(0.05, 0.1) / 12)

    streets[street_name] = {
        "type": "Real Estate",
        "color": color,
        "price": price,
        "rent": monthly_rent,
        "stars": stars,  # Use the average of the star ratings as the value of the "stars" key
        "house_multiplier": random.uniform(1.3, 2),
        "houses": 0,
        "owner": "Public"
    }
    
# Ensure that there are between 2 and 4 repetitions of each color
for color in colors:
    color_count = sum(1 for street in streets.values() if street["color"] == color)
    if color_count < 2 or color_count > 4:
        # Find a street with a different color and reassign its color
        for street in streets.values():
            if street["color"] != color:
                street["color"] = color
                break

organizations = {}

organizations = {
    "Department of Redundant Regulations": {
        "type": "Effect",
        "reward": 0,
        "punishment": 0,
        "owner": "Government",
        "effect_list": []
    },
    "Bureau of Endless Paperwork": {
        "type": "Effect",
        "reward": 0,
        "punishment": 0,
        "owner": "Government",
        "effect_list": []
    },
    "Office of Inefficient Procedures": {
        "type": "Effect",
        "reward": 0,
        "punishment": 0,
        "owner": "Government",
        "effect_list": []
    },
    "Agency of Unnecessary Complications": {
        "type": "Effect",
        "reward": 0,
        "punishment": 0,
        "owner": "Government",
        "effect_list": []
    }
}

def assign_positions():
    # Create an empty list to hold the values from the streets and organizations dictionaries
    positions = []

    # Add the values from the streets dictionary to the positions list
    positions.extend(streets.values())

    # Add the values from the organizations dictionary to the positions list
    positions.extend(organizations.values())

    random.shuffle(positions)

    # Print the positions list
    return positions

