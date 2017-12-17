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
2. Start Download
    ```
    # default model, videos will be saved to corresponding download_youtube_playlist/.../ folder
    python you_get_playlist.py
    
    # or you can customize the directory for saving
    python you_get_playlist.py --dir=D:\
    ```
    
---
    
# 融合了you-get and youParse的playlist下载程序
用于轻松下载大量的Youtube playlist；如果仅下载单个视频，请查看you-get
you-get: https://github.com/soimort/you-get

youParse: https://github.com/pantuts/youParse

## 环境与预安装
1. **测试可用环境**
    
    OS: 'Windows-10-10.0.15063-SP0'
    
    Python 3.5.3 |Anaconda custom (64-bit)
2. **需要的预安装**
    需安装you-get，具体方式请查看 https://github.com/soimort/you-get
    
    
## 快速开始
1. 修改'playlist.txt'文件
    "playlist.txt" 包含了每一个即将下载的Youtube playlist的id，以及存放视频的文件夹名字。
    
    ```
    https://www.youtube.com/playlist?list=PLyFUz_D_yq8t49nOefW_9oVHXnYh9BUMc
    -> playlist_id: PLyFUz_D_yq8t49nOefW_9oVHXnYh9BUMc
    ```
    
    例子:
    ```
    PLnb9O8b6HG-ohVjLN3itqaSTf6YuDbR9E, JJ # 以逗号分隔, [playlist_id, save_folder_name]
    playlist_id2, foldername2
    playlist_id3, foldername3
    ....
    ```
    
2. 开始下载
    ```
    # 默认视频将会被保存到相应的download_youtube_playlist/.../ 目录下
    python you_get_playlist.py
    
    # 或者你也可以自定义目标文件夹
    python you_get_playlist.py --dir=D:\
    ```
