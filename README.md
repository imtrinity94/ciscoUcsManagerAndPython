# Starters for working with Cisco UCS Manager Python SDK

* In a Windows machine, Open Powershell.
* Install lastest version of python from https://www.python.org/downloads/
* Download latest uscsdk.zip from https://github.com/CiscoUcs/ucsmsdk/releases/
* In a Windows machine, Open Powershell and,
* Install ucssdk using 
```
pip install \full\path\to\ucssdk.zip
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
* For starters, try to fetch some information about class computeBlade by taking reference from [Cisco UCS Python SDK Unofficial Guide.pdf](https://github.com/imtrinity94/ciscoUcsManagerAndPython/blob/5d2e60a28ba35c1bb5b9fb7603276f6a14887130/Cisco%20UCS%20Python%20SDK%20Unofficial%20Guide.pdf)
```python
blades = handle.query_classid("computeBlade")
print(len(blades))
for blade in blades:
    print(blade.model,blade.serial,blade.dn)
```
will print
```
6
UCSB-B200-M5 FLP2507012N sys/chassis-1/blade-5
UCSB-B200-M5 FLM240867CF sys/chassis-1/blade-3
UCSB-B200-M5 FLM2406A8M9 sys/chassis-1/blade-2
UCSB-B200-M5 FLM2501004J sys/chassis-1/blade-4
UCSB-B200-M5 FLM2X050245 sys/chassis-1/blade-1
UCSB-B200-M5 FLMD90701A3 sys/chassis-1/blade-6
```
*Find this file at [here](https://github.com/imtrinity94/ciscoUcsManagerAndPython/blob/ac33a7b028a3b1301b182b268c6b5588057aa08c/get_blade_info.py)*
* More advanced operations and classes are mentioned in [Cisco UCS Python SDK Official Guide for 0.8.3.pdf](https://github.com/imtrinity94/ciscoUcsManagerAndPython/blob/5d2e60a28ba35c1bb5b9fb7603276f6a14887130/Cisco%20UCS%20Python%20SDK%20Official%20Guide%20for%200.8.3.pdf)



