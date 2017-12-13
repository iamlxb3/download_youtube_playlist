import subprocess
import os

playlist_url_list = [
                     ('https://www.youtube.com/playlist?list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb', 'MIT Introduction to Algorithms'),
                     ]
                

current_dir = os.path.dirname(os.path.abspath(__file__))
                
for playlist_url, save_dir_name in playlist_url_list:
    
    # replace space with '_'
    save_dir_name = save_dir_name.replace(' ', '_')

    subprocess.call("python youParse.py {}".format(playlist_url), shell=True)
    save_dir_path = os.path.join(current_dir, save_dir_name)
    is_dir_exist = os.path.isdir(save_dir_path)
    if not is_dir_exist:
        print ("making dir '{}'".format(save_dir_path))
        os.makedirs(save_dir_path)
    
    with open ('urls.txt', 'r') as f:
        for i, line in enumerate(f):
            # if i == 2:
                # break
            url = line.strip()
            if save_dir_name:
                subprocess.call("you-get -o {} {}".format(save_dir_name, url), shell=True)
            else:
                subprocess.call("you-get {}".format(url), shell=True)
        
