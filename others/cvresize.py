import cv2 as cv

for x in range(8):
    img = cv.imread("/home/tskg/Pictures/unexpectFile/vsBackgroundIMG/jave" +  str(x) +".png", -1)
    print(img.shape)

    b_channel, g_channel, r_channel, achannel = cv.split(img)
    img_RGBA = cv.merge((b_channel, g_channel, r_channel, achannel))
    #
    height, width, channels = img.shape
    print("size:", height,width)
    widths = (500 / width) * width
    heights = (500 / width) * height
    print("size:", heights,widths)
    imgs=  cv.resize(img_RGBA, (int(widths),int(heights)),interpolation = cv.INTER_AREA)
    #
    # cv.imshow("Display window", imgs)
    # k = cv.waitKey(0) # Wait for a keystroke in the window
    cv.imwrite("/home/tskg/Pictures/unexpectFile/vsBackgroundIMG/resized/jave"+ str(x) + ".png", imgs)