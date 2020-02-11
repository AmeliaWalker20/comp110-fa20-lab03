"""
Module: comp110_lab03

Practice code for working with sounds in Python.
"""
import sound


love_sound = sound.load_sound("love.wav")
love_sound.play()
sound.wait_until_played()  # waits until love_sound is done playing

filtered_love = sound.copy(love_sound)

# change the volume of the love sound
for i in range(len(filtered_sound)):
    sample = filtered_sound[i]

    # change the left channel
    new_left_val = sample.left * 2
    sample.left = new_left_val

    # change the right channel (in only one line of code!)
    sample.right = sample.right * 2

filtered_sound.play()
sound.wait_until_played()  # waits until love_sound is done playing