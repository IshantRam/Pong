import util
import puck
import paddle

# Initializing pygame
util.pygame.init()

# The window
util.pygame.display.set_caption("Arcade Pong")
window = util.pygame.display.set_mode((util.WIDTH, util.HEIGHT))

# The font
font = util.pygame.font.SysFont("assets/font/COMIC.TTF", 50)

# The puck
ball = puck.Puck()

# The paddles
left = paddle.Paddle(0)
right = paddle.Paddle(util.WIDTH - left.Width)

# The guide
print(util.colored("To move left paddle use W and S Keys", "yellow"))
print(util.colored("To move right paddle use Up and Down Arrow", "yellow"))

# The game loop
while True:
    for event in util.pygame.event.get():
        # Quiting the game
        if event.type == util.pygame.QUIT:
            util.pygame.quit()
            util.exit(0)

        # Small hack
        if event.type == util.pygame.KEYUP:
            left.move(0)
            right.move(0)

        # Left paddle Movement
        if event.type == util.pygame.KEYDOWN:
            if event.key == util.pygame.K_w:
                left.move(-0.5)
            if event.key == util.pygame.K_s:
                left.move(0.5)

        # Right paddle Movement
        if event.type == util.pygame.KEYDOWN:
            if event.key == util.pygame.K_UP:
                right.move(-0.5)
            if event.key == util.pygame.K_DOWN:
                right.move(0.5)

    # Filling the background
    window.fill(util.BLACK)

    # Displaying the Paddle
    left.show(window)
    right.show(window)
    left.update()
    right.update()

    # Displaying the puck
    ball.update()
    ball.collision()
    ball.show(window)

    # Checking for paddle Collision
    ball.checkrightPaddleCollision(right)
    ball.checkleftPaddleCollision(left)

    # Displaying Score
    label = font.render(str(util.LEFT_SCORE), 1, util.WHITE)
    window.blit(label, (util.WIDTH / 2 - 100, 0))
    label = font.render(str(util.RIGHT_SCORE), 1, util.WHITE)
    window.blit(label, (util.WIDTH / 2 + 100, 0))

    # Displaying the Net
    util.pygame.draw.line(window, util.WHITE, (util.WIDTH / 2, 0), (util.WIDTH / 2, util.HEIGHT), 1)

    # Updating the display
    util.pygame.display.update()
