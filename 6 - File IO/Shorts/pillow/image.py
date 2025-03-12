from PIL import Image # type: ignore
from PIL import ImageFilter # type: ignore

def main():
    with Image.open("in.jpeg") as img:
        # print(img.size) # Prints size of image in pixels
        # print(img.format) # What filetype it is
        img = img.rotate(180)
        img = img.filter(ImageFilter.BLUR)
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save("out.jpg")


if __name__ == "__main__":
    main()