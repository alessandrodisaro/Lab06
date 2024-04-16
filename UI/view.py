import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_top_vendite = None
        self.btn_analizza_vendite = None
        self.txt_result = None
        self.txt_container = None
        self.txt_field = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analisi vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROWs

        # text fields
        # prima le inizializzo la roba da mettere nei dropdown

        self.txt_name = ft.Dropdown(label="Anno", width=200, options=[ft.dropdown.Option(key="", text="Nessun filtro")])
        self._controller.handle_add_anni()
        self.txt_container = ft.Dropdown(label="Brand", width=400,
                                         options=[ft.dropdown.Option(key="", text="Nessun filtro")])
        self._controller.handle_add_brand()
        self.txt_field = ft.Dropdown(label="Retailer", width=400,
                                     options=[ft.dropdown.Option(key="", text="Nessun filtro")])
        self._controller.handle_add_retailer()
        row1 = ft.Row([self.txt_name, self.txt_container, self.txt_field], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # buttons
        self.btn_top_vendite = ft.ElevatedButton(text="Top vendite", on_click=self._controller.handle_top_vendite)
        self.btn_analizza_vendite = ft.ElevatedButton(text="Analizza vendite",
                                                      on_click=self._controller.handle_analizza_vendite)
        row2 = ft.Row([self.btn_top_vendite, self.btn_analizza_vendite],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
