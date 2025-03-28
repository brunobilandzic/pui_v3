LEFT = "LEFT"
RIGHT = "RIGHT"
BOAT = "BOAT"

STRING_POSITIONS = {
    "wolf": 0,
    "sheep": 1,
    "cabbage": 2,
    "boat": 3
}

ABRIVIATIONS = {
    "W": "wolf",
    "S": "sheep",
    "C": "cabbage",
    "B": "boat"
}

class GameAgent:
    side = LEFT

    
    def __init__(self, name):
        self.name = name

    def eating(self):
        if(self.name == "wolf"):
            return "sheep"
        elif(self.name == "sheep"):
            return "cabbage"
        else:
            return None
    
    def  eaten(self):
        if(self.name == "sheep"):
            return "wolf"
        elif(self.name == "cabbage"):
            return "sheep"
        else:
            return None

        
class Boat:
    side = LEFT
    passengers = []


class GameState:
    agents = {
        "wolf": GameAgent("wolf"),
        "sheep": GameAgent("sheep"),
        "cabbage": GameAgent("cabbage")
    }

    boat = Boat()
    
    def agents_on_side(self, side):
        return [agent for agent in self.agents if agent.side == side]
   
    def __init__(self, key):
        sides = key.split(" | ")
        self.left = sides[0].strip()
        self.right = sides[1].strip()

        for abriviation in self.left:
            agent = self.agents[ABRIVIATIONS[abriviation]]
            agent.side = LEFT
        for abriviation in self.right:
            agent = self.agents[ABRIVIATIONS[abriviation]]
            agent.side = RIGHT

    def all_actions(self):
        actions = []
        for agent in self.agents:
            if agent.side == self.boat.side and self.boat.passengers.count(agent) == 0:
                actions.append(GameAction(agent, self.boat))
            else:
                actions.append(GameAction(agent, self.boat))
        
 

class Game:
    state = GameState()

    def __str__(self):
        left_string = " " * 4
        right_string = " " * 4
        for agent in self.agents:
            if agent.side == LEFT:
                left_string = left_string[:STRING_POSITIONS[agent.name]] + agent.name[0].capitalize() + left_string[STRING_POSITIONS[agent.name]+1:]
            else:
                right_string = right_string[:STRING_POSITIONS[agent.name]] + agent.name[0].capitalize() + right_string[STRING_POSITIONS[agent.name]+1:]

        return left_string + " | " + right_string




class GameAction:
    pass

