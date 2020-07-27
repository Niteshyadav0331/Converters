from PIL import Image

image1 = Image.open(r'D:\\red monkeys\\images\\bubble-shooter.jpeg')
im1 = image1.convert('RGB')
im1.save(r'D:\\red monkeys\\images\\my_images.pdf')