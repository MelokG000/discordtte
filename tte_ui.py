# DISCORD TEXT-TO-EMOJI CONVERTING UI                                                         
# LICENSE: CC BY-NC-SA 4.0 (https://creativecommons.org)
# MADE BY: Mlk

import pyfiglet
import discord_tte
import pyperclip

we_are_shutting_down = False

COLOR_RESET = "\x1b[0m"
COLOR_RED = "\x1b[31m"
COLOR_GREEN = "\x1b[32m"
COLOR_YELLOW = "\x1b[33m"
COLOR_BLUE = "\x1b[34m"
COLOR_PURPLE = "\x1b[35m"
COLOR_CYAN = "\x1b[36m"
COLOR_WHITE = "\x1b[37m"
COLOR_RED_TERMINAL = "\033[41m"

cyrillic_c = "с" # for all those russians and other people with cyrillic c on the same button as latin one

pnontextlist = discord_tte.shorten_to_non_text_emoji
psecret = False
pnitro = False
pmaxlength = 2000
pshorten = True
pprefix = "### "
ptoemoji = False
pareweindiscord = True
pmenufont = "graceful"

nontextlist = pnontextlist
secret = psecret
nitro = pnitro
maxlength = pmaxlength
shorten = pshorten
prefix = pprefix
toemoji = ptoemoji
areweindiscord = pareweindiscord
menufont = pmenufont

__version__ = "1.0.2"

while not we_are_shutting_down:
    try:
        text_part_1 = pyfiglet.figlet_format("TEXT TO ", font=menufont).rstrip()
        text_part_2 = pyfiglet.figlet_format("DISCORD ", font=menufont).rstrip()
        text_part_3 = pyfiglet.figlet_format("EMOJI", font=menufont).rstrip()

        lines1, lines2, lines3 = text_part_1.split("\n"), text_part_2.split("\n"), text_part_3.split("\n")
        max_lines = max(len(lines1), len(lines2), len(lines3))
        lines1, lines2, lines3 = [""]*(max_lines - len(lines1)) + lines1, [""]*(max_lines - len(lines2)) + lines2, [""]*(max_lines - len(lines3)) + lines3
        width1, width2 = max(len(line) for line in lines1), max(len(line) for line in lines2)

        for one, two, three in zip(lines1, lines2, lines3):
            one = one.ljust(width1)
            two = f"{COLOR_PURPLE}{two.ljust(width2)}{COLOR_RESET}"
            print(f"{one}{two}{three}")
    except pyfiglet.FontNotFound:
        print(f"TEXT TO {COLOR_PURPLE}DISCORD{COLOR_RESET} EMOJI\n")
        print(f"{COLOR_RED}Selected font does not exist.{COLOR_RESET}\n")
        
    print(f"UI: v{__version__}")
    print(f"LIB: v{discord_tte.__version__}")
    print("")
    print(f"c1 - Toggle discord nitro (current - {COLOR_GREEN if nitro else COLOR_RED}{nitro}{COLOR_RESET})")
    print(f"c2 - Change max message length (without nitro) (current -  {COLOR_BLUE}{maxlength}{COLOR_RESET})")
    print(f"c3 - Toggle shortening (reduced readability in exchange for increased message capacity) (current - {COLOR_GREEN if shorten else COLOR_RED}{shorten}{COLOR_RESET})")
    print(f"c4 - Change symbols before emojis (supports discord markdown) (current - {COLOR_BLUE}{prefix.strip()}{COLOR_RESET})")
    print(f"c5 - Toggle converting pieces of text to non-text emoji (current - {COLOR_GREEN if toemoji else COLOR_RED}{toemoji}{COLOR_RESET})")
    print("c6 - Add an emoji to c5")
    print("c7 - Show c5 emoji list")
    print(f"c8 - Do we need to cut emojis past the limit? (current - {COLOR_GREEN if areweindiscord else COLOR_RED}{areweindiscord}{COLOR_RESET})")
    print("c9 - Reset settings")
    print("c10 - Copy test string")
    print(f"c11 - Change menu font (current - {COLOR_BLUE+menufont+COLOR_RESET})")
    print(COLOR_RED+"c0 - Close"+COLOR_RESET)
    if secret:
        print(f"{COLOR_RED}S{COLOR_YELLOW}E{COLOR_GREEN}C{COLOR_CYAN}R{COLOR_BLUE}E{COLOR_PURPLE}T{COLOR_RESET} MODE!!!!!! Please {COLOR_RED}do not use c99 again!!!{COLOR_RESET}")
    print("")

    request = input()
    request = request.replace(cyrillic_c, "c")
    match request:
        case "c1": 
            nitro = not nitro
            if nitro:
                print("User now has Discord Nitro.")
            else:
                print("User does not have Discord Nitro.")
        case "c2":
            try:
                maxlength = int(input("New max length? "))
            except:
                print("Not a number.")
        case "c3":
            shorten = not shorten
            if shorten:
                print("Now shortening.")
            else:
                print("Now outputting full messages.")
        case "c4":
            prefix = f"{input('New symbols before emojis? ')} "
        case "c5":
            toemoji = not toemoji
            if toemoji:
                print("Now converting.")
            else:
                print("Now outputting text only.")
        case "c6":
            key = input("Keyword (a word that will be converted)? ")
            value = input("Emoji (without colons)? ")
            nontextlist[key] = value
        case "c7":
            print(nontextlist)
        case "c8":
            areweindiscord = not areweindiscord
            if areweindiscord:
                print("Now cutting messages.")
            else:
                print("Now outputting full messages.")
        case "c9":
            nontextlist = pnontextlist
            if secret:
                print(COLOR_RED_TERMINAL+COLOR_WHITE+"NO!"+COLOR_RESET+f" You can't just do that! {COLOR_RED}S{COLOR_RESET}{COLOR_YELLOW}E{COLOR_RESET}{COLOR_GREEN}C{COLOR_RESET}{COLOR_CYAN}R{COLOR_RESET}{COLOR_BLUE}E{COLOR_RESET}{COLOR_PURPLE}T{COLOR_RESET} MODE IS STILL ON!")
            nitro = pnitro
            maxlength = pmaxlength
            shorten = pshorten
            prefix = pprefix
            toemoji = ptoemoji
            areweindiscord = pareweindiscord
            menufont = pmenufont
            print("Settings reset.")
        case "c10":
            pyperclip.copy(discord_tte.tte_get_test_string()) 
            print("Copied!")
        case "c11":
            menufont = input("New menu font (uses FIGlet fonts)? ")
        case "c99":
            secret = not secret
            if secret:
                print(f"{COLOR_RED}S{COLOR_YELLOW}e{COLOR_GREEN}c{COLOR_CYAN}r{COLOR_BLUE}e{COLOR_PURPLE}t{COLOR_RESET} mode on!")
            else:
                print(f"{COLOR_RED}ẅ̴̢̮̲̪͕̱͖̇̾̅́͠h̷̛̳̠̀̅̕͘̕ŷ̵̫̮̬̄̇̄̿͛͝")
                we_are_shutting_down = True
        case "c0":
            break
        case _:
            pyperclip.copy(discord_tte.text_to_emoji(request, nitro, maxlength, shorten, prefix, secret, toemoji, areweindiscord)) 
            print("Copied!")
            
    a = input("Press enter to continue...") if not we_are_shutting_down else input("Ṗ̷͕͝ŗ̵͓̅e̸̮͒͝s̶͔͉̐̈́s̷͔͕̀͋ ̶̪̲͊e̸̖͉̊n̵̞͛t̶͔͊ȇ̶̙̓r̵̻͑ ̴̱̈t̷̗̍̾ͅō̶̢̥͂ ̶̗͗q̵̩̜̊̀ṷ̶̀͋i̶̢͚͌t̶̍̕ͅ.̷̲͍̑̓.̶̗̈̓.̸̔͊͜")
    
    print("\033[H\033[2J", end="")