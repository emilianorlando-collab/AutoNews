# =====================================================================
# SEMINARIO DE ACTUALIZACION 
# IFTS 11  - TECNICATURA EN CIENCIAS DE DATOS E IA 
# VERÓNICA ARCE
# TRABAJO FINAL: AUTOMATIZACIÓN
# =====================================================================

import urllib.request
import urllib.parse
import json
import xml.etree.ElementTree as ET
import schedule  # Librería para controlar la automatización horaria
import time # Librería para controlar los tiempos de espera

# =====================================================================
# PASO 1: EXTRACCIÓN DE DATOS (NODO DE ENTRADA Y FILTRADO RSS/XML)
# =====================================================================

def buscar_noticias_tecnologia():
    url = "https://feeds.weblogssl.com/genbeta"    # URL del canal RSS del portal de tecnología
    print("Buscando últimas noticias...")
    try:
        # Configuramos un User-Agent simulado para evitar bloqueos de seguridad del servidor
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        # Realizamos la petición HTTP y descargamos el archivo XML crudo
        with urllib.request.urlopen(req) as response:
            xml_data = response.read()
        
        # Análisis del árbol jerárquico del archivo XML
        root = ET.fromstring(xml_data)
        noticias = []

        # Filtramos y recorremos únicamente las primeras 5 noticias utilizando un rebanador [:5]
        for item in root.findall('.//item')[:5]:
            titulo = item.find('title').text
            link = item.find('link').text
            
            # Almacenamos la información limpia en una lista de diccionarios
            noticias.append({"titulo": titulo, "link": link})
        return noticias
    except Exception as e:
        
        # Control de excepciones para evitar que el script se caiga si falla internet
        print(f"Error al buscar noticias: {e}")
        return []


# =====================================================================
# PASO 2: INTEGRACIÓN CON TELEGRAM (NODO DE SALIDA / HTTP POST JSON)
# =====================================================================


def enviar_a_telegram(texto_reporte):
    # -------------------------------------------------------------
    # DATOS DE TELEGRAM (Credenciales de autenticación del Bot y dirección de red del grupo)
    TOKEN = "8974226118:AAEhgUWD-nQeRm8bEM1MsT4ws8C4197Brj8"
    CHAT_ID = "-4976435379"
    # -------------------------------------------------------------

    # URL oficial del método de la API de Telegram para enviar mensajes
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    # Diccionario de datos (Payload) estructurado para la API
    payload = {
        "chat_id": CHAT_ID,
        "text": texto_reporte,
        "parse_mode": "Markdown",  # Permite textos enriquecidos (negritas y links)
        "disable_web_page_preview": False  # Muestra la vista previa del link de la noticia
    }
    
    try:
        # Convertimos el diccionario de Python al formato estándar JSON requerido
        data = json.dumps(payload).encode('utf-8')
        
        # Configuramos la petición HTTP tipo POST especificando el Content-Type JSON
        req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
        
        # Disparamos el mensaje hacia los servidores de Telegram
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                print("¡Reporte enviado a Telegram con éxito! 🎉 Checkeá tu celu.")
    
    except Exception as e:

        # Evita que el programa colapse si los servidores de Telegram no responden
        print(f"Error de conexión con Telegram: {e}")


# =====================================================================
# PASO 3: DISEÑADOR DE INTERFAZ Y CONTENIDO (NODO TRANSFORMADOR)
# ======================================================================

def ejecutar_reporte_diario():
    print("⏰ ¡Hora del reporte! Buscando noticias...")
    lista_noticias = buscar_noticias_tecnologia()
    
    # Si la función anterior trajo datos, armamos la interfaz visual del mensaje
    if lista_noticias:
        mensaje = "🤖 *AUTONEWS - SEMINARIO IA* 🤖\n\n"
        for i, noti in enumerate(lista_noticias, 1):
            mensaje += f"{i}️⃣ *{noti['titulo']}*\n"
            mensaje += f"🔗 [Leer noticia]({noti['link']})\n\n"
       
       # Enviamos el paquete de texto final estructurado a Telegram
        enviar_a_telegram(mensaje)


# =====================================================================
# PASO 4: DISPARADOR TEMPORAL PRINCIPAL (NODO TRIGGER / CRONJOB)
# =====================================================================

if __name__ == "__main__":
    
    # Configuración de la hora diaria en la que correrá el sistema de fondo
    HORA_ENVIO = "09:00" 


    print("🛸 MODO DEFENSA ACTIVADO")
    print("1️⃣ Forzando un envío inmediato para demostración en clase...")
    
    # DISPARO DE DEMOSTRACIÓN: Corre una vez al presionar "Play" para demostración     
    ejecutar_reporte_diario() 
    
    print("\n2️⃣ Entrando en modo de espera diaria...")
    # Dejamos programado el reloj para los días siguientes:
    schedule.every().day.at(HORA_ENVIO).do(ejecutar_reporte_diario)
    
    
    print(f"🚀 Sistema AutoNews en segundo plano. Se enviará cada día a las {HORA_ENVIO}.")
    print("⚠️ IMPORTANTE: No cierres esta ventana para mantener el bot vivo.")
    print("--------------------------------------------------")

    # Bucle infinito para mantener a Python atento al reloj
    while True:
        schedule.run_pending()
        time.sleep(1)