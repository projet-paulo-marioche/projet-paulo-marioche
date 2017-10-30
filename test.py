import math
import numpy as np
from matplotlib.pyplot import *
import scipy.io.wavfile as wave
from numpy.fft import fft

"""
Ouverture du fichier .wav, représentation temporelle
"""

rate,data = wave.read('loop_batterie.wav')   #rate = frequence d'échantillonage, déjà intégrée dans le fichier .wav
n = len(data)                #nombre d'échantillons
duree = 1.0*n/rate



te = 1.0/rate
t = np.zeros(n)
for k in range(0,n):
    t[k] = te*k

print(len(t))
print(n)

plot(t,data)
xlabel("t (s)")
ylabel("amplitude")


"""
Analyse spectrale par transformation de Fourrier
"""

def tracerSpectre(data,rate,debut,duree):
    start = int(debut*rate)
    stop = int((debut+duree)*rate)
    spectre = np.absolute(fft(data[start:stop]))
    spectre = spectre/spectre.max()
    n = spectre.size
    freq = np.zeros(n)
    for k in range(n):
        freq[k] = 1.0/n*rate*k
    vlines(freq,[0],spectre,'r')
    xlabel('f (Hz)')
    ylabel('A')
    axis([0,0.5*rate,0,1])



figure(figsize=(12,4))
tracerSpectre(data,rate,0.0,duree)

show()
