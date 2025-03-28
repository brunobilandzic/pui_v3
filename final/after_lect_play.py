from after_lect import State

counter = 0

def generate(state: State, dict):
    global counter
    counter += 1
    if state.as_string() in dict:
        # print("DUPLICATE")
        # print(state)
        return 

    dict[state.as_string()] = state

    if state.is_terminal():
        # print("TERMINAL")
        # print(state)
        return

    if state.is_goal():
        path = get_path(state)
        return path, counter

    # dict[state.as_string()] = state
    # print(f"next states are:\n")
    # for next_state in state.next_states():
    #     print(f"\t{next_state}")
        
    for next_state in state.next_states():
        if next_state.as_string() not in dict:
            result = generate(next_state, dict)
            if result is not None:
                return result


def get_path(current):
    path = []
    while current is not None:
        path.append(current)
        current = current.parent
    return list(reversed(path))


def main():
    global counter
    state = State()

    path, i = generate(state, {})
    counter = 0

    print()
    print(f"'Wisdom' generate Path length: {len(path)}, i: {i}")
    print()
    for state in path:
        print(state)
        print()

    

if __name__ == "__main__":
    main()