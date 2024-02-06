# Below you will find a list containing the names of colors, such as blue, red, white and so on.
# Your job is to figure out who is hiding in that image, to do you you must transform the list into a list of rgb values
# eg. ['white','white'] => [[255,255,255],[255,255,255]]  
# use https://holdtemp.github.io/ to check your answers

secret_img = ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 
'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'dark_orange', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 
'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'dark_orange', 'blue', 'black', 'yellow', 'dark_orange', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'yellow', 'dark_orange', 'black', 'yellow', 'dark_orange', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 
'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'yellow', 'black', 'yellow', 'dark_orange', 'orange', 'yellow', 'dark_orange', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'dark_orange', 'dark_orange', 'dark_orange', 'dark_orange', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'yellow', 'yellow', 'black', 'yellow', 'dark_orange', 'dark_orange', 'dark_orange', 'dark_orange', 'dark_orange', 'dark_orange', 'dark_orange', 'blue', 'blue', 'dark_orange', 'dark_orange', 'yellow', 'yellow', 'yellow', 'black', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'yellow', 'yellow', 'black', 'yellow', 'dark_orange', 'dark_orange', 'dark_orange', 'dark_orange', 'dark_orange', 'dark_orange', 'dark_orange', 'blue', 'blue', 'dark_orange', 'dark_orange', 'yellow', 'yellow', 'yellow', 'black', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'light_grey', 'light_grey', 'black', 'black', 'black', 'dark_orange', 'orange', 'yellow', 'black', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'dark_orange', 'dark_orange', 'yellow', 'white', 'white', 'dark_orange', 'yellow', 'black', 'blue', 'blue', 'blue', 'blue', 'blue', 'light_grey', 'white', 'white', 'white', 'white', 'light_grey', 'black', 'black', 'dark_orange', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'white', 'white', 'dark_orange', 'yellow', 'dark_orange', 'blue', 'blue', 'blue', 'blue', 'blue', 'light_grey', 'white', 'white', 'light_grey', 'white', 'white', 'white', 'black', 'yellow', 'black', 'yellow', 'yellow', 'black', 
'black', 'white', 'white', 'black', 'black', 'yellow', 'yellow', 'dark_orange', 'white', 'dark_orange', 'yellow', 'black', 'blue', 'blue', 'blue', 'blue', 'light_grey', 'white', 'white', 'white', 'light_grey', 'white', 'white', 'white', 'black', 'black', 'black', 'yellow', 'dark_orange', 'white', 'white', 'white', 'white', 'white', 'white', 'dark_orange', 'dark_orange', 'yellow', 'dark_orange', 'yellow', 'dark_orange', 'blue', 'blue', 'blue', 'blue', 'blue', 'light_grey', 'white', 'white', 'white', 'white', 'light_grey', 'light_grey', 'black', 'black', 'blue', 'black', 'yellow', 'white', 'white', 'cyan', 'white', 'white', 'cyan', 'white', 'white', 'white', 'yellow', 'yellow', 'yellow', 'black', 'blue', 'blue', 'blue', 'blue', 'blue', 'light_grey', 'white', 'light_grey', 'white', 'white', 'black', 'black', 'white', 'white', 'black', 'black', 'yellow', 'white', 'white', 'black', 'yellow', 'yellow', 'black', 'white', 'white', 'white', 'yellow', 'yellow', 'black', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'light_grey', 'white', 'white', 'light_grey', 'black', 'white', 'white', 'white', 'black', 'black', 'dark_grey', 'dark_orange', 'white', 'white', 'blue', 'black', 'white', 'blue', 'white', 'white', 'white', 'yellow', 'dark_orange', 'black', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'black', 'black', 'light_grey', 'black', 'black', 'black', 'white', 'black', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'yellow', 'black', 'black', 'black', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'white', 'white', 'white', 'white', 'black', 'black', 'black', 'white', 'white', 'white', 'dark_red', 'red', 'red', 'dark_red', 'white', 'dark_orange', 'dark_orange', 'dark_orange', 'white', 'white', 'light_grey', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'black', 'black', 'yellow', 'yellow', 'black', 'white', 'white', 'white', 'white', 'dark_red', 'red', 'red', 'dark_red', 'white', 'white', 'white', 'white', 'white', 'light_grey', 'blue', 'blue', 
'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'yellow', 'yellow', 
'black', 'dark_grey', 'white', 'white', 'dark_red', 'red', 'red', 'dark_red', 'white', 'white', 'white', 'white', 'black', 'black', 'black', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'yellow', 'yellow', 'black', 'black', 'light_grey', 'white', 'dark_red', 'red', 'red', 'dark_red', 'white', 'white', 'white', 'light_grey', 'dark_grey', 'dark_grey', 'black', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'yellow', 'yellow', 'black', 'black', 'dark_grey', 
'dark_red', 'dark_red', 'dark_red', 'white', 'white', 'light_grey', 'light_grey', 'black', 'white', 'white', 'light_grey', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'dark_orange', 'yellow', 'yellow', 'black', 'dark_grey', 'dark_grey', 'black', 'black', 'black', 'black', 'black', 'white', 'light_grey', 'white', 'white', 'light_grey', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'black', 'yellow', 'white', 'white', 'white', 'white', 'black', 'orange', 'black', 'black', 'light_grey', 'white', 'white', 'white', 'light_grey', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'dark_orange', 'dark_orange', 'black', 'yellow', 'white', 'white', 'white', 'white', 'black', 'black', 'white', 'white', 'light_grey', 'light_grey', 
'white', 'white', 'light_grey', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'dark_orange', 'orange', 'yellow', 'black', 'yellow', 'white', 'white', 'white', 'white', 'black', 'black', 'white', 'white', 'black', 'white', 'white', 'white', 'light_grey', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'black', 'dark_orange', 'yellow', 'yellow', 'yellow', 'black', 'yellow', 'white', 
'white', 'white', 'white', 'black', 'orange', 'black', 'black', 'black', 'white', 'white', 'white', 'black', 'blue', 
'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'black', 'orange', 'yellow', 'yellow', 'yellow', 'black', 'yellow', 'light_grey', 'white', 'white', 'black', 'orange', 'black', 'black', 'black', 'yellow', 'black', 'black', 'black', 'light_grey', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'white', 'white', 'yellow', 'yellow', 'yellow', 'yellow', 'black', 'yellow', 'black', 'dark_orange', 'black', 'orange', 'orange', 'black', 'white', 'white', 'black', 'yellow', 'yellow', 'white', 'white', 'light_grey', 'blue', 'blue', 'blue', 
'blue', 'blue', 'blue', 'blue', 'black', 'white', 'white', 'yellow', 'yellow', 'yellow', 'white', 'black', 'yellow', 
'black', 'yellow', 'black', 'dark_orange', 'orange', 'black', 'white', 'white', 'black', 'yellow', 'yellow', 'yellow', 'white', 'white', 'light_grey', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'light_grey', 'white', 'white', 'white', 'yellow', 'white', 'white', 'black', 'yellow', 'black', 'white', 'black', 'white', 'white', 'white', 'dark_red', 'dark_red', 'dark_red', 'black', 'white', 'white', 'white', 'white', 'white', 'light_grey', 'blue', 'blue', 'blue', 'blue', 'blue', 'light_grey', 'white', 'white', 'white', 'white', 'white', 'white', 'dark_orange', 'yellow', 'black', 'white', 'black', 'black', 'dark_red', 'dark_red', 'dark_red', 'dark_red', 'dark_red', 'black', 'white', 'white', 'white', 'white', 'white', 'light_grey', 'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'white', 'white', 'white', 'white', 'white', 'black', 'dark_orange', 'yellow', 'black', 'black', 'blue', 'black', 'white', 'white', 'white', 'white', 'white', 'black', 'white', 'white', 'white', 'white', 'white', 'white', 'light_grey', 'blue', 'blue', 'blue', 'blue', 'black', 'white', 'white', 'white', 'white', 'white', 'black', 'dark_orange', 'yellow', 'black', 'black', 'blue', 'black', 'white', 'white', 'white', 'white', 'white', 'black', 'white', 'white', 'white', 'white', 'white', 'white', 'light_grey', 'blue', 'blue', 'blue', 'blue', 'black', 'white', 'white', 'white', 'white', 'white', 'black', 'dark_orange', 'yellow', 'black', 'black', 'blue', 'black', 'white', 'white', 'white', 'white', 'white', 'black', 'white', 'white', 'white', 'white', 'white', 'white', 'light_grey', 'blue', 'blue', 'blue', 'blue', 'blue', 'light_grey', 'light_grey', 'white', 'white', 'black', 'white', 'black', 'yellow', 'black', 'blue', 'blue', 'black', 'dark_grey', 'dark_grey', 'dark_grey', 'dark_grey', 'dark_grey', 'black', 'white', 'white', 'white', 'white', 'white', 'white', 'light_grey', 'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'black', 'white', 'white', 'black', 'black', 'white', 'white', 'white', 'black', 'blue', 'blue', 'black', 'black', 'black', 'black', 'black', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'light_grey', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'white', 'black', 'red', 'dark_red', 'dark_red', 'black', 'black', 'blue', 'blue', 'blue', 'blue', 'light_grey', 'light_grey', 
'light_grey', 'light_grey', 'white', 'white', 'white', 'white', 'white', 'white', 'light_grey', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'dark_red', 'red', 'red', 'red', 'dark_red', 'black', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'black', 'black', 'light_grey', 'white', 'white', 'white', 'light_grey', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'dark_red', 'white', 'white', 'white', 'dark_red', 'black', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'light_grey', 'white', 'light_grey', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'white', 'white', 'white', 'white', 'white', 'black', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 
'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'light_grey', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'white', 'white', 'white', 'white', 'white', 'black', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'light_grey', 'light_grey', 'light_grey', 'dark_grey', 'black', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'black', 'black', 'black', 'black', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 
'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 
'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']
