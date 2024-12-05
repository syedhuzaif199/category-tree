@echo off
echo Installing dependencies...

:: Ensure pip is installed
python -m ensurepip --default-pip

:: Upgrade pip
python -m pip install --upgrade pip

:: Install dependencies
python -m pip install graphviz Faker

echo Installation complete.
pause
