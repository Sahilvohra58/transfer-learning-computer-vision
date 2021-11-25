import zipfile
import urllib.request
import os
import shutil

def download_and_unzip(url, file_name):
    urllib.request.urlretrieve(url, file_name)
    print('Beginning file download...')

    #File Extraction
    zip_ref =  zipfile.ZipFile(file_name, 'r')
    zip_ref.extractall()
    zip_ref.close()
    if os.path.exists('__MACOSX'):
        shutil.rmtree('__MACOSX')
    if os.path.isfile(file_name):
        os.remove(file_name)
    return

import os 
def dir_explore(dir_path):
    for root, dirs, files in os.walk(dir_path):
        # root : Prints out directories only from what you specified.
        # dirs : Prints out sub-directories from root.
        # files : Prints out all files from root and directories.
        print(f"There are {len(dir)} directories and len{len(files)} in {root} folder.")
    return