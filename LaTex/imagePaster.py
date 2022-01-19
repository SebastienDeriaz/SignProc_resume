# imagePaster.py
# Sébastien Deriaz
# 09.11.2021
#
# Grabs an image from the clipboard and copies it where the script is
# The image will be named img_0.png, img_1.png (depending on which images
# are already present in the current directory)
# An appropriate include is then copied to the clipboard for a LaTex figure
# using \begin{figure}[H]...

from PIL import ImageGrab
from glob import glob
import re
import pyperclip

print("Image Paster V1.0 - Sébastien Deriaz - 09.11.2021\n\n")
im = ImageGrab.grabclipboard()
index = -1
if(im is not None):
    files = glob('img_*.*')
    for f in files:
        m = re.search('(?<=img_)([0-9]+)', f)
        index = max(int(m.group(0)), index)
    im.save(f'img_{index+1}.png', 'PNG')
    width = float(input("\nwidth="))
    text = f'\\begin{{figure}}[H]\n\centering\n\includegraphics[width={width:.2f}cm]{{img_{index+1}.png}}\n\end{{figure}}'
    print(f"Copied text to clipboard :\n\n{text}\n\n")
    pyperclip.copy(text)
else:
    print("No image in clipboard")