import random

from environments.grid_world import ManhattanGridWorld

class RandomAgent:
    """
    A simple agent that selects actions randomly.
    """

    def __init__(self):

        self.actions = [
            "NORTH",
            "SOUTH",
            "EAST",
            "WEST"
        ]

    def choose_action(self):
        """
        Select a random action.
        """

        return random.choice(self.actions)

if __name__ == "__main__":

    env = ManhattanGridWorld()

    agent = RandomAgent()

    state = env.reset()

    done = False

    step_counter = 0

    max_steps = 100

    print("Starting Random Agent...\n")

    env.render()

    while not done and step_counter < max_steps:

        action = agent.choose_action()

        state, reward, done = env.step(action)

        print(
            f"Step={step_counter:03d} | "
            f"Action={action:>5} | "
            f"State={state} | "
            f"Reward={reward}"
        )

        env.render()

        step_counter += 1

        if done:
            print("Goal reached!")

    if not done:
        print("Episode terminated (max steps reached).")