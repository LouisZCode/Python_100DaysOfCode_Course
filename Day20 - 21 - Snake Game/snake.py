import turtle

"""Global Constants are in Mayus and Snake Style"""
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    """Body Part Creation"""
    def __init__(self):
        self.n_parts = []

#Here we could create a method called "def create_snake" bu is it not redundant?
        for position in STARTING_POSITION:
           self.add_segment(position)

        self.head = self.n_parts[0]

    def move(self):
        """Movement logic, the parts of the body (segments) follow the head (segment[0])"""
        # for seg_num in range(start=2 (last part), stop=0 (first part - head), step=-1) for visualization
        for seg_num in range(len(self.n_parts) - 1, 0, -1):
            new_x = self.n_parts[seg_num - 1].xcor()
            new_y = self.n_parts[seg_num - 1].ycor()
            self.n_parts[seg_num].goto(new_x, new_y)
        """We take the head and move it, the code above will take the segments and move them accordingly"""
        self.n_parts[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:   #.heading is not the same as .setheading! careful with these little details
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self, position):
        new_segment = turtle.Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.n_parts.append(new_segment)

    def extend(self):
        self.add_segment(self.n_parts[-1].position())
