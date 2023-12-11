# Automatisierte Bewerbungserstellung und Versand

## Zielsetzung
Das Ziel ist es, eine automatisierte Bewerbungserstellung und Versand zu implementieren. Dabei sollen Adressen und Brieftexte aus Dateien eingelesen, Platzhalter im Brieftext ersetzt, PDF-Dateien erzeugt und optional per E-Mail versendet werden.

## Grundgedanke
Der Prozess soll die Erstellung und den Versand von Bewerbungen automatisieren, um Zeit zu sparen und Fehler zu vermeiden. 

## Durchführungsschritte
1. Einlesen der Adressen aus der Textdatei
2. Auswahl einer Adresse aus den vorhandenen Adressen
3. Einlesen des Brieftextes aus der Datei
4. Ersetzen der Platzhalter im Brieftext mit den entsprechenden Informationen aus der ausgewählten Adresse
5. Erzeugen einer PDF-Datei mit dem Brieftext und den Anhängen
6. Optional: Versenden der PDF-Datei per E-Mail

## Anforderungen
- Python 3
- Bibliotheken: csv, fpdf, PyPDF2, smtplib, ssl, email.mime.text, email.mime.multipart, email.mime.base, email

## Beispiel
```python
import csv
from fpdf import FPDF
from PyPDF2 import PdfMerger
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Einlesen der Adressen
with open("data/Adressen.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")
    adressen = list(reader)
    adressen = adressen[1:]

# Einlesen des Brieftextes
with open("data/Brieftext.txt", "r", encoding="utf-8") as file:
    Bewerbungstext = file.read()

# Verarbeitung der Adressen
for i in adressen:
    Firmenname = i[0].strip()
    Emailadresse = i[1].strip()
    Ansprechpartner = i[2].strip()
    Straße = i[3].strip()
    PLZ = i[4].strip()
    Ort = i[5].strip()
    Anrede = i[6].strip()
    Stellenbezeichnung = i[7].strip()
    brief = Bewerbungstext

    # Ersetzen der Platzhalter
    brief = brief.replace("{Firmenname}", Firmenname)
    brief = brief.replace("{Emailadresse}", Emailadresse)
    brief = brief.replace("{Ansprechpartner}", Ansprechpartner)
    brief = brief.replace("{Straße}", Straße)
    brief = brief.replace("{PLZ}", PLZ)
    brief = brief.replace("{Ort}", Ort)
    brief = brief.replace("{Anrede}", Anrede)    
    brief = brief.replace("{Stellenbezeichnung}", Stellenbezeichnung)

    # Erzeugen der PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 5, txt=brief, align="L")
    fileoutput = "./output/Bewerbung - Jörg Zeilinger - " + replace_special_characters(Stellenbezeichnung + " - " + Firmenname) + ".pdf"
    pdf.output(fileoutput)
    pdf.close()

    # Hinzufügen der Anhänge
    merger = PdfMerger()
    merger.append(fileoutput)
    merger.append("./data/Lebenslauf.pdf")
    merger.append("./data/Zeugnisse.pdf")
    merger.write(fileoutput)
    merger.close()

    # Optional: Versenden der E-Mail
    if Email == True:
        sender_email = "joerg.zeilinger@gmail.com"
        receiver_email = Emailadresse
        password = "xxx"
        
        message = MIMEMultipart("alternative")
        message["Subject"] = "Bewerbung - Jörg Zeilinger - " + Stellenbezeichnung
        message["From"] = sender_email
        message["To"] = receiver_email
        
        text = brief
        html = brief
        
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        
        message.attach(part1)
        message.attach(part2)
        
        filename = fileoutput
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            
        encoders.encode_base64(part)
        
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        
        message.attach(part)
        text = message.as_string()
        
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
            
        print("E-Mail wurde versendet")
```

## Offene Fragen
- Wie kann die Sicherheit beim Versenden der E-Mails verbessert werden?
- Wie kann die Qualität der generierten PDFs verbessert werden?
- Wie kann der Prozess weiter automatisiert werden?