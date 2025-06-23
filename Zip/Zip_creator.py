import  zipfile
import pathlib

def make_zip(filepaths ,dest_dir):
    dest_path=pathlib.Path(dest_dir,"compressed.zip")
    with zipfile.ZipFile(dest_path,'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath,arcname=filepath.name)



if __name__ == "__main__":
    make_zip(filepaths=["Zip_App.py","Zip_Creator.py"],dest_dir= "dest")


