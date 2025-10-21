from pygame import *


win_width = 700
win_height = 500
display.set_caption("Ping-Pong")
window = display.set_mode((win_width, win_height))


class GameSprite(sprite.Sprite):
    # class constructor
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # call for the class (Sprite) constructor:
        sprite.Sprite.__init__(self)

        # every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # every sprite must have the rect property that represents the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def update_ball(self):
        self.rect.x -= self.speed
        self.rect.y -= self.speed


    # method rawing the character on the window
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    # method to control the sprite with arrow keys
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 495:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 495:
            self.rect.y += self.speed

#create the elements of the game
player_1 = Player('actual_pong_bar.png', 150,150, 350, 100, 5)
player_2 = Player('actual_pong_bar.png', 350,350, 350, 100, 5)
ball = GameSprite("add_ball.png", 250, 250, 50, 50, 5) 

run = True
clock = time.Clock()
FPS = 60
speed = 5

while run:
    #carachter introduction in the loop
    player_1.update()
    player_2.update2()
    #carachter update per loop
    player_1.reset()
    player_2.reset()
    ball.update_ball()
    ball.reset()
    for e in event.get():  
        if e.type == QUIT:
            run = False

    display.update()
    clock.tick(FPS)
