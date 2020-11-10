import cv2

# image path   
image_path = (r'C:\Users\CHIJINDU\Desktop\ml learn\5.jpg')     
# Read or load image from its path     
image = cv2.imread(image_path)

img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("My Image", img_rgb)    
cv2.waitKey(0)
