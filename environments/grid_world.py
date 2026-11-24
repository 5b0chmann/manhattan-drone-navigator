
class ManhattanGridWorld:
    """
    Simple Manhattan Grid Environment.
    
    Start: (0, 0)
    Goal: (width - 1, height - 1)
    
    Available actions:
    - NORTH
    - SOUTH
    - EAST
    - WEST
    """

    def __init__(self, width=10, height=10):

        self.width = width
        self.height = height

        self.start = (0, 0)
        self.goal = (width - 1, height - 1)

        self.agent_position = self.start

        self.obstacles = {
            (3, 3),
            (3, 4),
            (3, 5),
            (4, 5),
            (5, 5)
        }

    def reset(self):
        """
        Reset the agent to the starting position.
        """

        self.agent_position = self.start
        return self.agent_position

    def manhattan_distance(self, position):
        """
        Calculate the Manhattan distance to the goal.
        """

        x, y = position
        gx, gy = self.goal
        
        return abs(x - gx) + abs(y - gy)

    def step(self, action):
        """
        Execute an action and return:
        
        state, reward, done
        """

        x, y = self.agent_position

        if action == "NORTH":
            y = min(y + 1, self.height -1)

        elif action == "SOUTH":
            y = max(y -1, 0)

        elif action == "EAST":
            x = min(x + 1, self.width -1)

        elif action == "WEST":
            x = max(x - 1, 0)

        # Candidate position
        new_position = (x, y)

        # Obstacle collision
        if new_position in self.obstacles:

            reward = -10

            done = False

            return(
                self.agent_position,
                reward,
                False
            )

        old_distance = self.manhattan_distance(self.agent_position)

        self.agent_position = new_position

        new_distance = self.manhattan_distance(self.agent_position)

        reward = old_distance - new_distance

        done = self.agent_position == self.goal

        if done:
            reward += 100

        return self.agent_position, reward, done
    

    def render(self):
        """
        Render the environment as ASCII text.
        """

        print()

        for y in reversed(range(self.height)):

            row = []

            for x in range(self.width):

                position = (x, y)

                if position == self.agent_position:
                    row.append("D")

                elif position == self.goal:
                    row.append("G")

                elif position in self.obstacles:
                    row.append("X")

                else:
                    row.append(".")

            print(" ".join(row))

        print()

if __name__ == "__main__":

    env = ManhattanGridWorld()

    state = env.reset()

    print("Initial State:", state)

    env.render()

    actions = [
        "EAST",
        "EAST",
        "EAST",
        "NORTH",
        "NORTH",
        "NORTH",
        "NORTH"
    ]

    for action in actions:

        state, reward, done = env.step(action)

        print(
            f"Action={action:>5} | "
            f"State={state} | "
            f"Reward={reward}"
        )

        env.render()

        if done:
            print("Goal reached!")
            break