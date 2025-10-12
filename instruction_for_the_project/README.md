# Systemutveckling i Python
## Individuell slutuppgift

### Deadline
- **Inlämning av kod (GitHub-länk) och rapport (PDF)**: 24/10
- **Presentationer**: 27/9 + 29/9 (bokas separat)

### Beskrivning
Slutuppgiften går ut på att utveckla en övervakningsapplikation i Python. Applikationen samlar in information från operativsystemet (t.ex. CPU-användning, minnesanvändning och diskanvändning) och presenterar den för användaren via en konsolbaserad meny.

Användaren interagerar med applikationen genom en konsolmeny för att hämta information. Inga konfigurerade larm aktiveras under interaktion med menyn.

### Krav för godkänd nivå (G)
Applikationen startas och presenterar en huvudmeny med fem alternativ:

1. **Starta övervakning**  
   Startar övervakning av CPU-användning, minnesanvändning och diskanvändning. Övervakning startar **inte** automatiskt vid programstart.

2. **Lista aktiv övervakning**  
   Visar aktiv övervakning och nuvarande status. Om ingen övervakning är aktiv visas en meddelandetext. Annars visas t.ex.:  
   ```
   CPU-användning: 35%
   Minnesanvändning: 65% (4.2 GB av 8 GB använt)
   Diskanvändning: 80% (400 GB av 500 GB använt)
   ```  
   Efter visning promptas användaren:  
   ```
   Tryck valfri tangent för att gå tillbaka till huvudmeny
   ```  
   Därefter återvänder till huvudmenyn.

3. **Skapa larm**  
   Öppnar en undermeny för att konfigurera larm inom tre områden eller återgå till huvudmenyn:  
   ```
   Konfigurera larm
   1. CPU-användning
   2. Minnesanvändning
   3. Diskanvändning
   4. Tillbaka till huvudmeny
   ```  
   Vid val av område anges en procentuell nivå (0–100) för larmaktivering, t.ex.:  
   ```
   Ställ in nivå för alarm mellan 0-100.
   ```  
   Bekräftelse visas, t.ex.:  
   ```
   Larm för CPU-användning satt till 80%.
   ```  
   Nivån måste vara en siffra mellan 1–100. Felaktig input ger felmeddelande. Därefter återvänder till huvudmenyn.

4. **Visa larm**  
   Listar alla konfigurerade larm, sorterade på typ. Exempel:  
   ```
   CPU-larm 70%
   Disklarm 95%
   Minneslarm 80%
   Minneslarm 90%
   ```  
   Notera: Flera larm av samma typ är tillåtna.  
   Efter visning promptas användaren:  
   ```
   Tryck valfri tangent för att gå tillbaka till huvudmeny
   ```

5. **Starta övervakningsläge**  
   Startar ett loopande övervakningsläge. Användaren informeras:  
   ```
   Övervakning är aktiv, tryck på valfri tangent för att återgå till menyn.
   ```  
   Meddelandet upprepas med jämna mellanrum. Om ett larm triggas visas t.ex.:  
   ```
   ***VARNING, LARM AKTIVERAT, CPU-ANVÄNDNING ÖVERSTIGER 80%***
   ```

#### Icke-funktionella krav för G-nivå
- Programmet ska bestå av **minst flera filer** med aktivt använd kod (inte allt i en fil).
- Använd **objektorienterad programmering (OOP)** där det passar.
- Använd **funktioner** för logik.
- Inkludera **funktionell programmering** på minst ett ställe (t.ex. sortering av larm).
- Koden ska vara **välskriven**: Lättlästa variabel- och funktionsnamn, kommentarer vid behov, bra struktur.
- Koden ska vara **bugfri** och hantera **felaktig input** (t.ex. nonsens) utan krasch – implementera rimlig input-sanitization.

### Krav för väl godkänd nivå (VG)
Utöver G-kraven läggs tre funktioner till:

1. **Loggning**  
   Alla händelser loggas till en fil, inklusive programstart, användarinput och konfigurationsändringar. Format: `Datum_Tid_Logg`, t.ex.:  
   ```
   20/9/2024_15:05_CPU_Användningslarm_Konfigurerat_80_Procent
   20/9/2024_15:09_Övervakningsläge_startat
   20/9/2024_15:16_CPU_Användningslarm_aktiverat_80_Procent
   ```

2. **Ta bort larm**  
   Nytt menyval som listar konfigurerade larm. Användaren väljer ett att ta bort via siffra, t.ex.:  
   ```
   Välj ett konfigurerat larm att ta bort:
   1. CPU-larm 70%
   2. Minneslarm 80%
   3. Minneslarm 90%
   4. Disklarm 95%
   ```  
   Efter borttagning återvänder till huvudmenyn.

3. **Persistens för larm**  
   Larm sparas i ett filformat (t.ex. JSON) och laddas vid start med meddelande:  
   ```
   Loading previously configured alarms...
   ```  
   Vid visning av larm inkluderas både nya och laddade larm.

#### Icke-funktionella krav för VG-nivå
- Alla G-krav plus: **Mycket välskriven kod** med utmärkt struktur, kommentarer och logghantering.  
  Exempel:  
  - Vid flera larm av samma typ aktiveras endast det **närmaste** (t.ex. vid 95% CPU aktiveras inte 60%/70% om 80% finns).  
  - Loggfiler skapas dynamiskt vid varje programstart (namngivna efter datum/tid) och fylls på under körning.

### Valfria tillägg (plus i kanten)
- **E-post vid larm**: Skicka e-post vid aktiverat larm (tips: Använd SendGrid – gratis registrering på sendgrid.com). Bibliotek:  
  ```python
  from sendgrid import SendGridAPIClient
  from sendgrid.helpers.mail import Mail
  ```
- **Versionshantering**: Använd GitHub med trunkbaserad utveckling och feature branches för varje ny funktionalitet (rekommenderas för alla nivåer).
- **Grafiskt gränssnitt (GUI)**: Ett enkelt GUI som visar aktiva larm och realtidsprocentuella nivåer.