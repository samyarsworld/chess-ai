import pygame, sys
from button import Button
from const import *
from chess import Chess

pygame.init()

screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Menu")

# BG = pygame.image.load("assets/images/Background.png")

PLAYER = 'AI'
DIFFICULTY = 3
FONT_SIZE1 = 60
FONT_SIZE2 = 30


def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

    
def options():
    while True:
        screen.fill((0,0, 10))


        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        OPTIONS_TEXT = get_font(FONT_SIZE1).render("CHOOSE DIFFICULTY", True, "#5C1C81")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 100))

        EASY_BUTTON = Button(image=pygame.image.load("assets/images/Play Rect.png"), pos=(640, 220), 
                            text_input="EASY", font=get_font(FONT_SIZE2), base_color="#d7fcd4", hovering_color=(0, 255, 0))
        MEDIUM_BUTTON = Button(image=pygame.image.load("assets/images/Play Rect.png"), pos=(640, 340), 
                            text_input="MEDIUM", font=get_font(FONT_SIZE2), base_color="#d7fcd4", hovering_color=(0, 255, 0))
        HARD_BUTTON = Button(image=pygame.image.load("assets/images/Play Rect.png"), pos=(640, 460), 
                            text_input="HARD", font=get_font(FONT_SIZE2), base_color="#d7fcd4", hovering_color=(0, 255, 0))
        BACK_BUTTON = Button(image=pygame.image.load("assets/images/Play Rect.png"), pos=(640, 580), 
                            text_input="BACK", font=get_font(FONT_SIZE2), base_color="#d7fcd4", hovering_color=(0, 255, 0))
        
        for button in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON, BACK_BUTTON]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    main_class = Chess()
                    main_class.mainloop('AI', 1)

                if MEDIUM_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    main_class = Chess()
                    main_class.mainloop('AI', 2)
                
                if HARD_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    main_class = Chess()
                    main_class.mainloop('AI', 3)

                if BACK_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()
       

def main_menu():
    while True:
        screen.fill((10,0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(FONT_SIZE1).render("MAIN MENU", True, "#5C1C81")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/images/Play Rect.png"), pos=(640, 220), 
                            text_input="START", font=get_font(FONT_SIZE2), base_color="#d7fcd4", hovering_color=(0, 255, 0))

        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/images/Play Rect.png"), pos=(640, 340), 
                            text_input="PLAY VS AI", font=get_font(FONT_SIZE2), base_color="#d7fcd4", hovering_color=(0, 255, 0))

        PLAYER_BUTTON = Button(image=pygame.image.load("assets/images/Options Rect.png"), pos=(640, 460), 
                            text_input="PLAY VS PLAYER", font=get_font(FONT_SIZE2), base_color="#d7fcd4", hovering_color=(0, 255, 0))
        
        QUIT_BUTTON = Button(image=pygame.image.load("assets/images/Quit Rect.png"), pos=(640, 580), 
                            text_input="QUIT", font=get_font(FONT_SIZE2), base_color="#d7fcd4", hovering_color=(0, 255, 0))

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, PLAYER_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_class = Chess()
                    main_class.mainloop(PLAYER, DIFFICULTY)

                if PLAYER_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_class = Chess()
                    main_class.mainloop('human', '')

                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == '__main__':
    main_menu()