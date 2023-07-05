import cv2 as cv
import numpy as np

# Create a blank image with dimensions 500x500 and 3 channels (RGB)
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)  # Display the blank image

# 1. Paint the image a certain colour
# Set a region of the image to the color (0, 0, 255) which is red
blank[200:300, 300:400] = 0, 0, 255
cv.imshow('Green', blank)  # Display the updated image

# 2. Draw a Rectangle
cv.rectangle(blank, (0, 0),
             (blank.shape[1] // 2, blank.shape[0] // 2), (0, 255, 0), thickness=-1)
# Draw a filled rectangle from (0, 0) to half of the width and height of the image with color (0, 255, 0) which is green
cv.imshow('Rectangle', blank)  # Display the updated image

# 3. Draw A circle
cv.circle(blank, (blank.shape[1] // 2,
          blank.shape[0] // 2), 40, (0, 0, 255), thickness=-1)
# Draw a filled circle at the center of the image with a radius of 40 and color (0, 0, 255) which is red
cv.imshow('Circle', blank)  # Display the updated image

# 4. Draw a line
cv.line(blank, (100, 250), (300, 400), (255, 255, 255), thickness=3)
# Draw a line from (100, 250) to (300, 400) with color (255, 255, 255) which is white and thickness 3 pixels
cv.imshow('Line', blank)  # Display the updated image

# 5. Write text
cv.putText(blank, 'Hello, my name is Jason!!!', (0, 225),
           cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
# Write the text 'Hello, my name is Jason!!!' at position (0, 225) with the FONT_HERSHEY_TRIPLEX font, scale 1.0,
# color (0, 255, 0) which is green, and thickness 2
cv.imshow('Text', blank)  # Display the updated image

cv.waitKey(0)  # Wait for any key press before closing all windows
