# -*- coding: utf-8 -*-
"""
@author: cjfaber

GMPyCurator - Command line python3 script for guided media curation. 
(GuidedMediaPythonCurator)

Description:

If you're anything like me you have one huge media/downloads folder that gets 
bloated all the time with images/media/videos save from online content which
eventually needs to organized into folders. This process using manual drag and
drop interfaces can take forever - even subsorting can take hours. This program
is designed to make the process as quick as possible, organizing media into
sub-directories based on tags supplied by the user and online resources to 
modify existing file tags. The intention is to preform these actions without
having the user ever take their hands off the keyboard. Allowing users to use 
key commands to guide the curation process. Tags become folder directories and
create a tree based on given tags. After completing a curation process a tag 
library is produced so that the user can quickly begin a new sorting process
using already created tags.

To begin select a specify a source folder. Users can decide to grab from
sub directories depeding on the level specified. The user can then specifiy a 
destination folder where media items will be moved. The user will then be
displayed a preview of the media along with a prompt for potential tags. 

Picture mode - Will scrape all pictures contained in a defined number of sub-
    directories and move them to target directories based on tags given as 
    folders. User can also add tags if the given image format supports tags. 
    (Works with the following formats: .tif(f) .gif .jp(e)g .jp2, .jpx, .png)
    
Music Mode - Will scrape all music in a given sub-directory and re-orgainze
    based on a user defined hierarchy (eg: ./Artist/Album/Artist-Songname.mp3)
    This mode can also use the musicbrainz database to define and edit tags.
    Users can delete all tags if desired and start fresh. 
    (Works with the following formats: .mp3 .wma .flac .m4a .wav )
    
Video Mode - Will scrape all video files in a given sub-direcotry and 
    re-orgainize based on a user defined tag hirarchy. 
    (Works with the following formats: .avi .mp4 .mpeg .wma, .webm)
    
    
Required libaries - PyQt5 (5.10.0 - current problems with 5.11), PyInquirer.

Ran and tested in Linux Mint Cinniamon (linux 4.8.17)

Current Status: Alpha - Only Images is currently implemented, more to come!


"""

import os
import sys,threading
from GMPC_Questions import *

from PyQt5.QtWidgets import *

from GMPC_FileManager import *
from GMPC_Tagger import *



if __name__ == "__main__":
    os.environ['QT_STYLE_OVERRIDE'] = ""    #Gets rid of warning for Qt5 in Mint 18 cinnamon
    app = QApplication(sys.argv)

    print("Welcome to the GMPyCurator!")
    if sys.stdin.isatty():
        answers = prompt(init_questions, style=init_style)
    else:
        print("\t Warn: Not in tty, running with default test values")
        answers = {'mode': 'Images', 'media_dst': '/home/cfaber/Development/GMPyCurator/dst',
                   'media_src': '/home/cfaber/Development/GMPyCurator/src/',
                   'database' : '/home/cfaber/Development/GMPyCurator/tagtest.csv'}
    print("Starting GMpyCurator in " + answers['mode'] + ' mode')

    print("Scraping files...")
    file_listing = FileScrape(answers['media_src'], answers['mode'])

    print("\rScraping Complete!")
    usr_inp = input("Press \"L + Enter\" to see a listing of files. Otherwise press Enter key to continue")
    if usr_inp == 'L':
        pprint (file_listing)


    print("Loading Tags...")
    user_tags = ImageTagDict()
    if answers['database'] == 'TESTVALUES':
        user_tags.AddTag('food', 'ROOT', 'food')
        user_tags.AddTag('Personas-Gajinka', 'ROOT', 'persona')
        # /%Root%/Memes/Macros
        user_tags.AddTag('Memes', 'ROOT', 'meme')
        user_tags.AddTag('Macro', 'meme', 'macro')
        # /%Root%/Wallpaper/My_wallpaper
        user_tags.AddTag('Wallpaper', 'ROOT', 'wallpaper')
        user_tags.AddTag('My_Wallpaper', 'wallpaper', 'my walls')
    else:
        user_tags.LoadTags(answers['database'])
    print("\rLoaded all tags!")
    print("Starting user interface")

    from GMPC_Display import *

    window = MediaDisplay(answers['mode'], user_tags)
    window.show()
    window.StartCuration(file_listing)





    sys.exit(app.exec_())



