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
Například pro přístup k zprávě o pozici formule (0x134)
`data[id][i-tá zpráva][1 pro data, 0 pro timestamp][název informace]`
`latitude = double(data[134][0][1]['Latitude'])`
`longitude = double(data[134][0][1]['Longitude'])`
`timestamp = data[134][0][0]`
je dobré specifikovat datový typ informace

### Typy zpráv a ID
- Akcelerace z IMU (id: 0x121)
    - *Accel_X* - akcelerace v ose X v [m/s^2]
    - *Accel_Y* - akcelerace v ose Y v [m/s^2]
    - *Accel_Z* - akcelerace v ose Z v [m/s^2]
- Zatáčení formule z IMU (id: 0x122)
    - *Gyro_X* - rychlost otáčení vzhledem k ose X v [°/s]
    - *Gyro_Y* - rychlost otáčení vzhledem k ose Y v [°/s]
    - *Gyro_Z* - rychlost otáčení vzhledem k ose Z v [°/s]
- Orientace formule/Kvaterniony z EKF (id: 0x131)
    - *Q0* - komponent Q0 kvaternionu orientace
    - *Q1* - komponent Q1 kvaternionu orientace
    - *Q2* - komponent Q2 kvaternionu orientace
    - *Q3* - komponent Q3 kvaternionu orientace
    - 3D orientace reprezentovaná normalizovaným kvaternionem Q = (Q0, Q1, Q2, Q3)
    - Pochoutka pro matematické gurmány
- Orientace formule/Eulerovy úhly z EKF(id: 0x132)
    - *Roll* - úhel mezi -180° až 180° v [°]
    - *Pitch* - úhel mezi -90° až 90° v [°]
    - *Yaw* - úhel mezi -180° až 180° v [°]
- Přesnost orientace formule z EKF (id: 0x133)
    - *Roll_acc* - úhel mezi 0° až 90° v [°]
    - *Pitch_acc* - úhel mezi 0° až 45° v [°]
    - *Yaw_acc* - úhel mezi 0° až 90° v [°]
- Pozice formule z EKF (id: 0x134)
    - *Latitude* - zeměpisná šířka v [°] 
    - *Longitude* - zeměpisná výška v [°]
- Přesnost pozice z EKF (id: 0x136)
    - *Latitude_acc* - přesnost zeměpisné šířky v [m]
    - *Longitude_acc* - přesnost zeměpisné výšky [m]
    - *Altitude_acc* - přesnost nadmořské výšky [m]
- Rychlost formule ke kompasovým osám z EKF (id: 0x137)
    - *Velocity_N* - rychlost severním směrem v [m/s]
    - *Velocity_E* - rychlost východním směrem v [m/s]
    - *Velocity_D* - rychlost směrem dolů v [m/s]
- Přesnost rychlosti formule z předešlé zprávy z EKF (id: 0x138)
    - *Velocity_acc_N* - přesnost rychlosti severním směrem v [m/s]
    - *Velocity_acc_E* - přesnost rychlosti východním směrem v [m/s]
    - *Velocity_acc_D* - přesnost rychlosti směrem dolů v [m/s]
- Rychlost formule z EKF (id: 0x139)
    - *VELOCITY_X* - rychlost v ose X v [m/s]
    - *VELOCITY_Y* - rychlost v ose Y v [m/s]
    - *VELOCITY_Z* - rychlost v ose Z v [m/s]




### Tipy na knihovny
- [Matplotlib](https://matplotlib.org/)
- [Plotly](https://plotly.com/python/)



