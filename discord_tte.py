# DISCORD TEXT-TO-EMOJI CONVERTING LIBRARY                                                         
# LICENSE: CC BY-NC-SA 4.0 (https://creativecommons.org)
# MADE BY: Mlk

LIBRARY_VERSION = "1.0.0"

emoji_letter_blank = ":regional_indicator_"
emoji_number_blank = ":number_" #it works like that too

letters = "abcdefghijklmnopqrstuvwxyz"
marks = "!?<>+-*/^#$="
emoji_marks = {"!":":exclamation:", "?":":question:", "<":":arrow_backward:", ">":":arrow_forward:", "+":":heavy_plus_sign:", "-":":heavy_minus_sign:", "*":":heavy_multiplication_x:","/":":heavy_division_sign:","^":":arrow_up_small:", "#":":hash:", "$":":dollar:", "=":":heavy_equals_sign:"}
numbers = "1234567890"
markstostay = ["(", ")", "[", "]", "{", "}", ";", "'", '"', "№", "@", "&", "%", "|", ",", "."] # no ":" because it will break L76
shorten = sorted(["id","ab","cl","sos","atm","wc","abc","ng","ok","up","cool","new","free","tm","top","soon","on","back","end","vs","o","a","b","m"], key=len, reverse=True)
shorten_to_other = {"p": "parking", "e": "email", "i": "information", "u": "ophiuchus"}
shorten_to_non_text_emoji = {"nose": "nose", "party": "partying_face"} # this can be used to convert any text into any emojis like "nose -> :nose:" or "party -> :partying_face: "

def shorten_emojis(text = ":regional_indicator_p: :regional_indicator_e: :regional_indicator_e:", secret_mode = False, convert_to_non_text_emoji = False):
    result_text = text
    if convert_to_non_text_emoji:
        for replacewith in shorten_to_non_text_emoji:
            searchingfor = ""
            for num in range(len(replacewith)):
                searchingfor += f":regional_indicator_{replacewith[num]}: "
            if searchingfor in result_text:
                result_text = result_text.replace(searchingfor, f":{shorten_to_non_text_emoji[replacewith]}: ")
    for replacewith in shorten: 
        searchingfor = ""
        for num in range(len(replacewith)):
            searchingfor += f":regional_indicator_{replacewith[num]}: "
        if searchingfor in result_text:
            result_text = result_text.replace(searchingfor, f":{replacewith}: ")
    for replacewith in shorten_to_other:
        searchingfor = ""
        for num in range(len(replacewith)):
            searchingfor += f":regional_indicator_{replacewith[num]}: "
        if searchingfor in result_text:
            result_text = result_text.replace(searchingfor, f":{shorten_to_other[replacewith]}: ")
    if secret_mode:
        searchingfor = ":regional_indicator_m: :regional_indicator_l: :regional_indicator_k: "
        if searchingfor in result_text:
            result_text = result_text.replace(searchingfor, ":face_holding_back_tears: :face_holding_back_tears: :face_holding_back_tears: ")
    return result_text

def letter_to_emoji(letter = "a"):
    return emoji_letter_blank + letter + ":"

def number_to_emoji(number = "1"):
    return emoji_number_blank + number + ":"

def mark_to_emoji(mark = "!"):
    return emoji_marks.get(mark)

def text_to_emoji(orig = "^^^ A $quick #brownfox [jumps] OVER the lazy, lazy {dog}?... $100! (1+9)*(8-5)+(42/6)+3-0=40! 3<5|7>2 ab cl ok tm atm", discordnitro = False, maxlength_without_nitro = 2000, shorten_the_text = True, add_before_emojis = "### ", secret_mode = False, nontext = False, are_we_in_discord = True):
    result = add_before_emojis # to make emojis smaller
    orig = orig.lower()
    maxlength = maxlength_without_nitro*2 if discordnitro else maxlength_without_nitro # nitro doubles your max message length
    for letter in orig:
        if letter in letters:
            result += letter_to_emoji(letter)
        elif letter in marks:
            result += mark_to_emoji(letter)
        elif letter in numbers:
            result += number_to_emoji(letter)
        elif letter == " ":
            result += "  "
        elif letter in markstostay:
            result += letter
        result += " " # fuck you discord and your damn flags
    if shorten_the_text:
        result = shorten_emojis(result, secret_mode, nontext)
    if are_we_in_discord:
        if len(result) > maxlength:
            result = result[:maxlength]
            if result.count(":") % 2 != 0:
                last_dt = result.rfind(":")
                result = result[:last_dt]
    result = result.rstrip()
    return result

def tte_get_test_string():
    return text_to_emoji()
