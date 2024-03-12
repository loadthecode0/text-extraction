#convert videos to wav

import os
from pydub import AudioSegment

# Get the list of all files and directories
path = "./test_videos/videos"
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")
# prints all files
print(dir_list)
print(len(dir_list))
for i in range(1, len(dir_list)):
    video = AudioSegment.from_file("test_videos/videos/test" + str(i) + ".mp4", format="mp4")
    audio = video.set_channels(1).set_frame_rate(16000).set_sample_width(2)
    audio.export("test_videos/gen_audios/audio" + str(i) + ".wav", format="wav")