from generatee import *

entities = build_entities("V(LEFT) O(LEFT) K(LEFT) B(LEFT,None)")
print(entities.keys()) # {'V': 'LEFT', 'O': 'LEFT', 'K': 'LEFT', 'B': ('LEFT', 'None')}

new_state = State(entities["V"], entities["O"], entities["K"], entities["B"])
print(new_state) # V(LEFT) O(LEFT) K(LEFT) B(LEFT,None)