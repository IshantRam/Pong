import util

class Puck:

    # The constructor
    def __init__(self, ):
        # Data members
        self.X = util.WIDTH / 2
        self.Y = util.HEIGHT / 2
        self.dX = util.random.uniform(0.2, 0.4)
        self.dY = util.random.uniform(0.1, 0.3)
        self.Raidus = 10
        if util.random.randint(0, 5) == 2:
            self.dX = -self.dX
        return

    # To check collision with right paddle
    def checkrightPaddleCollision(self, paddle):
        if self.X >= util.WIDTH + 1 - self.Raidus - paddle.Width and int(self.Y) in range(int(paddle.Y - (paddle.Height)), int(paddle.Y + (paddle.Height)), 1):
            util.paddleSound.play()
            self.dX = -self.dX
            self.dX *= 1
            self.dY *= 1
        elif self.X >= util.WIDTH + 1 - self.Raidus - paddle.Width:
            util.scoreSound.play()
            util.LEFT_SCORE += 1
            self.reset(True)
        return

    # To check collision with left paddle
    def checkleftPaddleCollision(self, paddle):
        if self.X <= self.Raidus + paddle.Width and int(self.Y) in range(int(paddle.Y - (paddle.Height)), int(paddle.Y + (paddle.Height)), 1):
            util.paddleSound.play()
            self.dX = -self.dX
            self.dX *= 1
            self.dY *= 1
        elif self.X <= self.Raidus + paddle.Width:
            util.scoreSound.play()
            util.RIGHT_SCORE += 1
            self.reset()

        return

    # To check collision with wall
    def collision(self):
        if (self.Y < 0 or self.Y > util.HEIGHT):
            self.dY *= -1
            util.wallSound.play()

        if (self.X < 0 or self.X > util.WIDTH):
            self.reset(False)
        return

    # To reset
    def reset(self, right=True):
        self.X = util.WIDTH / 2
        self.Y = util.HEIGHT / 2
        self.Raidus = 10
        self.dX = util.random.uniform(0.2, 0.4)
        self.dY = util.random.uniform(0.1, 0.3)
        if right == False:
            self.dX = -self.dX
        return

    # To display the Puck
    def show(self, window):
        util.pygame.draw.circle(window, util.WHITE, (self.X, self.Y), self.Raidus)
        return

    # To change position of Puck
    def update(self):
        self.X += self.dX
        self.Y += self.dY
        return
