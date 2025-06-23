def parse(feet_inches_l):
    part = feet_inches_l.split(" ")
    feet = float(part[0])
    inches = float(part[1])
    return feet, inches


def convert(feet ,inches):
    meters=feet*0.3048 + inches*0.0254
    #return  f"{feet} feet and {inches} inches is equal to {meters} meters."
    return  meters


def parse(user_input):
    """Extract the values split by a comma in a string
    and return the two values via a dictionary.
    """
    # Get the two values in a list
    parts = user_input.split(",")

    # Store the two values in variables
    lower_bound = float(parts[0])
    upper_bound = float(parts[1])

    # Inject the values in a dictionary
    return {"lower_bound": lower_bound, "upper_bound": upper_bound}