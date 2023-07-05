import cv2 as cv


# Function to rescale a video(frame)/image
def rescaleFrame(frame, scale=0.75):
    # Calculate the new dimensions for rescaling
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    # Perform the resizing using the calculated dimensions
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Function to change the resolution of a video (only for webcam)
def changeRes(width, height):
    # Set the width and height of the video capture object
    capture.set(3, width)
    capture.set(4, height)


# Reading an image
# Read the image 'cat.jpg' from the 'Photos' directory
img = cv.imread('Photos/cat.jpg')
cv.imshow('cat', img)  # Display the image in a window named 'cat'


# Reading a video
# Open the video file 'dog.mp4' for capturing frames
capture = cv.VideoCapture('Videos/dog.mp4')


while True:
    # Rescale the image
    # Rescale the image using the rescaleFrame() function
    resized_image = rescaleFrame(img)
    # Display the rescaled image in a window named 'Image'
    cv.imshow('Image', resized_image)

    # Read a frame from the video
    # Read a frame from the video capture object 'capture'
    isTrue, frame = capture.read()

    # Rescale the frame
    # Rescale the frame using the rescaleFrame() function with scale factor 0.90
    frame_resized = rescaleFrame(frame, scale=0.90)

    # Display the original and resized frames
    # Display the original frame in a window named 'Video'
    cv.imshow('Video', frame)
    # Display the resized frame in a window named 'Video Resized'
    cv.imshow('Video Resized', frame_resized)

    # Exit the loop if 'd' key is pressed
    # Wait for a key press event and check if it is 'd'
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Release the video capture object
capture.release()  # Release the video capture object 'capture'

# Close all windows
cv.destroyAllWindows()  # Close all OpenCV windows
