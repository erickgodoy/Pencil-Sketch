import cv2

if __name__:
    #Read image format BGR
    img = cv2.imread("./images/car.jpg", cv2.IMREAD_COLOR) 
    #Convert to format RGB
    img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 

    #Invert values in matrix img2 
    invert = cv2.bitwise_not(img2)
    #Add blur 
    blur = cv2.GaussianBlur(invert,(21,21),100)
    #Invert values in matrix blur
    invertt = cv2.bitwise_not(blur)
    #Operate (img2 * 256) / invertt
    sketch = cv2.divide(img2, invertt, scale=256.0)

    #Save image
    cv2.imwrite("./images/result.png",sketch)
  