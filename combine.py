import subprocess
def Mux(video,audio,original):
    cmd = 'ffmpeg -i '+ video +' -i '+audio+' -c copy -map 0:v -map 1:a '+ original +'.mkv'
    subprocess.call(cmd, shell=True)                                     # "Muxing Done
    print('Muxing Done')
#cmd = 'ffmpeg -i say_my_name.mp4 -i say_my_name1.mp3 -c copy -map 0:v -map 1:a say_my_name_original.mkv'
#subprocess.call(cmd, shell=True)
