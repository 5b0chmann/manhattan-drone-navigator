from environments.manhattan_graph_env import(
    ManhattanGraphEnv
)

import random

class FullManhattanQLearningAgent:

    def __init__(
            self,
            learning_rate=0.1,
            discount_factor=0.95,
            epsilon=1.0, 
            epsilon_decay=0.995,
            epsilon_min=0.05
    ):

        self.q_table = {}

        self.learning_rate = learning_rate
        self.discount_factor = discount_factor

        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min

    def get_q_value(
            self,
            state,
            action
    ):

        return self.q_table.get(
            (state, action),
            0.0
        )

    def choose_action(
            self,
            state,
            actions
    ):

        if random.random() < self.epsilon:

            return random.choice(actions)

        q_values = [

            self.get_q_value(
                state,
                action
            )

            for action in actions
        ]

        max_q = max(q_values)
        best_actions = [

            action

            for action, q in zip(
                actions,
                q_values
            )

            if q == max_q
        ]

        return random.choice(
            best_actions
        )

    def update_q_value(
            self,
            state,
            action,
            reward,
            next_state,
            next_actions
    ):

        current_q = self.get_q_value(
            state,
            action
        )

        if next_actions:

            max_future_q = max(

                self.get_q_value(
                    next_state,
                    next_action
                )

                for next_action
                in next_actions
            )

        else:

            max_future_q = 0.0

        updated_q = (

            current_q

            + self.learning_rate * (

                reward

                + self.discount_factor
                * max_future_q

                - current_q
            )
        )

        self.q_table[
            (state, action)
        ] = updated_q

    def decay_epsilon(self):

        self.epsilon = max(
            self.epsilon_min,
            self.epsilon
            * self.epsilon_decay
        ) 

def train():

    env = ManhattanGraphEnv()

    agent = FullManhattanQLearningAgent()

    episodes = 5000
    max_steps = 500

    successes = 0

    print("\n=== FULL MANHATTAN Q-LEARNING ===")

    print(
        f"Nodes: {env.graph.number_of_nodes()}"
    )

    print(
        f"Edges: {env.graph.number_of_edges()}"
    )

    route = env.a_star_route()

    print(
        f"A* Route Length: "
        f"{len(route)}"
    )
    for episode in range(episodes):

        state = env.reset()

        total_reward = 0

        for step in range(max_steps):

            actions = env.get_actions()

            if not actions:
                break

            action = agent.choose_action(
                state,
                actions
            )

            next_state, reward, done = (
                env.step(action)
            )

            next_actions = (
                env.get_actions()
            )

            agent.update_q_value(
                state,
                action,
                reward,
                next_state,
                next_actions
            )

            state = next_state

            total_reward += reward

            if done:

                successes += 1

                break

        agent.decay_epsilon()

        if (episode + 1) % 500 == 0:

            success_rate = (
                successes
                / (episode + 1)
            ) * 100

            print(
                f"Episode "
                f"{episode + 1}"
            )

            print(
                f"Success Rate: "
                f"{success_rate:.2f}%"
            )

            print(
                f"Q-Table Size: "
                f"{len(agent.q_table)}"
            )

            print(
                f"Epsilon: "
                f"{agent.epsilon:.3f}"
            )

            print()

    print("\n=== FINAL RESULTS ===")

    print(
        f"Episodes: {episodes}"
    )

    print(
        f"Successes: {successes}"
    )

    print(
        f"Success Rate: "
        f"{(successes / episodes) * 100:.2f}%"
    )

    print(
        f"Q-Table Entries: "
        f"{len(agent.q_table)}"
    )

if __name__ == "__main__":

    train()
