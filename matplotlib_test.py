'''
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pandas
print(pandas.read_excel("trips_data.xlsx")) #вывод полной таблицы
df = pandas.read_excel("trips_data.xlsx") # создаем объект
print(df.head()) #Вывод первых пяти строк

df.hist() # гистограмма
plt.show()
#x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
#num_bins = 5
#n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
#plt.show()
'''

import librosa
#%matplotlib inline
import matplotlib.pyplot as plt
import librosa.display
import numpy as np
#spisok =['/content/drive/MyDrive/am/1.wav', '/content/drive/MyDrive/am/10.wav', '/content/drive/MyDrive/am/11.wav', '/content/drive/MyDrive/am/12.wav', '/content/drive/MyDrive/am/13.wav', '/content/drive/MyDrive/am/2.wav', '/content/drive/MyDrive/am/3.wav', '/content/drive/MyDrive/am/4.wav', '/content/drive/MyDrive/am/5.wav', '/content/drive/MyDrive/am/6.wav', '/content/drive/MyDrive/am/7.wav', '/content/drive/MyDrive/am/8.wav', '/content/drive/MyDrive/am/9.wav']
spisok= ['am3.wav']
for i in range(len(spisok)):
  audio_data = spisok[i]
  x , sr = librosa.load(audio_data)
  S = np.abs(librosa.stft(x, n_fft=4096))**2
  chroma = librosa.feature.chroma_stft(S=S, sr=sr)
  fig, ax = plt.subplots()
  img = librosa.display.specshow(chroma, y_axis='chroma', x_axis='time', ax=ax)
  for i in range(len(chroma)-1,-1,-1):
    for j in range(len(chroma[i])):
      if chroma[i][j]<0.8:
        chroma[i][j]=0
    print("i= ",i,sum(chroma[i]))
  fig.colorbar(img, ax=ax)
  ax.set(title='Chromagram')
  plt.show()