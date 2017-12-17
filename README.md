# A wrapper for you-get and youParse
Download multiple youtube playlists in an easy manner. For single youtube video, please check you-get.

you-get: https://github.com/soimort/you-get

youParse: https://github.com/pantuts/youParse

## Environment and Prerequisites
1. **Tested Envionment**
    
    OS: 'Windows-10-10.0.15063-SP0'
    
    Python 3.5.3 |Anaconda custom (64-bit)
2. **Prerequisites**

    Download and install you-get, for details, check https://github.com/soimort/you-get
    
    


## Quick Start
1. Modify 'playlist.txt'

    "playlist.txt" contains the playlists' ids and the names of the folders where videos are going to be saved.
    ```
    https://www.youtube.com/playlist?list=PLyFUz_D_yq8t49nOefW_9oVHXnYh9BUMc
    -> playlist_id: PLyFUz_D_yq8t49nOefW_9oVHXnYh9BUMc
    ```
    
    Example:
    ```py
    PLnb9O8b6HG-ohVjLN3itqaSTf6YuDbR9E, JJ # seperated by comma, [playlist_id, save_folder_name]
    playlist_id2, foldername2
    playlist_id3, foldername3
    ....
    ```
