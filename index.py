from nicegui import html, ui

estilos = open("./estilos.css").read()

ui.add_css(estilos)

with ui.header().classes('items-center') as header:
    with ui.button(icon='menu'):
        with ui.menu() as menu:
            with html.nav() as nav:
                ui.menu_item('Menu item 1')
                ui.menu_item('Menu item 2')
                ui.menu_item('Menu item 3',auto_close=False)
                ui.separator()
                ui.menu_item('Cerrar', menu.close)
    html.h1('Sitio de prueba')
    
with ui.column().classes('items-center self-center') as body:
    with html.article() as article1:
        ui.html('<h3>Articulo 1</h3>')
        html.p('Contenido de este articulo')
    
    with html.article() as article2:
        ui.html('<h3>Article 2</h3>')
        with ui.expansion('Expandir!', icon='description').classes('w-full'):
            html.p('Like with any other element, you can add classes, style, props, tooltips and events. One convenience is that the keyword arguments are automatically added to the elements props dictionary.')

with ui.footer() as footer:
    ui.label('Marcos Garcia 2025')

ui.query('article').classes('bg-blue-200 rounded-2xl p-2 w-1/2')

ui.run(port=8181, host='0.0.0.0')