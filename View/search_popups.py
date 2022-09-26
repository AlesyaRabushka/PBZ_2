from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp




class SearchPopupWorkArea(Popup, Widget):
    """
    Popup for WORK AREA table
    """
    def __init__(self, controller, model, table, **kw):
        super().__init__(**kw)
        self.model = model
        self.controller = controller
        self.table = table

    def set_work_area_number(self, number):
        self.controller.set_work_area_number(number)
    def set_work_area_name(self, name):
        self.controller.set_work_area_name(name)
    def set_work_area_equipment_type(self, type):
        self.controller.set_work_area_equipment_type(type)
    def add_work_area(self):
        self.controller.add_work_area()
        self.table.to_table_work_area()

class SearchPopupEquipment(Popup, Widget):
    """
        Popup for EQUIPMENT table
        """
    def __init__(self, controller, model, table, **kw):
        super().__init__(**kw)
        self.model = model
        self.controller = controller
        self.table = table

    def set_equipment_number(self, number):
        self.controller.set_equipment_number(number)
    def set_equipment_name(self, name):
        self.controller.set_equipment_name(name)
    def set_equipment_type(self, type):
        self.controller.set_equipment_type(type)
    def add_equipment(self):
        self.controller.add_equipment()
        self.table.to_table_equipment()


class SearchPopupTechInspection(Popup, Widget):
    """
        Popup for TECH INSPECTION table
        """
    def __init__(self, controller, model, **kw):
        super().__init__(**kw)
        self.model = model
        self.controller = controller
        # self.table = MDDataTable(pos_hint={'center_y': 0.56, 'center_x': 0.5},
        #                          use_pagination=True,
        #                          check=True,
        #                          column_data=[
        #                              ("Дата", dp(40)),
        #                              ("Номер оборудования", dp(40)),
        #                              ("Результат", dp(60))], size_hint=(1, 0.7),
        #                          row_data=self.model.return_table_search_tech_inspection())
        #
        # self.add_widget(self.table)


    def set_search_tech_inspection_equipment_number(self, number):
        self.controller.set_search_tech_inspection_equipment_number(number)

    def search_tech_inspection(self):
        self.controller.search_tech_inspection()

class FoundPopupTechInspection(Popup, Widget):
    def __init__(self, controller, model, **kw):
        super().__init__(**kw)
        self.controller = controller
        self.model = model
        self.found_list = self.model.return_table_search_tech_inspection()
        self.table = MDDataTable(pos_hint={'center_y': 0.56, 'center_x': 0.5},
                                 use_pagination=True,
                                 check=True,
                                 column_data=[
                                     ("Дата", dp(40)),
                                     ("Номер оборудования", dp(40)),
                                     ("Название",dp(40)),
                                     ("Тип", dp(40)),
                                     ("Результат", dp(60))], size_hint=(1, 0.7),
                                 row_data=self.found_list)

        self.add_widget(self.table)





class SearchPopupEmployee(Popup, Widget):
    """
        Popup for EMPLOYEE table
        """
    def __init__(self, controller, model, table, **kw):
        super().__init__(**kw)
        self.model = model
        self.controller = controller
        self.table = table

    # set employee's number
    def set_employee_number(self, employee_number):
        self.controller.set_employee_number(employee_number)

    # set employee's fio
    def set_employee_fio(self, employee_fio):
        self.controller.set_employee_fio(employee_fio)

    # set employee's job
    def set_employee_job(self, employee_job):
        self.controller.set_employee_job(employee_job)

    # insert employee information into DB
    def add_employee(self):
        # add employee to DB
        self.controller.add_employee()
        # tell the table to update
        self.table.to_table_employee()