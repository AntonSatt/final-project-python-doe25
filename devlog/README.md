# Dev Log
### My thoughts and things I had to tackle with during this project. 
### 29th of September 2025
- Har förstått hur man använder psutil för att få fram CPU, RAM-minne och hårddisk data. 
- Har tänkt lite på hur man ska köra övervakningen i bakgrunden, threading?
    - Använde mig av threading för att få det att fungera i bakgrunden i monitoring.py, läste också om daemon för att köra threading där den avslutas om programmet avslutas utan att vänta på den. Tror man mest kör utan daemon om man ska typ ladda upp en fil och inte vill att det ska avslutas eller liknande. 
- Måste förstå mig på lite mer hur klasser fungerar i Python då det verkar vara bra för att köra olika funktioner.
    - La till en class i monitoring.py för att det ska bli enklare att hålla koll på funktionerna och variablerna. 
- Skapade en utils.py fil för ofta användna funktioner så de inte ligger och skräpar och tar upp plats i main eller annanstans. 