import flet as ft
import model.model


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._retailer = None

    def handle_hello(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def handle_top_vendite(self):
        pass

    def handle_analizza_vendite(self):
        pass

    def handle_add_anni(self):
        lista_anni = self._model.trova_anni()
        for anno in lista_anni:
            self._view.txt_name.options.append(ft.dropdown.Option(key=anno, text=str(anno)))
        self._view.update_page()

    def handle_add_brand(self):
        lista_brand = self._model.trova_brand()
        for brand in lista_brand:
            self._view.txt_container.options.append(ft.dropdown.Option(key=brand, text=str(brand)))
        self._view.update_page()

    def handle_add_retailer(self):
        lista_retailer = self._model.trova_retailer()
        for r in lista_retailer:
            self._view.txt_field.options.append(ft.dropdown.Option(key=r.retailer_code, text=r.retailer_name,data = r, on_click=self.read_retailer))
        self._view.update_page()


    def read_retailer(self,e):
        self._retailer=e.control.data