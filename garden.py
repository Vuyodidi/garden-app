
def seasons(season):
    # Variable to hold gardening advice
    # Determine advice based on the season
    advice = ''
    # the if statements help to differentiate the users outcome or answer from the season they choose
    if season == "summer":
        advice += "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        advice += "Protect your plants from frost with covers.\n"
    else:
        advice += "No advice for this season.\n"
    return advice


def plant_types(plant_type):
    # Variable to hold plant type advice
    # Determine advice based on the season
    advice = ''
    # Determine advice based on the plant type
    # the if statements help to differentiate the users outcome or answer from the season they choose
    if plant_type == "flower":
        advice += "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        advice += "Keep an eye out for pests!"
    else:
        advice += "No advice for this type of plant."
    return advice




# Hardcoded values for the season and plant type
season = input("Whats season would you like to choose?").lower() 
plant_type = input("Whats plant type would you like to choose?").lower() 


# callin these functions for the values to be returned / funtion to be activated
season_var = seasons(season)
plant_types_var = plant_types(plant_type)


# Print the generated advice
print(season_var+plant_types_var)




