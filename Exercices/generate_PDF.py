import subprocess
import os
import glob
import argparse

#
# NOTE : Bullet lists in markdown must have an empty line, otherwise they won't be rendered correctly in the .pdf
#


notebook_condition = "*.ipynb"
markdown_condition = "*.md"

parser = argparse.ArgumentParser(description="Convert exercises to .pdf")
parser.add_argument("--folders", type=str, default=None)
parser.add_argument("--debug", type=str, default=None)
args = parser.parse_args()

folders = args.folders
if folders is None:
    foldersList = os.listdir()
else:
    foldersList = folders.split(',')

enable_debug = args.debug

print(folders)
preprocessor_style = "colorful"


for folder in foldersList:
    folder = os.getcwd() + "/" + folder
    print(folder)
    
    if(os.path.isdir(folder)):
        print(f"Scanning folder {folder}...")
        os.chdir(folder)
        # Convert notebooks to pdf
        for ex in glob.glob(notebook_condition):
            print(f"   converting {ex}...")
            debug = subprocess.run(['jupyter', 'nbconvert', ex, '--to', 'pdf', '--output', ex.replace('ipynb', 'pdf'), f'--LatexPreprocessor.style={preprocessor_style}'], capture_output=True)
            print("   " + debug.stderr.decode())
            if not enable_debug is None:
                print(debug)
        # Convert markdowns to pdf
        for ex in glob.glob(markdown_condition):
            print(f"   converting {ex}...")
            debug = subprocess.run(['pandoc', ex, '--pdf-engine=xelatex', '-o', ex.replace('md', 'pdf')])
            print("   " + debug.stderr.decode())
            if not enable_debug is None:
                print(debug)

        os.chdir("..")
print("Finished")