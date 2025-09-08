import exifread
import pyfiglet
from colorama import Fore, Style
import sys

def banner():
    ascii_banner = pyfiglet.figlet_format("PekoExif")
    print(Fore.CYAN + ascii_banner + Style.RESET_ALL)
    print(Fore.GREEN + "Created by: Peko Sarshu")
    print(Fore.YELLOW + "GitHub   : p3k0h4ck3r")
    print(Fore.MAGENTA + "Instagram: @pekopekoboy5\n" + Style.RESET_ALL)

def extract_metadata(img_file):
    try:
        with open(img_file, 'rb') as f:
            tags = exifread.process_file(f)
            if not tags:
                print(Fore.RED + "[-] No EXIF metadata found!" + Style.RESET_ALL)
            else:
                print(Fore.CYAN + f"[+] Metadata for {img_file}:\n" + Style.RESET_ALL)
                for tag, value in tags.items():
                    print(f"{Fore.YELLOW}{tag}: {Fore.CYAN}{value}{Style.RESET_ALL}")
    except FileNotFoundError:
        print(Fore.RED + f"[-] File not found: {img_file}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"[-] Error: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    banner()
    if len(sys.argv) < 2:
        print(Fore.RED + "Usage: python pekoexif.py <image_file>" + Style.RESET_ALL)
        sys.exit(1)

    img_path = sys.argv[1]
    extract_metadata(img_path)
