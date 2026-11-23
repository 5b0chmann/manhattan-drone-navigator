import random

from environments.grid_world import ManhattanGridWorld

class QLearningAgent:
    """
    Q-Learning agent for the Manhattan Grid World.
    """

    def __init__(
            self, 
            learning_rate=0.1,
            discount_factor=0.95,
            epsilon=0.1
    ):

        self.alpha = learning_rate
        self.gamma = discount_factor
        self.epsilon = epsilon

        self.actions = [
            "NORTH",
            "SOUTH",
            "EAST",
            "WEST"
        ]

        self.q_table = {}

    def get_q_value(self, state, action):
        """
        Return Q(state, action).
        If the pair does not exist yet, initialize with 0.
        """

        if (state, action) not in self.q_table:
            self.q_table[(state, action)] = 0.0

        return self.q_table[(state, action)]

    def choose_action(self, state):
        """
        Epsilon-greed policy.
        """

        if random.random() < self.epsilon:
            return random.choice(self.actions)

        q_values = [
            self.get_q_value(state, action)
            for action in self.actions
        ]

        max_q = max(q_values)

        best_actions = [
            action
            for action, q in zip(self.actions, q_values)
            if q == max_q
        ]

        return random.choice(best_actions)

    def update_q_value(
            self,
            state,
            action,
            reward,
            next_state
    ):
        """
        Q-Learning update rule.
        """

        current_q = self.get_q_value(
            state,
            action
        )

        max_future_q = max(
            self.get_q_value(next_state, future_action)
            for future_action in self.actions
        )

        updated_q = current_q + self.alpha * (
            reward
            + self.gamma * max_future_q
            - current_q
        )

        self.q_table[(state, action)] = updated_q

if __name__ == "__main__":

    env = ManhattanGridWorld()

    agent = QLearningAgent()

    episodes = 1000
    max_steps = 100

    for episode in range(episodes):

        state = env.reset()

        total_reward = 0

        for _ in range(max_steps):

            action = agent.choose_action(state)

            next_state, reward, done = env.step(action)

            agent.update_q_value(
                state,
                action,
                reward,
                next_state
            )

            state = next_state

            total_reward += reward

            if done:
                break
        if episode % 100 == 0:

            print(
                f"Episode {episode:4d} | "
                f"Total Reward: {total_reward:4d}"
            )

    print("\nTraining finished.\n")

    print("Learned policy examples:\n")

    important_states =[
        (0, 0),
        (1, 0),
        (2, 0),
        (5, 5),
        (8, 8)
    ]

    for state in important_states:

        q_values = {
            action: agent.get_q_value(
                state,
                action
            )
            for action in agent.actions
        }

        best_action = max(
            q_values,
            key=q_values.get
        )

        print(
            f"State {state} "
            f"-> Best Action: {best_action}"
        )
        