import os
import pygame
import random
import time
import itertools

pygame.font.init()
myfont = pygame.font.SysFont('timesnewromanbold', 30)
myfont1 = pygame.font.SysFont('Comic Sans MS', 70)
bg = pygame.image.load("bg1.png")
piano_tile_color = (0, 0, 0)
window_height = 780
window_width = 468
rectangle_height = 260
rectangle_width = 117
no_of_seconds_to_wait = 1
speed = 800
os.environ["SDL_VIDEO_CENTERED"] = "1"
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Piano Tiles")
count = 0


class tile(object):
    def move(self, rect_no):
        pygame.draw.rect(screen, (0, 0, 0), rect[rect_no])
        rect[rect_no][1] += 2


clock = pygame.time.Clock()
rect = [pygame.rect.Rect((0, 0 - rectangle_height - 100, rectangle_width, rectangle_height)),
        pygame.rect.Rect((rectangle_width + 1, 0 - rectangle_height - 100, rectangle_width, rectangle_height)),
        pygame.rect.Rect((rectangle_width * 2 + 2, 0 - rectangle_height - 100, rectangle_width, rectangle_height)),
        pygame.rect.Rect((rectangle_width * 3 + 3, 0 - rectangle_height - 100, rectangle_width, rectangle_height)),
        pygame.rect.Rect((rectangle_width + 1, 0 - rectangle_height - 100, rectangle_width, rectangle_height)),
        pygame.rect.Rect((rectangle_width * 2 + 2, 0 - rectangle_height - 100, rectangle_width, rectangle_height)),
        pygame.rect.Rect((rectangle_width * 3 + 2, rectangle_height, rectangle_width, rectangle_height)),
        pygame.rect.Rect((rectangle_width * 2 + 2, rectangle_height + 260, rectangle_width, rectangle_height))]
rect_active_states = [0, 0, 0, 0, 0, 0]
a_list = {0, 1, 2, 3, 4, 5}
list_cycle = itertools.cycle(a_list)
next(list_cycle)
pygame.init()
starting_tile_1 = tile()
starting_tile_2 = tile()
tile0 = tile()
tile1 = tile()
tile2 = tile()
tile3 = tile()
tile4 = tile()
tile5 = tile()


def button(mouse, rect):
    global count
    for i in range(7):
        x = rect[i][0]
        y = rect[i][1]
        w = rect[i][2]
        h = rect[i][3]
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            rect_active_states[i] = 0
            rect[i][1] = 0 - rectangle_height - 100
            count += 1


def move_rect():
    if rect_active_states[0] == 1:
        tile0.move(0)
    if rect_active_states[1] == 1:
        tile1.move(1)
    if rect_active_states[2] == 1:
        tile1.move(2)
    if rect_active_states[3] == 1 and rect_active_states[0] == 0:
        tile0.move(3)
    if rect_active_states[4] == 1 and rect_active_states[1] == 0:
        tile1.move(4)
    if rect_active_states[5] == 1 and rect_active_states[2] == 0:
        tile1.move(5)


def main():
    global speed
    global count
    running = True
    time_at_beginning = round(time.time() * 1000)
    while running:
        for event in pygame.event.get():
            if event.type == "QUIT":
                pygame.quit()
                sys.exit()
        # screen.fill((162, 237, 250))
        screen.blit(bg, (0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (rectangle_width, 0, 2, window_height))
        pygame.draw.rect(screen, (255, 255, 255), (rectangle_width * 2, 0, 2, window_height))
        pygame.draw.rect(screen, (255, 255, 255), (rectangle_width * 3, 0, 2, window_height))
        time_now = round(time.time() * 1000)
        # print(time_now - time_at_beginning)
        if (time_now - time_at_beginning) >= speed:
            time_at_beginning = time_now
            seq = [next(list_cycle), random.randint(0, 4)]
            rect_no = random.choice(seq)
            rect_active_states[rect_no] = 1
            # print(rect[0])
            speed -= 0.5
        starting_tile_1.move(6)
        starting_tile_2.move(7)
        move_rect()
        textsurface = myfont1.render(str(count), False, (209, 77, 112))
        screen.blit(textsurface, (rectangle_width + 60, rectangle_height + 350))
        pygame.display.update()
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if click[0]:
            button(mouse, rect)
        # button(mouse, rect)
        if rect[0][1] >= 520 or rect[1][1] >= 520 or rect[2][1] >= 520 or rect[3][1] >= 520 or rect[4][1] >= 520 or \
                rect[5][
                    1] >= 520:
            return
        speed -= 0.5


def load():
    start_string = "start"
    while True:
        for event in pygame.event.get():
            if event.type == "QUIT":
                pygame.quit()
                sys.exit()
        screen.blit(bg, (0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (rectangle_width, 0, 2, window_height))
        pygame.draw.rect(screen, (255, 255, 255), (rectangle_width * 2, 0, 2, window_height))
        pygame.draw.rect(screen, (255, 255, 255), (rectangle_width * 3, 0, 2, window_height))
        pygame.draw.rect(screen, (61, 182, 219), rect[7])
        pygame.draw.rect(screen, (0, 0, 0), rect[6])
        textsurface = myfont.render(start_string, False, (255, 255, 255))
        screen.blit(textsurface, (rectangle_width * 2 + 30, rectangle_height + 290))
        pygame.display.update()
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if click[0]:
            x = rect[7][0]
            y = rect[7][1]
            w = rect[7][2]
            h = rect[7][3]
            if x + w > mouse[0] > x and y + h > mouse[1] > y:
                main()
                rect[7][1] = rectangle_height + 260
                start_string = "END"


load()
