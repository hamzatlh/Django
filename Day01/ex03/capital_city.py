import sys

states = {
    "Oregon": "OR",
    "Alabama": "AL",
    "New Jersey": "NJ",
    "Colorado": "CO"
}

capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
}

def find_capital_city(state):
    if state in states:
        return capital_cities[states[state]]
    return "Unknown capital city"

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(find_capital_city(sys.argv[1]))
    else:
        exit(1)