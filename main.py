import moviepy.editor

video = moviepy.editor.VideoFileClip('video5262558238775190524.mp4')
audio = video.audio
audio.write_audiofile('video5262558238775190524.mp3')