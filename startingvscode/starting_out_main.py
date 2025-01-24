#importing the pygame ( pygame can also be named as pg to keep it simple.)
import pygame as pg
import sys






#initalizes the pygame itself
pg.init()

#sets both the height and width of the display and sets it with the width and height
width = 1080
height = 720
# the display can also be set by numbers or strings like (720,1080) etc..
display = pg.display.set_mode((width, height))
##what font is set as
font = pg.font.Font(None, 36)
# what location
location = (500, 10)
#what color
color = (0, 185, 195)
# what text_surface it is
text_surface = font.render("minecraft", True, color)
#setting the title
pg.display.set_caption("my first go")
# displays the font
display.blit(text_surface, location)
# same thing for the title but for the button:
font_button = pg.font.Font(None, 13)

location_button =(200, 50)

color_button = (0, 255, 200)

text_surface_button_1 = font.render("after pressing escape, press ENTER to see what happens :)", True, color_button)

display.blit(text_surface_button_1, location_button)

#initals the sound/song mixer
pg.mixer.init()
#loads up the song/sound that needs to play
pg.mixer_music.load("music\CalmEmbrace.wav")
#sets the volume to the developers or users ckhoice
pg.mixer_music.set_volume(0.5)
#plays the music/sound
pg.mixer.music.play()

#game loop
 #set running to make a part of the loop
running = True

while running:

    
    #gets event of any type
    for event in pg.event.get():
        
        #gets the pygame quit function from the top right button is press
        if event.type == pg.QUIT:
            running = False
            
        ## event where the escape key is quitting
        elif event.type == pg.KEYDOWN:
            if event.key in (pg.K_RETURN, pg.K_ESCAPE):
                running = False
            

    #flip a part of a two to three frame dispay from the back to the front
    pg.display.flip()
    # update the display
    pg.display.update()

#quits the entire code
pg.quit()
sys.exit()