import random

from environments.neighborhood_manhattan_env import(
    NeighborhoodManhattanEnv
)

def benchmark():

    env = NeighborhoodManhattanEnv(
        radius=10
    )

    episodes = 1000
    max_steps = 100

    success_count = 0

    print(
        "\n=== RANDOM AGENT BENCHMARK ===\n"
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
        f"{len(env.shortest_route())} nodes\n"
    )

    for episode in range(episodes):

        state = env.reset()

        done = False

        total_reward = 0

        for step in range(max_steps):

            actions = env.get_actions()

            if not actions:
                break

            action = random.choice(
                actions
            )

            next_state, reward, done = (
                env.step(action)
            )

            state = next_state

            total_reward += reward

            if done:

                success_count += 1

                break
        
        if episode % 100 == 0:

            success_rate = (
                success_count
                /
                (episode + 1)
            ) * 100

            print(
                f"Episode {episode:4d} | "
                f"Reward: {total_reward:6.2f} | "
                f"Steps: {step:3d} | "
                f"Done: {done} | "
                f"Success: "
                f"{success_rate:5.1f}%"
            )

    print(
        "\n=== RANDOM BENCHMARK FINISHED ===\n"
    )

    print(
        f"Success Rate: "
        f"{success_count / episodes * 100:.2f}%"
    )

if __name__ == "__main__":

    benchmark()
