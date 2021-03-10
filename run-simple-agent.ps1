${env:PYTHONPATH}='./src'
& venv/Scripts/Activate.ps1
faust -A simple_agent worker -l info