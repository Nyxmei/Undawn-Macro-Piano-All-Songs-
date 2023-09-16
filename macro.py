import mido
import pyautogui
import time
import sys

def map_piano_note_to_key(note):
    piano_keymap = ['q', '1', 'w', '2', 'e', 'r', '3', 't', '4', 'y', '5',
              'u', 'i', '6', 'o', '7', 'p', '[', '8', ']', '9', '\\', '0', '-', '=']
    
    if not (60 <= note <= 96):
        return '', ''
    
    if 60 <= note <= 83:
        change_G = 'f2'
        baseline = 60
    else:
        change_G = 'f3'
        baseline = 84
    
    return change_G, piano_keymap[note - baseline]

def main():
    # Check if a command-line argument for the MIDI file path was provided
    if len(sys.argv) < 2:
        print("Please provide the path to the MIDI file as a command-line argument.")
        return

    # Extract the MIDI file path from the command-line arguments
    midi_file_path = sys.argv[1]
    print(f"Using MIDI file: {midi_file_path}")

    # Parse the MIDI file
    midi = mido.MidiFile(midi_file_path)
    print(f"MIDI File parsed.")
    time.sleep(5)
    curr_pitch = 'f2'
    pyautogui.press(curr_pitch)
    pyautogui.PAUSE = 0

    for msg in midi.play():
        if msg.type == 'note_on' and msg.velocity != 0:
            pitch, key = map_piano_note_to_key(msg.note)
            if curr_pitch != pitch:
                pyautogui.press(pitch)
                curr_pitch = pitch
            pyautogui.press(key)

if __name__ == "__main__":
    main()
