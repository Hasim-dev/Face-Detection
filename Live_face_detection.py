import cv2, pafy

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")


url = "https://www.youtube.com/watch?v=vsI_pKNcgeQ&ab_channel=WatchedWalker"
video = pafy.new(url)
play = video.getbest(preftype="webm")
cap = cv2.VideoCapture(play.url)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=3)
    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

    cv2.imshow("frame", frame)
    key = cv2.waitKey(16)


    if key == ord('a'):
        break

cap.release()
cv2.destroyAllWindows()



