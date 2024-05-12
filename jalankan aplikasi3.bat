@echo off
echo ini adalah file bat yang saya buat DODIMAN TAKIMPOO
pause

cmd /k "d:\projects\myenv\scripts\activate.bat && python -m flask --app app.py run --debug"