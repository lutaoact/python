import random, easygui
secret = random.randint(1, 99)
guess = 0
tries = 0

easygui.msgbox("""AHOY!""");

while guess != secret and tries < 6:
    guess = easygui.integerbox("What's yer guess, matey?" + str(secret))
    if not guess: break
    if guess < secret:
        easygui.msgbox(str(guess) + 'is too low, ye!')
    elif guess > secret:
        easygui.msgbox(str(guess) + 'is too high')
    tries += 1

if guess == secret:
    easygui.msgbox("avast!")
else:
    easygui.msgbox("No more guess!")
