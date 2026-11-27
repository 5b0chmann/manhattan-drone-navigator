from agents.manhattan_drone_agent import(
    DroneNavigatorAgent
)

from environments.neighborhood_manhattan_env import(
    NeighborhoodManhattanEnv
)

def evaluate_agent(
        env,
        agent,
        max_steps=1000):

    # keine Exploration
    agent.epsilon = 0.0

    state = env.reset()

    path = [state]

    done = False

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

        path.append(
            next_state
        )

        total_reward += reward
        state = next_state

        if done:
            break

    print(
        f"\n=== POLICY EVALUATION ===\n"
    )

    print(
        f"Start Node : "
        f"{env.start_node}"
    )

    print(
        f"Goal Node : "
        f"{env.goal_node}"
    )

    print(
        f"Done : "
        f"{done}"
    )

    print(
        f"Steps: "
        f"{len(path) - 1}"
    )

    print(
        f"Reward: "
        f"{total_reward}"
    )

    print(
        f"Path Nodes: "
        f"{len(path)}"
    )

    print(
        "\nVisited Route:\n"
    )

    for node in path:

        print(node)

    return{
        "done": done,
        "steps": len(path) -1,
        "reward": total_reward,
        "path": path                   
    }

def train_for_evaluation():

    env = NeighborhoodManhattanEnv(
        radius=10
    )

    agent= DroneNavigatorAgent(
        epsilon=0.05
    )

    episodes = 1000
    max_steps = 100

    for episode in range(episodes):

        state = env.reset()

        done = False
        for _ in range(max_steps):

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
            if done:
                break
    
    return env, agent

if __name__ == "__main__":

    env, agent = (
        train_for_evaluation()
    )

    evaluate_agent(
        env,
        agent
    )
