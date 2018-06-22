import librosa
import matplotlib.pyplot as plt
import numpy
import pandas as pd
from matplotlib.mlab import specgram

df = pd.read_excel('labels2.xlsx', sheet_name='labels2')
df.as_matrix()

number_row=df.shape[0]
print(number_row)
raw_sounds = []
labels = []

#for i in range(number_row):#
for i in range (7):
    file = df.at[i, 'fname']
    label = df.at[i, 'label']
    labels.append(label)
    file = "C:\\Users\\User\\Downloads\\audio_train\\" + file
    signal, sr = librosa.load(file)
    print(i)
    raw_sounds.append(signal)


#numpy.savetxt("all_signals.csv", raw_sounds, delimiter=",")#

#plt.figure()
##librosa.display.waveplot(numpy.array(raw_sounds[0]),sr=22050)
#plt.title('Raw Signal')
#plt.show()

plt.figure()
#plt.figure(figsize=(25,60), dpi = 900)
plt.specgram(numpy.array(raw_sounds[6]), Fs=22050)
plt.title('Sepctrogram')
plt.show()

#for i in range (3):#
    #raw_sounds.append(file)#

#print(raw_sounds)#
