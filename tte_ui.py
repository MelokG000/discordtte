# DISCORD TEXT-TO-EMOJI CONVERTING UI                                                         
# LICENSE: CC BY-NC-SA 4.0 (https://creativecommons.org)
# MADE BY: Mlk

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

cyrillic_c = "с" # for all those russians and other people with cyrillic c on the same button as latin one

pnontextlist = discord_tte.shorten_to_non_text_emoji
psecret = False
pnitro = False
pmaxlength = 2000
pshorten = True
pprefix = "### "
ptoemoji = False
pareweindiscord = True

nontextlist = pnontextlist
secret = psecret
nitro = pnitro
maxlength = pmaxlength
shorten = pshorten
prefix = pprefix
toemoji = ptoemoji
areweindiscord = pareweindiscord

version = "1.0.0"



while not we_are_shutting_down:
    print(r" ____  ____  _  _  ____    ____  __  ", COLOR_PURPLE, r"   ____  __  ____   ___  __  ____  ____  ", COLOR_RESET, r"  ____  _  _   __     __  __  ")
    print(r"(_  _)(  __)( \/ )(_  _)  (_  _)/  \ ", COLOR_PURPLE, r"  (    \(  )/ ___) / __)/  \(  _ \(    \ ", COLOR_RESET, r" (  __)( \/ ) /  \  _(  )(  ) ")
    print(r"  )(   ) _)  )  (   )(      )( (  O )", COLOR_PURPLE, r"   ) D ( )( \___ \( (__(  O ))   / ) D ( ", COLOR_RESET, r"  ) _) / \/ \(  O )/ \) \ )(  ")
    print(r" (__) (____)(_/\_) (__)    (__) \__/ ", COLOR_PURPLE, r"  (____/(__)(____/ \___)\__/(__\_)(____/ ", COLOR_RESET, r" (____)\_)(_/ \__/ \____/(__) ")
    print(f"UI: v{version}")
    print(f"LIB: v{discord_tte.LIBRARY_VERSION}")
    print("")
    print(f"c1 - Toggle discord nitro (current - {COLOR_GREEN if nitro else COLOR_RED}{nitro}{COLOR_RESET})")
    print(f"c2 - Change max message length (without nitro) (current -  {COLOR_BLUE}{maxlength}{COLOR_RESET})")
    print(f"c3 - Toggle shortening (reduced readability in exchange for longer messages) (current - {COLOR_GREEN if shorten else COLOR_RED}{shorten}{COLOR_RESET})")
    print(f"c4 - Change symbols before emojis (supports discord markdown) (current - {COLOR_BLUE}{prefix.strip()}{COLOR_RESET})")
    print(f"c5 - Toggle converting pieces of text to non-text emoji (current - {COLOR_GREEN if toemoji else COLOR_RED}{toemoji}{COLOR_RESET})")
    print("c6 - Add an emoji to c5")
    print("c7 - Show c5 emoji list")
    print(f"c8 - Do we need to cut emojis past the limit? (current - {COLOR_GREEN if areweindiscord else COLOR_RED}{areweindiscord}{COLOR_RESET})")
    print("c9 - Reset settings")
    print("c10 - Copy test string")
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
                print("\033[41m"+COLOR_RED+"NO!"+COLOR_RESET+f" You can't just do that! {COLOR_RED}S{COLOR_RESET}{COLOR_YELLOW}E{COLOR_RESET}{COLOR_GREEN}C{COLOR_RESET}{COLOR_CYAN}R{COLOR_RESET}{COLOR_BLUE}E{COLOR_RESET}{COLOR_PURPLE}T{COLOR_RESET} MODE IS STILL ON!")
            nitro = pnitro
            maxlength = pmaxlength
            shorten = pshorten
            prefix = pprefix
            toemoji = ptoemoji
            areweindiscord = pareweindiscord
            print("Settings reset.")
        case "c10":
            pyperclip.copy(discord_tte.tte_get_test_string()) 
            print("Copied!")
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