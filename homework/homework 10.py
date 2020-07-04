import pygame

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
SOLAR = (255, 100, 50)
MERCURY = (132, 132, 132)
VENUS = (163, 113, 56)
EARTH = (50, 80, 120)
MARS = (255, 130, 50)

# Set the height and width of the screen
size = [1000, 700]
screen = pygame.display.set_mode(size)

size_of_planet = [10]
x_of_planet = [250]
mode_of_planet = [1]

pygame.display.set_caption("Solar System Simulator")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
tick = 0

color_p = input("Choose planet's color(choose in MER,VEN,EAR,MAR)")
if color_p == "MER":
    PLANET = MERCURY
elif color_p == "VEN":
    PLANET = VENUS
elif color_p == "MAR":
    PLANET = MARS
else:
    PLANET = EARTH

while not done:
    clock.tick(100)

    # quit event checking
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # if user clicks QUIT btn, this statement will be true.
            done = True

    # set screen
    screen.fill((0, 0, 0))

    # SOLAR
    pygame.draw.circle(screen, SOLAR, [500, 350], 100)

    # PLANET
    pygame.draw.circle(screen, PLANET, [x_of_planet[0], 350], size_of_planet[0])

    # Physics Engine
    if mode_of_planet[0] == 1:
        if x_of_planet[0] <= 500:
            x_of_planet[0] += 1
            size_of_planet[0] += 1
        if x_of_planet[0] >= 500:
            x_of_planet[0] += 1
            size_of_planet[0] -= 1
        if x_of_planet[0] >= 750:
            mode_of_planet[0] = 0
    if mode_of_planet[0] == 0:
        pygame.draw.circle(screen, SOLAR, [500, 350], 100)
        size_of_planet[0] = 10
        x_of_planet[0] -= 1
        if x_of_planet[0] <= 250:
            mode_of_planet[0] = 1

    pygame.display.flip()

# Be IDLE friendly
pygame.quit()