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


def find_state(capital_city):
    for state in states:
        if capital_cities[states[state]] == capital_city:
            return state
    return "Unknown state"


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(find_state(sys.argv[1]))
    else:
        exit(1)