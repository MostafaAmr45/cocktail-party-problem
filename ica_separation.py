import time
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import FastICA
import librosa
from scipy.io import wavfile
import tkinter
import tkinter.filedialog
import os

#############################################
# Load an example of mixed voices.
root = tkinter.Tk()
root.withdraw()  # use to hide tkinter window

myAudioFile = tkinter.filedialog.askopenfilename()

sr, y = wavfile.read(myAudioFile)

#############################################
# implement the fastICA library on the audio file
ica = FastICA(n_components=y.shape[1])
S_ = ica.fit_transform(y)
S_ = S_ * 100  # magnifying the output of the ICA

#############################################
# export each component of the mixed audio
components = ['component1.wav', 'component2.wav', 'component3.wav']

for i in range(y.shape[1]):
    librosa.output.write_wav(components[i], S_[:, i], sr)

#############################################
# plotting time domain representation of mixed signal
figure_1 = plt.figure("Mixed Signal")
plt.title("Time Domain Representation of mixed signal")
plt.xlabel("Time")
plt.ylabel("Signal")
plt.plot(y[:, 0])

# plotting time domain representation of estimated signals
estimated_signals = ["Estimated Signal1", "Estimated Signal2", "Estimated Signal3"]

figure_2 = plt.figure("Estimated Signals")
for i in range(y.shape[1]):
    plt.subplot(y.shape[1], 1, i+1)
    plt.title(estimated_signals[i])
    plt.xlabel("Time")
    plt.ylabel("Signal")
    plt.plot(S_[:, i])

plt.show()