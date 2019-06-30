import pygame.font #render text to screen

class Button():

    def __init__(self, ai_settings, screen, msg): #msg contains text for button
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 200, 50 #button dimensiont
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48) #none: uses default,size of text - 48

        self.rect = pygame.Rect(0, 0, self.width, self.height) #buttons rect
        self.rect.center = self.screen_rect.center #center button on screen
        self.prep_msg(msg) #button message witch is following:

    def prep_msg(self, msg):
        #turn text (msg) into a image and center text on the button
        # image is stored in msg_image
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color) #font render  turns text to image
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect) #draws the button on the screen