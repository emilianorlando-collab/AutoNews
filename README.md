# 📰 AutoNews: Pipeline Automatizado de Inteligencia Artificial

![n8n](https://img.shields.io/badge/n8n-FF6D5A?style=for-the-badge&logo=n8n&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google%20gemini&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)

Proyecto desarrollado en el marco de la **Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial**. 

Este repositorio contiene la arquitectura y configuración de un flujo de automatización *self-hosted* que extrae, procesa y distribuye información utilizando integraciones API y Modelos de Lenguaje de Gran Escala (LLMs).

## 🚀 Descripción del Proyecto

El objetivo de este sistema es mitigar la sobrecarga de información mediante un curador de contenidos autónomo. El pipeline se ejecuta de forma local, consume el feed de noticias de tecnología/ciencia (vía RSS), normaliza la estructura de datos mediante scripting, delega la síntesis semántica al modelo **Google Gemini**, y distribuye el reporte final a través de la API de **Gmail** utilizando autenticación segura OAuth2.

### ⚙️ Arquitectura del Flujo (Nodos)
1. **HTTP Request / XML:** Extracción de datos en crudo desde fuentes RSS.
2. **JavaScript Processing:** Limpieza de metadatos y normalización de la estructura JSON.
3. **AI Agent (Gemini):** Inferencia cognitiva para resumir y estructurar la información clave.
4. **Gmail API:** Envío automatizado del reporte aplicando credenciales OAuth2.

## 📂 Estructura del Repositorio

\`\`\`text
AutoNews/
├── docs/                   # Justificación teórica y documentación en PDF
├── screenshots/            # Evidencia visual del flujo en ejecución
├── workflows/              # Archivo JSON exportado con el código fuente de n8n
├── .env.example            # Plantilla de variables de entorno requeridas
├── docker-compose.yml      # Archivo de orquestación para despliegue en contenedores
└── README.md               # Documentación principal del proyecto
\`\`\`

## 🛠️ Requisitos Previos

Para ejecutar este proyecto en un entorno local (optimizado para macOS / procesadores Apple Silicon), se requiere:

* **n8n:** Instalado de forma local (vía `npm` o Docker).
* **Google Cloud Console:** Un proyecto activo con la *Gmail API* habilitada y credenciales OAuth2 configuradas (Client ID & Secret).
* **Google AI Studio:** Una API Key válida para consumir el modelo Gemini.

## 💻 Instalación y Despliegue

**1. Clonar el repositorio:**
\`\`\`bash
git clone https://github.com/TU_USUARIO/AutoNews.git
cd AutoNews
\`\`\`

**2. Configurar el entorno:**
* Duplica el archivo `.env.example` y renómbralo a `.env`.
* Completa tus credenciales privadas (Gemini API Key, Google Client ID y Secret).

**3. Importar el flujo:**
* Inicia tu servidor local de n8n.
* Accede a la interfaz web (por defecto `http://localhost:5678`).
* En el panel principal, selecciona *Import from File* y elige el archivo `.json` ubicado en la carpeta `workflows/`.
* Conecta tus credenciales de Google cuando el nodo de Gmail lo solicite.

## 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
