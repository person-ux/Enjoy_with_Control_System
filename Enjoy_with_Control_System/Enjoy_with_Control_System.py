import math
import pygame
import pygame.gfxdraw
from pygame.locals import *

pygame.init()

WIN_SIZE=(800,500)
WIN=pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption("Enjoy_with_Control_System")
score_font=pygame.font.Font('freesansbold.ttf',32)
clock=pygame.time.Clock()

BLACK  = (0,0,0)
WHITE  = (255,255,255)
RED    = (255,0,0)
GREEN  = (0,255,0)
BLUE   = (0,0,255)

circles=[[40,250,0],[120,250,0],[200,250,0],[280,250,0],[360,250,0],[440,250,0]]
answer=[["01","12","23","31"],["01","12","23","34","41","21"],["01","12","23","34","45","41","21","54"]]
temps=[0,0,0,0,0,0]
myans=[]
level=1
score=0

def Draw():
    ######################Draw Nodes#############################
    for i in circles:
        if i[2]==1:
            pygame.gfxdraw.filled_circle(WIN,i[0],i[1],20,BLACK)
        else:
            pygame.gfxdraw.circle(WIN,i[0],i[1],20,BLACK)
    ###########################Score/Highscore#####################################
    score_print=score_font.render("Score: "+str(score),True,(255,50,100))
    WIN.blit(score_print,(0,0))

def score_calc(time):
    global score
    global highscore
    score=score+(10000//time)

def win_check():
    global myans
    global score
    global level
    ans_sub=level-1
    if len(myans)==len(answer[ans_sub]):
        myans_len=len(myans)
        for i in myans:
            if i in answer[ans_sub]:
               temps[2]+=1
            else: break

        if temps[2]==myans_len:
            myans=[]
            level+=1
            score_calc(temps[4])
            temps[2],temps[4]=0,0
        else:
            myans=[]
            level+=1
            if score>=4: score= score-4
            temps[2],temps[4]=0,0

def collision(mouse_x,mouse_y):
    global temps
    global myans
    global circles
    nodes=len(circles)
    for i in range(nodes):
        Dis=math.sqrt((math.pow(mouse_x-circles[i][0],2))+(math.pow(mouse_y-circles[i][1],2)))
        if Dis<=20:
            temps[0]+=1
            circles[i][2]=1
            if temps[0]==2:
                temps[1]=temps[1]+i
                if temps[1]==1: myans.append("01")
                else: myans.append(str(temps[1]))
                temps[0],temps[1]=0,0
            else:
                temps[1]=i*10

################################ MAIN ######################################
def main():  
    global temps
    global myans
    global circles
    global score_font
    show_img=True
    run=True
    
    while run:
        clock.tick(60)
        WIN.fill(WHITE)
        mouse_x,mouse_y= pygame.mouse.get_pos()

        if level>temps[5]:
            show_img=True
            temps[5]=level
            image=str(level)+".png"
            qus=pygame.image.load(image)
            for i in range(len(circles)): circles[i][2]=0

        ###############Show qustion###################
        while(show_img):
            clock.tick(60)
            WIN.blit(qus,(0,0))
            score_print=score_font.render("Score: "+str(score),True,(255,50,100))
            WIN.blit(score_print,(0,0))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run,show_img=False,False
                if event.type==MOUSEBUTTONDOWN:
                    if event.button==1:
                        show_img=False
                        WIN.fill(WHITE)
            pygame.display.update()
        #############################################
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False

            if event.type==MOUSEBUTTONDOWN:
                if event.button==1:
                    collision(mouse_x,mouse_y)
                    
        if temps[4]<5000:
            temps[4]+=1

        win_check()
        Draw()
        pygame.display.update()

        if level>3:
            score_font=pygame.font.Font('freesansbold.ttf',40)
            while run:
                WIN.fill(WHITE)
                score_print=score_font.render("Your Score: "+str(score),True,(255,50,100))
                WIN.blit(score_print,(100,200))
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        run=False
                pygame.display.update()
    pygame.quit()
############################################################################
if __name__ == "__main__":
    main()
