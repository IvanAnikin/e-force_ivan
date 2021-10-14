#  Pokročilý nováčkovský úkol
### Téma
- práce s CanDB
- zpracování a vizualizace dat z INS

*INS - Inercial navigation system*


### Úkoly
Výsledkem práce by měl být
- graf trajektorie formule
    - barva trajektorie bude závislá na rychlosti
    - vyznačit body ve kterých formule zrychlovala
    - vyznačení nejistot v estimaci trajektorie
- počet kol, které formule ujela (algoritmus, ne hardcoded číslo)
- průměrný čas kola
- nejrychlejší kolo
- Kreativitě se meze nekladou

### Použití CanDB
-Rozpoznávání zpráv pomocí ID
    Každé ID reprezentuje zprávu s nějakým typem
    Tyto typy jsou definovány v souboru D1.json
Například pro přístup k první zprávě o pozici formule
`data[id][i-tá zpráva][1 pro data, 0 pro timestamp][název informace]`
`latitude = double(data[134][0][1]['Latitude'])`
`longitude = double(data[134][0][1]['Longitude'])`
`timestamp = data[134][0][0]`
je dobré specifikovat datový typ informace

### Typy zpráv a ID
- Pozice formule id: 134
    - *Latitude* - zeměpisná šířka v [°] 
    - *Longitude* - zeměpisná výška v [°]
- Přesnost pozice id: 136
    - *Latitude_acc* - přesnost zeměpisné šířky v [m]
    - *Longitude_acc* - přesnost zeměpisné výšky [m]
    - *Altitude_acc* - přesnost nadmořské výšky [m]
- Rychlost formule id: 139
    - *VELOCITY_X* - rychlost v ose X v [m/s]
    - *VELOCITY_Y* - rychlost v ose Y v [m/s]
    - *VELOCITY_Z* - rychlost v ose Z v [m/s]




### Tipy na knihovny
- [Matplotlib](https://matplotlib.org/)
- [Plotly](https://plotly.com/python/)



