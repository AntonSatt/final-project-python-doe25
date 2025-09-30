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