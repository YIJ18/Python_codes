import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from cryptography.fernet import Fernet

# Leer la clave y descifrar la contraseña
with open('clave.key', 'rb') as key_file:
    clave = key_file.read()

with open('password.enc', 'rb') as enc_file:
    password_cifrada = enc_file.read()

fernet = Fernet(clave)
password_descifrada = fernet.decrypt(password_cifrada).decode()

# Crear el mensaje
mensaje = MIMEMultipart()
mensaje['From'] = "jassoiris96@gmail.com"
mensaje['To'] = "p37676@correo.uia.mx, a2272426@correo.uia.mx, irisyulit.jassoc@cejv.edu.mx"
mensaje['Subject'] = "Correo de prueba con HTML y adjunto"

# Cargar contenido HTML desde archivo
with open('msj.html', 'r') as file:
    html_content = file.read()

mensaje.attach(MIMEText(html_content, 'html'))

# Adjuntar archivo
archivo_adjunto = "archivo.pdf"
part = MIMEBase('application', 'octet-stream')
with open(archivo_adjunto, 'rb') as file:
    part.set_payload(file.read())

encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment', filename=archivo_adjunto)
mensaje.attach(part)

# Enviar correo
try:
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login('jassoiris96@gmail.com', password_descifrada)
    texto = mensaje.as_string()
    servidor.sendmail(mensaje['From'], mensaje['To'].split(', '), texto)
    servidor.quit()
    
    print("✅ Correo enviado con éxito a:", mensaje['To'])

    # Registrar el envío en un archivo de log
    with open('registro_envios.txt', 'a') as log:
        log.write(f"Correo enviado a {mensaje['To']} con asunto '{mensaje['Subject']}'\n")

except Exception as e:
    print(f"❌ Error al enviar correo: {e}")
