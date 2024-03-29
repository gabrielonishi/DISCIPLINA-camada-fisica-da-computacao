
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal as window

class signalMeu:
    def __init__(self):
        self.init = 0

    def generateSin(self, freq, time, fs, amplitude=1):
        """
        Gera um sinal a partir dos parâmetros enviados
        
        Parâmetros:
         - freq: frequência da onda
         - time: quanto tempo durará o sinal
         - fs: taxa de amostragem (Hz)
        """
        n = time*fs
        x = np.linspace(0.0, time, n)
        s = amplitude*np.sin(freq*x*2*np.pi)
        return (x, s)

    def calcFFT(self, signal, fs):
        """
        Calcula a fast-fourier-function para um sinal

        Parâmetros;
         - signal: sinal recebido
         - fs: taxa de amostragem (Hz)
        """
        # https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html
        N  = len(signal)
        W = window.hamming(N)
        T  = 1/fs
        xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
        yf = fft(signal*W)
        return(xf, np.abs(yf[0:N//2]))

    def plotFFT(self, signal, fs):
        x,y = self.calcFFT(signal, fs)
        plt.figure()
        plt.plot(x, np.abs(y))
        plt.title('Fourier')
