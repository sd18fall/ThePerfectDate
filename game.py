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
            font = pygame.font.SysFont('comicsans', 21)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def __repr__(self):
        return self.text

class Button(TextBox):
    """Child to text box,
    on screen and where it leads"""

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

# def buttongenerator(i=0):
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

def display():
    """clears last display and puts up what should currently be on the screen"""
