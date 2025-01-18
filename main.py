key_switch_camera = 'c'
key_switch_mode = 'i'

key_forward = 'q'
key_back = 's'
key_left = 'a'
key_right = 'd'
key_up = 'space'
key_down = 'shift'

key_turn_left = 'q'
key_turn_right = 'e'

step = 0.2

class Hero():
    def __ini__(self, pos, land):
        self.land = land
        self.mode = True
        self.hero = loader.loadModer('smiley')
        self.hero.setColor(1,0.5,0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()
    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0,0,1.5)
        self.cameraOn = True
    def CameraUp(self):
        x, y, z = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-x,-y,-z,-3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False
    def changeViev(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()
    def turn_left(self):
        self.hero.setH((self.hero.getH()+5)%360)
    def turn_right(self):
        self.hero.setH((self.hero.getH()-5)%360)
    def look_at(self, angle):
        x_from = self.hero.getX()
        y_from = self.hero.getY()
        z_from = self.hero.getZ()
        dx,dy = self.check_dir(angle)
        x_to = x_from + dx
        y_to = y_from + dy
        return x_to, y_to, z_from
    def justMove(self):
        x,y,z = self.look_at(angle)
        if not self.land.isBlockAt((round(x),round(y),round(z))):
            self.hero.setPos((x,y,z))
            print(f"Герой переміщений на {(x,y,z)}")
        else:
            print(f"Неможливо рухатись, є блок на {(x,y,z)}")
    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)
    def check_dir(self, angle):
        if angle >= 0 and angle <= 20:
            return(0, -step)
        elif angle <= 65:
            return (step, -step)
        elif angle <= 110:
            return(step, 0)
        elif angle <= 155:
            return
        elif angle <= 200:
            return (0,step)
        elif angle <= 245:
            return (-step,step)
        elif angle <= 290:
            return (-step, 0)
        elif angle <= 335:
            return (-step,-step)
        else:
            return (0, -step)
    def forward(self):
        angle = (self.hero.getH()) % 360
        self.move_to(angle)
    def back(self):
        angle = (self.hero.getH()+180)%360
        self.move_to(angle)
    def left(self):
        angle = (self.hero.getH()+90)%360
        self.move_to(angle)
    def right(self):
        angle = (self.hero.getH()+270)%360
        self.move_to(angle)
    def move_up(self):
        x,y,z = self.hero.getPos()
        if not z == 5:
            new_pos = (x,y,z + step)
            self.hero.setPos(new_pos)
    def move_down(self):
        x,y,z = self.hero.getPos()
        if not z == 0 and not self.land.isBlockAt((round(x),round(y),round(z-step))):
            new_pos (x,y,z - step)
            self.hero.setPos(newPos)
