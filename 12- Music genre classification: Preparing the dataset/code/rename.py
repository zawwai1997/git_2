import os
from pydub import AudioSegment
dataset_path = "18-08-2020_dataset"

def rename():
    # loop through all genre sub-folder
    g = 0
    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):
        for f in filenames:

            file_name = os.path.join(dirpath, f)
            print("file name : " + file_name)
            sp = file_name.split(".")
            if (sp.__len__() == 3):
                g = g + 1
                if (sp[2] == 'mp3'):
                    song = AudioSegment.from_mp3(file_name)
                else:
                    song = AudioSegment.from_wav(file_name)

                # print(str(g))
                song.export(sp[0] + '_' + str(g) + '.wav', format='wav')
                os.remove(file_name)
            else:
                if (sp[1] == 'mp3'):
                    song = AudioSegment.from_mp3(file_name)
                    print('exporting ' + sp[0] + '.wav')
                    song.export(sp[0] + '.wav', format="wav")
                    os.remove(file_name)

if __name__ == "__main__":
    rename()
