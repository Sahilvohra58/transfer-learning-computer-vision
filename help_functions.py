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
        print(f"There are {len(dirs)} directories and {len(files)} files in {root} folder.")
    return


import datetime
import tensorflow as tf
def create_callbacks(tensorboard_dir_name, checkpoint_path, experiment_name, monitor='val_accuracy', patience= 5, verbose= 0, save_weights_only=False):
    log_dir = tensorboard_dir_name + "/" + experiment_name + "/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir)
    early_stopping_callback = tf.keras.callbacks.EarlyStopping(monitor=monitor, 
                                                                patience=patience, 
                                                                verbose=verbose)
    check_point_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                                save_weights_only=save_weights_only,
                                                                verbose=verbose)
    print(f"Saving TensorBoard log files to: {log_dir}")
    return [tensorboard_callback, early_stopping_callback, check_point_callback]



import matplotlib.pyplot as plt
def plot_loss_curves(model_history):

    print(model_history.history.keys())
    # summarize history for accuracy
    plt.plot(model_history.history['accuracy'])
    plt.plot(model_history.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend()
    plt.show()

    plt.plot(model_history.history['loss'])
    plt.plot(model_history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend()
    plt.show()


import matplotlib.image as mpimg
import random
def view_random_image(train_data_path):
    target_class = random.choice(os.listdir(train_data_path)) # choose a random class
    target_dir = train_data_path + '/' + target_class # create the target directory
    random_image = random.choice(os.listdir(target_dir)) # choose a random image from target directory
    random_image_path = target_dir + "/" + random_image # create the choosen random image path
    img = mpimg.imread(random_image_path) # read in the chosen target image
    plt.imshow(img) # plot the target image
    plt.title(f"Original random image from class: {target_class}")
    plt.axis(False); # turn off the axes
    return img, target_class