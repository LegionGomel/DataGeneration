from random import choice


class RandomWalk:
    """Class for generating random walks"""

    def __init__(self, num_points=5000):
        """Init walk attributes"""
        self.num_points = num_points

        # All walks starts from (0, 0) point
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Define all walks points"""

        # Steps are generating until needed length is reached
        while len(self.x_values) < self.num_points:
            # Define direction and length of moving
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Deviation of zero movements
            if x_step == 0 and y_step == 0:
                continue

            # Define next x and y values
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)