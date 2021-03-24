set day=0
echo >"%temp%\%~n0.vbs" s=DateAdd("d",%day%,now) : d=weekday(s)
echo>>"%temp%\%~n0.vbs" WScript.Echo year(s)^& right(100+month(s),2)^& right(100+day(s),2)
for /f %%a in ('cscript /nologo "%temp%\%~n0.vbs"') do set "result=%%a"
del "%temp%\%~n0.vbs"
set "YYYY=%result:~0,4%"
set "MM=%result:~4,2%"
set "DD=%result:~6,2%"

F:
cd spartan_fdrs
cd data
md titik_hotspot
cd titik_hotspot
mkdir %yyyy%%mm%%dd%
cd %yyyy%%mm%%dd%
mkdir indonesia
cd indonesia

wget -q http://satelit.bmkg.go.id/IMAGE/HOTSPOT/Hotspot_Indonesia.txt -O /spartan_fdrs/data/titik_hotspot/%yyyy%%mm%%dd%/indonesia/hotspot_%yyyy%%mm%%dd%_indonesia.txt

F:
cd F:/spartan_fdrs/
py -3 F:/spartan_fdrs/HOTSPOT_JSON_INDO.py

pause