from agents.manhattan_drone_agent import(
    DroneNavigatorAgent
)

from environments.mini_manhattan_env import(
    MiniManhattanEnv
)

def train():

    env = MiniManhattanEnv()

    agent = DroneNavigatorAgent()

    episodes = 500
    max_steps = 25

    success_count = 0

    print(
        "\n=== MINI MANHATTAN TRAINING ===\n"
    )

    print(
        f"Nodes: {len(env.nodes)}"
    )

    print(
        f"Start: {env.start_node}"
    )

    print(
        f"Goal : {env.goal_node}"
    )

    print(
        f"Shortest Route: "
        f"{len(env.shortest_route())} nodes \n"
    )

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

                success_count += 1

                break

        if episode % 50 == 0:

            success_rate = (
                success_count
                / (episode +1)
            ) * 100

            print(
                f"Episode {episode:4d} | "
                f"Reward: {total_reward:6.2f} | "
                f"Steps: {step:3d} | "
                f"Done: {done} | "
                f"Success: {success_rate:5.1f}% | "
                f"Q-Entries: "
                f"{agent.q_table_size()}"
            )
    print(
        "\n=== TRAINING FINISHED ===\n"
    )

    print(
        f"Success Rate: "
        f"{success_count / episodes * 100:.2f}%"
    )

    agent.print_statistics()

    return agent

if __name__ == "__main__":
    train()