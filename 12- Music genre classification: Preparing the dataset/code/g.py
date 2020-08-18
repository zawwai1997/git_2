file_path = "18-08-2020_dataset/english_sar/EnglishSarLMM.mp3_0.mp3"
sp  =file_path.split(".")
if(sp.__len__() == 3):
    file_path = sp[0]+ '.' + sp[2]
print(file_path)