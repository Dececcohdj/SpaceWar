import turtle
import random
import math
wn = turtle.Screen()

wn.screensize(300, 300)

wn.bgcolor("green")

pen = turtle.Turtle()

pen.shape("circle")

pen.color("white")

pen.shapesize(0.7)

pen.penup()

variable2 = random.randint(-255, 255)

variable = random.randint(-255, 255)

pen.goto(variable, variable2)

urmom = turtle.Turtle()

urmom.shapesize(1.1)

urmom.shape("circle")
# golf ball


class Sprite():

    @staticmethod
    def is_collision(sprite1, sprite2, threshold):

        d = math.sqrt((sprite1.x - sprite2.x) ** 2 + (sprite1.y - sprite2.y) ** 2)

        if d < threshold:

            return True

        else:

            return False

    @staticmethod
    def is_on_screen(sprite, screen_width, screen_height, x_offset, y_offset):

        if sprite.x - x_offset < screen_width / 2 and sprite.x - x_offset > -screen_width / 2 \
 \
                and sprite.y - y_offset < screen_height / 2 and sprite.y - y_offset > - screen_height / 2:

            return True

        else:

            return False

    def __init__(self, x, y, shape="square", color="white"):

        self.shape = shape

        self.color = color

        self.width = 20.0

        self.height = 20.0

        self.heading = 0.0

        self.dx = 0.0

        self.dy = 0.0

        self.da = 0.0

        self.thrust = 0.0

        self.max_d = 2.0

        self.x = x

        self.y = y

        self.state = "active"

    def bounce(self, other):

        temp_dx = self.dx

        temp_dy = self.dy

        self.dx = other.dx

        self.dy = other.dy

        other.dx = temp_dx

        other.dy = temp_dy

    def update(self):

        self.heading += self.da

        self.heading %= 360.0

        self.dx += math.cos(math.radians(self.heading)) * self.thrust

        self.dy += math.sin(math.radians(self.heading)) * self.thrust

        self.x += self.dx

        self.y += self.dy

        self.border_check()

    def border_check(self):

        if self.x > game.width / 2.0 - 10.0:

            self.x = game.width / 2.0 - 10.0

            self.dx *= -1.0

        elif self.x < -game.width / 2.0 + 10.0:

            self.x = -game.width / 2.0 + 10.0

            self.dx *= -1.0

        if self.y > game.height / 2.0 - 10.0:

            self.y = game.height / 2.0 - 10.0

            self.dy *= -1.0

        elif self.y < -game.height / 2.0 + 10.0:

            self.y = -game.height / 2.0 + 10.0

            self.dy *= -1.0

    def render(self, pen, x_offset=0, y_offset=0):

        # Check if active

        if self.state == "active":

            # Check if it is on the screen

            screen_x = self.x - x_offset

            screen_y = self.y - y_offset

            if (
                    screen_x > -game.width / 2.0 and screen_x < game.width / 2.0 and screen_y > -game.height / 2.0 and screen_y < game.width / 2.0):
                pen.goto(self.x - x_offset, self.y - y_offset)

                pen.shape(self.shape)

                pen.color(self.color)

                pen.shapesize(stretch_wid=1, stretch_len=1, outline=None)

                pen.setheading(self.heading)

                pen.stamp()

class Player(Sprite):

    def __init__(self):

        Sprite.__init__(self, 0.0, 0.0, "circle")

        self.da = 0.0

        self.heading = 90.0

        self.score = 0

        self.max_health = 40

        self.health = self.max_health

        self.sensor_range = 500

        self.thrust = 0.0

        self.acceleration = 0.2

        self.lives = 3

    def rotate_left(self):

        self.da = 10.0

    def rotate_right(self):

        self.da = -10.0

    def stop_rotation(self):

        self.da = 0.0

    def accelerate(self):



        self.thrust += self.acceleration

        dx = math.cos(math.radians(self.heading + 180)) * 5

        dy = math.sin(math.radians(self.heading + 180)) * 5

        exhaust.explode(self.x - 100, self.y, dx, dy)

    def decelerate(self):

        self.thrust = 0.0

    def fire(self):



        directions = [0, 5, -5]

        for missile in missiles:

            # print(directions)

            if missile.state == "ready":

                missile.x = player.x

                missile.y = player.y

                missile.heading = player.heading + directions[0]

                missile.dx = math.cos(math.radians(missile.heading)) * missile.thrust

                missile.dy = math.sin(math.radians(missile.heading)) * missile.thrust

                missile.dx += player.dx

                missile.dy += player.dy

                missile.state = "active"

                self.dx -= missile.dx * 0.01

                self.dy -= missile.dy * 0.01

                directions.pop(0)

                if len(directions) == 0:
                    break

    def reset(self):

        self.x = 0.0

        self.y = 0.0

        self.dx = 0.0

        self.dy = 0.0

        self.da = 0.0

        self.heading = 90.0

        self.health = self.max_health

    def render(self, pen, x_offset=0, y_offset=0):

        pen.shapesize(stretch_wid=0.5, stretch_len=1, outline=None)

        pen.goto(self.x - x_offset, self.y - y_offset)

        pen.shape(self.shape)

        pen.color(self.color)

        pen.setheading(self.heading)

        pen.stamp()

        # Draw health

        pen.goto(self.x - x_offset - 10.0, self.y - y_offset + 20.0)

        pen.width(3.0)

        pen.pendown()

        pen.setheading(0.0)

        try:

            if self.health / self.max_health < 0.3:

                pen.color("red")

            elif self.health / self.max_health < 0.7:

                pen.color("yellow")

            else:

                pen.color("green")

            pen.fd(20.0 * (self.health / self.max_health))

            pen.color("grey")

            pen.fd(20.0 * ((self.max_health - self.health) / self.max_health))

        except:

            pass

        pen.penup()

while True:
    wn.update()
