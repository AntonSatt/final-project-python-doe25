# Dev Log
### My thoughts and things I had to tackle with during this project. 
### 29th of September 2025
- Har förstått hur man använder psutil för att få fram CPU, RAM-minne och hårddisk data. 
- Har tänkt lite på hur man ska köra övervakningen i bakgrunden, threading?
    - Använde mig av threading för att få det att fungera i bakgrunden i monitoring.py, läste också om daemon för att köra threading där den avslutas om programmet avslutas utan att vänta på den. Tror man mest kör utan daemon om man ska typ ladda upp en fil och inte vill att det ska avslutas eller liknande. 
- Måste förstå mig på lite mer hur klasser fungerar i Python då det verkar vara bra för att köra olika funktioner.
    - La till en class i monitoring.py för att det ska bli enklare att hålla koll på funktionerna och variablerna. 
- Skapade en utils.py fil för ofta användna funktioner så de inte ligger och skräpar och tar upp plats i main eller annanstans. 

### 30th of September 2025
- Jobbar vidare med projektet, känner att jag är lite bättre på klasser nu och köra med samma still i nya filen alarm.py fungerar bra!
- Fick tänkte till lite när jag körde massa funktioner och att det ska ha 'self' i sig när använder sig klasser. 
- I projektet står det också att man ska kunna gå vidare när man trycker "any key", det var en google/ai sökning på det då det är lite mer komplicerat än att köra input(). Fick till det så att den kollar om man kör Windows eller Unix (Linux & Mac), samma som i clear_console funktionen. Fungerar bra. 
- Jag är också ganska nöjd att jag fick till en bra funktion som fungerar för alla larm även om det är CPU, RAM, hårddisk som ska kollas. Så man inte behöver 3 funktioner för varje typ.
- Hoppsan märkte att man skulle kunna flera av samma larm. Så behöver bygga om alarm.py lite, tror det är smart att köra listor för en variable för alarm. Så vi kan ha flera alarm.
- Får jobba vidare imorgon med att skriva ut alarm-listan klart. 

### 1st of October 2025
- Lärde mig använda tree i terminalen för att få fram kodstrukturen, exempel: <br>
```tree -L 2  -I venv > repo_structure.md``` <br>
-L 2 är att den inte går djupare än 2 "layers", -I är att ignorera en directory, > är för att spara resultatet till en fil. 

### 2nd of October 2025
- Försöker göra klart projektet, men får inte riktigt till 5:an (Övervakningsystemet), får köra vidare lite senare. 

### 3rd of October 2025
- Känner att jag är klar med projektet för G iaf. Nu är det bara att jobba och testa och fixa det för VG. 3 veckor från idag till uppgiften ska lämnas in så det känns bra. 
- Jag Kom på att jag inte behöver treading eller liknande till sista uppgiften då data ändå bara uppdateras var 10 sekund. Så kör en enkel while loop var 10:e sekund och kollar om några larm går. 
Största problemet jag hade var att hitta en lösning hur man får så att man trycka "any key" när man vill så går man tillbaka till huvudmenyn. Får läsa på lite mer om det, hittade en lösning när jag googlade och körde AI. Men förstår inte riktigt. Känns ganska advancerad lösning. Tänk att det ska vara så komplicerat att få till en sån sak som låter enkel. 

### 5th of October 2025
- Idag fixade jag loggar, vilket var väldigt lätt. Import logging och så sätter man in hur och var man vill spara sin log-fil och i vilket sorts format den ska skriva ut, datum och sånt. Sedan var det bara att sätta in en loggning under varje print-text man ville att den skulle logga. Gick riktigt smidigt. 
- Gjorde också "Ta bort larm" vilket var mycket svårare än jag trodde. Satt ganska länge och tänkte hur man skulle göra på bästa sätt. Problemet är att det är 3 listor man har av olika larm. Så hur ska man skriva ut allt i en lista för att sedan låta användaren skriva in den siffra han vill ha. Kollade runt lite och förstod att ett bra sätt är att slå ihop de 3 listorna till en temperär lista för alla larm. Sedan printar man ut den med hjälpa av ```enumerate```som gör att man kan lägga till en siffra för talen innan. Sedan ser det bra ut för användaren och de kan välja vad de vill ta bort. 
- Att ta bort var ganska komplicerat, blir att läsa på lite mer om detta. 

### 11th of October 2025
- Lärde mig att man inte ska använda sig av funktioner som print() i classer, så nu har jag spenderat lång tid att bygga om mitt program från grunden och ta bort att print() och loggning jag hade i metoder förut. Det ser mycket bättre ut och gick ändå ganska snabbt.
- Är nästan tillbaka där jag var förut, men nu känns det bättre. 
- Jag tog också bort threading då jag inte riktigt förstår det ännu och så behövdes det inte i koden. 
- Ska försöka göra klart upp till VG imorgon. Sedan efter det är det bara presentationen och en rapport kvar. 