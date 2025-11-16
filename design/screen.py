import pygame
pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Tic tac Toe")


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            click = pygame.mouse.get_pos()

            if 200 > click[0] and 200 > click[1]:
                print(1)
            if 400 > click[0] > 200 > click[1]:
                print(2)
            if click[0] > 400 and 200 > click[1]:
                print(3)
            if  400 > click[1] > 200 > click[0]:
                print(4)
            if  400 > click[0] > 200 and 400 > click[1] > 200:
                print(5)
            if click[0] > 400 > click[1] > 200:
                print(6)
            if 200 > click[0] and 400 < click[1]:
                print(7)
            if click[1] > 400 > click[0] > 200:
                print(8)
            if click[0] > 400 and click[1] > 400:
                print(9)







        screen.fill((250,250,250))

        pygame.draw.line(screen, (25, 25, 25), (200, 0), (200, 600), 5)
        pygame.draw.line(screen, (25, 25, 25), (400, 0), (400, 600), 5)
        pygame.draw.line(screen, (25, 25, 25), (0, 200), (600, 200), 5)
        pygame.draw.line(screen, (25, 25, 25), (0, 400), (600, 400), 5)


        pygame.display.update()



