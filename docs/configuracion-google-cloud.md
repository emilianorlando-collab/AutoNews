# Configuración de Google Cloud y Gmail API

Este documento describe la configuración necesaria para que AutoNews pueda enviar reportes por correo electrónico usando la **Gmail API** con autenticación **OAuth2**.

La configuración se realiza desde Google Cloud Console y luego se conecta dentro de n8n mediante credenciales OAuth2.

## Requisitos

- Cuenta de Google.
- Proyecto activo en Google Cloud Console.
- Gmail API habilitada.
- Credenciales OAuth2 configuradas.
- Instancia local de n8n en ejecución.

## 1. Crear un Proyecto en Google Cloud

1. Ingresar a [Google Cloud Console](https://console.cloud.google.com/).
2. Crear un proyecto nuevo o seleccionar uno existente.
3. Asignar un nombre identificable, por ejemplo:

```text
AutoNews Gmail Automation
```

## 2. Habilitar Gmail API

1. Ir a **APIs & Services**.
2. Seleccionar **Library**.
3. Buscar **Gmail API**.
4. Presionar **Enable**.

Esto permite que el proyecto pueda interactuar con Gmail mediante llamadas autenticadas.

## 3. Configurar la Pantalla de Consentimiento OAuth

1. Ir a **APIs & Services > OAuth consent screen**.
2. Seleccionar el tipo de usuario correspondiente.
3. Completar los datos básicos de la aplicación:

| Campo | Valor sugerido |
| --- | --- |
| App name | AutoNews |
| User support email | Tu correo de Google |
| Developer contact information | Tu correo de Google |

4. Guardar la configuración.

Para un proyecto académico o de uso personal, puede mantenerse como aplicación en estado de prueba mientras solo la use el propietario o usuarios autorizados.

## 4. Crear Credenciales OAuth2

1. Ir a **APIs & Services > Credentials**.
2. Seleccionar **Create Credentials**.
3. Elegir **OAuth client ID**.
4. Seleccionar el tipo de aplicación según el uso en n8n.
5. Configurar la URL de redirección autorizada.

Para una instalación local de n8n, la URL suele tener este formato:

```text
http://localhost:5678/rest/oauth2-credential/callback
```

Si n8n se ejecuta en otro dominio o puerto, la URL debe ajustarse al entorno real.

## 5. Variables de Entorno

El repositorio incluye un archivo `.env.example` como plantilla. No deben subirse credenciales reales a GitHub.

Ejemplo:

```env
GEMINI_API_KEY=your_gemini_api_key_here

GOOGLE_CLIENT_ID=your_google_client_id_here
GOOGLE_CLIENT_SECRET=your_google_client_secret_here
GMAIL_USER=your_email@gmail.com

N8N_HOST=localhost
N8N_PORT=5678
N8N_PROTOCOL=http
WEBHOOK_URL=http://localhost:5678
```

El archivo real `.env` debe quedar únicamente en el entorno local y estar incluido en `.gitignore`.

## 6. Configurar Credenciales en n8n

Dentro de n8n:

1. Abrir el panel de credenciales.
2. Crear una nueva credencial para Gmail OAuth2.
3. Cargar el **Client ID** y **Client Secret** generados en Google Cloud.
4. Iniciar el proceso de autorización.
5. Aceptar los permisos solicitados.
6. Guardar la credencial.

Una vez conectada, el nodo de Gmail podrá enviar el reporte generado por AutoNews.

## 7. Scopes de Gmail

El scope exacto depende de la configuración del nodo de Gmail en n8n. Para el envío de correos, suele utilizarse un permiso asociado a envío de mensajes.

Ejemplo habitual:

```text
https://www.googleapis.com/auth/gmail.send
```

Se recomienda usar el menor nivel de permisos posible para cumplir con la función del proyecto.

## 8. Buenas Prácticas de Seguridad

- No subir `.env` a GitHub.
- No compartir capturas donde se vean tokens, claves o secretos.
- Usar `.env.example` solo con valores ficticios.
- Revocar y regenerar credenciales si una clave fue expuesta accidentalmente.
- Limitar los permisos OAuth al alcance necesario.
- Mantener las credenciales de n8n protegidas en el entorno local.

## 9. Verificación

Para comprobar que la integración funciona:

1. Ejecutar el workflow manualmente en n8n.
2. Verificar que el nodo de Gmail finalice sin errores.
3. Confirmar la recepción del correo.
4. Revisar que el reporte incluya fecha, títulos, resúmenes y enlaces.

Si el envío falla, revisar:

- URL de callback configurada en Google Cloud.
- Client ID y Client Secret.
- Permisos OAuth aceptados.
- Estado de la Gmail API.
- Configuración del nodo Gmail en n8n.
