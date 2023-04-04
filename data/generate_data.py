import cv2


def cut_images(file, save, size=224):

    img = cv2.imread(file)


    x_axis = (img.shape[0] // size) * size
    y_axis = (img.shape[1] // size) * size

    i = 0
    for x in range(0, x_axis, size):
        for y in range(0, y_axis, size):
            cv2.imwrite(f"{save}/{i}.png", img[x : x + size, y : y + size])
            i += 1

images_name = ["DBE3", "DBE4", "DBE4a"]

for file in images_name:
    cut_images(f"images/{file}.tif", f"images/{file}_cut")

