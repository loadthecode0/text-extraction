import os
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

path = "./test_videos/gen_audios"
dir_list = os.listdir(path)

for i in range(1, len(dir_list)):
    print(i)
    # Open the audio file
    with sr.AudioFile("test_videos/gen_audios/audio" + str(4) + ".wav") as source:
        audio_text = r.record(source)
        # Recognize the speech in the audio
        text = r.recognize_google(audio_text, language='en-US')
        # Print the transcript
        file_name = "output_video_text/video_transcript" + str(4) + ".txt"

    with open(file_name, "w") as file:
        # Write to the file
        file.write(text)
    # Open the file for editing by the user
    # os.system(f"start {file_name}")