import os
from pathlib import Path
from pydub import AudioSegment
from pydub.silence import split_on_silence
date = '16-08-2020'
human_count = 9
dataset_path = "18-08-2020_dataset"
export_path = "prepare_step_1/step_1/ok_output/"
range_1 = "prepare_step_1/step_1/input/range_1/"
range_2 = "prepare_step_1/step_1/input/range_2/"
range_3 = "prepare_step_1/step_1/input/range_3/"


# def file_name():
#     my_file_name = f
#     my_file_name = my_file_name.split(".")
#     my_file_name = my_file_name[0]

def match_target_amplitude(aChunk, target_dBFS):
    ''' Normalize given audio chunk '''
    change_in_dBFS = target_dBFS - aChunk.dBFS
    return aChunk.apply_gain(change_in_dBFS)

def is_wav(file_name):
    temp_file_name = file_name.split('.')
    if (temp_file_name[1] == 'wav'):
        return True
    else:
        return False
def export_song(song,range,count_no,show_text,s,):
    chunks = split_on_silence(
        # Use the loaded audio.
        song,
        # Specify that a silent chunk must be at least 2 seconds or 2000 ms long.
        min_silence_len=300,
        # Consider a chunk silent if it's quieter than -16 dBFS.
        # (You may want to adjust this parameter.)
        silence_thresh=-50
    )

    for i, chunk in enumerate(chunks):
        # Create a silence chunk that's 0.5 seconds (or 500 ms) long for padding.
        my_i = str(i)
        my_duration = (int)(2000 - len(chunk)) / 2
        silence_chunk = AudioSegment.silent(duration=my_duration)

        # Add the padding chunk to beginning and end of the entire chunk.
        audio_chunk = silence_chunk + chunk + silence_chunk

        # Normalize the entire chunk.
        normalized_chunk = match_target_amplitude(audio_chunk, -20.0)

        # Export the audio chunk with new bitrate.
        print("Exporting " + show_text + "_{0}.wav.".format(i))

        if not os.path.exists(export_path + show_text):
            os.makedirs(export_path + show_text)

        normalized_chunk.export(
            export_path  + show_text+'/'+count_no+'_' + s + '_'+ my_i + '.wav',
            bitrate="192k",
            format="wav"
        )
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


            # file_name = os.path.join(dirpath, f)
            # my_file_name = f
            # my_file_name = my_file_name.split(".")
            # my_file_name = my_file_name[0]
            # song = AudioSegment.from_mp3(filenames)


if __name__ == "__main__":
    rename()