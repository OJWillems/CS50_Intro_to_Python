import sys
from PIL import Image, ImageOps
import os.path

def main():
    cli_error_handling()
    shirtify()

def cli_error_handling():
    permitted_file_extensions = [".jpg", ".jpeg", ".png"]
    file_1_extension = os.path.splitext(sys.argv[1])[1].lower()
    file_2_extension = os.path.splitext(sys.argv[2])[1].lower()
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif file_1_extension not in permitted_file_extensions:
        sys.exit("The first file is not a .jpg, .jpeg, or .png file")
    elif file_2_extension not in permitted_file_extensions:
        sys.exit("The second file is not a .jpg, .jpeg, or .png file")
    elif file_1_extension != file_2_extension:
        sys.exit("The files must be of the same file type")

def shirtify():
    try:
        with Image.open(sys.argv[1]) as input_image, Image.open("shirt.png") as t_shirt_overlay:
            cropped_input_image = ImageOps.fit(input_image, size=t_shirt_overlay.size, method=3, bleed=0, centering=(0.5, 0.5))
            cropped_input_image.paste(t_shirt_overlay, t_shirt_overlay)
            cropped_input_image.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("File not found")

if __name__ == "__main__":
    main()