PyInstaller main.py --clean --console --onefile --distpath Windows
wsl python -m PyInstaller main.py --clean --onefile --distpath Linux
rmdir build /S /Q
del main.spec