import exifread
import sys
import pyfiglet
from colorama import Fore, Style

def banner():
    ascii_banner = pyfiglet.figlet_format("PekoExif")
    print(Fore.CYAN + ascii_banner + Style.RESET_ALL)
    print(Fore.GREEN + "Created by: Peko Sarshu")
    print(Fore.YELLOW + "GitHub   : p3k0h4ck3r")
    print(Fore.MAGENTA + "Instagram: @pekopekoboy5\n" + Style.RESET_ALL)

banner()

def extract_metadata(image_path):
    try:
        with open(image_path, 'rb') as f:
            tags = exifread.process_file(f)

        if not tags:
            print(Fore.RED + "No metadata found in this image." + Style.RESET_ALL)
            return

        print(Fore.YELLOW + f"\nMetadata for {image_path}:\n" + Style.RESET_ALL)
        for tag in tags.keys():
            print(f"{Fore.CYAN}{tag}{Style.RESET_ALL}: {tags[tag]}")

        # GPS Info
        if "GPS GPSLatitude" in tags and "GPS GPSLongitude" in tags:
            lat = tags["GPS GPSLatitude"]
            lon = tags["GPS GPSLongitude"]
            print(Fore.GREEN + f"\nGoogle Maps Link: https://www.google.com/maps/?q={lat},{lon}" + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    banner()
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python pekoexif.py <image_path>" + Style.RESET_ALL)
        sys.exit(1)

    image_path = sys.argv[1]
    extract_metadata(image_path)
