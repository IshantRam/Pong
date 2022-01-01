import util

class Paddle:

    # Constructor
    def __init__(self, _X):
        # Data members
        self.X = _X
        self.Y = util.HEIGHT / 2
        self.Velocity = 0
        self.Width = 8
        self.Height = 80
        return

    # To display the Paddle
    def show(self, window):
        paddle = util.pygame.Rect(self.X, self.Y, self.Width, self.Height)
        util.pygame.draw.rect(window, util.WHITE, paddle)
        return

    # To move the paddle
    def move(self, steps):
        self.Velocity = steps
        return

    # To update the paddel
    def update(self):
        self.Y += self.Velocity
        self.Y = util.constrain(self.Y, self.Height / 16, (util.HEIGHT - self.Height) - 16 / 2)
        return
