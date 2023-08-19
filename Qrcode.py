import cv2

img = cv2.imread(r'C:\Users\Ariya Rayaneh\Desktop\qr.png')
qcd = cv2.QRCodeDetector()

retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(img)
print(retval)
print(decoded_info)
print(type(points))
print(points)
print(points.shape)
print(type(straight_qrcode))
print(type(straight_qrcode[0]))
print(straight_qrcode[0].shape)
img = cv2.polylines(img, points.astype(int), True, (0, 255, 0), 3)

# for s, p in zip(decoded_info, points):
#     img = cv2.putText(img, s, p[0].astype(int),
#                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imwrite(r'C:\Users\Ariya Rayaneh\Desktop\qr_output.png', img)

