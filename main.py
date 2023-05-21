import tkinter as tk
import time

class Game:
    def __init__(self):
        #Root setup
        self.root = tk.Tk()
        self.root.title('Platformer')
        self.root.geometry('650x650')

        #Canvas Setup
        self.canvas = tk.Canvas(self.root,width=650,height=650)
        self.canvas.pack()

        self.shape = [self.canvas.create_rectangle(650/2,600,650/2+50,600-50,fill='white')] #Edit for the player
        self.ground = [self.canvas.create_rectangle(650/2 - 100,600, 650/2 + 100, 600+50,fill='white')] #Edit for the ground
        self.speed = 4
        self.yVel = 0
        self.toMove = 0

        self.root.bind('<Key>',self.keyHandle)
        self.root.bind('<space>',self.jump)

        self.jumping = False
        self.grounded = False
    def updateSelf(self):
        if self.yVel <= 0:
            self.jumping = False
        col = self.collision()
        self.grounded = False
        print(self.yVel)
        self.gravity()
        for i in self.ground:
            if i in col and self.yVel >= -0.05:
                print('Set')
                self.yVel = 0
            if i in col:
                self.grounded = True
        for i in self.shape:
            self.canvas.move(i, self.toMove,self.yVel)
        self.toMove = 0
    def keyHandle(self,event):
        if event.char == 'a':
            self.toMove -= self.speed
            return
        if event.char == 'd':
            self.toMove += self.speed
            return
    def gravity(self):
        self.yVel += 0.05
    def jump(self,event):
        print('Jump')
        if self.grounded == True:
            self.jumping = True
            self.yVel = -4

    def collision(self):
        pos = self.canvas.bbox(self.shape)
        return self.canvas.find_overlapping(pos[0],pos[1],pos[2],pos[3])
    def getRoot(self):
        return self.root
    def getCanvas(self):
        return self.canvas

game = Game()

while 1:
    game.updateSelf()
    game.getCanvas().update()
    time.sleep(0.01)
game.getRoot().mainloop()