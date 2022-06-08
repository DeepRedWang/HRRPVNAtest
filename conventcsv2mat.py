import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class Dataconvent:
    def __init__(self, frompath, topath=None):
        self.from_path = frompath
        self.to_path = topath

    def csv2mat(self):
        csvdata = pd.read_csv(self.from_path)
        a = csvdata['!CSV A.01.01'].index[5:-1].to_numpy()
        real = []
        img = []
        for i in a:
            real.append(i[1])
            img.append(i[2])
        real = np.array(real, dtype=np.double)
        img = np.array(img, dtype=np.double)
        data = real+1j*img
        HRRP = np.fft.ifft(data)
        plt.plot(20*np.log(np.absolute(HRRP)/np.max(np.absolute(HRRP))))
        plt.title('Airplane HRRP')
        plt.xlabel('Frequency Point')
        plt.ylabel('Energy')
        plt.show()

# frompath = 'D:\C919HRRPLinmag_8.3G12.3G05131024realimag.csv'        #0dBm
# frompath = 'D:\C919HRRP_LogMag_10_dBm_8.3G12.3G05131146realimag.csv'  #10dBm
frompath = 'D:\diff_SNR\power_-15_dBm.csv'  #15dBm
dataconv = Dataconvent(frompath)
dataconv.csv2mat()