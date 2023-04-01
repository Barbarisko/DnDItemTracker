## Reminders

### To create env

    python -m venv venv
    python -m pip install -r .\backend\requirements.txt

### To activate env  

    . venv/bin/activate

or

    & c:/Users/kosti/source/repos/DnDItemTracker/.venv/Scripts/Activate.ps1

or in vscode:

> ctrl + shift + p
> Python: Select Interpretor

### To start in dev mode 

    flask --app .\backend\main run 

### To start in rel mode 

    waitress-serve backend.main:app