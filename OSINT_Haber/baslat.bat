@echo off
title Bolgesel Haber OSINT Araci
color 0B

echo =========================================
echo    OSINT Haber Araci Baslatiliyor...
echo =========================================
echo.

:: Python'un tam yolu tanimlaniyor
set PYTHON_EXE="C:\Users\Eren Furkan\AppData\Local\Python\pythoncore-3.14-64\python.exe"

:: Gerekli kütüphanelerin kontrolü ve kurulumu
echo [1/3] Python kutuphaneleri kontrol ediliyor...
%PYTHON_EXE% -m pip install flask requests >nul 2>&1

:: Tarayıcıyı 3 saniye gecikmeli açması için arka planda bir komut tetikliyoruz
echo [2/3] Tarayici arayuzu hazirlaniyor...
start cmd /c "timeout /t 3 >nul & start http://127.0.0.1:5050"

:: Sunucuyu bu pencerede çalıştırıyoruz
echo [3/3] Sistem aktif! Kapatmak icin bu pencereyi (X) ile kapatiniz.
echo.
%PYTHON_EXE% app.py

pause