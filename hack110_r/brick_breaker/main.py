import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")

FPS: int = 60
PADDLE_WIDTH: int = 100
PADDLE_HEIGHT: int = 15
BALL_RADIUS: int = 10
PADDLE_X: int = WIDTH/2 - PADDLE_WIDTH/2
PADDLE_Y: int = HEIGHT - PADDLE_HEIGHT - 5
GAP: int = 20

LIVES_FONT = pygame.font.SysFont("comicsans", 40)

class Paddle:
    """The user controlled player."""

    VEL = 5

    def __init__(self, x: int, y: int, width: int, height: int, color: tuple[int]) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def move(self, direction: int):
        self.x += self.VEL * direction

class Ball:

    VEL = 5

    def __init__(self, x: int, y: int, radius: int, color: tuple[int]) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.x_vel: int = 2 
        self.y_vel: int = self.VEL * -1

    def move(self) -> None:
        self.x += self.x_vel
        self.y += self.y_vel

    def set_vel(self, x_vel: int, y_vel: int):
        self.x_vel = x_vel
        self.y_vel = y_vel

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

class Brick:

    def __init__(self, x: int, y: int, width: int, height: int, health: int, colors: list[tuple]) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.max_health = health
        self.colors = colors
        self.color = colors[1]

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def collide(self, ball: Ball):
        if not (ball.x <= self.x + self.width and ball.x >= self.x):
            return False
        if not (ball.y - ball.radius <= self.y + self.height):
            return False

        self.hit()
        ball.set_vel(ball.x_vel, ball.y_vel * -1)
        return True
    
    def hit(self):
        self.health -= 1
        self.color = self.interpolate(self.colors[0], self.colors[1], (self.health/self.max_health))

    def interpolate(self, color_a, color_b, t):
        return tuple(int(a + (b - a) * t) for a, b in zip(color_a, color_b))

def draw(win, paddle, ball, bricks, lives):
    win.fill("white")
    paddle.draw(win)
    ball.draw(win)
    for brick in bricks:
        brick.draw(win)

    lives_text = LIVES_FONT.render(f"Lives: {lives}", 1, "black")
    win.blit(lives_text, (10, HEIGHT - lives_text.get_height() - 10))
    
    pygame.display.update()

def ball_collision(ball: Ball):
    if ball.x - BALL_RADIUS <= 0 or ball.x + BALL_RADIUS >= WIDTH:
        ball.set_vel(ball.x_vel * -1, ball.y_vel)
    if ball.y + BALL_RADIUS >= HEIGHT or ball.y - BALL_RADIUS <= 0:
        ball.set_vel(ball.x_vel, ball.y_vel * -1)

def ball_paddle_collision(ball: Ball, paddle: Paddle):
    if not (ball.x < paddle.x + paddle.width and ball.x >= paddle.x):
        return
    if not (ball.y + ball.radius >= paddle.y):
        return
    
    paddle_center: int = paddle.x + paddle.width/2
    distance_to_center: int = ball.x - paddle_center

    percent_width: int = distance_to_center/paddle.width
    angle: int = percent_width * 90
    angle_radians: int = math.radians(angle)

    #SOHCAHTOA
    x_vel = math.sin(angle_radians) * Ball.VEL
    y_vel = math.cos(angle_radians) * Ball.VEL * -1

    ball.set_vel(x_vel, y_vel)

def generate_bricks(rows: int, cols: int):
    brick_width: int = WIDTH // cols - GAP
    brick_height: int = 20
    bricks: list[Brick] = []
    for row in range(rows):
        for col in range(cols):
            brick = Brick(col * (brick_width + GAP), row * (brick_height + GAP), brick_width, brick_height, 5, [(255,0,0), (0,255,0)])
            bricks.append(brick)
    return bricks

def main():
    clock = pygame.time.Clock()

    paddle = Paddle(PADDLE_X, PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT, "black")
    ball = Ball(WIDTH/2, PADDLE_Y - BALL_RADIUS, BALL_RADIUS, "black")
    bricks = generate_bricks(3, 10)
    lives: int = 3

    def reset() -> None:
        paddle.x = PADDLE_X
        paddle.y = PADDLE_Y
        ball.x = WIDTH/2
        ball.y = PADDLE_Y - BALL_RADIUS
        
    def display_text(text: str) -> None:
        text_render = LIVES_FONT.render(text, 1, "red")
        win.blit(text_render, (WIDTH/2 - text_render.get_width() / 2, HEIGHT / 2 - text_render.get_height() / 2))
        pygame.display.update()
        pygame.time.delay(3000)
        


    # Set a running bool variable to True, can be set to False at any time to end the game loop
    run = True
    # Main loop
    while run:
        clock.tick(FPS)
        keys = pygame.key.get_pressed()

        # Event queue
        for event in pygame.event.get():
        # Stop loop when X button is hit
            if event.type == pygame.QUIT:
                run = False
                break
        if keys[pygame.K_ESCAPE]: 
            run = False 
            break 
        
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and paddle.x - paddle.VEL >= 0:
            paddle.move(-1)
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and paddle.x + paddle.width + paddle.VEL <= WIDTH:
            paddle.move(1)

        ball.move()
        ball_collision(ball)
        ball_paddle_collision(ball, paddle)

        for brick in bricks:
            brick.collide(ball)

            if brick.health <= 0:
                    bricks.remove(brick)
        
        #lives check
        if ball.y + ball.radius >= HEIGHT:
            lives -= 1
            ball.x = paddle.x + paddle.width/2
            ball.y = paddle.y - BALL_RADIUS
            ball.set_vel(0, ball.VEL * -1)

        #lose condition
        if lives <= 0:
            bricks = generate_bricks(3, 10)
            lives: int = 3
            reset()
            display_text("You Lost!")

        #win condition
        if len(bricks) == 0:
            bricks = generate_bricks(3, 10)
            lives: int = 3
            reset()
            display_text("You Won!")

            

        draw(win, paddle, ball, bricks, lives)
        
    
    pygame.quit()
    quit()



if __name__ == "__main__":
    main()