import os
from pydub import AudioSegment
dataset_path = "18-08-2020_dataset/arr_twin"

def rename():
    # loop through all genre sub-folder
    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):
        for f in filenames:
            file_name = os.path.join(dirpath, f)
            sp = file_name.split(".")
            if (sp.__len__() == 3):
                if(sp[2] == 'mp3'):
                    song = AudioSegment.from_mp3(file_name)
                else:
                    song = AudioSegment.from_wav(file_name)

                print('exporting '+ sp[0] + '.' + sp[2])
                song.export(sp[0] + '.' + sp[2], format="wav")
                os.remove(file_name)

            else:
                if (sp[1] == 'mp3'):
                    print(file_name)
                    song = AudioSegment.from_mp3(file_name)
                    print('exporting ' + sp[0] + '.' + sp[1])
                    song.export(sp[0] + '.' + sp[1], format="wav")
                    #os.remove(file_name)

if __name__ == "__main__":
    rename()