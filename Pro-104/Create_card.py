
import cv2

img=cv2.imread("solar-system.jpg")


cv2.putText(img,
           "Sun",
            (100, 80),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            2,
            (0,0,255)
            )

cv2.putText(img,
           "Mercury",
            (110, 150),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255)
            )


cv2.imshow("output",img)
cv2.waitKey(0)

cv2.imwrite("Solar-System with name.jpg",img)