import pygame
import A_star
import BFS
import DFS
pygame.init()
WIDTH = 700
screen = pygame.display.set_mode((WIDTH , WIDTH))
pygame.display.set_caption("ALGORITHMS VISUALIZER")

class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win,text=''):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 40)
            text = font.render(self.text, 1, (152, 111, 233))
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


def draw(screen,A_STAR_BUTTON,DFS_BUTTON,BFS_BUTTON):
    screen.fill((255,255,255))
    A_STAR_BUTTON.draw(screen)
    DFS_BUTTON.draw(screen)
    BFS_BUTTON.draw(screen)

def MAIN(screen):
     run =True

     A_STAR_BUTTON=button((183,178,193), 100, 50, 500, 100,'A STAR ALGORITHM')
     DFS_BUTTON=button((183,178,193),100,200,500,100,'DFS ALGORITHM')
     BFS_BUTTON=button((183,178,193),100,350,500,100,'BFS ALGORITHM')
     while run:
         draw(screen,A_STAR_BUTTON,DFS_BUTTON,BFS_BUTTON)

         for event in pygame.event.get():
               pos=pygame.mouse.get_pos()
               if event.type==pygame.QUIT:
                   run=False
                   pygame.quit()
                   quit()


               if A_STAR_BUTTON.isOver(pos):
                   A_STAR_BUTTON.color = (70, 195, 66)
               else:
                   A_STAR_BUTTON.color = (183, 178, 193)

               if DFS_BUTTON.isOver(pos):
                   DFS_BUTTON.color = (70, 195, 66)
               else:
                   DFS_BUTTON.color = (183, 178, 193)
               if BFS_BUTTON.isOver(pos):
                   BFS_BUTTON.color = (70, 195, 66)
               else:
                   BFS_BUTTON.color = (183, 178, 193)

               if event.type == pygame.MOUSEBUTTONDOWN:
                   if A_STAR_BUTTON.isOver(pos):
                       A_STAR_BUTTON.color=(70,195,66)
                       A_star.start(screen,WIDTH)
                       break
                   else:
                       A_STAR_BUTTON.color =(183,178,193)

                   if DFS_BUTTON.isOver(pos):
                       DFS_BUTTON.color = (70, 195, 66)
                       DFS.main(screen,WIDTH)
                       break
                   else:
                       DFS_BUTTON.color = (183, 178, 193)

                   if BFS_BUTTON.isOver(pos):
                       BFS_BUTTON.color = (70, 195, 66)
                       BFS.main(screen,WIDTH)
                   else:
                       BFS_BUTTON.color = (183, 178, 193)

         pygame.display.flip()


MAIN(screen)