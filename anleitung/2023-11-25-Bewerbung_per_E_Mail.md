# Bewerbung per E-Mail

## Zielsetzung
Das Skript soll automatisch Bewerbungen per E-Mail versenden. Dazu werden die Adressen der Empfänger aus einer CSV-Datei eingelesen und der Brieftext aus einer Textdatei. Der Brieftext wird personalisiert und als PDF-Datei erstellt. Optional kann die Bewerbung auch direkt per E-Mail versendet werden.

## Grundgedanke
Das Skript liest die Adressen der Empfänger aus einer CSV-Datei ein und den Brieftext aus einer Textdatei. Anschließend wird für jeden Empfänger der Brieftext personalisiert und als PDF-Datei erstellt. Optional kann die Bewerbung auch direkt per E-Mail versendet werden.

## Durchführungsschritte
1. Einlesen der Adressen aus der CSV-Datei "Adressen.csv"
2. Einlesen des Brieftextes aus der Textdatei "Brieftext.txt"
3. Für jeden Empfänger:
   - Personalisierung des Brieftextes mit den Daten aus der CSV-Datei
   - Erstellung eines PDF-Dokuments mit dem personalisierten Brieftext und optionalen Anhängen (Lebenslauf, Zeugnisse)
   - Speicherung des PDF-Dokuments unter einem Dateinamen, der Sonderzeichen ersetzt
   - Optional: Versenden der Bewerbung per E-Mail an den Empfänger

## Anforderungen
- Python 3.x
- Installierte Pakete: `csv`, `fpdf`, `PyPDF2`, `smtplib`, `ssl`

## Beispiel
### Adressen.csv
```
Firmenname;Emailadresse;Ansprechpartner;Straße;PLZ;Ort;Anrede;Stellenbezeichnung
Firma A;info@firma-a.de;Herr Müller;Musterstraße 1;12345;Musterstadt;Sehr geehrter Herr;Softwareentwickler
Firma B;info@firma-b.de;Frau Schmidt;Musterstraße 2;54321;Musterstadt;Sehr geehrte Frau;Projektmanager
```

### Brieftext.txt
```
Sehr {Anrede} {Ansprechpartner},

hiermit bewerbe ich mich auf die Stelle als {Stellenbezeichnung} in Ihrem Unternehmen {Firmenname}. ...

Mit freundlichen Grüßen,
Jörg Zeilinger
```

### Ausgabe
- Erstellt PDF-Dokumente mit personalisiertem Brieftext für jede Adresse
- Speichert die PDF-Dokumente unter Dateinamen, in denen Sonderzeichen durch Unterstriche ersetzt wurden
- Optional: Versendet die Bewerbungen per E-Mail an die Empfänger

## Offene Fragen
- Wie werden die Anhänge (Lebenslauf, Zeugnisse) erstellt?
- Wie ist die genaue Struktur der CSV-Datei "Adressen.csv"?
- Wie ist die genaue Struktur der Textdatei "Brieftext.txt"?
- Wie ist der genaue Aufbau der E-Mail?