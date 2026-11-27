from environments.manhattan_graph_env import(
    ManhattanGraphEnv
)

import random

def run_random_benchmark():

    env = ManhattanGraphEnv()

    episodes = 100
    max_steps = 500

    successes = 0

    rewards = []
    steps_to_goal = []

    print("\n=== FULL MANHATTAN RANDOM BENCHMARK ===")

    print(
        f"Nodes: {env.graph.number_of_nodes()}"
    )

    print(
        f"Edges: {env.graph.number_of_edges()}"
    )

    route = env.a_star_route()

    print(
        f"Shortest Path Length: "
        f"{len(route)}"
    )

    print(
        f"Goal Reached: "
        f"{route[-1] == env.goal_node}"
    )

    for episode in range(episodes):

        state = env.reset()

        total_reward = 0

        for step in range(max_steps):

            actions = env.get_actions()

            if not actions:
                break

            action = random.choice(actions)

            state, reward, done = env.step(
                action
            )

            total_reward += reward

            if done:
                successes += 1

                steps_to_goal.append(
                    step + 1
                )

                break

    rewards.append(
        total_reward
    )

    if (episode + 1) % 10 == 0:

        print(
            f"Episode {episode +1}/"
            f"{episodes}"
        )

    success_rate = (
        successes / episodes
    ) * 100

    average_reward = (
        sum(rewards) / len(rewards)
    )

    print("\n=== RESULTS ===")

    print(
        f"Episodes: {episodes}"
    )

    print(
        f"Successes: {successes}"
    )

    print(
        f"Success Rate: "
        f"{success_rate:.2f}%"
    )

    print(
        f"Average Reward: "
        f"{average_reward:.2f}"
    )


    if steps_to_goal:

        print(
            f"Average Success Steps: "
            f"{sum(steps_to_goal) / len(steps_to_goal):.2f}"
        )

        print(
            f"Best Success Steps: "
            f"{min(steps_to_goal)}"
        )

        print(
            f"Worst Success Steps: "
            f"{max(steps_to_goal)}"
        )

    else:

        print(
            "Average Success Steps: N/A"
        )

        print(
            "Best Success Steps: N/A"
        )

        print(
            "Worst Success Steps: N/A"
        )

if __name__ == "__main__":

    run_random_benchmark()