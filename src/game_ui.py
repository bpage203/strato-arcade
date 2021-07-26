class Game_UI:
    def __init__(self):
        self.dic_arrows = {}
        self.dic_buttons = {}
        self.dic_responses = {}
        self.homeScreen_images = []
        self.arrow_locations = {}
        self.button_locations = {}
        self.logo_locations = {}


    # Setter functions

    def set_homeScreenImages(self):
        pic_names = []
        for filename in glob.iglob('front-end\spiral\**'):
            pic_names.append(filename)
        for x in pic_names:
            self.homeScreen_images.append(pygame.image.load(x))

    def set_buttons(self):
        self.dic_buttons['single'] = pygame.image.load(r'front-end\buttons\single_button.png')
        self.dic_buttons['double'] = pygame.image.load(r'front-end\buttons\double.png')
        self.dic_buttons['start'] = pygame.image.load(r'front-end\buttons\start.png')
        self.dic_buttons['easy'] = pygame.image.load(r'front-end\buttons\easy.png')
        self.dic_buttons['hard'] = pygame.image.load(r'front-end\buttons\hard.png')


    def set_arrows(self):
        # Arrows needed for a single player 
        self.dic_arrows['left_gray1'] = pygame.image.load(r'front-end\arrows\left_gray.png')
        self.dic_arrows['right_gray1'] = pygame.image.load(r'front-end\arrows\right_gray.png')
        self.dic_arrows['up_gray1'] = pygame.image.load(r'front-end\arrows\up_gray.png')
        self.dic_arrows['down_gray1'] = pygame.image.load(r'front-end\arrows\down_gray.png')
        self.dic_arrows['left_blue1'] = pygame.image.load(r'front-end\arrows\left_blue.png')
        self.dic_arrows['right_blue1'] = pygame.image.load(r'front-end\arrows\right_blue.png')
        self.dic_arrows['up_blue1'] = pygame.image.load(r'front-end\arrows\up_blue.png')
        self.dic_arrows['down_blue1'] = pygame.image.load(r'front-end\arrows\down_blue.png')
        # Arrows needed for two players
        self.dic_arrows['left_gray2'] = pygame.image.load(r'front-end\arrows\left_gray.png')
        self.dic_arrows['right_gray2'] = pygame.image.load(r'front-end\arrows\right_gray.png')
        self.dic_arrows['up_gray2'] = pygame.image.load(r'front-end\arrows\up_gray.png')
        self.dic_arrows['down_gray2'] = pygame.image.load(r'front-end\arrows\down_gray.png')
        self.dic_arrows['left_blue2'] = pygame.image.load(r'front-end\arrows\left_blue.png')
        self.dic_arrows['right_blue2'] = pygame.image.load(r'front-end\arrows\right_blue.png')
        self.dic_arrows['up_blue2'] = pygame.image.load(r'front-end\arrows\up_blue.png')
        self.dic_arrows['down_blue2'] = pygame.image.load(r'front-end\arrows\down_blue.png')
    

    def set_responses(self):
        self.dic_responses['excellent'] = pygame.image.load(r'front-end\responses\excellent.png')
        self.dic_responses['good'] = pygame.image.load(r'front-end\responses\good.png')
        self.dic_responses['great'] = pygame.image.load(r'front-end\responses\great.png')
        self.dic_responses['miss'] = pygame.image.load(r'front-end\responses\miss.png')
        self.dic_responses['perfect'] = pygame.image.load(r'front-end\responses\perfect.png')

    # Getter functions
    def get_responses(self):
        return self.dic_responses

    def get_buttons(self):
        return self.dic_buttons

    def get_arrows(self):
        return self.dic_arrows

    def get_homeScreenImages(self):
        return self.homeScreen_images
    