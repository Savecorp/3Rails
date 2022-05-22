#Linux users: install ursina

import platform
import os
if platform.system() == "Windows":
    os.system("pip install ursina")
import io
from ursina import *
from ursina import Ursina, printvar
import time
import random
from random import randint

if not os.path.exists("scoreh.txt"):
    f = open("scoreh.txt", "w")
    f.write("0")
    f.close()

print ("3Rails version: 1.01")


window.title = 'Train sim'
window.borderless = False
camera.orthographic = True
camera.position = (30/2,8)
camera.fov = 16
tekstuuri = 'juna.png'
kuolit = 0
kiviy = 0


window = Ursina()

tausta = Entity(model='quad', texture='tausta.png',poisiton=(0,0,0.001),scale_y=8,scale_x=15)

scoretext = Text(text="Your Score is: 0", color=color.white, scale=2, x=-.87, y=.48,popup = True)
scoretexth = Text(text="Your High Score is: 0", color=color.white, scale=2, x=.17, y=.48,popup = True)

x=-2
speed=30


#random track 1-3
if __name__ == '__main__':
    start = 1  # inclusive
    end = 4  # exclusive
    n = 1  # size
    track = random.choices(range(1, 4))
#print (track)






class juna(Entity):
    def __init__(self, x, speed):
        super().__init__()
        self.model = 'quad'
        self.texture = tekstuuri
        self.scale_y=1
        self.scale_x=2
        self.x=-15
        self.speed=speed
        self.collider = 'box'
        self.score = 0
        scoreh = open("scoreh.txt", "r")
        self.scoreh = int(scoreh.read())
        self.z = -0.01
        if track == [3]:
            finaltrack = -2.23
        if track == [2]:
            finaltrack = 0.35
        if track == [1]:
            finaltrack = 2.9
        self.y=finaltrack





    def update(self):
        
        scoreh = open("scoreh.txt", "r")
        scoretexth.text = "Your High Score is: " + str(scoreh.read())

        nuoli.y = self.y - 1.15
        self.scale_y=1
        self.scale_x=2

        self.x+=0.1 * time.dt*self.speed
        kuolit = 0
        #osuuko juna kiveen
        if juna.intersects(kivi1).hit:
            print ("kuolit")
            kivenpaikka1 = [-2.23, 0.35, 2.9]
            kivi1.y = random.choice(kivenpaikka1)
            self.speed = speed
            self.score = 0
            scoretext.text = "Your Score is: " + str(self.score)
            if kuolit == 1:
                time.sleep(1)
            self.scale_y = 1
            self.scale_x = 2
            kuolit = 1

        if juna.intersects(kivi2).hit:
            print ("kuolit")
            kivenpaikka2 = [-2.23, 0.35, 2.9]
            kivi2.y = random.choice(kivenpaikka2)
            self.speed = speed
            self.score = 0
            scoretext.text = "Your Score is: " + str(self.score)
            if kuolit == 1:
                time.sleep(1)
            self.scale_y = 1
            self.scale_x = 2
            kuolit = 1


        #1 -> 2
        if self.x > -5.0:
            if self.x < -4.0:
                if self.y > 2.8:
                    if self.rotation_z > 14:
                        self.y = 0.35
                        self.rotation_z = 0

        #2 -> 3
        if self.x > -1.4:
            if self.x < -0.9:
                if self.y > 0.34:
                    if self.y < 0.36:
                        if self.rotation_z > 14:
                            self.y = -2.23
                            self.rotation_z = 0

        # 1 -> 2
        if self.x > 0.0:
            if self.x < 1.0:
                if self.y > 2.8:
                    if self.rotation_z > 14:
                        self.y = 0.35
                        self.rotation_z = 0

        #3 -> 2
        if self.x > -5.6:
            if self.x < -4.9:
                if self.y < 2.22:
                    if self.rotation_z < -14:
                        self.y = 0.35
                        self.rotation_z = 0

        #3 -> 2
        if self.x > 3.9:
            if self.x < 4.6:
                if self.y < -2.22:
                    if self.rotation_z < -14:
                        self.y = 0.35
                        self.rotation_z = 0

        #2 -> 1
        if self.x > 3.9:
            if self.x < 4.6:
                if self.y > 0.34:
                    if self.y < 0.36:
                        if self.rotation_z < -14:
                            self.y = 2.9
                            self.rotation_z = 0



        if self.x > 10.5:
            self.x = -15
            #self.scale_y = 1
            #self.scale_x = 2

        if self.x > 10:
            self.score += 1

            testi1 = open("scoreh.txt", "r")
            SH1 = int(testi1.read())

            if SH1 < self.score:
                self.scoreh += 1
                file = open("scoreh.txt", "w")
                file.write(str(self.scoreh))
                file.close()
            self.speed += 5
            print ("speed:", self.speed)
            scoretext.text = "Your Score is: " + str(self.score)


            scoreh = open("scoreh.txt", "r")
            scoretexth.text = "Your High Score is: " + str(scoreh.read())


            print("Score:", self.score)
            self.x = -15
            kivenpaikka1 = [-2.23, 0.35, 2.9]
            kivi1.y = random.choice(kivenpaikka1)
            kivenpaikka2 = [-2.23, 0.35, 2.9]
            kivi2.y = random.choice(kivenpaikka2)


            if __name__ == '__main__':
                start = 1  # inclusive
                end = 4  # exclusive
                n = 1  # size
                track = random.choices(range(1, 4))
            #print(track)
            if track == [3]:
                finaltrack = -2.23
            if track == [2]:
                finaltrack = 0.35
            if track == [1]:
                finaltrack = 2.9
            self.y = finaltrack

        if kuolit == 1:
            poks = Audio('poks.mp3', pitch=1, loop=False, autoplay=True)
            if __name__ == '__main__':
                start = 1  # inclusive
                end = 4  # exclusive
                n = 1  # size
                track = random.choices(range(1, 4))
            #print(track)
            if track == [3]:
                time.sleep(2)
                finaltrack = -2.23
            if track == [2]:
                time.sleep(2)
                finaltrack = 0.35
            if track == [1]:
                time.sleep(2)
                finaltrack = 2.9
            self.y = finaltrack






    def input(self, key):
        if key=='down arrow':
            if self.rotation_z<15:
                self.rotation_z+=15
                #print ("käännyttiin suuntaan",self.rotation_z)

        if key=='up arrow':
            if self.rotation_z > -15:
                self.rotation_z-=15
                #print ("käännyttiin suuntaan", self.rotation_z)




#nuoliy = self.y



#kivi 1
kivi1 = Entity(model='quad',texture='kivi.png',position=(6.5,-2.23,-0.01),scale_y=1,scale_x=1,collider='box')
#kivi 2
kivi2 = Entity(model='quad',texture='kivi.png',position=(6.5,2.9,-0.01),scale_y=1,scale_x=1,collider='box')
#nuoli
nuoli = Entity(model='quad',texture='punainennuoli.png',position=(-6.4,0,-0.01), rotation_z=(180),scale_y=0.75,scale_x=1)


juna = juna(x, speed)

musiikki = Audio('WoodWhistles.mp3', pitch=1, loop=True, autoplay=True)



window.run()


