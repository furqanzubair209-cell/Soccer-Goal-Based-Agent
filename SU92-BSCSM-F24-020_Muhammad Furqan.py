# Soccer Agent Simulation using PEAS Framework
# Goal-Based Agent: Move toward ball → Gain possession → Move toward goal → Score

import math
import time


class SoccerAgent:

    def __init__(self):
        # Positions (x, y)
        self.agent_pos = [0, 0]
        self.ball_pos = [5, 5]
        self.goal_pos = [10, 10]

        # Agent state
        self.has_ball = False

    # Function to calculate distance
    def distance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    # Incremental movement toward target
    def move_toward(self, target):

        # Move in X direction
        if self.agent_pos[0] < target[0]:
            self.agent_pos[0] += 1
        elif self.agent_pos[0] > target[0]:
            self.agent_pos[0] -= 1

        # Move in Y direction
        if self.agent_pos[1] < target[1]:
            self.agent_pos[1] += 1
        elif self.agent_pos[1] > target[1]:
            self.agent_pos[1] -= 1

    # Main simulation loop
    def play(self):

        print("Soccer Agent Simulation Started\n")

        while True:

            print("Agent Position:", self.agent_pos)

            # If agent does not have ball
            if not self.has_ball:

                print("Agent moving toward ball...")
                self.move_toward(self.ball_pos)

                # Check possession
                if self.agent_pos == self.ball_pos:
                    self.has_ball = True
                    print("Agent reached the ball → Possession gained!")

            # If agent has ball
            else:
                print("Agent moving toward goal...")
                self.move_toward(self.goal_pos)

                if self.agent_pos == self.goal_pos:
                    print("GOAL SCORED! ⚽")
                    break

            time.sleep(1)


# Run simulation
agent = SoccerAgent()
agent.play()