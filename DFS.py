import pygame



WIDTH = 700
screen = pygame.display.set_mode((WIDTH , WIDTH))
pygame.display.set_caption("BFS Algorithm Visualizer")

LIGHT_GREEN = (128, 255, 128)
DARK_GREEN = (0, 153, 51)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
OBSCOLOR = (0, 38, 51)
PURPLE = (255, 77, 196)
ORANGE_RED = (255, 69, 0)
GREY = (128, 128, 128)
DODGER_BLUE = (30, 144, 255)

class spot:
    def __init__(self,row,col,width,total_row):
        self.row=row
        self.col=col
        self.width=width
        self.x=width*row
        self.y=width*col
        self.total_row=total_row
        self.color=WHITE
        self.neighbours=[]


    def get_pos(self):
        return self.row,self.col
    def is_start(self):
        return self.color == ORANGE_RED
    def is_end(self):
        return self.color == DODGER_BLUE
    def is_barrier(self):
        return self.color == OBSCOLOR
    def is_closed(self):
        return self.color == LIGHT_GREEN
    def is_open(self):
        return self.color == DARK_GREEN


    def reset(self):
        self.color=WHITE

    def make_start(self):
        self.color=ORANGE_RED
    def make_end(self):
        self.color=DODGER_BLUE
    def make_barrier(self):
        self.color=OBSCOLOR
    def make_path(self):
        self.color=PURPLE
    def make_open(self):
        self.color=DARK_GREEN
    def make_closed(self):
        self.color=LIGHT_GREEN

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.width))
    def update_neighbours(self,grid):
        self.neighbours=[]
        if self.row<self.total_row-1 and not grid[self.row+1][self.col].is_barrier():#down
            self.neighbours.append(grid[self.row+1][self.col])

        if self.row>0 and not grid[self.row-1][self.col].is_barrier():#up
            self.neighbours.append(grid[self.row-1][self.col])

        if self.col>0 and not grid[self.row][self.col-1].is_barrier():#left
            self.neighbours.append(grid[self.row][self.col-1])

        if self.col<self.total_row-1 and not grid[self.row][self.col+1].is_barrier():#right
            self.neighbours.append(grid[self.row][self.col+1])



    def __lt__(self, other):
        return False


def h(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return abs(x1-x2)+abs(y2-y1)


def redraw_path(current,draw,start):
    while current in parent_node:
        current=parent_node[current]
        current.make_path()
        draw()
    start.make_start()
    draw()

visited=[]
parent_node={}
def DFS(draw,grid,start,end,visited,current):


   visited.append(current)
   current.make_open()
   for u in current.neighbours:
           for event in pygame.event.get():
               if event.type==pygame.QUIT:
                   pygame.quit()



           if u==end:
                    print("end reached")
                    parent_node[u]=current
                    redraw_path( end, draw, start)
                    return True



           if u  not in visited:
               parent_node[u]=current
               x=  DFS(draw,grid,start,end,visited,u)
               if x==True:
                   return True

           draw()

           if u != start:
               u.make_closed()

   current.make_closed()
   return False










def make_grid(rows,width):
    gap=width//rows
    grid=[]
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            a = spot(i,j,gap,rows)
            grid[i].append(a)

    return grid

def draw_grid(screen,rows,width):
    gap=width//rows
    for i in range(rows):
        pygame.draw.line(screen,GREY,(0,i*gap),(width,i*gap))
        pygame.draw.line(screen,GREY,(i*gap,0),(i*gap,width))

def draw(screen,grid,rows,width):
    screen.fill(WHITE)

    for i in range(rows):
        for j in range(rows):
            grid[i][j].draw(screen)



    draw_grid(screen,rows,width)
    pygame.display.update()

def get_row_col_pos(rows,width,pos):
    y,x=pos
    gap=width//rows

    row=y//gap
    col=x//gap
    return row,col


def main(screen,WIDTH):
    ROWS=35
    grid=make_grid(ROWS,WIDTH)

    start=None

    end=None

    run=True
    while run:
        draw(screen,grid,ROWS,WIDTH)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run =False
            if pygame.mouse.get_pressed()[0]:#left mouse button
                pos=pygame.mouse.get_pos()
                row,col=get_row_col_pos(ROWS,WIDTH,pos)
                block=grid[row][col]
                print(row,col)
                if not start and block!=end:
                    start=block
                    start.make_start()
                elif not end and block!=start:
                    end=block
                    end.make_end()
                elif block!=start and block!=end:
                    block.make_barrier()


            elif pygame.mouse.get_pressed()[2]:#right mouse button
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_pos(ROWS, WIDTH, pos)
                block = grid[row][col]
                block.reset()
                if block==start:
                    start=None
                elif block==end:
                    end=None

            if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_SPACE and start and end:
                   for row in grid:
                       for block in row:
                           block.update_neighbours(grid)


                   current=start



                   DFS(lambda :draw(screen,grid,ROWS,WIDTH),grid,start,end,visited,current)

               if event.key==pygame.K_ESCAPE:
                   start=None
                   end=None
                   grid=make_grid(ROWS,WIDTH)


if __name__=="__main__":
    main(screen,WIDTH)