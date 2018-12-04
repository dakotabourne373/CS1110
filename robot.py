import gamebox, random

class Robot:
    """Represents a robot stuck inside a grid of rooms"""
    def __init__(self, kind=1, start=None):
        """Robot() makes a robot in the corer of a square grid, as does Robot(1)
        Robot(2) makes a robot in the corer of a rectangular grid
        Robot(3) makes a robot randomly placed in a rectangular grid
        Robot(4) makes a robot randomly placed in a random mess of rooms
        Robot('''
          xxxxx
         xxxxxxx
        xx xxx xx
        xxxx xxxx
        xxxx xxxx
        xx xxx xx
        xxx   xxx
         xxxxxxx
          xxxxx
        ''') makes a robot inside a smiley face
        
        All versions have an optional "start position" parameter; if given
        it should be an x,y coordinate, with (0,0) the top left corner
        with x increasing to right and y to bottom"""
        import pygame
        self.scale = 35
        try:
            self.scale = min(pygame.display.Info().current_w, pygame.display.Info().current_h)//24
        except:
            pass
        surf = pygame.surface.Surface((self.scale*2,self.scale*2), pygame.SRCALPHA, 32)
        pygame.draw.polygon(surf, (95,47,0), [(0,0),(self.scale,self.scale),(0,self.scale*2)])
        pygame.draw.polygon(surf, (191,255,0), [(0,0),(self.scale,self.scale),(self.scale*2,0)])
        pygame.draw.polygon(surf, (63,0,63), [(self.scale*2,0),(self.scale,self.scale),(self.scale*2,self.scale*2)])
        pygame.draw.polygon(surf, (207,191,63), [(0,self.scale*2),(self.scale,self.scale),(self.scale*2,self.scale*2)])
        pygame.draw.rect(surf, (191,191,191), pygame.rect.Rect(
            self.scale//4, self.scale//4,
            6*self.scale//4, 6*self.scale//4,
        ))
        self.room = gamebox.SpriteBox(0,0,surf,None)
        self.door = gamebox.from_color(0,0, (0,127,127), 1,1)
        self.b = gamebox.from_circle(self.scale*3, self.scale*3, 'white', self.scale//2, 'black', 3*self.scale//8)
        self.eye = gamebox.from_circle(self.scale*3, self.scale*3, 'black', self.scale//2, 'white', 7*self.scale//16)
        self.pupil = gamebox.from_circle(self.scale*3, self.scale*3, 'black', self.scale//4)
        self.ok = True
        self.look = (0,0)
    
        if kind == 1:
            s = random.randrange(2,10)
            self.open = {(a,b) for a in range(s) for b in range(s)}
            self.c = gamebox.Camera(self.scale*s*2, self.scale*s*2)
            if start not in self.open: start = (0,0)
            self.b.center = (start[0]*2+1)*self.scale, (start[1]*2+1)*self.scale
        elif kind == 2:
            w,h = random.randrange(2,10), random.randrange(2,10)
            self.open = {(a,b) for a in range(w) for b in range(h)}
            self.c = gamebox.Camera(self.scale*w*2, self.scale*h*2)
            if start not in self.open: start = (0,0)
            self.b.center = (start[0]*2+1)*self.scale, (start[1]*2+1)*self.scale
        elif kind == 3:
            w,h = random.randrange(2,10), random.randrange(2,10)
            self.open = {(a,b) for a in range(w) for b in range(h)}
            self.c = gamebox.Camera(self.scale*w*2, self.scale*h*2)
            if start not in self.open: start = random.choice(list(self.open))
            self.b.center = (start[0]*2+1)*self.scale, (start[1]*2+1)*self.scale
        elif kind == 4:
            cells = [(0,0)]
            w,h = 1,1
            while w < 10 and h < 10:
                x,y = random.choice(cells)
                if random.randrange(2) == 0:
                    x += random.randrange(-1,2,2)
                else:
                    y += random.randrange(-1,2,2)
                if (x,y) not in cells:
                    cells.append((x,y))
                w = 1 + max(_[0] for _ in cells) - min(_[0] for _ in cells)
                h = 1 + max(_[1] for _ in cells) - min(_[1] for _ in cells)
            mx, my = min(_[0] for _ in cells), min(_[1] for _ in cells)
            self.open = {(a-mx, b-my) for (a,b) in cells}
            self.c = gamebox.Camera(self.scale*w*2, self.scale*h*2)
            if start not in self.open: start = random.choice(list(self.open))
            self.b.center = (start[0]*2+1)*self.scale, (start[1]*2+1)*self.scale
        elif type(kind) is str:
            cells = set()
            for y in range(len(kind.split('\n'))):
                row = kind.split('\n')[y]
                for x in range(len(row)):
                    cell = row[x]
                    if not cell.isspace():
                        cells.add((x,y))
            w = 1 + max(_[0] for _ in cells) - min(_[0] for _ in cells)
            h = 1 + max(_[1] for _ in cells) - min(_[1] for _ in cells)
            mx, my = min(_[0] for _ in cells), min(_[1] for _ in cells)
            self.open = {(a-mx, b-my) for (a,b) in cells}
            self.c = gamebox.Camera(self.scale*w*2, self.scale*h*2)
            if start not in self.open: start = random.choice(list(self.open))
            self.b.center = (start[0]*2+1)*self.scale, (start[1]*2+1)*self.scale
        else:
            raise ValueError('Invalid room kind: '+repr(kind))
        
        self.moves = 0
        self.looks = 0
        print('Correct answer:', len(self.open))
     
    def _tick(self, keys):
        if not self.ok: return False
        self.c.clear('black')
        
        for x,y in sorted(self.open):
            self.room.center = (2*x+1)*self.scale, (2*y+1)*self.scale
            self.c.draw(self.room)
            if (x-1,y) in self.open:
                self.door.size = self.scale/2, self.scale
                self.door.center = (2*x)*self.scale, (2*y+1)*self.scale
                self.c.draw(self.door)
            if (x,y-1) in self.open:
                self.door.size = self.scale, self.scale/2
                self.door.center = (2*x+1)*self.scale, (2*y)*self.scale
                self.c.draw(self.door)
        
        self.b.move_speed()
        self.eye.center = self.b.center
        self.pupil.x = self.eye.x + self.look[0]*self.scale/4
        self.pupil.y = self.eye.y + self.look[1]*self.scale/4
        self.c.draw(self.eye)
        self.c.draw(self.pupil)
        
        if (self.b.x//(self.scale*2), self.b.y//(self.scale*2)) not in self.open:
            self.c.draw("Crash!", self.scale*2, 'red', self.c.center)
            print("Crashed into a wall!")
            self.ok = False
            gamebox.stop_loop()
            gamebox.keys_loop(lambda x: gamebox.stop_loop())
            
        self.c.display()
    def left(self):
        self.b.speed = -self.scale/8,0
        self.look = (-1,0)
        if self.ok:
            tmp = gamebox.timer_loop(60, self._tick, 16)
            self.ok &= tmp
            self.moves += 1
        return self.ok
    def right(self):
        self.b.speed = self.scale/8,0
        self.look = (1,0)
        if self.ok:
            tmp = gamebox.timer_loop(60, self._tick, 16)
            self.ok &= tmp
            self.moves += 1
        return self.ok
    def up(self):
        self.b.speed = 0,-self.scale/8
        self.look = (0,-1)
        if self.ok:
            tmp = gamebox.timer_loop(60, self._tick, 16)
            self.ok &= tmp
            self.moves += 1
        return self.ok
    def down(self):
        self.b.speed = 0,self.scale/8
        self.look = (0,1)
        if self.ok:
            tmp = gamebox.timer_loop(60, self._tick, 16)
            self.ok &= tmp
            self.moves += 1
        return self.ok
    
    def l(self): return self.left()
    def w(self): return self.left()
    def west(self): return self.left()
    
    def r(self): return self.right()
    def e(self): return self.right()
    def east(self): return self.right()

    def u(self): return self.up()
    def n(self): return self.up()
    def north(self): return self.up()
    
    def d(self): return self.down()
    def s(self): return self.down()
    def south(self): return self.down()

    def check_left(self):
        if not self.ok: return False
        self.looks += 1
        self.b.speed = 0,0
        if self.look != (-1,0):
            self.look = (-1,0)
            self.ok &= gamebox.timer_loop(60, self._tick, 8)
        return (self.b.x//(self.scale*2) - 1, self.b.y//(self.scale*2)) in self.open
    def check_right(self):
        if not self.ok: return False
        self.looks += 1
        self.b.speed = 0,0
        if self.look != (1,0):
            self.look = (1,0)
            self.ok &= gamebox.timer_loop(60, self._tick, 8)
        return (self.b.x//(self.scale*2) + 1, self.b.y//(self.scale*2)) in self.open
    def check_up(self):
        if not self.ok: return False
        self.looks += 1
        self.b.speed = 0,0
        if self.look != (0,-1):
            self.look = (0,-1)
            self.ok &= gamebox.timer_loop(60, self._tick, 8)
        return (self.b.x//(self.scale*2), self.b.y//(self.scale*2) - 1) in self.open
    def check_down(self):
        if not self.ok: return False
        self.looks += 1
        self.b.speed = 0,0
        if self.look != (0,1):
            self.look = (0,1)
            self.ok &= gamebox.timer_loop(60, self._tick, 8)
        return (self.b.x//(self.scale*2), self.b.y//(self.scale*2) + 1) in self.open

    def cl(self): return self.check_left()
    def cw(self): return self.check_left()
    def check_west(self): return self.check_left()
    
    def cr(self): return self.check_right()
    def ce(self): return self.check_right()
    def check_east(self): return self.check_right()

    def cu(self): return self.check_up()
    def cn(self): return self.check_up()
    def check_north(self): return self.check_up()
    
    def cd(self): return self.check_down()
    def cs(self): return self.check_down()
    def check_south(self): return self.check_down()


    def say(self, num):
        if not self.ok: return
        self.look = (0,0)
        self._tick(())
        self.c.draw(str(num), self.scale*4, 'red', self.c.center)
        self.c.display()
        print('said',num,'after',self.moves,'moves and',self.looks,'looks')
        gamebox.keys_loop(lambda x: gamebox.stop_loop())
    def done(self):
        self.look = (0,0); self._tick(())
        print('waited for program to be terminated after',self.moves,'moves and',self.looks,'looks')
        gamebox.keys_loop(lambda x: None)


