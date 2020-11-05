'''
Pygame test
80/30/2019
https://pythonprogramming.net/pygame-python-3-part-1-intro/
'''
import pygame                                                   #Import the pygame module

pygame.init()                                                   #Intitiate pygame (required for every pygame)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height)) #Sets up the canvas
pygame.display.set_caption('A bit Racey')                       #Names the canvas

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()                                     #the clock tracks time in the game and sets the fps for the game
carImg = pygame.image.load('racecar.png')                       #The racecar in the game

#Crashed variable logs if the player looses
crashed = False

def car(x,y):                                                   #Car draws the car on the screen. Blit draws the image on the screen
    gameDisplay.blit(carImg, (x,y))

x =  (display_width * 0.45)                                     #X an Y use the width and height to determinwe th xy position of the car
y = (display_height * 0.8)

while not crashed:                                              #this loop runs until the player looses (crashed)

    #This tells that if the player quits the game, they loose
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            
        #Uses the arrow keys to move the kare +5 or -5
        if event.type == pygame.KEYDOWN:                        #Asks if a key is being presses
            if event.key == pygame.K_LEFT:                      #If the left key is pressed, move -5 on the x-axis
                x_change = -5
            elif event.key == pygame.K_RIGHT:                   #If the right key is pressed, move +5 on the x-axis
                x_change = 5
        if event.type == pygame.KEYUP:                          #If a key is released, the change is zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

    x += x_change                                               #The current x position is equal to the position of the current plus the new one

    gameDisplay.fill(white)                                     #Adds the screen color using our previos color variables
    car(x,y)                                                    #Draws the car based on the previous x, y variables
    
    pygame.display.update()                                     #This updates certain parts of the screen every frame
    clock.tick(60)                                              #the clock runs at 50 fps

pygame.quit                                                     #Ends pygame instance
quit()                                                          #exits python and application
