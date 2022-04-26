import cv2

cap = cv2.VideoCapture(0)  # 0 is the id of your default webcam
while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    if ret == False:
        continue
    cv2.imshow("My Video Frame", frame)
    cv2.imshow("My Gray Frame", gray_frame)
    key_pressed = cv2.waitKey(1) & 0xFF
    # Wait for user input - q,then you will stop the loop
    if key_pressed == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
