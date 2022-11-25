#ord("value") gets the ascii character value
#char(356)  gives the character

"""
from playsound import playsound
from pynput import mouse
from tkinter  import *

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y))) 

def sound():
        playsound('gun1.wav', SND_ASYNC)



def on_click(x, y, button, pressed):
    sound()
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))


def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()

# ...or, in a non-blocking fashion:

neww = ""
s = "fuck World"
dic = len(s)-1
for x in s:
    neww= neww + ((s[dic]))
    print(s[dic])
    dic= dic-1

print(neww)
print(len(neww))

"""
word = "ABC"

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
value = 0
i=0
for x in word:
    if ord(word[i]) % 2 != 0:
        value = ord(word[i])+value
    i = i +1

print(value)