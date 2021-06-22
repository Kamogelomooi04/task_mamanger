# This is my first game.
# The game contains a player character, 3 enemy characters and a prize character.
# The objective is for the user to try get the player character to the prize character. 
# If the user manages to do so, then they win.
# However to make it a tiny bit of a challenge there are 3 enemy characters
# moving towards the player character at different positions.
# If the the player character the collides with any of the enemies, then the user loses.

import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers. 
import os     # Operating system to help define the path to the images used.
pygame.font.init() # Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.
# This here is the width and height of the screen the game will appear on.

screen_width = 1040
screen_height = 680

screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.
pygame.display.set_caption("My First game!!") # This create a heading or title for the game on the top of our screen.
black = (0, 0, 0) # The colour black
green = (0, 255, 0) # The colour green

# This here is the code for the text that will appear on the screen.
# Text will appear if the user wins or if the user loses the game.
# In the arguments there is the type of font and the size of the text.
# The other arguments contain the text that will appear and the colour that the text will be on the screen.

loser_font_type = pygame.font.SysFont("comicsans", 100)
winner_font_type = pygame.font.SysFont("comicsans", 100)
loser_text = loser_font_type.render("You Lose!", 1, green)
winner_text = winner_font_type.render("You Win!", 1, green)

# In this section of code we defining the characters that will be in the game.

# Here we have the player character, we have given it a variable name and then we add the directory 
# so that the program can go grab the image of the player character from its location so it can be displayed on the game screen.
# In the second line of code we are just resizing the image of the player character to our preference.
# In this section of code we do the same for all the game characters.
player = pygame.image.load(os.path.join("Desktop", "player.jpg"))
player = pygame.transform.scale(player, (66, 50))

prize = pygame.image.load(os.path.join("Desktop", "cherry.jpg"))
prize = pygame.transform.scale(prize, (66, 50))

enemy = pygame.image.load(os.path.join("Desktop", "enemy.png"))
enemy = pygame.transform.scale(enemy, (90, 80))

enemy_two = pygame.image.load(os.path.join("Desktop", "enemy.png"))
enemy_two = pygame.transform.scale(enemy_two, (66, 50))

enemy_three = pygame.image.load(os.path.join("Desktop", "enemy.png"))
enemy_three = pygame.transform.scale(enemy_three, (66, 50))

background_window = pygame.image.load(os.path.join("Desktop", "background.jpg"))
background_window = pygame.transform.scale(background_window, (1040, 680))


# Here we are getting the width and height of the images in order to do boundary detection 
# to make sure the images of the game characters stay within screen boundaries or know when the image is off the screen).

image_height = player.get_height()
image_width = player.get_width()

enemy_height = enemy.get_height()
enemy_width = enemy.get_width()

enemy_two_height = enemy_two.get_height()
enemy_two_width = enemy_two.get_width()

enemy_three_height = enemy_three.get_height()
enemy_three_width = enemy_three.get_width()

# Here we storing the positions of the player character, prize character and
# enemy characters as variables so that they can be changed later.

playerXPosition = 100
playerYPosition = 50

prizeXPosition = 900
prizeYPosition = 600


# In this section of code we are making all the enemy characters start off the game screen 
# and appear from the side of the game screen at a random y position.

enemyXPosition =  screen_width
enemyYPosition =  random.randint(0, screen_height - enemy_height)

enemy_twoXPosition = screen_width
enemy_twoYPosition = random.randint(0, screen_height - enemy_height)

enemy_threeXPosition = screen_width
enemy_threeYPosition = random.randint(0, screen_height - enemy_height)

# This checks if the up or down key is pressed.
# Right now they are not so they are equal to the boolean value of False. 
 
keyUp= False
keyDown = False
keyLeft = False
keyRight = False 

# This is the game loop.
# This game loop will run the game logic over and over again.
# This game looping structure that will loop the indented code until it is instructed to stop
# in the event where the user exits the program by quitting). 
# In Python the int 1 has the boolean value of 'true'. 



while 1: 
    # This bit of code draws on all the things we would like to appear on the game screen.
    # In this case it will be the game background,
    # the player character, the prize character and the enemy chracters.
    # We enter what we would like to draw on th screen and the position at which we would like it to appear on the screen
    screen.fill(black)
    screen.blit(background_window, (0, 0))
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(enemy_two,(enemy_twoXPosition, enemy_twoYPosition))
    screen.blit(enemy_three,(enemy_threeXPosition, enemy_threeYPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    
 

    pygame.display.flip()# This updates the screen. 
    
    # Here we have a for loop inside of our while loop.
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            
        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Tests if the key pressed is the one we want.
            # pygame.K_UP represents a keyboard key constant. 
            # If the specific key is presed by the user 
            # then we want to set that key to the boolean value of True.

            if event.key == pygame.K_UP:  
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True      
        
        # This event checks if the key is up, in other words, if it is not pressed by the user.
        
        if event.type == pygame.KEYUP:
        
            # Tests if the key released is the one we want.
            # If a specific key is not being pressed by the user 
            # then we want to set that key  to the boolean value of False.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False

            
    # After events are checked for in the for loop above and values are set,
    # we want to check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position. 
    # This means that if you want the player to move up you will have to decrease the y position.
    # This means that if you want the player to move to the left you will have to decrease the x position.
    # This means that if you want the player to move to the right you will hae to increase the x position.

    if keyUp == True:
        if playerYPosition > 0: # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height: # This makes sure that the user does not move the player below the window.
            playerYPosition += 1
    if keyLeft == True:
        if playerXPosition < screen_height - image_height: 
            playerXPosition -= 1
    if keyRight == True:
        if playerXPosition < screen_width - image_width:         
            playerXPosition += 1

    # In this next chunk of code we want to check for collision of the enemy characters with the player character.
    # To do this we put bounding boxes around the images of the player character and enemy characters.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player character:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # Bounding box for the prize character:

    prizeBox = pygame.Rect(prize.get_rect())

    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    
    # Bounding box for the enemy characters:
    
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    enemy_twoBox = pygame.Rect(enemy_two.get_rect())
    enemy_twoBox.top = enemy_twoYPosition
    enemy_twoBox.left = enemy_twoXPosition
    
    enemy_threeBox = pygame.Rect(enemy_three.get_rect())
    enemy_threeBox.top = enemy_threeYPosition
    enemy_threeBox.left = enemy_threeXPosition
    
    # This if-statement tests for collisions of the bounding boxes:
    # If the player bounding box collides with the enemy bounding box
    # a 'You Lose!' message will appear on the screen for aboutt 3 seconds.
    # Then the game will be stopped and exited.
    if playerBox.colliderect(enemyBox):
        screen.blit(loser_text, (400, 250))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        exit(0)
        
        
        
        
    # This if-statement tests for collisions of the bounding boxes:
    # If the player bounding box collides with the enemy bounding box
    # a 'You Lose!' message will appear on the screen for aboutt 3 seconds.
    # Then the game will be stopped and exited.
    if playerBox.colliderect(enemy_twoBox):
        screen.blit(loser_text, (400, 250))
        pygame.display.update() 
        pygame.time.delay(3000)
        pygame.quit()
        exit(0)
            
    # This if-statement tests for collisions of the bounding boxes:
    # If the player bounding box collides with the enemy bounding box
    # a 'You Lose!' message will appear on the screen for aboutt 3 seconds.
    # Then the game will be stopped and exited.
    if playerBox.colliderect(enemy_threeBox):
        screen.blit(loser_text, (400, 250))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        exit(0)
            
    # This if-statement tests for collisions of the bounding boxes:
    # If the player bounding box collides with the prize bounding box
    # a 'You Win!' message will appear on the screen for aboutt 3 seconds.
    # Then the game will be stopped and exited.     
    if playerBox.colliderect(prizeBox):
        screen.blit(winner_text, (400, 250))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        exit(0)
    

        
    # This last bit of code makes the enemy characters approach the player character.
    
    enemyXPosition -= 0.15
    enemy_twoXPosition -= 0.07
    enemy_threeXPosition -= 0.10
    # ================The game loop logic ends here. =============
  
