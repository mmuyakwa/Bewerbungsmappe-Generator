import csv
from fpdf import FPDF
from PyPDF2 import PdfMerger
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Decide if you want to send via email or not
Email = False #False

# Read the environment variables from the .env file
YOUR_NAME = os.getenv("YOUR_NAME").strip()
YOUR_GMAIL_EMAIL = os.getenv("YOUR_GMAIL_EMAIL").strip()
YOUR_GMAIL_PASSWORD = os.getenv("YOUR_GMAIL_PASSWORD").strip()
YOUR_ATTACHMENTS = os.getenv("YOUR_ATTACHMENTS")

# Attachments as list of filenames
# YOUR_ATTACHMENTS = ["./data/Lebenslauf.pdf", "./data/Zeugnisse.pdf"]
YOUR_ATTACHMENTS = YOUR_ATTACHMENTS.replace("[", "").replace("]", "").replace("\"", "").split(",")
# Make sure every filename is stripped
for i in range(len(YOUR_ATTACHMENTS)):
    YOUR_ATTACHMENTS[i] = YOUR_ATTACHMENTS[i].strip()

# Replace special characters in the filename
def replace_special_characters(text):
    text = text.replace(" ", "_")
    text = text.replace("ä", "ae")
    text = text.replace("ö", "oe")
    text = text.replace("ü", "ue")
    text = text.replace("Ä", "Ae")
    text = text.replace("Ö", "Oe")
    text = text.replace("Ü", "Ue")
    text = text.replace("ß", "ss")
    text = text.replace(":", "")
    text = text.replace(";", "")
    text = text.replace(",", "")
    text = text.replace("(", "")
    text = text.replace(")", "")
    text = text.replace("/", "")
    text = text.replace("\\", "")
    text = text.replace("?", "")
    text = text.replace("!", "")
    text = text.replace("=", "")
    text = text.replace("+", "")
    text = text.replace("*", "")
    text = text.replace("#", "")
    text = text.replace("<", "")
    text = text.replace(">", "")
    text = text.replace("|", "")
    text = text.replace("\"", "")
    # text = text.replace("-", "")
    return text

# Create PDF file
def create_pdf(brief, fileoutput, attachments=[]):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 5, txt=brief, align="L")
    pdf.output(fileoutput)
    pdf.close()

    # Merge PDF files (Letter + CV + Certificates)
    merger = PdfMerger()
    merger.append(fileoutput)
    for attachment in attachments:
        merger.append(attachment)
    merger.write(fileoutput)
    merger.close()

# Send email (Emailreceiver, Letter, PDF file)
def send_email(receiver_email, brief, fileoutput):
    sender_email = YOUR_GMAIL_EMAIL
    password = YOUR_GMAIL_PASSWORD

    message = MIMEMultipart("alternative")
    message["Subject"] = "Bewerbung - " + YOUR_NAME + " - " + Stellenbezeichnung
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = brief
    html = brief

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    filename = fileoutput
    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

    print("Email was sent to " + receiver_email)


# Read the addresses from the CSV file
with open("data/Adressen.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")
    adressen = list(reader)[1:]

# Read the letter text from the text file
with open("data/Brieftext.txt", "r", encoding="utf-8") as file:
    Bewerbungstext = file.read()

# Loop through the addresses and create the PDF files
for adresse in adressen:
    Firmenname, Emailadresse, Ansprechpartner, Straße, PLZ, Ort, Anrede, Stellenbezeichnung = adresse

    # Strip the spaces at the beginning and end of the strings
    # Company name, email address, contact person, street, zip code, city, salutation, job title
    Firmenname = Firmenname.strip()
    Emailadresse = Emailadresse.strip()
    Ansprechpartner = Ansprechpartner.strip()
    Straße = Straße.strip()
    PLZ = PLZ.strip()
    Ort = Ort.strip()
    Anrede = Anrede.strip()
    Stellenbezeichnung = Stellenbezeichnung.strip()

    # Create the letter text
    brief = Bewerbungstext.format(Firmenname=Firmenname, Emailadresse=Emailadresse, Ansprechpartner=Ansprechpartner,
                                  Straße=Straße, PLZ=PLZ, Ort=Ort, Anrede=Anrede, Stellenbezeichnung=Stellenbezeichnung, YOUR_NAME=YOUR_NAME)

    # Replace special characters in the filename
    fileoutput = replace_special_characters(f"{Stellenbezeichnung} - {Firmenname}")
    # Create the PDF filename
    fileoutput = f"./output/Bewerbung - {YOUR_NAME} - {fileoutput}.pdf"
    # Create the PDF file. Example: YOUR_ATTACHMENTS=["./data/Lebenslauf.pdf", "./data/Zeugnisse.pdf"]
    #print(YOUR_ATTACHMENTS) # For testing
    create_pdf(brief, fileoutput, YOUR_ATTACHMENTS)

    # Send email if Email is True at the beginning of the file
    if Email:
        send_email(Emailadresse, brief, fileoutput)
