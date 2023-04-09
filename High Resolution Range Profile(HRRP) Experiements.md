# High Resolution Range Profile(HRRP) Experiements
Python implementation of SCPI Instruments to control an PMA-X Network Analyzer(N5245B 10MHz-50GHz).

>The Standard Commands for Programmable Instruments (SCPI; often pronounced "skippy") defines a standard for syntax and commands to use in controlling programmable test and measurement devices, such as automatic test equipment and electronic test equipment.

## Connect
The network analyzer needs to be connected to the PC via the Ethernet port and both need to be configured in the same network segment.

## Install dependent libraries
```bash
# build a new conda environment by conda
conda create -n Pyvisa python=3.8
# activate the environment
conda activate Pyvisa 
# install the packages in requirements.txt
python -m pip install -r requirements.txt
```

## File analysis by [==Academic_ChatGPT==](https://github.com/binary-husky/chatgpt_academic)
| File Name| Main Function | 
| --- | --- | 
|pna_ctl.py |Connects to PNA, sets experiment parameters, collects data, and saves data to csv files | 
|conventcsv2mat.py | Reads CSV format data in a specified folder, converts it to MAT format, and plots frequency domain images |

## License
[MIT](./LICENSE)
