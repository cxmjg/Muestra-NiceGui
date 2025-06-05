from nicegui import html, ui

estilos = open("./estilos.css").read()

ui.add_css(estilos)

with ui.header().classes('items-center') as header:
    html.h1('Sitio de prueba')

with ui.row() as principal:
    
    with html.nav() as contenedorMenu:
        ui.menu_item('Menu item 1')
        ui.menu_item('Menu item 2')
        ui.menu_item('Menu item 3')

    with ui.column().props('aria-label="Contenido principal" role="document"') as contenido:
        html.h1('Contenido del sitio')
        
        with html.article() as article:
            ui.html('<h3>Article 1</h3>')
            html.p('Like with any other element, you can add classes, style, props, tooltips and events. One convenience is that the keyword arguments are automatically added to the elements props dictionary.')

with ui.footer() as footer:
    ui.label('Marcos Garcia 2025')


principal.classes('flex-nowrap')
ui.query('nav').classes('bg-blue-400 rounded-2xl p-2 w-1/6 h-[70vh]')
contenido.classes('bg-blue-400 rounded-2xl p-2 w-5/6 h-[70vh] items-center')
ui.query('article').classes('bg-blue-200 rounded-2xl p-2 w-1/2')


ui.run(port=8182, host='0.0.0.0')