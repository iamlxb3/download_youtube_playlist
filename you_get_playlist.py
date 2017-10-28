import subprocess
import os

playlist_url_list = [
                     ('https://www.youtube.com/playlist?list=PLZ9qNFMHZ-A4rycgrgOYma6zxF4BZGGPW', 'Machine learning coursera'),
                     ('https://www.youtube.com/playlist?list=PLbkzipe1EfZ7lxuiSK74ORwjDEzHQ69Z6', 'HIIT'),
                     ('https://www.youtube.com/playlist?list=PLVU0H2WW8HDeDLuh3E8Xmu2pM7IffYAPH', 'Gordon Ramsay Desserts'),
                     ('https://www.youtube.com/playlist?list=PLyFUz_D_yq8sWsolcsuFy93Myx_CXqRPR', 'English'),
                     ('https://www.youtube.com/playlist?list=PLyFUz_D_yq8v5ourcsWcbYqBgGtyKum1i', 'Machine Learning'),
                     ('https://www.youtube.com/playlist?list=PLTOBJKrkhpoMdsT9RUERSDdEVrViykAEQ', 'Advanced Python'),
                     ('https://www.youtube.com/playlist?list=PLhoHEZlJjdQLDmn0aMkX9uzb4EYjEYh_8', 'MLAI 2015'),
                     ('https://www.youtube.com/playlist?list=PLkDaE6sCZn6FcbHlDzbVzf3TVgxzxK7lr', 'Heroes_of_Deep_Learning_Interviews'),
                     ('https://www.youtube.com/playlist?list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc', 'Improving_deep_neural_networks'),
                     ('https://www.youtube.com/playlist?list=PLkDaE6sCZn6Ec-XTbcX1uRg2_u4xOEky0', 'Neural_Networks_and_Deep_Learning'),
                     ('https://www.youtube.com/playlist?list=PLkDaE6sCZn6E7jZ9sN_xHwSHOdjUxUW_b', 'Structuring_Machine_Learning_Projects'),
                     ('https://www.youtube.com/playlist?list=PLyFUz_D_yq8tB5SdoThPkHUoPdwj_UbqK', 'Andrew_Ng')
                     
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
        
