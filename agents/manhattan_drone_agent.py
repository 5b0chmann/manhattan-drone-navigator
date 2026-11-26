import random

class DroneNavigatorAgent:
    """
    Q-Learning based agent for the
    Manhattan Drone Navigator project.
    
    State:
        Graph Node ID
        
    Action:
        Neighbor Node ID
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

        self.q_table = {}

    #--------------------------------------
    # Q TABLE
    #--------------------------------------

    def get_q_value(
            self,
            state,
            action
    ):
        """
        Return Q (state, action).
        Initialize with 0 if unknown.
        """

        if (state, action) not in self.q_table:
            self.q_table[(state, action)] = 0.0

        return self.q_table[(state, action)]

    #--------------------------------------
    # POLICY
    #--------------------------------------

    def choose_action(
            self,
            state,
            actions
    ):
        """
        Epsilon-greedy action selection.
        """

        if not actions:
            return None

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

        return random.choice(best_actions)

    #--------------------------------------
    # LEARNING
    #--------------------------------------

    def update_q_value(
            self,
            state,
            action,
            reward,
            next_state,
            next_actions
    ):
        """
        Q-Learning update rule.
        """

        current_q = self.get_q_value(
            state,
            action
        )

        if next_actions:

            max_future_q = max(

                self.get_q_value(
                    next_state,
                    future_action
                )

                for future_action
                in next_actions
            )

        else:

            max_future_q = 0.0

            updated_q = (

                current_q

                +

                self.alpha 
                * (
                    reward 
                    + self.gamma * max_future_q
                    - current_q
                )
            )

            self.q_table[
                (state, action)
            ] = updated_q

    #--------------------------------------
    # INFO
    #--------------------------------------

    def q_table_size(self):

        return len(
            self.q_table
        )

    def reset(self):

        self.q_table = {}

    def print_statistics(self):

        print("\n=== AGENT STATISTICS ===")

        print(
            f"Q-Table Entries: "
            f"{len(self.q_table)}"
        )

        print(
            f"Learning Rate : "
            f"{self.alpha}"
        )

        print(
            f"Discount      : "
            f"{self.gamma}"
        )

        print(
            f"Epsilon       : "
            f"{self.epsilon}"
        )

#--------------------------------------
# SIMPLE TEST
#--------------------------------------

if __name__ == "__main__":

    from environments.manhattan_graph_env import(
        ManhattanGraphEnv
    )

    env = ManhattanGraphEnv()

    agent = DroneNavigatorAgent()

    state = env.reset()

    actions = env.get_actions()

    action = agent.choose_action(
        state,
        actions
    )

    print("\n=== DRONE NAVIGATOR AGENT ===")

    print(
        f"State   : {state}"
    )

    print(
        f"Action  : {action}"
    )

    print(
        f"Known Q-Values : "
        f"{agent.q_table_size()}"
    )