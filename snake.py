from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create(self):
        for position in STARTING_POSITIONS:
            self.addSegment(position)

    def addSegment(self, position):
        newSegment = Turtle('square')
        newSegment.color('white')
        newSegment.penup()
        newSegment.goto(position)
        self.segments.append(newSegment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            segment = self.segments[i - 1]
            nextPosition = self.getSegmentPosition(segment)
            self.segments[i].goto(nextPosition)
        self.head.forward(20)

    def getSegmentPosition(self, segment):
        return (segment.xcor(), segment.ycor())

    def up(self):
        if(self.head.heading() != DOWN):
            self.head.setheading(UP)

    def down(self):
        if (self.head.heading() != UP):
            self.head.setheading(DOWN)

    def left(self):
        if (self.head.heading() != RIGHT):
            self.head.setheading(LEFT)

    def right(self):
        if (self.head.heading() != LEFT):
            self.head.setheading(RIGHT)

    def extend(self):
        self.addSegment(self.getSegmentPosition(self.tail))
        self.tail = self.segments[-1]



