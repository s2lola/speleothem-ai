import cv2

size = 256
file = 1600

img = cv2.imread(f"image/dbe/DBE_4_900_cut_2.tif")


x_axis = (img.shape[0] // size) * size
y_axis = (img.shape[1] // size) * size

i = 0
for x in range(0, x_axis, size):
    for y in range(0, y_axis, size):
        cv2.imwrite(f"image/dbe/classify_{file}_size{size}/{i}.png", img[x : x + size, y : y + size])
        i += 1


