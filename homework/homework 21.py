# Import a library of functions called 'pygame'
import pygame

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the height and width of the screen
size = [491, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Heron's Note")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

scene_count = 0

while not done:
    scene_count += 0.1
    clock.tick(10)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    screen.fill(WHITE)
    screen.blit(pygame.image.load('bg.png'), pygame.image.load('bg.png').get_rect())

    font = pygame.font.Font('font.ttf', 80)  # font setting
    title = font.render("헤론의 노트", True, (28, 0, 0))
    font = pygame.font.Font('font.ttf', 20)  # font setting
    subtitle = font.render("헤론의 공식을 알아보자!", True, (28, 0, 0))
    screen.blit(title, (120, 50))
    screen.blit(subtitle, (170, 150))

    pygame.draw.polygon(screen, BLACK, [[120, 400], [245.5, 200], [371, 400]], 5)

    if scene_count < 3:
        font = pygame.font.Font('font.ttf', 40)
        text = font.render("다음과 같은 삼각형이 있습니다.", True, (28, 0, 0))
        screen.blit(text, (50, 500))
    elif scene_count < 6:
        font = pygame.font.Font('font.ttf', 40)
        text = font.render("삼각형의 변 길이는 다음과 같습니다.", True, (28, 0, 0))
        screen.blit(text, (30, 500))
    elif scene_count < 9:
        font = pygame.font.Font('font.ttf', 40)
        text = font.render("3", True, (28, 0, 0))
        screen.blit(text, (250, 500))
    elif scene_count < 10:
        font = pygame.font.Font('font.ttf', 40)
        text = font.render("3, 14", True, (28, 0, 0))
        screen.blit(text, (250, 500))
    elif scene_count < 13:
        font = pygame.font.Font('font.ttf', 40)
        text = font.render("3, 14, 15", True, (28, 0, 0))
        screen.blit(text, (200, 500))
    elif scene_count < 15:
        font = pygame.font.Font('font.ttf', 40)
        text = font.render("세 변의 합의 절반을 s라 하면", True, (28, 0, 0))
        screen.blit(text, (70, 500))
    elif scene_count < 18:
        font = pygame.font.Font('font.ttf', 30)
        text = font.render("넓이는 s(s-3)(s-14)(2-5)의 제곱근이 됩니다.", True, (28, 0, 0))
        screen.blit(text, (70, 500))
    elif scene_count < 21:
        font = pygame.font.Font('font.ttf', 30)
        text = font.render("계산 결과, 20.4가 넓이가 됨을 알 수 있습니다.", True, (28, 0, 0))
        screen.blit(text, (40, 500))
    elif scene_count < 23:
        font = pygame.font.Font('font.ttf', 30)
        text = font.render("일반화 시켜보면,", True, (28, 0, 0))
        screen.blit(text, (200, 500))
    elif scene_count < 26:
        font = pygame.font.Font('font.ttf', 30)
        text = font.render("변의 길이인 a, b, c로 이루어진 삼각형의 넓이는", True, (28, 0, 0))
        screen.blit(text, (40, 500))
    else:
        font = pygame.font.Font('font.ttf', 30)
        prev_text = font.render("변의 길이인 a, b, c로 이루어진 삼각형의 넓이는", True, (28, 0, 0))
        screen.blit(prev_text, (40, 450))
        font = pygame.font.Font('font.ttf', 40)
        text = font.render("s(s-a)(s-b)(s-c)의 제곱근입니다", True, (28, 0, 0))
        font = pygame.font.Font('font.ttf', 30)
        subtext = font.render("(단, s = (a+b+c) / 2)", True, (28, 0, 0))
        screen.blit(text, (40, 500))
        screen.blit(subtext, (200, 550))

    pygame.display.flip()

# Be IDLE friendly
pygame.quit()