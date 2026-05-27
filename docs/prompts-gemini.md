# Prompts de Google Gemini

Este documento reúne los prompts sugeridos para que AutoNews genere reportes claros, breves y útiles a partir de noticias tecnológicas obtenidas desde fuentes RSS.

Los prompts están pensados para ejecutarse dentro del nodo **AI Agent** de n8n utilizando **Google Gemini**.

## Objetivo del Prompt

El modelo debe actuar como un curador y analista de noticias tecnológicas. Su tarea no es copiar el contenido original, sino sintetizarlo, organizarlo y convertirlo en un reporte diario fácil de leer.

El resultado esperado debe:

- Resumir las noticias más importantes.
- Mantener un tono profesional y claro.
- Conservar enlaces a las fuentes originales.
- Indicar fechas cuando estén disponibles.
- Evitar exageraciones o afirmaciones no verificadas.
- Priorizar relevancia tecnológica, impacto y actualidad.

## Prompt Principal

```text
Actuá como un analista de noticias tecnológicas.

Vas a recibir una lista de noticias provenientes de fuentes RSS. Cada noticia puede incluir título, fecha de publicación, descripción, enlace y fuente.

Tu tarea es generar un reporte diario profesional con las noticias tecnológicas más relevantes.

Instrucciones:
- Resumí cada noticia en lenguaje claro y breve.
- Priorizá noticias relacionadas con inteligencia artificial, software, ciberseguridad, ciencia, innovación, empresas tecnológicas y regulación digital.
- No inventes datos que no estén presentes en la entrada.
- Conservá los enlaces originales cuando estén disponibles.
- Si una fecha está disponible, incluíla junto a la noticia.
- Agrupá las noticias por tema cuando sea posible.
- Usá español neutro.
- Evitá tono sensacionalista.

Formato de salida:

# Reporte Tecnológico Diario

Fecha del reporte: {{fecha_reporte}}

## Resumen ejecutivo
Incluí un párrafo breve con las tendencias principales del día.

## Noticias destacadas

### 1. {{titulo}}
- Fecha: {{fecha_publicacion}}
- Fuente: {{fuente}}
- Resumen: {{resumen_breve}}
- Relevancia: {{por_que_importa}}
- Enlace: {{url}}

## Conclusión
Incluí una conclusión breve sobre el panorama tecnológico del día.
```

## Prompt para Resumen Ejecutivo

```text
Analizá la siguiente lista de noticias tecnológicas y generá un resumen ejecutivo de no más de 120 palabras.

El resumen debe explicar cuáles son los temas dominantes del día y por qué son relevantes.

Condiciones:
- No inventes información.
- No menciones noticias que no estén en la lista.
- Escribí en español claro y profesional.
- Evitá frases genéricas.

Noticias:
{{noticias}}
```

## Prompt para Clasificación Temática

```text
Clasificá las siguientes noticias tecnológicas en categorías.

Categorías sugeridas:
- Inteligencia Artificial
- Ciberseguridad
- Software y desarrollo
- Ciencia e innovación
- Empresas tecnológicas
- Regulación digital
- Otros

Para cada categoría, listá las noticias correspondientes con título, breve resumen y enlace.

Si una noticia puede pertenecer a más de una categoría, elegí la categoría más representativa.

Noticias:
{{noticias}}
```

## Prompt para Email Final

```text
Convertí el siguiente contenido en un email profesional y fácil de leer.

Objetivo:
Enviar un reporte diario con las noticias tecnológicas más importantes.

Instrucciones:
- Usá un asunto breve y claro.
- Organizá el cuerpo con títulos y subtítulos.
- Mantené el texto conciso.
- Conservá los enlaces originales.
- Incluí la fecha del reporte.
- Cerrá con una conclusión breve.

Contenido:
{{reporte_generado}}

Formato esperado:

Asunto: Reporte tecnológico diario - {{fecha_reporte}}

Cuerpo:
{{email_html_o_texto}}
```

## Variables Sugeridas

Estas variables pueden ser reemplazadas dinámicamente desde n8n:

| Variable | Descripción |
| --- | --- |
| `{{fecha_reporte}}` | Fecha en la que se ejecuta el workflow. |
| `{{fecha_publicacion}}` | Fecha original de publicación de la noticia. |
| `{{titulo}}` | Título de la noticia. |
| `{{fuente}}` | Medio o fuente RSS de origen. |
| `{{url}}` | Enlace original de la noticia. |
| `{{noticias}}` | Lista normalizada de noticias enviada al modelo. |
| `{{reporte_generado}}` | Resultado previo generado por Gemini. |

## Recomendaciones de Uso

- Enviar al modelo datos limpios y normalizados desde el nodo JavaScript.
- Limitar la cantidad de noticias para evitar reportes demasiado extensos.
- Mantener siempre los enlaces originales para trazabilidad.
- Validar que el modelo no genere información adicional no presente en las fuentes.
- Usar temperatura baja o moderada si se busca una salida consistente.

## Ejemplo de Salida Esperada

```md
# Reporte Tecnológico Diario

Fecha del reporte: 26 de mayo de 2026

## Resumen ejecutivo

La jornada estuvo marcada por avances en inteligencia artificial, nuevas medidas de seguridad digital y actualizaciones relevantes de empresas tecnológicas.

## Noticias destacadas

### 1. Nueva herramienta de IA para desarrollo de software
- Fecha: 26 de mayo de 2026
- Fuente: Fuente RSS
- Resumen: Una empresa tecnológica presentó una herramienta orientada a mejorar la productividad de equipos de desarrollo.
- Relevancia: Refleja la adopción creciente de IA en procesos de programación y automatización.
- Enlace: https://example.com/noticia

## Conclusión

El panorama tecnológico del día muestra una fuerte continuidad en la integración de IA en productos, servicios y procesos empresariales.
```
