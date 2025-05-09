import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizza(self, e):
        miglia = self._view.miglia.value
        if miglia is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Devi inserire un valore", color="red"))
            self._view.update_page()
            return
        try:
            miglia_int = int(miglia)
            self._model.getAllConnessioni(miglia_int)
            self._model.buildGraph()
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato", color="blue"))
            self._view.txt_result.controls.append(ft.Text(f"NUmero di nodi: {self._model.getNumNodi}"))
            self._view.txt_result.controls.append(ft.Text(f"NUmero di archi: {self._model.getNumArchi}"))
            self._view.update_page()


        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Devi inserire un numero", color="red"))
            self._view.update_page()
            return


