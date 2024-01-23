import demopack.screens as sc
import demopack.const as con

# создать объекты
samsung_4k = sc.Screen('Samsung UE43AU7170UXRU',con.SMART_TV,con.UHD_WIDTH,con.UHD_HEIGHT)
teclast = sc.Screen('Teclast P20HD',con.PLANCHETEE,con.FHD_WIDTH,con.FHD_HEIGHT)
smartphone = sc.Screen('BQ-5560L',con.SMARTPHONE,con.HD_WIDTH,con.HD_HEIGHT)
gamescrren = sc.Screen('AOC CQ27G3SU', con.SMARTPHONE,con.UHD_6K_WIDTH,con.UHD_6K_HEIGHT)

# вывести информацию об устройствах
print(samsung_4k)
print(teclast)
print(smartphone)
print(gamescrren)