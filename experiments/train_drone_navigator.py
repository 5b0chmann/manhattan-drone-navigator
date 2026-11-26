from agents.manhattan_drone_agent import(
    DroneNavigatorAgent
)

from environments.manhattan_graph_env import(
    ManhattanGraphEnv
)

def train():

    env = ManhattanGraphEnv()

    agent = DroneNavigatorAgent()

    episodes = 50
    max_steps = 250

    print("\n=== TRAINING STARTED ===\n")

    for episode in range(episodes):

        state = env.reset()

        total_reward = 0

        done = False

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
                break

        if episode % 100 == 0:

            print(
                f"Episode {episode:4d} | "
                f"Reward: {total_reward:6.2f} | "
                f"Steps: {step:4d} | "
                f"Done: {done} | "
                f"Q-Entries: {agent.q_table_size()}"
            )

    print("\n=== TRAINING FINISHED ===\n")

    agent.print_statistics()

    return agent

if __name__ == "__main__":

    train()