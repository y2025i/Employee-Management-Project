from nicegui import ui

# Arayüze başlık ve buton ekleyelim
ui.label('Hello World! NiceGUI is working 🚀').classes('text-h3')
ui.button('Click me!', on_click=lambda: ui.notify('Zeljko, you can start here!'))

# Web sunucusunu başlat
ui.run()