# DaKotA BoURnE (db2nb) and Nick Manalac (ntm4kd)

# Our game idea is a horror game in which the user will try to collect books before they are caputured by the demon, who
# in this case will be librarian, as the game takes place in alderman library. The game will have a top-down view on the
# player, who will have a limited view of their surroundings, using only a flashlight.

#       Optional Features
# Enemies: The librarian will follow the player around and attempt to catch them before they are able to find all the
# books.

# Health meter: The player will have a health meter that will take hits if they hit obstacles and go to zero when they
# are captured by the librarian.

# Scrolling Level: The entire game will be a sort of scrolling level, in that the player will be scrolling through the
# library, passing through doors to get to the next sections.

# Collectibles: The books will be the collectibles, and collecting all of them will result in the win.

# 2 players simultaneously: There will be a two player mode in which another player can control player 2, and there will
# be 2 librarians trying to find the players.

import pygame
import gamebox
import random
import re

camera = gamebox.Camera(800, 600)

# Variables needed to transistion between movies
one_player = True
title_screen = True
players_screen = False
control_screen = False
room1 = False
room2 = False
room3 = False
room4 = False
room5 = False
room6 = False
room7 = False
room8 = False
room9 = False
room10 = False

#Enemy Declaration
room2_enemies = True
room2_baddies_killed = False
room3_enemies = True
room3_baddies_killed = False
room4_enemies = True
room4_baddies_killed = False
room5_enemies = True
room5_baddies_killed = False
room6_enemies = True
room6_baddies_killed = False
room7_enemies = True
room7_baddies_killed = False
room8_enemies = True
room8_baddies_killed = False
room9_enemies = True
room9_baddies_killed = False
room10_enemies = True
room10_baddies_killed = False


# AI
enemies = [
    gamebox.from_color(random.randint(21, 779), random.randint(21, 579), 'Cyan', 20, 20),
    gamebox.from_color(random.randint(21, 779), random.randint(21, 579), 'white', 25, 25)
    ]
d = {}

last_touch1 = ''
last_touch2 = ''

# Player Position
p1_xpos = 383
p1_ypos = 500
p2_ypos = 500
p2_xpos = 425
bullet1_xpos = 383
bullet1_ypos = 500
bullet2_xpos = 425
bullet2_ypos = 500
p1_health = 10
p12_health = 6
p2_health = 6

# shooting variables
shootup1 = False
shootdown1 = False
shootleft1 = False
shootright1 = False
shootup2 = False
shootdown2 = False
shootleft2 = False
shootright2 = False

# Position for control text
a = 0
b = 0

# Wall lists defined
room1_walls = [
    (gamebox.from_color(181, 10, 'brown', 362, 20)),
    (gamebox.from_color(181, 590, 'brown', 362, 20)),
    (gamebox.from_color(619, 10, 'brown', 362, 20)),
    (gamebox.from_color(619, 590, 'brown', 362, 20)),
    (gamebox.from_color(10, 300, 'brown', 20, 600)),
    (gamebox.from_color(790, 300, 'brown', 20, 600)),

    gamebox.from_color(350, 500, 'brown', 20, 220),
    gamebox.from_color(10, 500, 'brown', 20, 220),
    gamebox.from_color(457, 500, 'brown', 20, 220),
    gamebox.from_color(697, 638, 'brown', 500, 500),
    gamebox.from_color(697, -98, 'brown', 500, 500),
    gamebox.from_color(103, -38, 'brown', 500, 500),
    gamebox.from_color(650, 202, 'brown', 400, 20),
    gamebox.from_circle(540, 180, 'brown', 20),
    gamebox.from_circle(720, 180, 'brown', 20),
]

room2_walls = [
    (gamebox.from_color(181, 10, 'brown', 362, 20)),
    (gamebox.from_color(181, 590, 'brown', 362, 20)),
    (gamebox.from_color(619, 10, 'brown', 362, 20)),
    (gamebox.from_color(619, 590, 'brown', 362, 20)),
    (gamebox.from_color(10, 300, 'brown', 20, 600)),
    (gamebox.from_color(790, 300, 'brown', 20, 600)),

    (gamebox.from_color(70, 170, 'brown', 10, 210)),
    (gamebox.from_color(140, 170, 'brown', 10, 210)),
    (gamebox.from_color(220, 170, 'brown', 10, 210)),
    (gamebox.from_color(300, 170, 'brown', 10, 210)),
    (gamebox.from_color(380, 170, 'brown', 10, 210)),
    (gamebox.from_color(460, 170, 'brown', 10, 210)),
    (gamebox.from_color(540, 170, 'brown', 10, 210)),
    (gamebox.from_color(620, 170, 'brown', 10, 210)),
    (gamebox.from_color(700, 170, 'brown', 10, 210)),

    (gamebox.from_color(70, 430, 'brown', 10, 210)),
    (gamebox.from_color(140, 430, 'brown', 10, 210)),
    (gamebox.from_color(220, 430, 'brown', 10, 210)),
    (gamebox.from_color(300, 430, 'brown', 10, 210)),
    (gamebox.from_color(380, 430, 'brown', 10, 210)),
    (gamebox.from_color(460, 430, 'brown', 10, 210)),
    (gamebox.from_color(540, 430, 'brown', 10, 210)),
    (gamebox.from_color(620, 430, 'brown', 10, 210)),
    (gamebox.from_color(700, 430, 'brown', 10, 210)),
]

room3_walls = [
    (gamebox.from_color(181, 10, 'brown', 362, 20)),
    (gamebox.from_color(181, 590, 'brown', 362, 20)),
    (gamebox.from_color(619, 10, 'brown', 362, 20)),
    (gamebox.from_color(619, 590, 'brown', 362, 20)),
    (gamebox.from_color(10, 300, 'brown', 20, 600)),
    (gamebox.from_color(790, 300, 'brown', 20, 600)),

    (gamebox.from_color(150, 200, 'brown', 300, 10)),
    (gamebox.from_color(150, 400, 'brown', 300, 10)),
    (gamebox.from_color(650, 200, 'brown', 300, 10)),
    (gamebox.from_color(650, 400, 'brown', 300, 10)),
    (gamebox.from_circle(200, 300, 'brown', 50)),
    (gamebox.from_color(650, 300, 'brown', 200, 100)),
    (gamebox.from_color(400, 100, 'brown', 400, 100)),
    (gamebox.from_color(200, 500, 'brown', 200, 100)),
    (gamebox.from_color(600, 500, 'brown', 200, 100))
]

room4_walls = [
    (gamebox.from_color(181, 10, 'brown', 362, 20)),
    (gamebox.from_color(181, 590, 'brown', 362, 20)),
    (gamebox.from_color(619, 10, 'brown', 362, 20)),
    (gamebox.from_color(619, 590, 'brown', 362, 20)),
    (gamebox.from_color(10, 300, 'brown', 20, 600)),
    (gamebox.from_color(790, 300, 'brown', 20, 600)),

    (gamebox.from_color(200, 400, 'brown', 500, 100)),
    (gamebox.from_color(725, 300, 'brown', 150, 600)),
    (gamebox.from_color(12.5, 100, 'green', 25, 200)),
    (gamebox.from_color(50, 200, 'green', 100, 25)),
    (gamebox.from_color(349.5, 100, 'blue', 25, 200)),
    (gamebox.from_color(312, 200, 'blue', 100, 25)),
    (gamebox.from_color(450.5, 100, 'white', 25, 200)),
    (gamebox.from_color(488, 200, 'white', 100, 25))
]

room5_walls = [
    (gamebox.from_color(10, 300, 'brown', 20, 600)),
    (gamebox.from_color(790, 300, 'brown', 20, 600)),
    (gamebox.from_color(175, 75, 'blue', 350, 150)),
    (gamebox.from_color(625, 75, 'blue', 350, 150)),
    (gamebox.from_color(175, 525, 'blue', 350, 150)),
    (gamebox.from_color(625, 525, 'blue', 350, 150)),
    (gamebox.from_circle(400, 300, 'white', 70))
]

room6_walls = [
    (gamebox.from_color(181, 10, 'brown', 362, 20)),
    (gamebox.from_color(181, 590, 'brown', 362, 20)),
    (gamebox.from_color(619, 10, 'brown', 362, 20)),
    (gamebox.from_color(619, 590, 'brown', 362, 20)),
    (gamebox.from_color(10, 300, 'brown', 20, 600)),
    (gamebox.from_color(790, 300, 'brown', 20, 600)),

    (gamebox.from_circle(152, 140, 'blue', 40)),
    (gamebox.from_circle(304, 140, 'blue', 40)),
    (gamebox.from_circle(456, 140, 'blue', 40)),
    (gamebox.from_circle(608, 140, 'blue', 40)),

    (gamebox.from_circle(152, 280, 'blue', 40)),
    (gamebox.from_circle(304, 280, 'blue', 40)),
    (gamebox.from_circle(456, 280, 'blue', 40)),
    (gamebox.from_circle(608, 280, 'blue', 40)),

    (gamebox.from_circle(152, 420, 'blue', 40)),
    (gamebox.from_circle(304, 420, 'blue', 40)),
    (gamebox.from_circle(456, 420, 'blue', 40)),
    (gamebox.from_circle(608, 420, 'blue', 40))
]

room7_walls = [
    (gamebox.from_color(181, 10, 'brown', 362, 20)),
    (gamebox.from_color(181, 590, 'brown', 362, 20)),
    (gamebox.from_color(619, 10, 'brown', 362, 20)),
    (gamebox.from_color(619, 590, 'brown', 362, 20)),
    (gamebox.from_color(10, 300, 'brown', 20, 600)),
    (gamebox.from_color(790, 300, 'brown', 20, 600)),

    (gamebox.from_color(187, 550, 'brown', 350, 100)),
    (gamebox.from_color(625, 550, 'brown', 350, 100)),
    (gamebox.from_color(448, 400, 'white', 20, 400)),
    (gamebox.from_color(285, 275, 'white', 308, 150)),

    (gamebox.from_color(181, 10, 'blue', 362, 200)),
    (gamebox.from_color(506, 90, 'blue', 288, 40)),

    (gamebox.from_color(650, 215, 'green', 70, 290))
]

room8_walls = [
    (gamebox.from_color(181, 10, 'brown', 362, 20)),
    (gamebox.from_color(181, 590, 'brown', 362, 20)),
    (gamebox.from_color(619, 10, 'brown', 362, 20)),
    (gamebox.from_color(619, 590, 'brown', 362, 20)),
    (gamebox.from_color(10, 300, 'brown', 20, 600)),
    (gamebox.from_color(790, 300, 'brown', 20, 600)),

    (gamebox.from_circle(400, 300, 'blue', 40)),
    (gamebox.from_circle(200, 300, 'blue', 40)),
    (gamebox.from_circle(600, 300, 'blue', 40)),

    (gamebox.from_color(400, 100, 'green', 550, 15)),
    (gamebox.from_color(400, 200, 'green', 550, 15)),
    (gamebox.from_color(400, 400, 'green', 550, 15)),
    (gamebox.from_color(400, 500, 'green', 550, 15))
]

room9_walls = [
    (gamebox.from_color(181, 10, 'brown', 362, 20)),
    (gamebox.from_color(181, 590, 'brown', 362, 20)),
    (gamebox.from_color(619, 10, 'brown', 362, 20)),
    (gamebox.from_color(619, 590, 'brown', 362, 20)),
    (gamebox.from_color(10, 300, 'brown', 20, 600)),
    (gamebox.from_color(790, 300, 'brown', 20, 600)),

    (gamebox.from_color(150, 300, 'brown', 300, 600)),
    (gamebox.from_color(650, 300, 'brown', 300, 600)),
    (gamebox.from_color(400, 50, 'brown', 800, 200))
]

room10_walls = [
    (gamebox.from_color(200, 100, 'blue', 20, 200)),
    (gamebox.from_color(200, 500, 'blue', 20, 200)),
    (gamebox.from_color(600, 200, 'blue', 400, 50)),
    (gamebox.from_color(600, 400, 'blue', 400, 50)),

    (gamebox.from_color(400, 12.5, 'brown', 800, 25)),
    (gamebox.from_color(787.5, 300, 'brown', 25, 600)),
    (gamebox.from_color(400, 587.5, 'brown', 800, 25)),
    (gamebox.from_color(12.5, 131, 'brown', 25, 262)),
    (gamebox.from_color(12.5, 469, 'brown', 25, 262))
]

# bar when touched, everything scrolls so the player goes in that direction
go_north = gamebox.from_color(400, 0, 'black', 76, 1)
go_east = gamebox.from_color(800, 300, 'black', 1, 76)
go_south = gamebox.from_color(400, 600, 'black', 76, 1)
directions = [go_north, go_east, go_south]


def tick(keys):
    global title_screen, control_screen, a, b, players_screen, one_player, room1, room2, room3, room4, room5, room6, room7, room8, room9, room10
    global shootup1, shootdown1, shootleft1, shootright1, shootup2, shootdown2, shootleft2, shootright2
    global room2_enemies, room3_enemies, room4_enemies, room5_enemies, room6_enemies, room7_enemies, room8_enemies, room9_enemies, room10_enemies
    global chooser_var, d, p1_health, p12_health, p2_health
    global p1_xpos, p1_ypos, p2_xpos, p2_ypos, bullet1_xpos, bullet1_ypos, bullet2_xpos, bullet2_ypos
    global room2_baddies_killed, room3_baddies_killed, room4_baddies_killed, room5_baddies_killed, room6_baddies_killed, room7_baddies_killed, room8_baddies_killed, room9_baddies_killed, room10_baddies_killed
    global last_touch1, last_touch2

    overlap1_right = False
    overlap1_left = False
    overlap1_top = False
    overlap1_bottom = False

    overlap2_right = False
    overlap2_left = False
    overlap2_top = False
    overlap2_bottom = False

    # Players
    p1 = gamebox.from_color(p1_xpos, p1_ypos, "cadetblue1", 30, 30)
    p2 = gamebox.from_color(p2_xpos, p2_ypos, "Blue", 30, 30)
    bullet1 = gamebox.from_color(bullet1_xpos, bullet1_ypos, 'blue', 5, 5)
    bullet2 = gamebox.from_color(bullet2_xpos, bullet2_ypos, 'green', 5, 5)

    if title_screen:
        # starting title screen
        p1_health = 10
        p12_health = 10
        p2_health = 10
        camera.clear('black')
        camera.draw(gamebox.from_text(400, 100, 'Escape from', 100, 'red', True))
        camera.draw(gamebox.from_text(400, 200, 'Alderman Stacks', 100, 'red', True))
        camera.draw(gamebox.from_text(400, 300, 'DaKotA BoURnE (db2nb) and NiCk MaNaLAc (ntm4kd)', 30, 'white', False))
        camera.draw(gamebox.from_text(400, 500, 'Press SPACE to Continue', 90, 'red', False))
        if pygame.K_SPACE in keys:
             # Changes title screen to player select screen
            title_screen = False
            players_screen = True

    if players_screen:
        # The Player select screen, player chooses between 1 or 2 players
        camera.clear('black')
        camera.draw(gamebox.from_text(400, 100, 'Press "1" for One Player', 70, 'red'))
        camera.draw(gamebox.from_text(400, 200, 'Press "2" for Two Players', 70, 'red'))
        if pygame.K_1 in keys:
            one_player = True
            players_screen = False
            control_screen = True
        if pygame.K_2 in keys:
            one_player = False
            players_screen = False
            control_screen = True

    if one_player:
        # Determines the displayed controls positions for either one or two players
        a = 400
        b = 10000
    else:
        a = 200
        b = 600

    if control_screen:
        # The text that displays the control scheme for players
        camera.clear('black')
        camera.draw(gamebox.from_text(a, 100, 'Player 1 Controls:', 50, 'red'))
        camera.draw(gamebox.from_text(a, 200, 'Movement:', 30, 'white'))
        camera.draw(gamebox.from_text(a, 250, 'Arrow Keys', 35, 'red'))
        camera.draw(gamebox.from_text(a, 350, 'Shoot AR-15:', 30, 'white'))
        camera.draw(gamebox.from_text(a, 400, '"/" Key', 35, 'red'))
        camera.draw(gamebox.from_text(b, 100, 'Player 2 Controls:', 50, 'red'))
        camera.draw(gamebox.from_text(b, 200, 'Movement:', 30, 'white'))
        camera.draw(gamebox.from_text(b, 250, '"WASD" Keys', 35, 'red'))
        camera.draw(gamebox.from_text(b, 350, 'Shoot AR-15:', 30, 'white'))
        camera.draw(gamebox.from_text(b, 400, '"E" Key', 35, 'red'))
        camera.draw(gamebox.from_text(400, 500, 'Press SPACE to Start', 90, 'red', False))
    if pygame.K_SPACE in keys and control_screen:
        # Changes control screen to the actual game
        room1 = True
        control_screen = False

    if room1:
        camera.clear('black')
        # doors
        camera.draw(gamebox.from_color(385, 595, 'brown', 36, 5))
        camera.draw(gamebox.from_color(425, 595, 'brown', 36, 5))
        camera.draw(gamebox.from_color(385, 5, 'brown', 36, 5))
        camera.draw(gamebox.from_color(425, 5, 'brown', 36, 5))
        for direction in directions:
            camera.draw(direction)
        if one_player:
            # statement that determines whether or not to draw two players
            camera.draw(bullet1)
            camera.draw(p1)
            if p1.touches(go_north):
                p1_xpos = 383
                p1_ypos = 550
                bullet1_xpos = 383
                bullet1_ypos = 550
                room1 = False
                room2 = True
        else:
            camera.draw(bullet1)
            camera.draw(bullet2)
            camera.draw(p1)
            camera.draw(p2)
            if p1.touches(go_north) or p2.touches(go_north):
                p1_xpos = 383
                p1_ypos = 550
                bullet1_xpos = 383
                bullet1_ypos = 550
                p2_xpos = 425
                p2_ypos = 550
                bullet2_xpos = 425
                bullet2_ypos = 550
                room1 = False
                room2 = True
        for wall in room1_walls:
            camera.draw(wall)
            if p1.right_touches(wall):
                overlap1_right = True
            if p1.left_touches(wall):
                overlap1_left = True
            if p1.bottom_touches(wall):
                overlap1_bottom = True
            if p1.top_touches(wall):
                overlap1_top = True
            if p2.right_touches(wall):
                overlap2_right = True
            if p2.left_touches(wall):
                overlap2_left = True
            if p2.bottom_touches(wall):
                overlap2_bottom = True
            if p2.top_touches(wall):
                overlap2_top = True
    elif room2:
        camera.clear('black')
        if room2_enemies:
            number_of_enemies = random.randint(1, 6)
            for i in range(0, number_of_enemies):
                chooser_var = random.randint(0, 1)
                if '25' in str(enemies[chooser_var]):
                    new_enemy = gamebox.from_color(random.randint(21, 779), random.randint(21, 579), 'white', 25, 25)
                else:
                    new_enemy = gamebox.from_color(random.randint(21, 779), random.randint(21, 579), 'cyan', 20, 20)
                if '25' in str(enemies[chooser_var]):
                    d[new_enemy] = 3
                else:
                    d[new_enemy] = 2
            room2_enemies = False
        if not room2_baddies_killed:
            for enemy in list(d.keys()):
                camera.draw(enemy)
                if bullet1.touches(enemy) or bullet2.touches(enemy):
                    d[enemy] -= 1
                    if d[enemy] == 0:
                        del d[enemy]
                if enemy.touches(p1):
                    if one_player:
                        p1_health -= 1
                    else:
                        p12_health -= 1
                if enemy.touches(p2):
                    p2_health -= 1
                if '20x20' or '25x25' in str(enemy):
                    match = re.search(r'(\d+),(\d+)', str(enemy))
                    enemy_xpos = int(match.group(1))
                    enemy_ypos = int(match.group(2))
                    if one_player:
                        enemy.xspeed = 0
                        enemy.yspeed = 0
                        if enemy_xpos < p1_xpos:
                            enemy.xspeed = 2
                        else:
                            enemy.xspeed = -2
                        if enemy_ypos < p1_ypos:
                            enemy.yspeed = 2
                        else:
                            enemy.yspeed = -2
                        enemy.move(enemy.xspeed, enemy.yspeed)
        if d == {}:
            room2_baddies_killed = True
        if one_player:
            # statement that determines whether or not to draw two players
            camera.draw(bullet1)
            camera.draw(p1)
            if p1.touches(go_south):
                p1_xpos = 383
                p1_ypos = 50
                bullet1_xpos = 383
                bullet1_ypos = 50
                room1 = True
                room2 = False
            if p1.touches(go_north):
                p1_xpos = 383
                p1_ypos = 550
                bullet1_xpos = 383
                bullet1_ypos = 550
                room2 = False
                room3 = True
            if p1_health == 0:
                room2 = False
                title_screen = True
        else:
            camera.draw(bullet1)
            camera.draw(bullet2)
            camera.draw(p1)
            camera.draw(p2)
            if p1.touches(go_south) or p2.touches(go_south):
                p1_xpos = 383
                p1_ypos = 50
                bullet1_xpos = 383
                bullet1_ypos = 50
                p2_xpos = 425
                p2_ypos = 50
                bullet2_xpos = 425
                bullet2_ypos = 50
                room1 = True
                room2 = False
            if p1.touches(go_north) or p2.touches(go_north):
                p1_xpos = 383
                p1_ypos = 550
                bullet1_xpos = 383
                bullet1_ypos = 550
                p2_xpos = 425
                p2_ypos = 550
                bullet2_xpos = 425
                bullet2_ypos = 550
                room2 = False
                room3 = True
        for direction in directions:
            camera.draw(direction)
            # doors
        camera.draw(gamebox.from_color(385, 595, 'brown', 36, 5))
        camera.draw(gamebox.from_color(425, 595, 'brown', 36, 5))
        camera.draw(gamebox.from_color(385, 5, 'brown', 36, 5))
        camera.draw(gamebox.from_color(425, 5, 'brown', 36, 5))
        for wall in room2_walls:
            camera.draw(wall)
            if p1.right_touches(wall):
                overlap1_right = True
            if p1.left_touches(wall):
                overlap1_left = True
            if p1.bottom_touches(wall):
                overlap1_bottom = True
            if p1.top_touches(wall):
                overlap1_top = True
            if p2.right_touches(wall):
                overlap2_right = True
            if p2.left_touches(wall):
                overlap2_left = True
            if p2.bottom_touches(wall):
                overlap2_bottom = True
            if p2.top_touches(wall):
                overlap2_top = True
        for direction in directions:
            camera.draw(direction)
        # doors
        camera.draw(gamebox.from_color(385, 595, 'brown', 36, 5))
        camera.draw(gamebox.from_color(425, 595, 'brown', 36, 5))
        camera.draw(gamebox.from_color(385, 5, 'brown', 36, 5))
        camera.draw(gamebox.from_color(425, 5, 'brown', 36, 5))
        #Transition statement
        if p1.touches(go_south):
            p1.move(0, -550)
            room1 = True
            room2 = False
        if p1.touches(go_north):
            p1.move(0, 550)
            room2 = False
            room3 = True
        #Drawing statement
        for wall in room2_walls:
            camera.draw(wall)
            if p1.touches(wall) or p2.touches(wall):
                p1.move_to_stop_overlapping(wall)
                p2.move_to_stop_overlapping(wall)
    elif room3:
        camera.clear('black')
        if room3_enemies:
            d = {}
            number_of_enemies = random.randint(1, 6)
            for i in range(0, number_of_enemies):
                chooser_var = random.randint(0, 1)
                if '25' in str(enemies[chooser_var]):
                    new_enemy = gamebox.from_color(random.randint(21, 779), random.randint(21, 579), 'white', 25, 25)
                else:
                    new_enemy = gamebox.from_color(random.randint(21, 779), random.randint(21, 579), 'cyan', 20, 20)
                if '25' in str(enemies[chooser_var]):
                    d[new_enemy] = 3
                else:
                    d[new_enemy] = 2
            room3_enemies = False
        if not room3_baddies_killed:
            for enemy in list(d.keys()):
                camera.draw(enemy)
                if bullet1.touches(enemy) or bullet2.touches(enemy):
                    d[enemy] -= 1
                    if d[enemy] == 0:
                        del d[enemy]
                if enemy.touches(p1):
                    if one_player:
                        p1_health -= 1
                    else:
                        p12_health -= 1
                if enemy.touches(p2):
                    p2_health -= 1
        if d == {}:
            room3_baddies_killed = True
        if one_player:
            # statement that determines whether or not to draw two players
            camera.draw(bullet1)
            camera.draw(p1)
            if p1.touches(go_south):
                p1_xpos = 383
                p1_ypos = 50
                bullet1_xpos = 383
                bullet1_ypos = 50
                room2 = True
                room3 = False
            if p1.touches(go_north):
                p1_xpos = 383
                p1_ypos = 550
                bullet1_xpos = 383
                bullet1_ypos = 550
                room3 = False
                room4 = True
            if p1_health == 0:
                room3 = False
                title_screen = True
        else:
            camera.draw(bullet1)
            camera.draw(bullet2)
            camera.draw(p1)
            camera.draw(p2)
            if p1.touches(go_south) or p2.touches(go_south):
                p1_xpos = 383
                p1_ypos = 50
                bullet1_xpos = 383
                bullet1_ypos = 50
                p2_xpos = 425
                p2_ypos = 50
                bullet2_xpos = 425
                bullet2_ypos = 50
                room2 = True
                room3 = False
            if p1.touches(go_north) or p2.touches(go_north):
                p1_xpos = 383
                p1_ypos = 550
                bullet1_xpos = 383
                bullet1_ypos = 550
                p2_xpos = 425
                p2_ypos = 550
                bullet2_xpos = 425
                bullet2_ypos = 550
                room3 = False
                room4 = True
        for direction in directions:
            camera.draw(direction)
            # doors
        camera.draw(gamebox.from_color(385, 595, 'brown', 36, 5))
        camera.draw(gamebox.from_color(425, 595, 'brown', 36, 5))
        camera.draw(gamebox.from_color(385, 5, 'brown', 36, 5))
        camera.draw(gamebox.from_color(425, 5, 'brown', 36, 5))
        for wall in room3_walls:
            camera.draw(wall)
            if p1.right_touches(wall):
                overlap1_right = True
            if p1.left_touches(wall):
                overlap1_left = True
            if p1.bottom_touches(wall):
                overlap1_bottom = True
            if p1.top_touches(wall):
                overlap1_top = True
            if p2.right_touches(wall):
                overlap2_right = True
            if p2.left_touches(wall):
                overlap2_left = True
            if p2.bottom_touches(wall):
                overlap2_bottom = True
            if p2.top_touches(wall):
                overlap2_top = True
    elif room4:
        camera.clear('black')
        if room4_enemies:
            number_of_enemies = random.randint(1, 6)
            for i in range(0, number_of_enemies):
                chooser_var = random.randint(0, 1)
                if '25' in str(enemies[chooser_var]):
                    new_enemy = gamebox.from_color(random.randint(21, 779), random.randint(21, 579), 'white', 25, 25)
                else:
                    new_enemy = gamebox.from_color(random.randint(21, 779), random.randint(21, 579), 'cyan', 20, 20)
                if '25' in str(enemies[chooser_var]):
                    d[new_enemy] = 3
                else:
                    d[new_enemy] = 2
            room4_enemies = False
        if not room4_baddies_killed:
            for enemy in list(d.keys()):
                camera.draw(enemy)
                if bullet1.touches(enemy) or bullet2.touches(enemy):
                    d[enemy] -= 1
                    if d[enemy] == 0:
                        del d[enemy]
                if enemy.touches(p1):
                    if one_player:
                        p1_health -= 1
                    else:
                        p12_health -= 1
                if enemy.touches(p2):
                    p2_health -= 1
        if d == {}:
            room4_baddies_killed = True
        if one_player:
            # statement that determines whether or not to draw two players
            camera.draw(bullet1)
            camera.draw(p1)
            if p1.touches(go_south):
                p1_xpos = 383
                p1_ypos = 50
                bullet1_xpos = 383
                bullet1_ypos = 50
                room3 = True
                room4 = False
            if p1.touches(go_north):
                p1_xpos = 383
                p1_ypos = 550
                bullet1_xpos = 383
                bullet1_ypos = 550
                room4 = False
                room5 = True
            if p1_health == 0:
                room4 = False
                title_screen = True
        else:
            camera.draw(bullet1)
            camera.draw(bullet2)
            camera.draw(p1)
            camera.draw(p2)
            if p1.touches(go_south) or p2.touches(go_south):
                p1_xpos = 383
                p1_ypos = 50
                bullet1_xpos = 383
                bullet1_ypos = 50
                p2_xpos = 425
                p2_ypos = 50
                bullet2_xpos = 425
                bullet2_ypos = 50
                room3 = True
                room4 = False
            if p1.touches(go_north) or p2.touches(go_north):
                p1_xpos = 383
                p1_ypos = 550
                bullet1_xpos = 383
                bullet1_ypos = 550
                p2_xpos = 425
                p2_ypos = 550
                bullet2_xpos = 425
                bullet2_ypos = 550
                room4 = False
                room5 = True
        for direction in directions:
            camera.draw(direction)
            # doors
        camera.draw(gamebox.from_color(385, 595, 'brown', 36, 5))
        camera.draw(gamebox.from_color(425, 595, 'brown', 36, 5))
        camera.draw(gamebox.from_color(385, 5, 'brown', 36, 5))
        camera.draw(gamebox.from_color(425, 5, 'brown', 36, 5))
        for wall in room4_walls:
            camera.draw(wall)
            if p1.right_touches(wall):
                overlap1_right = True
            if p1.left_touches(wall):
                overlap1_left = True
            if p1.bottom_touches(wall):
                overlap1_bottom = True
            if p1.top_touches(wall):
                overlap1_top = True
            if p2.right_touches(wall):
                overlap2_right = True
            if p2.left_touches(wall):
                overlap2_left = True
            if p2.bottom_touches(wall):
                overlap2_bottom = True
            if p2.top_touches(wall):
                overlap2_top = True
    elif room5:
        camera.clear('black')
        if room5_enemies:
            number_of_enemies = random.randint(1, 6)
            for i in range(0, number_of_enemies):
                chooser_var = random.randint(0, 1)
                if '25' in str(enemies[chooser_var]):
                    new_enemy = gamebox.from_color(random.randint(21, 779), random.randint(21, 579), 'white', 25, 25)
                else:
                    new_enemy = gamebox.from_color(random.randint(21, 779), random.randint(21, 579), 'cyan', 20, 20)
                if '25' in str(enemies[chooser_var]):
                    d[new_enemy] = 3
                else:
                    d[new_enemy] = 2
            room5_enemies = False
        if not room5_baddies_killed:
            for enemy in list(d.keys()):
                camera.draw(enemy)
                if bullet1.touches(enemy) or bullet2.touches(enemy):
                    d[enemy] -= 1
                    if d[enemy] == 0:
                        del d[enemy]
                if enemy.touches(p1):
                    if one_player:
                        p1_health -= 1
                    else:
                        p12_health -= 1
                if enemy.touches(p2):
                    p2_health -= 1
        if d == {}:
            room5_baddies_killed = True
        if one_player:
            # statement that determines whether or not to draw two players
            camera.draw(bullet1)
            camera.draw(p1)
            if p1.touches(go_south):
                p1_xpos = 383
                p1_ypos = 50
                bullet1_xpos = 383
                bullet1_ypos = 50
                room4 = True
                room5 = False
            if p1.touches(go_north):
                p1_xpos = 383
                p1_ypos = 550
                bullet1_xpos = 383
                bullet1_ypos = 550
                room5 = False
                room6 = True
            if p1_health == 0:
                room5 = False
                title_screen = True
        else:
            camera.draw(bullet1)
            camera.draw(bullet2)
            camera.draw(p1)
            camera.draw(p2)
            if p1.touches(go_south) or p2.touches(go_south):
                p1_xpos = 383
                p1_ypos = 50
                bullet1_xpos = 383
                bullet1_ypos = 50
                p2_xpos = 425
                p2_ypos = 50
                bullet2_xpos = 425
                bullet2_ypos = 50
                room4 = True
                room5 = False
            if p1.touches(go_north) or p2.touches(go_north):
                p1_xpos = 383
                p1_ypos = 550
                bullet1_xpos = 383
                bullet1_ypos = 550
                p2_xpos = 425
                p2_ypos = 550
                bullet2_xpos = 425
                bullet2_ypos = 550
                room5 = False
                room6 = True
        for direction in directions:
            camera.draw(direction)
            # doors
        camera.draw(gamebox.from_color(385, 595, 'brown', 36, 5))
        camera.draw(gamebox.from_color(425, 595, 'brown', 36, 5))
        camera.draw(gamebox.from_color(385, 5, 'brown', 36, 5))
        camera.draw(gamebox.from_color(425, 5, 'brown', 36, 5))
        for wall in room5_walls:
            camera.draw(wall)
            if p1.right_touches(wall):
                overlap1_right = True
            if p1.left_touches(wall):
                overlap1_left = True
            if p1.bottom_touches(wall):
                overlap1_bottom = True
            if p1.top_touches(wall):
                overlap1_top = True

            if p2.right_touches(wall):
                overlap2_right = True
            if p2.left_touches(wall):
                overlap2_left = True
            if p2.bottom_touches(wall):
                overlap2_bottom = True
            if p2.top_touches(wall):
                overlap2_top = True
    elif room6:
        camera.clear('black')
        if room6_enemies:
            number_of_enemies = random.randint(1, 6)
            for i in range(0, number_of_enemies):
                chooser_var = random.randint(0, 1)
                if '25' in str(enemies[chooser_var]):
                    new_enemy = gamebox.from_color(random.randint(21, 779), random.randint(21, 579), 'white', 25, 25)
                else:
                    new_enemy = gamebox.from_color(random.randint(21, 779), random.randint(21, 579), 'cyan', 20, 20)
                if '25' in str(enemies[chooser_var]):
                    d[new_enemy] = 3
                else:
                    d[new_enemy] = 2
            room6_enemies = False
        if not room6_baddies_killed:
            for enemy in list(d.keys()):
                camera.draw(enemy)
                if bullet1.touches(enemy) or bullet2.touches(enemy):
                    d[enemy] -= 1
                    if d[enemy] == 0:
                        del d[enemy]
                if enemy.touches(p1):
                    if one_player:
                        p1_health -= 1
                    else:
                        p12_health -= 1
                if enemy.touches(p2):
                    p2_health -= 1
        if d == {}:
            room6_baddies_killed = True
        if one_player:
            # statement that determines whether or not to draw two players
            camera.draw(bullet1)
            camera.draw(p1)
            if p1.touches(go_south):
                p1_xpos = 383
                p1_ypos = 50
                bullet1_xpos = 383
                bullet1_ypos = 50
                room5 = True
                room6 = False
            if p1.touches(go_north):
                p1_xpos = 383
                p1_ypos = 550
                bullet1_xpos = 383
                bullet1_ypos = 550
                room6 = False
                room7 = True
            if p1_health == 0:
                room6 = False
                title_screen = True
        else:
            camera.draw(bullet1)
            camera.draw(bullet2)
            camera.draw(p1)
            camera.draw(p2)
            if p1.touches(go_south) or p2.touches(go_south):
                p1_xpos = 383
                p1_ypos = 50
                bullet1_xpos = 383
                bullet1_ypos = 50
                p2_xpos = 425
                p2_ypos = 50
                bullet2_xpos = 425
                bullet2_ypos = 50
                room5 = True
                room6 = False
            if p1.touches(go_north) or p2.touches(go_north):
                p1_xpos = 383
                p1_ypos = 50
                bullet1_xpos = 383
                bullet1_ypos = 50
                p2_xpos = 425
                p2_ypos = 50
                bullet2_xpos = 425
                bullet2_ypos = 50
                room6 = False
                room7 = True
        for direction in directions:
            camera.draw(direction)
            # doors
        camera.draw(gamebox.from_color(385, 595, 'brown', 36, 5))
        camera.draw(gamebox.from_color(425, 595, 'brown', 36, 5))
        camera.draw(gamebox.from_color(385, 5, 'brown', 36, 5))
        camera.draw(gamebox.from_color(425, 5, 'brown', 36, 5))
        for wall in room6_walls:
            camera.draw(wall)
            if p1.right_touches(wall):
                overlap1_right = True
            if p1.left_touches(wall):
                overlap1_left = True
            if p1.bottom_touches(wall):
                overlap1_bottom = True
            if p1.top_touches(wall):
                overlap1_top = True

            if p2.right_touches(wall):
                overlap2_right = True
            if p2.left_touches(wall):
                overlap2_left = True
            if p2.bottom_touches(wall):
                overlap2_bottom = True
            if p2.top_touches(wall):
                overlap2_top = True
    elif room7:
        camera.clear('black')
        if room7_enemies:
            number_of_enemies = random.randint(1, 6)
            for i in range(0, number_of_enemies):
                chooser_var = random.randint(0, 1)
                if '25' in str(enemies[chooser_var]):
                    new_enemy = gamebox.from_color(random.randint(21, 779), random.randint(21, 579), 'white', 25, 25)
                else:
                    new_enemy = gamebox.from_color(random.randint(21, 779), random.randint(21, 579), 'cyan', 20, 20)
                if '25' in str(enemies[chooser_var]):
                    d[new_enemy] = 3
                else:
                    d[new_enemy] = 2
            room7_enemies = False
        if not room7_baddies_killed:
            for enemy in list(d.keys()):
                camera.draw(enemy)
                if bullet1.touches(enemy) or bullet2.touches(enemy):
                    d[enemy] -= 1
                    if d[enemy] == 0:
                        del d[enemy]
                if enemy.touches(p1):
                    if one_player:
                        p1_health -= 1
                    else:
                        p12_health -= 1
                if enemy.touches(p2):
                    p2_health -= 1
        if d == {}:
            room7_baddies_killed = True
        if one_player:
            # statement that determines whether or not to draw two players
            camera.draw(bullet1)
            camera.draw(p1)
            if p1.touches(go_south) or p2.touches(go_south):
                p1_xpos = 383
                p1_ypos = 50
                bullet1_xpos = 383
                bullet1_ypos = 50
                room6 = True
                room7 = False
            if p1.touches(go_north) or p2.touches(go_north):
                p1_xpos = 383
                p1_ypos = 550
                bullet1_xpos = 383
                bullet1_ypos = 550
                room7 = False
                room8 = True
            if p1_health == 0:
                room7 = False
                title_screen = True
        else:
            camera.draw(bullet1)
            camera.draw(bullet2)
            camera.draw(p1)
            camera.draw(p2)
            if p1.touches(go_south) or p2.touches(go_south):
                p1_xpos = 383
                p1_ypos = 50
                bullet1_xpos = 383
                bullet1_ypos = 50
                p2_xpos = 425
                p2_ypos = 50
                bullet2_xpos = 425
                bullet2_ypos = 50
                room6 = True
                room7 = False
            if p1.touches(go_north) or p2.touches(go_north):
                p1_xpos = 383
                p1_ypos = 550
                bullet1_xpos = 383
                bullet1_ypos = 550
                p2_xpos = 425
                p2_ypos = 550
                bullet2_xpos = 425
                bullet2_ypos = 550
                room7 = False
                room8 = True
        for direction in directions:
            camera.draw(direction)
            # doors
        camera.draw(gamebox.from_color(385, 595, 'brown', 36, 5))
        camera.draw(gamebox.from_color(425, 595, 'brown', 36, 5))
        camera.draw(gamebox.from_color(385, 5, 'brown', 36, 5))
        camera.draw(gamebox.from_color(425, 5, 'brown', 36, 5))
        for wall in room7_walls:
            camera.draw(wall)
            if p1.right_touches(wall):
                overlap1_right = True
            if p1.left_touches(wall):
                overlap1_left = True
            if p1.bottom_touches(wall):
                overlap1_bottom = True
            if p1.top_touches(wall):
                overlap1_top = True

            if p2.right_touches(wall):
                overlap2_right = True
            if p2.left_touches(wall):
                overlap2_left = True
            if p2.bottom_touches(wall):
                overlap2_bottom = True
            if p2.top_touches(wall):
                overlap2_top = True
    elif room8:
        camera.clear('black')
        if room8_enemies:
            number_of_enemies = random.randint(1, 6)
            for i in range(0, number_of_enemies):
                chooser_var = random.randint(0, 1)
                if '25' in str(enemies[chooser_var]):
                    new_enemy = gamebox.from_color(random.randint(21, 779), random.randint(21, 579), 'white', 25, 25)
                else:
                    new_enemy = gamebox.from_color(random.randint(21, 779), random.randint(21, 579), 'cyan', 20, 20)
                if '25' in str(enemies[chooser_var]):
                    d[new_enemy] = 3
                else:
                    d[new_enemy] = 2
            room8_enemies = False
        if not room8_baddies_killed:
            for enemy in list(d.keys()):
                camera.draw(enemy)
                if bullet1.touches(enemy) or bullet2.touches(enemy):
                    d[enemy] -= 1
                    if d[enemy] == 0:
                        del d[enemy]
                if enemy.touches(p1):
                    if one_player:
                        p1_health -= 1
                    else:
                        p12_health -= 1
                if enemy.touches(p2):
                    p2_health -= 1
        if d == {}:
            room8_baddies_killed = True
        if one_player:
            # statement that determines whether or not to draw two players
            camera.draw(bullet1)
            camera.draw(p1)
            if p1.touches(go_south):
                p1_xpos = 383
                p1_ypos = 50
                bullet1_xpos = 383
                bullet1_ypos = 50
                room7 = True
                room8 = False
            if p1.touches(go_north):
                p1_xpos = 383
                p1_ypos = 550
                bullet1_xpos = 383
                bullet1_ypos = 550
                room8 = False
                room9 = True
            if p1_health == 0:
                room8 = False
                title_screen = True
        else:
            camera.draw(bullet1)
            camera.draw(bullet2)
            camera.draw(p1)
            camera.draw(p2)
            if p1.touches(go_south) or p2.touches(go_south):
                p1_xpos = 383
                p1_ypos = 50
                bullet1_xpos = 383
                bullet1_ypos = 50
                p2_xpos = 425
                p2_ypos = 50
                bullet2_xpos = 425
                bullet2_ypos = 50
                room7 = True
                room8 = False
            if p1.touches(go_north) or p2.touches(go_north):
                p1_xpos = 383
                p1_ypos = 550
                bullet1_xpos = 383
                bullet1_ypos = 550
                p2_xpos = 425
                p2_ypos = 550
                bullet2_xpos = 425
                bullet2_ypos = 550
                room8 = False
                room9 = True
        for direction in directions:
            camera.draw(direction)
            # doors
        camera.draw(gamebox.from_color(385, 595, 'brown', 36, 5))
        camera.draw(gamebox.from_color(425, 595, 'brown', 36, 5))
        camera.draw(gamebox.from_color(385, 5, 'brown', 36, 5))
        camera.draw(gamebox.from_color(425, 5, 'brown', 36, 5))
        for wall in room8_walls:
            camera.draw(wall)
            if p1.right_touches(wall):
                overlap1_right = True
            if p1.left_touches(wall):
                overlap1_left = True
            if p1.bottom_touches(wall):
                overlap1_bottom = True
            if p1.top_touches(wall):
                overlap1_top = True

            if p2.right_touches(wall):
                overlap2_right = True
            if p2.left_touches(wall):
                overlap2_left = True
            if p2.bottom_touches(wall):
                overlap2_bottom = True
            if p2.top_touches(wall):
                overlap2_top = True
    elif room9:
        camera.clear('black')
        if room9_enemies:
            number_of_enemies = random.randint(1, 6)
            for i in range(0, number_of_enemies):
                chooser_var = random.randint(0, 1)
                if '25' in str(enemies[chooser_var]):
                    new_enemy = gamebox.from_color(random.randint(21, 779), random.randint(21, 579), 'white', 25, 25)
                else:
                    new_enemy = gamebox.from_color(random.randint(21, 779), random.randint(21, 579), 'cyan', 20, 20)
                if '25' in str(enemies[chooser_var]):
                    d[new_enemy] = 3
                else:
                    d[new_enemy] = 2
            room9_enemies = False
        if not room9_baddies_killed:
            for enemy in list(d.keys()):
                camera.draw(enemy)
                if bullet1.touches(enemy) or bullet2.touches(enemy):
                    d[enemy] -= 1
                    if d[enemy] == 0:
                        del d[enemy]
                if enemy.touches(p1):
                    if one_player:
                        p1_health -= 1
                    else:
                        p12_health -= 1
                if enemy.touches(p2):
                    p2_health -= 1
        if d == {}:
            room9_baddies_killed = True
        if one_player:
            # statement that determines whether or not to draw two players
            camera.draw(bullet1)
            camera.draw(p1)
            if p1.touches(go_south):
                p1_xpos = 383
                p1_ypos = 50
                bullet1_xpos = 383
                bullet1_ypos = 50
                room8 = True
                room9 = False
            if p1_health == 0:
                room9 = False
                title_screen = True
        else:
            camera.draw(bullet1)
            camera.draw(bullet2)
            camera.draw(p1)
            camera.draw(p2)
            if p1.touches(go_south) or p2.touches(go_south):
                p1_xpos = 383
                p1_ypos = 50
                bullet1_xpos = 383
                bullet1_ypos = 50
                p2_xpos = 425
                p2_ypos = 50
                bullet2_xpos = 425
                bullet2_ypos = 50
                room8 = True
                room9 = False
        for direction in directions:
            camera.draw(direction)
            # doors
        camera.draw(gamebox.from_color(385, 595, 'brown', 36, 5))
        camera.draw(gamebox.from_color(425, 595, 'brown', 36, 5))
        for wall in room9_walls:
            camera.draw(wall)
            if p1.right_touches(wall):
                overlap1_right = True
            if p1.left_touches(wall):
                overlap1_left = True
            if p1.bottom_touches(wall):
                overlap1_bottom = True
            if p1.top_touches(wall):
                overlap1_top = True

            if p2.right_touches(wall):
                overlap2_right = True
            if p2.left_touches(wall):
                overlap2_left = True
            if p2.bottom_touches(wall):
                overlap2_bottom = True
            if p2.top_touches(wall):
                overlap2_top = True
    elif room10:
        camera.clear('black')
        if room10_enemies:
            number_of_enemies = random.randint(1, 6)
            for i in range(0, number_of_enemies):
                chooser_var = random.randint(0, 1)
                if '25' in str(enemies[chooser_var]):
                    new_enemy = gamebox.from_color(random.randint(21, 779), random.randint(21, 579), 'white', 25, 25)
                else:
                    new_enemy = gamebox.from_color(random.randint(21, 779), random.randint(21, 579), 'cyan', 20, 20)
                if '25' in str(enemies[chooser_var]):
                    d[new_enemy] = 3
                else:
                    d[new_enemy] = 2
            room10_enemies = False
        if not room10_baddies_killed:
            for enemy in list(d.keys()):
                camera.draw(enemy)
                if bullet1.touches(enemy) or bullet2.touches(enemy):
                    d[enemy] -= 1
                    if d[enemy] == 0:
                        del d[enemy]
                if enemy.touches(p1):
                    if one_player:
                        p1_health -= 1
                    else:
                        p12_health -= 1
                if enemy.touches(p2):
                    p2_health -= 1
        if d == {}:
            room10_baddies_killed = True
        if one_player:
            # statement that determines whether or not to draw two players
            camera.draw(p1)
            camera.draw(bullet1)
        else:
            camera.draw(p1)
            camera.draw(p2)
            camera.draw(bullet1)
            camera.draw(bullet2)
        if p1_health == 0:
            room10 = False
            title_screen = True
        for direction in directions:
            camera.draw(direction)
            # doors
        camera.draw(gamebox.from_color(385, 595, 'brown', 36, 5))
        camera.draw(gamebox.from_color(425, 595, 'brown', 36, 5))
        for wall in room10_walls:
            camera.draw(wall)
            if p1.right_touches(wall):
                overlap1_right = True
            if p1.left_touches(wall):
                overlap1_left = True
            if p1.bottom_touches(wall):
                overlap1_bottom = True
            if p1.top_touches(wall):
                overlap1_top = True

            if p2.right_touches(wall):
                overlap2_right = True
            if p2.left_touches(wall):
                overlap2_left = True
            if p2.bottom_touches(wall):
                overlap2_bottom = True
            if p2.top_touches(wall):
                overlap2_top = True

    if one_player:
        # Determines whether or not to utilize both 1 player or 2 player inputs
        if pygame.K_UP in keys and not overlap1_top:
            p1_ypos += -5
            last_touch1 = 'up'
            if not shootup1 and not shootdown1 and not shootleft1 and not shootright1:
                bullet1_ypos += -5
        if pygame.K_DOWN in keys and not overlap1_bottom:
            p1_ypos += 5
            last_touch1 = 'down'
            if not shootup1 and not shootdown1 and not shootleft1 and not shootright1:
                bullet1_ypos += 5
        if pygame.K_RIGHT in keys and not overlap1_right:
            p1_xpos += 5
            last_touch1 = 'right'
            if not shootup1 and not shootdown1 and not shootleft1 and not shootright1:
                bullet1_xpos += 5
        if pygame.K_LEFT in keys and not overlap1_left:
            p1_xpos += -5
            last_touch1 = 'left'
            if not shootup1 and not shootdown1 and not shootleft1 and not shootright1:
                bullet1_xpos += -5
        if pygame.K_SLASH in keys and pygame.K_UP in keys or pygame.K_SLASH in keys and last_touch1 == 'up':
            shootup1 = True
        if pygame.K_SLASH in keys and pygame.K_DOWN in keys or pygame.K_SLASH in keys and last_touch1 == 'down':
            shootdown1 = True
        if pygame.K_SLASH in keys and pygame.K_RIGHT in keys or pygame.K_SLASH in keys and last_touch1 == 'right':
            shootright1 = True
        if pygame.K_SLASH in keys and pygame.K_LEFT in keys or pygame.K_SLASH in keys and last_touch1 == 'left':
            shootleft1 = True
        if shootup1:
            bullet1_ypos += -50
        if shootdown1:
            bullet1_ypos += 50
        if shootright1:
            bullet1_xpos += 50
        if shootleft1:
            bullet1_xpos += -50
        if bullet1_ypos < 0 or bullet1_ypos > 600 or bullet1_xpos < 0 or bullet1_xpos > 800:
            shootup1 = False
            shootdown1 = False
            shootleft1 = False
            shootright1 = False
            bullet1_xpos = p1_xpos
            bullet1_ypos = p1_ypos
    else:
        # p1 controls
        if pygame.K_UP in keys and not overlap1_top:
            p1_ypos += -5
            last_touch1 = 'up'
            if not shootup1 and not shootdown1 and not shootleft1 and not shootright1:
                bullet1_ypos += -5
        if pygame.K_DOWN in keys and not overlap1_bottom:
            p1_ypos += 5
            last_touch1 = 'down'
            if not shootup1 and not shootdown1 and not shootleft1 and not shootright1:
                bullet1_ypos += 5
        if pygame.K_RIGHT in keys and not overlap1_right:
            p1_xpos += 5
            last_touch1 = 'right'
            if not shootup1 and not shootdown1 and not shootleft1 and not shootright1:
                bullet1_xpos += 5
        if pygame.K_LEFT in keys and not overlap1_left:
            p1_xpos += -5
            last_touch1 = 'left'
            if not shootup1 and not shootdown1 and not shootleft1 and not shootright1:
                bullet1_xpos += -5
        if pygame.K_SLASH in keys and pygame.K_UP in keys or pygame.K_SLASH in keys and last_touch1 == 'up':
            shootup1 = True
        if pygame.K_SLASH in keys and pygame.K_DOWN in keys or pygame.K_SLASH in keys and last_touch1 == 'down':
            shootdown1 = True
        if pygame.K_SLASH in keys and pygame.K_RIGHT in keys or pygame.K_SLASH in keys and last_touch1 == 'right':
            shootright1 = True
        if pygame.K_SLASH in keys and pygame.K_LEFT in keys or pygame.K_SLASH in keys and last_touch1 == 'left':
            shootleft1 = True
        if shootup1:
            bullet1_ypos += -50
        if shootdown1:
            bullet1_ypos += 50
        if shootright1:
            bullet1_xpos += 50
        if shootleft1:
            bullet1_xpos += -50
        if bullet1_ypos < 0 or bullet1_ypos > 600 or bullet1_xpos < 0 or bullet1_xpos > 800:
            shootup1 = False
            shootdown1 = False
            shootleft1 = False
            shootright1 = False
            bullet1_xpos = p1_xpos
            bullet1_ypos = p1_ypos
        for enemy in list(d.keys()):
            if bullet1.touches(enemy):
                shootup1 = False
                shootdown1 = False
                shootleft1 = False
                shootright1 = False
                bullet1_xpos = p1_xpos
                bullet1_ypos = p1_ypos

        # p2 controls
        if pygame.K_w in keys and not overlap2_top:
            p2_ypos += -5
            last_touch2 = 'up'
            if not shootup2 and not shootdown2 and not shootleft2 and not shootright2:
                bullet2_ypos += -5
        if pygame.K_d in keys and not overlap2_right:
            p2_xpos += 5
            last_touch2 = 'right'
            if not shootup2 and not shootdown2 and not shootleft2 and not shootright2:
                bullet2_xpos += 5
        if pygame.K_a in keys and not overlap2_left:
            p2_xpos += -5
            last_touch2 = 'left'
            if not shootup2 and not shootdown2 and not shootleft2 and not shootright2:
                bullet2_xpos += -5
        if pygame.K_s in keys and not overlap2_bottom:
            p2_ypos += 5
            last_touch2 = 'down'
            if not shootup2 and not shootdown2 and not shootleft2 and not shootright2:
                bullet2_ypos += 5
        if pygame.K_e in keys and pygame.K_w in keys or pygame.K_e in keys and last_touch2 == 'up':
            shootup2 = True
        if pygame.K_e in keys and pygame.K_s in keys or pygame.K_e in keys and last_touch2 == 'down':
            shootdown2 = True
        if pygame.K_e in keys and pygame.K_d in keys or pygame.K_e in keys and last_touch2 == 'right':
            shootright2 = True
        if pygame.K_e in keys and pygame.K_a in keys or pygame.K_e in keys and last_touch2 == 'left':
            shootleft2 = True
        if shootup2:
            bullet2_ypos += -50
        if shootdown2:
            bullet2_ypos += 50
        if shootright2:
            bullet2_xpos += 50
        if shootleft2:
            bullet2_xpos += -50
        if bullet2_ypos < 0 or bullet2_ypos > 600 or bullet2_xpos < 0 or bullet2_xpos > 800:
            shootup2 = False
            shootdown2 = False
            shootleft2 = False
            shootright2 = False
            bullet2_xpos = p2_xpos
            bullet2_ypos = p2_ypos

    camera.display()


ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)

