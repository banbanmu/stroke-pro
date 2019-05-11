import os
import sys

input_mp4_name = "input.mp4"
# TODO 1.make sure that input.mp4 exist
# TODO 2.check taht input.mp4 is valid
frame_name = "frame"
# 스켈레톤 그렸다
tagged_name = "frame"
output_name = "output.mp4"

# TODO make all the stirng as arguenmets from cli argv[0]? < sth like this

os.system (f"ffmpeg -i {input_mp4_name} {frame_name}/{frame_name}%05d.png -hide_banner" )
# TODO make sure framed exits, if not make the folder

os.system(f"ffmpeg -framerate 30 -pattern_type glob -i '{tagged_name}/*.png' -c:v libx264 -pix_fmt yuv420p output_name")
# TODO make sure {frame_names} folder exitst if not raise Exception

 