import numpy as np
import cv2

foto = cv2.imread("./maymun.png")


#print(foto.shape)
#
#x=15
#y=25
#kanal=1
#
#yogunluk = foto[y,x,kanal]
#
#print("yogunluk : ",  yogunluk)
#
#maximum_yogunluk = np.max(foto)
#minimum_yogunluk = np.min(foto)
#
#print("maximum yogunluk : " , maximum_yogunluk)
#print("minimum yogunluk : " , minimum_yogunluk)
#crop = foto[25:125, 50:150]

mavi_kanali = foto[ :, :, 0]
kirmizi_kanali = foto[ :, :, 2]
yesil_kanali = foto[ :, :, 1]

print("Fotoğrafın boyutu: " , foto.shape)
print("Mavi kanalının boyutu : " , kirmizi_kanali.shape)
cv2.imshow("fotograf" , kirmizi_kanali)
cv2.waitKey(0)
cv2.destroyAllWindows()



