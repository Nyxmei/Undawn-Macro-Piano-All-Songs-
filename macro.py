import mido
import pyautogui
import time
import keyboard
import sys

def map_piano_note_to_key(note):
    piano_G = ['f1', 'f2', 'f3']
    piano_keymap = ['q', '1', 'w', '2', 'e', 'r', '3', 't', '4', 'y', '5',
              'u', 'i', '6', 'o', '7', 'p', '[', '8', ']', '9', '\\', '0', '-', '=']
    if not(36 <= note <= 96):
        return '', ''

    if 36 <= note <= 59:
        change_G = piano_G[0]
        baseline = 36
    elif 60 <= note <= 83:
        change_G = piano_G[1]
        baseline = 60
    else:
        change_G = piano_G[2]
        baseline = 84

    key_index = note - baseline

    if 0 <= key_index < len(piano_keymap):
        return change_G, piano_keymap[key_index]

    return '', ''

def play_midi(path, pitch_modulation=10):
    midi = mido.MidiFile(path)
    print("Press F5 to play. F6 to stop")
    keyboard.wait('F5')
    time.sleep(2)

    curr_pitch = 'f2'
    pyautogui.press(curr_pitch)
    pyautogui.PAUSE = 0

    for msg in midi.play():
        if msg.type == 'note_on' and msg.velocity != 0:
            pitch, key = map_piano_note_to_key(msg.note + pitch_modulation)
            if curr_pitch != pitch:
                pyautogui.press(pitch)
                curr_pitch = pitch
            if key:
                pyautogui.press(key)

        if keyboard.is_pressed('F6'):
            break

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python macro.py 'path'")
        sys.exit(1)

    midi_path = sys.argv[1]
    play_midi(midi_path, pitch_modulation=10)
