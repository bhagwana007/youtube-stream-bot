import ffmpeg

rtmp_url = "rtmp://a.rtmp.youtube.com/live2/vj67-y5kp-7d2f-9y8q-3d6e"

(
    ffmpeg
    .input('sample.mp4', stream_loop=-1)
    .output(rtmp_url, format='flv')
    .run()
)
