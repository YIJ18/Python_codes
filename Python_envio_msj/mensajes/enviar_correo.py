import smtplib
from email.message import EmailMessage
from email.mime.application import MIMEApplication
from email.header import Header
from cryptography.fernet import Fernet

# Leer contraseña cifrada
with open("clave.key", "rb") as f:
    clave = f.read()
fernet = Fernet(clave)

with open("password_encriptado.txt", "rb") as f:
    password_cifrado = f.read()
password = fernet.decrypt(password_cifrado).decode('utf-8')  # Decodificar en UTF-8

# Crear el mensaje
mensaje = EmailMessage()

# Utiliza Header para el asunto, asegurando que se convierte en una cadena
mensaje["Subject"] = str(Header("Correo de prueba con HTML y adjunto", "utf-8"))
mensaje["From"] = "tunombrefake@gmail.com"
mensaje["To"] = "p37676@correo.uia.mx, tucorreoalumno@ibero.mx"

# Cargar contenido HTML
with open("mensaje.html", "r", encoding="utf-8") as f:
    contenido_html = f.read()

# Asegurarse de que el contenido se maneje como UTF-8
mensaje.set_content("Tu cliente no soporta HTML", charset="utf-8")
mensaje.add_alternative(contenido_html, subtype='html', charset="utf-8")

# Adjuntar archivo PDF
with open("archivo.pdf", "rb") as f:
    archivo_adjunto = MIMEApplication(f.read(), _subtype="pdf")
    archivo_adjunto.add_header('Content-Disposition', 'attachment', filename='archivo.pdf')
    mensaje.attach(archivo_adjunto)

# Enviar el correo
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("iris@gmail.com", password)
        smtp.send_message(mensaje)
        print("Correo enviado exitosamente.")
except Exception as e:
    print(f"Error al enviar correo: {e}")
