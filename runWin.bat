@echo off
echo Activating the Virtual Environment...
call venv\Scripts\activate.bat

echo Running the Application...
python market/manage.py runserver

echo Visit the application in your web browser at http://localhost:8000/.