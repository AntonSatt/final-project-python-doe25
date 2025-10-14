# Systemutveckling i Python – Individuell slutuppgift

## Studentinformation
**Namn: Anton Sätterkvist**  
**Klass: DOE25**  
**Datum: 14 Oktober 2025**  
**GitHub-länk till projektet: https://github.com/AntonSatt/final-project-python-doe25**  

---

## 1. Inledning
Beskriv kortfattat vad uppgiften gick ut på.

**Exempel:**
I denna uppgift har jag utvecklat en övervakningsapplikation i Python som samlar in systeminformation och visar den i terminalen. Programmet kan starta övervakning, visa status, skapa och visa larm, samt hantera övervakningsläge.

Syftet är att visa hur man kan använda Python för systemutveckling inom DevOps, med fokus på struktur, funktioner och objektorientering.

---

## 2. Planering och design
- Hur planerade du arbetet?
- Hur började du?
- Hur delade du upp uppgiften i delar (funktioner eller klasser)?
- Skissade du meny/flödesschema?

**Exempel:**
Jag började med att läsa igenom kravspecifikationen och dela upp den i fem huvuddelar: starta övervakning, visa status, skapa larm, visa larm och starta övervakningsläge.  
Jag ritade sedan ett enkelt flöde över hur användaren navigerar i menyn och vilka funktioner som behövs.

---

## 3. Programstruktur
Beskriv hur din kod är uppbyggd:
- Vilka filer består programmet av?
- Hur är klasser och funktioner organiserade?
- Hur kommunicerar de med varandra?

**Exempel:**
Programmet är uppdelat i flera filer.  
`main.py` innehåller huvudmenyn och startpunkten.  
`Monitor` ansvarar för att läsa systeminformation.  
`Alarm` hanterar larm, och `AlarmManager` håller reda på alla aktiva larm.

---

## 4. Viktiga funktioner eller klasser
Välj 2–3 centrala delar av din kod och beskriv dem mer i detalj:
- Vad gör de?
- Varför implementerade du dem så?

**Exempel:**
`Monitor.get_system_status()` använder psutil för att hämta CPU-, minnes- och diskanvändning.  
Jag valde att använda en klass för att kunna återanvända samma kod både i menyn och i övervakningsläget.

---

## 5. Bibliotek och verktyg
Lista vilka bibliotek du använde och till vad.

**Exempel:**
- `psutil` – läsa systemresurser  
- `os` – filhantering  
- `json` – spara/läsa larm  
- `time` – loopar i övervakningsläge  
- `logging` – loggning (VG)

Beskriv även hur du versionshanterade projektet med Git och GitHub.

---

## 6. Testning och felsökning
- Hur testade du programmet?
- Testade du olika användarinmatningar?
- Hanterade du buggar/fel?

**Exempel:**
Jag testade alla menyval manuellt genom att köra programmet i terminalen.  
Jag använde `try/except` för att undvika krascher vid felaktig inmatning.  
Jag lade till `print()` i början för att förstå flödet innan jag bytte till loggning.

---

## 7. Resultat
- Vad fungerar bra?
- Finns det delar du är extra nöjd med?

**Exempel:**
Jag är nöjd med hur programmet hanterar flera larm samtidigt och sorterar dem korrekt.  
Loggningen fungerar som tänkt och skapar en ny loggfil vid varje start.

---

## 8. Reflektion och lärdomar
Vad har du lärt dig under projektet?
- Om Python/programmering
- Om att strukturera kod
- Om testning, Git och arbetsflöden

**Exempel:**
Jag har lärt mig hur klasser gör program mer strukturerade och lättare att underhålla.  
Jag har förstått vikten av att planera innan man börjar koda och att använda Git ofta.

---

## 9. Möjliga förbättringar och vidareutveckling
Om du hade mer tid – vad skulle du vilja lägga till eller förbättra?

**Exempel:**
Jag skulle vilja lägga till e-postnotifiering vid aktiverat larm och ett GUI med tkinter.  
Jag skulle också vilja skriva enhetstester för vissa funktioner.

---

## 10. Sammanfattning
En kort summering av projektet (2–4 meningar):

Projektet visar hur man kan använda Python för att skapa en enkel men effektiv övervakningsapplikation.  
Jag har tillämpat objektorientering, filhantering, felhantering och versionshantering i praktiken.

---
