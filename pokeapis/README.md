# Pokédex Web (Flask)

Esta es una versión web de la Pokédex que tenías en `pract3.py`. Usa Flask y HTML/Bootstrap para presentar una UI más agradable y un formulario.

Archivos principales:

- `pract3_web.py` - aplicación Flask
- `templates/index.html` - plantilla principal
- `static/css/style.css` - estilos adicionales
- `requirements.txt` - dependencias

Cómo ejecutar (PowerShell):

```powershell
# crear entorno (opcional pero recomendado)
python -m venv venv; .\venv\Scripts\Activate
pip install -r requirements.txt
python pract3_web.py
```

Luego abre en tu navegador: http://127.0.0.1:5000

Notas:
- Las imágenes usan URLs públicas de PokeAPI. Si quieres usar imágenes locales, colócalas en `static/` y ajusta la ruta en `pract3_web.py`.
- El formulario permite seleccionar un Pokémon y opcionalmente darle un "apodo" (nickname). Esto se procesa en memoria y no se persiste.

Siguientes pasos sugeridos:
- Guardar apodos en un archivo o base de datos
- Añadir más campos y validaciones
- Tests y despliegue
