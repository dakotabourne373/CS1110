# Dakota Bourne (db2nb) Nick Manalac (ntm4kd)

import robot


def square():
    answer = 1
    r = robot.Robot(1)
    while True:
        if r.check_south():
            r.south()
            answer += 1
        else:
            r.say(answer ** 2)
            break


def rect():
    r = robot.Robot(2)
    vert = 1
    horz = 1
    while True:
        if r.check_south():
            r.south()
            vert += 1
        else:
            break
    while True:
        if r.check_east():
            r.east()
            horz += 1
        else:
            r.say(vert * horz)
            break


def middle1():
    r = robot.Robot(3)
    vert = 1
    horz = 1
    while True:
        if r.check_west():
            r.west()
        elif r.check_north():
            r.north()
        else:
            break
    while True:
        if r.check_south():
            r.south()
            vert += 1
        else:
            break
    while True:
        if r.check_east():
            r.east()
            horz += 1
        else:
            r.say(vert * horz)
            break


def middle():
    r = robot.Robot(4)
    room_lst = [[0, 0]]
    x = 0
    y = 0
    new_cord = [x, y]
    while True:
        if r.check_north():
            if [x,y+1] not in room_lst:
                r.north()
                y += 1
                room_lst.append(new_cord)
        elif r.check_west():
            if [x-1,y] not in room_lst:
                r.west()
                x -= 1
                room_lst.append(new_cord)
        elif r.check_south():
            if [x,y-1] not in room_lst:
                r.south()
                y -= 1
                room_lst.append(new_cord)
        else:
            if [x+1,y] not in room_lst:
                r.east()
                x += 1
                room_lst.append(new_cord)
        if [x,y+1] not in room_lst and [x-1,y] not in room_lst and [x,y-1] not in room_lst and [x+1,y] not in room_lst:
            break
    a = 'at least ' + str(len(room_lst)) + ' rooms'
    r.say(a)
middle()