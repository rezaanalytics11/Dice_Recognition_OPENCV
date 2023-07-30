import cv2
import numpy as np

def rectangle(file_name):
  image = cv2.imread(rf"C:\Users\Ariya Rayaneh\Desktop\{file_name}")
  dice = image.copy()
  image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  image = cv2.resize(image, (0, 0), fx=2, fy=2)
  dst = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
  #image=255-image

  circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1,5, param1=165, param2=200, maxRadius=21)

  _, thresh = cv2.threshold(image, 135, 255, cv2.THRESH_BINARY)
  contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)



  for contour in contours:
    if cv2.contourArea(contour) > 500 and cv2.contourArea(contour) <10000:
      x, y, w, h = cv2.boundingRect(contour)
      cv2.rectangle(image, (x, y), (x + w - 1, y + h - 1), (0, 0, 0), 20)

      rec = cv2.rectangle(dst, (x, y), (x + w, y + h), (0, 255, 0), 5)

      if circles is not None:
        for i in range(circles.shape[1]):
          cx, cy, radius = circles[0][i]
          cv2.circle(dst, (round(cx), round(cy)), round(radius), (0, 0, 255), 2, cv2.LINE_AA)
        print(circles.shape[1])

  #cv2.putText(dst, f'score: {circles.shape[1]}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
  cv2.imshow('out', dst)
  cv2.imwrite(rf'C:\Users\Ariya Rayaneh\Desktop\picture_{file_name}dice.png',dst)
  cv2.waitKey()


rectangle('dice22.jpg')