set day=0
echo >"%temp%\%~n0.vbs" s=DateAdd("d",%day%,now) : d=weekday(s)
echo>>"%temp%\%~n0.vbs" WScript.Echo year(s)^& right(100+month(s),2)^& right(100+day(s),2)
for /f %%a in ('cscript /nologo "%temp%\%~n0.vbs"') do set "result=%%a"
del "%temp%\%~n0.vbs"
set "YYYY=%result:~0,4%"
set "MM=%result:~4,2%"
set "DD=%result:~6,2%"


F:
cd fdrs_bmkg
cd data
md titik_hotspot
cd titik_hotspot
mkdir %yyyy%%mm%%dd%
cd %yyyy%%mm%%dd%
mkdir pagi
cd pagi
wget http://satelit.bmkg.go.id/IMAGE/HOTSPOT/2020/08/hotspot_%yyyy%%mm%%dd%.txt


F:
cd F:/fdrs_bmkg/
py -2 F:/fdrs_bmkg/TXT_TO_JSON_SATELITBMKG.py

pause