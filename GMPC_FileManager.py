
'''
 fileScrape: Returns a list of all file names given a mode
    Verifies that the file does exist before
'''

import glob
from pprint import pprint

#Returns a list of files in the WorkingDir path
def FileScrape(WorkingDir, mode):
    files = []
    if mode == 'Images':
        files.extend(glob.glob(WorkingDir + '/*.jpg', recursive=True))
        files.extend(glob.glob(WorkingDir + '/*.jpeg', recursive=True))
        files.extend(glob.glob(WorkingDir + '/*.jp2', recursive=True))
        files.extend(glob.glob(WorkingDir + '/*.jpx', recursive=True))
        files.extend(glob.glob(WorkingDir + '/*.png', recursive=True))
        files.extend(glob.glob(WorkingDir + '/*.tif.', recursive=True))
        files.extend(glob.glob(WorkingDir + '/*.png', recursive=True))
    elif mode == 'Music':
        files.extend(glob.glob(WorkingDir + '/*.mp3', recursive=True))
        files.extend(glob.glob(WorkingDir + '/*.wma', recursive=True))
        files.extend(glob.glob(WorkingDir + '/*.flac', recursive=True))
        files.extend(glob.glob(WorkingDir + '/*.m4a', recursive=True))
        files.extend(glob.glob(WorkingDir + '/*.wav', recursive=True))
    else:
        files.extend(glob.glob(WorkingDir + '/*.avi', recursive=True))
        files.extend(glob.glob(WorkingDir + '/*.mp4', recursive=True))
        files.extend(glob.glob(WorkingDir + '/*.mpeg', recursive=True))
        files.extend(glob.glob(WorkingDir + '/*.wma', recursive=True))
        files.extend(glob.glob(WorkingDir + '/*.webm', recursive=True))
    return files