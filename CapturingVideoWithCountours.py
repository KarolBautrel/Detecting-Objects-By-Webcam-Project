import pandas
import cv2
from datetime import datetime

from bokeh.plotting import output_file, show, figure

first_frame = None
status_list = [None, None]
times = []
video = cv2.VideoCapture(0)
df = pandas.DataFrame(columns=["Start", "End"])
while True:

    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)

    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=5)

    (cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL,
                                 cv2.CHAIN_APPROX_SIMPLE)
    for countour in cnts:
        if cv2.contourArea(countour) < 10000:
            continue

        status = 1
        cv2.drawContours(image=frame, contours=cnts, contourIdx=-1,
                         color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    status_list.append(status)

    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())

    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())
    #cv2.imshow('capturing', gray)

    #cv2.imshow("delta", delta_frame)
    #cv2.imshow("threshold", thresh_frame)
    cv2.imshow("colorframe", frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

for i in range(0, len(times), 2):
    df = df.append({"Start": times[i], "End": times[i+1]}, ignore_index=True)

df.to_csv("Times.csv")


video.release()
cv2.destroyAllWindows
