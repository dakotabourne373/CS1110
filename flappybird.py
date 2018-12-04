# Dakota Bourne db2nb
import pygame, gamebox, random
camera=gamebox.Camera(800,600)

#Declares needed variable
player_speed = 14
score = 0
game_over = False
game_on = False

#Originial Column position declaration
column1_xpos = 1200
column2_xpos = 1600
column3_xpos = 2000

column1_ypos = random.randint(-225, 100)
column2_ypos = random.randint(-225, 100)
column3_ypos = random.randint(-225, 100)

column1_ypos_top = column1_ypos + random.randint(680, 875)
column2_ypos_top = column2_ypos + random.randint(680, 875)
column3_ypos_top = column3_ypos + random.randint(680, 875)

#Player gamebox definition
p1 = gamebox.from_image(200, 300, 'flamingo.png')


def tick(keys):
    #--- Global Variable Declaration ---
    global column1_xpos
    global column2_xpos
    global column3_xpos
    global column1_ypos
    global column2_ypos
    global column3_ypos
    global column1_ypos_top
    global column2_ypos_top
    global column3_ypos_top
    global game_on
    global score
    global game_over

    #--------------------------- The Column Code ------------------------------------
    top_column1 = gamebox.from_color(column1_xpos, column1_ypos_top, "white", 50, 500)
    bottom_column1 = gamebox.from_color(column1_xpos, column1_ypos, "white", 50, 500)
    bottom_column2 = gamebox.from_color(column2_xpos, column2_ypos, "blue", 50, 500)
    top_column2 = gamebox.from_color(column2_xpos, column2_ypos_top, "blue", 50, 500)
    top_column3 = gamebox.from_color(column3_xpos, column3_ypos_top, "purple", 50, 500)
    bottom_column3 = gamebox.from_color(column3_xpos, column3_ypos, "purple", 50, 500)
    column_lst = [top_column1,bottom_column1,top_column2,bottom_column2,top_column3,bottom_column3]

    # ------- Input ---------
    if pygame.K_SPACE in keys:
        game_on = True
        p1.yspeed = -10

    # ----- Column Movement ------
    if game_on:
        p1.move(0, p1.yspeed)
        p1.yspeed += 3
        column1_xpos -= 10
        column2_xpos -= 10
        column3_xpos -= 10
        if column1_xpos == -20:
            column1_xpos += 1200
            column1_ypos = random.randint(-225, 100)
            column1_ypos_top = column1_ypos + random.randint(680, 875)
        if column2_xpos == -20:
            column2_xpos += 1200
            column2_ypos = random.randint(-225, 100)
            column2_ypos_top = column2_ypos + random.randint(680, 875)
        if column3_xpos == -20:
            column3_xpos += 1200
            column3_ypos = random.randint(-225, 100)
            column3_ypos_top = column3_ypos + random.randint(680, 875)

    # --------------- Collision Detection ------------------
    if p1.touches(top_column1) or p1.touches(bottom_column1):
        game_on = False
        game_over = True
    if p1.touches(top_column2) or p1.touches(bottom_column2):
        game_on = False
        game_over = True
    if p1.touches(top_column3) or p1.touches(bottom_column3):
        game_on = False
        game_over = True

    # ----- Scoring ------
    if column1_xpos == 200:
        score += 1
    if column2_xpos == 200:
        score += 1
    if column3_xpos == 200:
        score += 1



    # ----- Draw Methods --------
    camera.clear('black')
    camera.draw(gamebox.from_text(400, 50, str(score), 50, "Red", bold=True))
    if game_over:
        camera.draw(gamebox.from_text(400, 200, "You Lost! Your score is", 30, "Green", bold=False))
        camera.draw(gamebox.from_text(400, 250, str(score), 30, "Blue", bold=True))
        gamebox.pause()
    if game_over is False and game_on is False:
        camera.draw(gamebox.from_text(400, 200, "Welcome to Flappy Flamingo!", 40, "Green", bold=False))
        camera.draw(gamebox.from_text(400, 250, "Press Space To Play", 40, "Green", bold=False))
    # Draw all the walls
    for wall in column_lst:
        camera.draw(wall)

    # Draw the player paddles and the ball
    camera.draw(p1)



    camera.display()

ticks_per_second = 40

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)

