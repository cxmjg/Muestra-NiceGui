from nicegui import html, ui

with ui.header() as cabecera:
    html.h1('Sitio de prueba').style('font-size: xx-large; font-weight: bolder; font-family: monospace;')


with html.section().classes('self-center') as contenido:
    with html.article().classes('bg-blue-200 p-2') as article1:
        ui.html('<h3>Articulo 1</h3>').classes('font-bold')
        html.p('Contenido de este articulo')

ui.run(port=8181, host='0.0.0.0')