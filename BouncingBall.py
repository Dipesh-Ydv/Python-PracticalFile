import pygame

pygame.init()

speed = [1, 1]
background = 255, 255, 255
size = width, height = 800, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncing Ball")
ball = pygame.image.load("ball.png")
ball_rect = ball.get_rect()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
    ball_rect = ball_rect.move(speed)
    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(background)
    screen.blit(ball, ball_rect)
    pygame.display.filp()
    