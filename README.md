# Bewerbungsmappe als PDF generieren und versenden

## Zielsetzung

Das Ziel dieses Skripts ist es, eine Bewerbungsmappe als PDF zu generieren und diese anschließend zu versenden. Dabei sollen die Adressen, der Brieftext und die Anhänge aus verschiedenen Dateien ausgelesen und in das PDF-Dokument eingefügt werden.

## Grundgedanke

Das Skript soll die Informationen aus den Dateien zusammenführen und daraus eine Bewerbungsmappe als PDF generieren. Anschließend kann diese entweder per E-Mail versendet oder manuell ausgedruckt und per Post verschickt werden.

## Durchführungsschritte

1. Einlesen der Adressen aus der Textdatei
2. Auswahl einer Adresse aus den vorhandenen Adressen
3. Einlesen des Brieftextes aus der Datei
4. Ersetzen der Platzhalter im Brieftext mit den entsprechenden Informationen aus der ausgewählten Adresse
5. Erzeugen einer PDF-Datei mit dem Brieftext und den Anhängen
6. Optional: Versenden der PDF-Datei per E-Mail

## Anforderungen

- Textdatei mit Adressen im angegebenen Format
- Datei mit dem Brieftext im angegebenen Format
- Anhänge als separate Dateien im gewünschten Format (Lebenslauf, Zeugnisse, Zertifikate, Arbeitsproben, Arbeitszeugnisse, Sonstiges)
- Installation eines PDF-Generators (z.B. LaTeX mit pdflatex oder ein anderes Tool zur Erzeugung von PDF-Dateien)
- Optional: E-Mail-Client zur automatischen Versendung der PDF-Datei

## Beispiel

### Adressen (Adressen.txt)

```text
Firmenname; Emailadresse; Ansprechpartner; Straße; PLZ; Ort; Anrede; Stellenbezeichnung
Firma XY GmbH; info@firma-xy.de; Max Mustermann; Musterstraße 1; 12345 Musterstadt; Herr Mustermann; Bewerbung als Fachinformatiker Anwendungsentwicklung
Firma XZ GmbH; info@firma-xz.de;; Musterstraße 2; 12345 Musterstadt;; Fachinformatiker Zentrale BS2000-Services (m/w/d) – ID 321
```

### Brieftext (Brieftext.txt)

```text
Betreff: Bewerbung als <Stellenbezeichnung>

Sehr geehrte(r) Frau/Herr <Anrede>,

hiermit bewerbe ich mich auf die Stelle <Stellenbezeichnung> in Ihrem Unternehmen.

Bla Bla Bla

Mit freundlichen Grüßen

<Unterschrift>
```

### Anhänge

- Lebenslauf.pdf
- Zeugnisse.pdf
- Zertifikate.pdf
- Arbeitsproben.pdf
- Arbeitszeugnisse.pdf
- Sonstiges.pdf

### Erzeugte PDF-Datei

Die erzeugte PDF-Datei enthält den Brieftext mit den entsprechenden Informationen aus der ausgewählten Adresse sowie die Anhänge.

## Offene Fragen

- Welches Tool soll zur Erzeugung der PDF-Datei verwendet werden?
- Soll die PDF-Datei automatisch per E-Mail versendet werden? Wenn ja, welcher E-Mail-Client soll verwendet werden?
