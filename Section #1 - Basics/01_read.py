
import cv2 as cv

# # Read the image
# img = cv.imread("photos/cats 2.jpg")

# # Display the image in a window
# cv.imshow('cats 2', img)

# # Wait for a key press for 900 milliseconds
# cv.waitKey(900)


# Open the video file for capturing frames
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    # Read a frame from the video
    isTrue, frame = capture.read()

    # Display the frame in a window
    cv.imshow('Video', frame)

    # Wait for a key press for 20 milliseconds
    # if cv.waitKey(20) & 0xFF == ord('d'):
    #     break
    if isTrue:
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF == ord('d'):
            #  This line waits for a key press for 20 milliseconds. If the key press is the letter 'd', which is determined by checking the ASCII value returned by ord(), the loop is exited using the break statement.
            break
    else:
        break


    # it is possible that error will occur so that means video is out of range

    # This is the preferred way - if `isTrue` is false (the frame could
    # not be read, or we're at the end of the video), we immediately
    # break from the loop.
#     

# Release the video capture object
capture.release()

# Close all windows
cv.destroyAllWindows()
