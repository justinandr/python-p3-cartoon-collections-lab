def roll_call_dwarves(dwarves):
    for i in range(len(dwarves)):
        print(f"{i + 1}. {dwarves[i]}")

def summon_captain_planet(calls):
    return [call.title() + "!" for call in calls]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(foods):
    cheeses = ['cheddar', 'gouda', 'camembert']

    for food in foods:
        if food in cheeses:
            return food
        
    return None
