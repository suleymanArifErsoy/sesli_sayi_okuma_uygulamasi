from playsound import playsound
import os

def play_sound(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)
    playsound(file_path)

def speak_number(number, sound_files):
    if number == 0:
        play_sound(sound_files[0])
        return

    positions = ["", "bin", "milyon", "milyar", "trilyon", "katrilyon"]
    number_str = str(int(number))

    while len(number_str) % 3 != 0:
        number_str = '0' + number_str

    chunks = [number_str[i:i+3] for i in range(0, len(number_str), 3)]
    chunks.reverse()

    for chunk in chunks:
        if chunk != '000':
            speak_chunk(chunk, sound_files)
        positions.pop()


def speak_chunk(chunk, sound_files):
    hundred, ten, one = map(int, chunk)
    
    if hundred != 0:
        play_sound(f"{hundred}.wav")
        play_sound("yuz.wav")
    
    if ten != 0:
        if ten == 1:
            play_sound(f"{ten}{one}.wav")
        else:
            play_sound(f"{ten}0.wav")
    
    if one != 0 and ten != 1:
        play_sound(f"{one}.wav")

def main():
    sound_files = [
        "0.wav", "1.wav", "2.wav", "3.wav", "4.wav",
        "5.wav", "6.wav", "7.wav", "8.wav", "9.wav",
        "10.wav", "20.wav", "30.wav", "40.wav", "50.wav",
        "60.wav", "70.wav", "80.wav", "90.wav", "100.wav",
        "1000.wav", "1000000.wav", "1000000000.wav", "1000000000000.wav", "1000000000000000.wav"
    ]


    user_input = input("Lütfen bir sayı girin: ")

    try:
        number = float(user_input)
        speak_number(number, sound_files)
    except ValueError:
        print("Geçersiz bir sayı girişi.")

main()