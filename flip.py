from PIL import Image
img=Image.open('normal.png')
transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)
transposed_img.save('flipped.png')
print("Done flipping")