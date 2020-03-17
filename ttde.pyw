import pyperclip
import re
import n2w

def regionalize(letter):
    return ":regional_indicator_" + letter + ": "

user_clipboard = pyperclip.paste()
user_clipboard = user_clipboard.lower()
res_string = ""
for letter in user_clipboard:
    if re.match("[a-zA-Z]", letter):
        res_string += regionalize(letter)
    elif re.match("[0-9]", letter):
        num = ":" + n2w.convert(int(letter)) + ": "
        res_string += num
    else:
        res_string += letter

pyperclip.copy(res_string)