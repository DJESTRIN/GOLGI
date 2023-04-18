def delete_spaces():
    import os
    directory = input('type the path to your folder')
    os.chdir(directory)
    path = os.getcwd()
    filenames = os.listdir(path)
    for filename in filenames:
        os.rename(os.path.join(path,filename),os.path.join(path,filename.replace(' ','')))
