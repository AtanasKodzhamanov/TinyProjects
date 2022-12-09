import random 

#initialize the properties
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Brown", "Gray", "Black"]

street_names = ["Maple Ave", "Main St", "Washington Blvd", "Park Ave", "Elm St", "First St", "Second St", "Third St", "Fourth Ave", "Fifth Ave", "Sixth Ave", "Seventh Ave", "Eighth Ave", "Ninth Ave", "Tenth Ave", "Eleventh Ave", "Twelfth Ave", "Thirteenth Ave", "Fourteenth Ave", "Fifteenth Ave", "Sixteenth Ave", "Seventeenth Ave", "Eighteenth Ave", "Nineteenth Ave", "Twenty-First Ave", "Twenty-Second Ave", "Twenty-Third Ave", "Twenty-Fourth Ave", "Twenty-Fifth Ave"]

streets = {}

for i, street_name in enumerate(street_names):
    color = random.choice(colors)
    streets[street_name] = {
        "color": color,
        "price": (i + 1) * 100,
        "rent": (i + 1) * 5,
        "house_multiplier": random.uniform(1.2, 1.4),
        "houses": 0,
        "owner": None
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
        "reward": 0,
        "punishment": 0,
        "effect_list": []
    },
    "Bureau of Endless Paperwork": {
        "reward": 0,
        "punishment": 0,
        "effect_list": []
    },
    "Office of Inefficient Procedures": {
        "reward": 0,
        "punishment": 0,
        "effect_list": []
    },
    "Agency of Unnecessary Complications": {
        "reward": 0,
        "punishment": 0,
        "effect_list": []
    }
}


def assign_positions():
    # Create an empty array with the same length as the number of organizations and streets
    positions = [None] * (len(organizations) + len(streets))

    # Assign each organization a position in the array
    for i, organization_name in enumerate(organizations.keys()):
        positions[i] = (organization_name, organizations[organization_name])

    # Assign each street a position in the array
    for i, street_name in enumerate(streets.keys()):
        positions[len(organizations) + i] = (street_name, streets[street_name])
    print(positions)
    return positions