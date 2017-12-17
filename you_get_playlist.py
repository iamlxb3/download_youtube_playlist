'''A wrapper of youParse and youget
<<<<<<< HEAD
Only for downloading Youtube playlists, for single youtube viedo, check you-get.
=======
youParse: https://github.com/pantuts/youParse
you-get: https://github.com/soimort/you-get
Only for downloading videos from Youtube playlists, for single youtube video, check you-get.
'''

__version__ = '0.0.1'
__license__ = 'GPL'
__author__ = 'PJS'



import sys
import subprocess
from youParse import crawl
import os
import platform
import getopt
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


# customize save folder
save_dir_path = ''
try:
    opts, args = getopt.getopt(sys.argv[1:], "", ["dir="])
    for o, a in opts:
        if o == '--dir':
            save_dir_path = a
except getopt.GetoptError:
    raise Exception('Usage: python you_get_playlist.py --dir=D:\\example')


# default save_dir_path
if not save_dir_path:
    save_dir_path = os.path.dirname(os.path.abspath(__file__))
else:
    # check user input dir
    is_save_dir_path = os.path.isdir(save_dir_path)
    if not is_save_dir_path:
        raise Exception('Target dir "{}" does not exist!!'.format(save_dir_path))
#


# the encoding is for windows notepad
with open ('playlists.txt', 'r', encoding='utf-8-sig') as f:

    # iterate over all playlists
    for line in f:
        # get playlist url and name
        if line.count(',') != 1:
            raise Exception('Invalid format for input!! Please check readme.')
        url, folder_name = line.split(',')
        url = url.strip()
        url = "https://www.youtube.com/playlist?list={}".format(url)
        folder_name = folder_name.strip()
        #
    
        # replace space with '_'
        save_folder_name = folder_name.replace(' ', '_')
        #

        # get all video urls for 1 playlist
        print (url)
        all_video_urls = crawl(url)
        #

        # make new folders and be ready for saving videos
        playlist_save_dir_path = os.path.join(save_dir_path, save_folder_name)
        is_playlist_dir = os.path.isdir(playlist_save_dir_path)
        if not is_playlist_dir:
            os.makedirs(playlist_save_dir_path)
            dir_naming_valid = os.path.isdir(playlist_save_dir_path)
            if not dir_naming_valid:
                raise Exception('Please check the name of your folder-{}! Maybe invalid in your system: {}'
                                .format(folder_name, platform.platform()))
            else:
                print("Create directory '{}' done!".format(playlist_save_dir_path))
                print("Calling you-get...Wait...".format(playlist_save_dir_path))
        #

        # call you-get
        for video_url in all_video_urls:
            subprocess.Popen(['you-get', '-o', save_folder_name, video_url])
        #
