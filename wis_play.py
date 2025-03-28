from wis_wolf import State

def generate(state: State, dict):
    
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
        print("GOAL")
        print(state, len(dict))
        return dict

    # dict[state.as_string()] = state
    # print(f"next states are:\n")
    # for next_state in state.next_states():
    #     print(f"\t{next_state}")
        
    for next_state in state.next_states():
        if next_state.as_string() not in dict:
            generate(next_state, dict)




def main():
    state = State()

    generate(state, {})

    

if __name__ == "__main__":
    main()