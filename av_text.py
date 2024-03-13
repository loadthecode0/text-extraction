import os
import speech_recognition as sr
import wave, math, contextlib
import whisper

def write_output(text, dir, index):
    f = open("output_video_text/" + dir + "/video_transcript" + str(index) + ".txt", "w")
    f.write(text)
    f.close()

def audproc_speechrecognition(index):
    r = sr.Recognizer()
    text = ""
    
    with contextlib.closing(wave.open("test_videos/gen_audios/audio" + str(index) + ".wav",'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    total_duration = math.ceil(duration / 30)
    
    for i in range(0, total_duration):
        with sr.AudioFile("test_videos/gen_audios/audio" + str(index) + ".wav") as source:
            r.adjust_for_ambient_noise(source)
            r.energy_threshold = 100
            audio_text = r.record(source, offset=i*30, duration=30)
            text += r.recognize_google(audio_text, language='en-US') + " "
            print(text)
    write_output(text, "speechrecognition", index)
    
def audproc_whisper(index):
    DEVICE = "cpu"
    model = whisper.load_model("medium", device=DEVICE)
    audio = whisper.load_audio("test_videos/gen_audios/audio" + str(index) + ".wav")
    audio = whisper.pad_or_trim(audio)
    result = model.transcribe("test_videos/gen_audios/audio" + str(index) + ".wav", verbose=True)
    print(result["text"])
    if (index!=6) : 
        write_output(result["text"], "whisper", index)

def main():    
    path = "./test_videos/gen_audios"
    dir_list = os.listdir(path)
    for i in range (1, len(dir_list)+1):
        audproc_whisper(i)
    audproc_whisper(6)

if __name__ == "__main__":
    main()


        
