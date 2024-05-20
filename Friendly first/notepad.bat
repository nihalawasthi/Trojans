@echo off
powershell -Command "notepad"
cd %TEMP%
Powershell -Command "Invoke-WebRequest 'https://raw.githubusercontent.com/nihalawasthi/Trojans/main/Friendly%20first/prank.txt' -OutFile prank.txt"
powershell -Command "cat prank.txt"
