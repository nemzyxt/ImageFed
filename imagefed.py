# Author : Nemuel Wainaina

import os
from colorama import init, Fore
from PIL import Image
from PIL.ExifTags import TAGS
from pyfiglet import figlet_format

init()
GREEN = Fore.GREEN
RED = Fore.RED
RESET = Fore.RESET

# display the welcome banner
def welcomeMsg():
    banner = figlet_format("ImageFed")
    print(f"{GREEN}{banner} {RESET}")
    print(f"\t{GREEN}   Author : Nemuel Wainaina \n")
    print('-' * 48)
    print(f"{RESET}")

# extract the EXIF Data and display it to the user
def dispExif(img):
    img = Image.open(img)
    exif_data = img.getexif()

    for tag_id in exif_data:
        tag = TAGS[tag_id]
        data = exif_data.get(tag_id)

        if isinstance(data, bytes):
            data = data.decode()

        print(f"   {tag:20} : {data}")

if __name__ == "__main__":
    welcomeMsg()

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--img", dest="img", required=True, help="The image whose metadata is to be extracted")

    args = parser.parse_args()
    img = args.img

    if not os.path.exists(img):
        print(f"{RED}[!] The file {img} could not be found {RESET}")

    if img.split('.')[-1].lower() not in ["jpg", "jpeg"]:
        print(f"{RED}[!] JPEG Image expected {RESET}")

    dispExif(img)
    
    print(f"{GREEN}")
    print('-' * 48)
    print(f"{RESET}")

