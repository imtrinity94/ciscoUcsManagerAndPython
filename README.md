# Starters for working with Cisco UCS Manager Python SDK

* In a Windows machine, Open Powershell.
* Install lastest version of python from https://www.python.org/downloads/
* Download latest uscsdk from https://github.com/CiscoUcs/ucsmsdk/releases/
* In a Windows machine, Open Powershell and,
* Install ucssdk using
```
pip install \full\path\to\ucssdk.zip or tar.gz
```
* Copy\Download the skeleton_file.py from https://github.com/imtrinity94/ciscoUcsManagerAndPython/blob/main/skeleton_file.py
* Go to that file directory where you saved the skeleton_file.py and run
```
python .\skeleton_file.py
```
* If Authorization is done, the outcome will be similar to
```
PS C:\Users\temp\pyapi> python .\skeleton_file.py
<ucsmsdk.ucshandle.UcsHandle object at 0x0000020688073128>
```
* Now that you connection made, try to perform other operation by edit the YOUR CODE in skeleton_file.py with desired code.
* For starters, try to fetch some information about LsServer by taking reference from this file https://github.com/imtrinity94/ciscoUcsManagerAndPython/blob/main/Cisco%20UCS%20Python%20SDK%20Unofficial%20Guide.pdf
* More advanced operations and classes are mentioned in https://github.com/imtrinity94/ciscoUcsManagerAndPython/blob/main/Cisco%20UCS%20Python%20SDK%20Official%20Guide%20for%200.8.3.pdf



