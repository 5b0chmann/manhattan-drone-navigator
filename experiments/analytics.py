from environments.grid_world import ManhattanGridWorld
from agents.q_learning_agent import QLearningAgent

def run_analytics():

    env = ManhattanGridWorld()

    agent = QLearningAgent()

    episodes = 1000
    max_steps = 100

    successful_episodes = 0
    total_rewards =[]
    total_steps = []

    print("Trainig agent...\n")

    for episode in range(episodes):

        state = env.reset()

        episode_reward = 0

        for step in range(max_steps):

            action = agent.choose_action(state)

            next_state, reward, done = env.step(action)

            agent.update_q_value(
                state,
                action,
                reward,
                next_state
            )

            state = next_state
            episode_reward += reward

            if done:

                successful_episodes += 1
                total_steps.append(step + 1)

                break

        total_rewards.append(episode_reward)

    success_rate = (
        successful_episodes / episodes
    ) * 100

    average_reward = (
        sum(total_rewards) / len(total_rewards)
    )

    average_steps = (
        sum(total_steps) / len(total_steps)
        if total_steps
        else 0
    )

    best_steps = min(total_steps)
    worst_steps = max(total_steps)

    print("====ANALYTICS====")
    print(f"Episodes       : {episodes}")
    print(f"Success Rate   : {success_rate:.2f}%")
    print(f"Average Reward : {average_reward:.2f}")
    print(f"Average Steps  : {average_steps:.2f}")
    print(f"Best Reward    : {max(total_rewards)}")
    print(f"Worst Reward   : {min(total_rewards)}")
    print(f"Best Steps     : {best_steps}")
    print(f"Worst Steps    : {worst_steps}")

if __name__== "__main__":
    run_analytics()