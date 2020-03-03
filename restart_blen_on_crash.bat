@echo off
:start
start /w C:\Blends\Blender281\blender.exe -b filename.blend -s 35 -e 200 -o c:\root\to_yourfile_ -a
goto start
