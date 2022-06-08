import pyvisa as pv
"""
Attention!!!

The code is tested on the PMA-X Network Analyzer N5245B 10Mhz-50GHz
If you have another type instrument, please modify its code according to this.

Thanks to pyvisa community, please ref https://pyvisa.readthedocs.io/en/latest/index.html.
Author: Wangjianyang
"""
rm = pv.ResourceManager() #resourcemanager
pna = rm.open_resource('TCPIP::192.168.0.1::INSTR') #build connect with PNA
fd = pna.query('*IDN?') #query the IDN of the PNA
print(fd)               #if you get a response, the connect is successful
pna.write('INIT:CONT OFF') #sweep at once, if you want to sweep all the time, you can set it as on.

"""Vaule Setting"""
start_frequency = 8.3E9
stop_frequency = 12.3E9
num_frequency = 128
power = 15 #dBm
# sweep_delay = 0

"""Parameter Setting"""
pna.write('SENSe:FREQuency:STARt ' + str(start_frequency))  # 中心频率
pna.write('SENSe:FREQuency:STOP ' + str(stop_frequency))  # 频率宽带
pna.write('SENSe:SWEep:POINts ' + str(num_frequency))  # 频率宽带
# pna.write('SENS:SWE:DWEL:SDEL '+str(sweep_delay))  #the delay time of sweep

"""Measurement Setting"""
pna.write('CALCulate1:MEASure1:PARameter "S21"')  # 第一条默认曲线测试改为S21
pna.write('DISPlay:MEASure1:Y:AUTO')  #autodisplay
pna.timeout = 30000 #ms
# pna.baud_rate = 57600
pna.write('CALCulate1:MEASure1:FORMat MLINear')  #which format you want to see (eg. Phase、delay..)

"""Power and Sweep mode Setting"""
pna.write('SOURce1:POWer1 '+str(power)) #power strengrh
pna.write('OUTP ON')   #power on
pna.write('INIT')  # 开始扫描 start sweep
pna.query('*OPC?')  # *OPC?同步，询问扫描是否完成
print('Sweep has been finished.')

"""Save file parts
You should save data file twice because the first save is to save the last data, 
you can choose discard the first data.
"""
pna.write('MMEMory:STORe:DATA "G:/diff_SNR/trash.csv", "CSV FORMatted Data","Trace","RI",1')
pna.write(f'MMEMory:STORe:DATA "G:/diff_SNR/power_{power}_dBm.csv", "CSV FORMatted Data","Trace","RI",1')
print('Experimental data has been saved in U disk')

pna.close()   #close pna connect
rm.close()    #close resource management

# pna.write('CALC:MEAS:FORM REAL') #set up real part
# traceASC = pna.query_binary_values('CALCulate1:Measure1:DATA:FDATA?', container=np.array)
# print(traceASC)
#7.03 6.70
# pna.write('CALC:MEAS:FORM REAL') #set up real part
# traceASC = pna.read('calculate1:measure1:data:sdata data(ri)')
# print(traceASC)

# pna.write('CALC:MEAS:FORM REAL') #set up real part
# traceASC = pna.query_binary_values('CALCulate1:Measure1:DATA:FDATA?', container=np.array)
# print(traceASC)
#
#
# pna.write('CALC:MEAS:FORM IMAGinary') #set up imaginary part
# traceASC = pna.query_binary_values('CALCulate1:Measure1:DATA:FDATA?', container=np.array)
# print(traceASC)

# imag = pna.query_ascii_values('CALC:MEAS:FROM IMAGinary')
