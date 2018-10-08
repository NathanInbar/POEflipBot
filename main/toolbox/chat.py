from toolbox.general import *

def clearTextBox():
    tap(Key.enter)
    keyboard.press(Key.ctrl)
    tap('a')
    keyboard.release(Key.ctrl)
    tap(Key.backspace)
    tap(Key.esc)

def typeMessage(message, channel):# message to be sent, || channel d @character = whisper, % = party, etc. (LOCAL [blank] DOES NOT WORK)
    tap(Key.enter)
    keyboard.type(channel + ' ' + message)
    tap(Key.enter)
