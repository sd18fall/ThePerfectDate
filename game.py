"""
MetaGame
An interactive video cd ~
game!

Authors: Cynthia Yong, Sabrina Pereira, Sophie Schaffer
"""
import pygame

pygame.init()
win = pygame.display.set_mode((800,600))
win.fill((43, 226, 229))


class TextBox():
    """needs to accept dimensions, color, text, location """

    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)

        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)

        if self.text != '':
            #Set font and size of button text, display centered
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def __repr__(self):
        return self.text

class Button(TextBox):
    """Child to text box,
    on screen and where it leads"""

    def isOver(self,pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] < self.y + self.height:
                    #print('WOW')
                    return True
            return False

    def isClick(self):
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('CLICK')
                if self.isOver(pos):
                    print('OVER')
                    return True
        else:
            return False

class State():
    """stores all the information of what has already happened"""
    def __init__(self, level, inventory, location):
        self.level = level
        self.inventory = inventory
        self.location = location

    def __str__(self):
        return "Level: " + str(self.level)+", Inventory: "+ str(self.inventory) + ", Location: "+str(self.location)

class Room():
    """needs to accept name, picture, artifacts"""
    def __init__(self, name, picture, artifacts):
        self.name = name
        self.picture = picture
        self.artifacts = artifacts

class Artifact():
    """needs to accept name, description, picture"""
    def __init__(self, location, name, description, picture):
        self.name = name
        self.description = description
        self.picture = picture

#class Screen():

# def screengenerator(i=0):
#     """
#     Generates and displays buttons with a question and its corresponding answer choices.
#     Takes in the index for the desired question from the question list qlist.
#     Returns a list of the generated button objects for the answer choices.
#     """
#     win.fill((43, 226, 229))
#
#     question = qlist[i].message
#     questionbutton = button((184, 231, 242),225,150,150, 75, question)
#     questionbutton.draw(win, (0,0,0))
#
#     buttonlist = []
#     incrementx = 0
#     for choice in qlist[i].choices:
#         b = button((184, 231, 242), 100 + incrementx, 300, 100, 75, choice)
#         buttonlist.append(b)
#         b.draw(win, (0,0,0))
#         incrementx += 150
#     return buttonlist

# def display(dictkey):
#     """clears last display and puts up what should currently be on the screen"""
#     win.fill((43, 226, 229))
#
#     newScreen = ItemDictionary(dictkey)
#         for item in newScreen:
#             button()






        # question = qlist[i].message
        # questionbutton = button((184, 231, 242),225,150,150, 75, question)
        # questionbutton.draw(win, (0,0,0))
        #
        # buttonlist = []
        # incrementx = 0
        # for choice in qlist[i].choices:
        #     b = button((184, 231, 242), 100 + incrementx, 300, 100, 75, choice)
        #     buttonlist.append(b)
        #     b.draw(win, (0,0,0))
        #     incrementx += 150
        # return buttonlist


a = Button((255,255,255),100,100,250,250, text='I am a, I go to b')
b = Button((255,255,255),100,100,250,250, text='i AM B I GO TO A')
ItemDictionary = {a : b, b: a}

win.fill((0,0,0))

while True:
    pygame.display.update()
    for event in pygame.event.get():

        a.draw(win,(0,0,0))
        if a.isClick() == True:
            print('draw')
            b.draw(win,(0,0,0))


        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

while Middle:
    buttonlist = buttongenerator(i)
    pygame.display.update()

    if Dog_list == []:
        Middle = False
        SadEnd = True

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        #Advances to next question if the user clicks on an answer choice, proceeds to end sequence if finished of if no dogs are applicable
        if event.type == pygame.MOUSEBUTTONDOWN:
            for b in buttonlist:
                if b.isOver(pos):
                    user_input = b.text
                    filter_doglist(user_input, Dog_list, qlist[i].name)
                    if i < len(qlist):
                        i += 1
                        if i == len(qlist):
                            Middle = False
                            if Dog_list == []:
                                SadEnd = True
                            else:
                                End = True
