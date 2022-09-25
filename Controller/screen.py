from Model.screen import Model
from View.screen import MainScreen

class Controller:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection

        self.model = Model(controller = self, cursor = self.cursor, connection = self.connection)
        self.main_view = MainScreen(controller = self, model = self.model)


    # -------- EMPLOYEE --------
    # set EMPLOYEE info
    def set_employee_number(self, employee_number):
        self.model.set_employee_number(employee_number)
    def set_employee_old_number(self, number):
        self.model.set_employee_old_number(number)
    def set_employee_fio(self, employee_fio):
        if self.is_string(employee_fio) and not self.is_empty(employee_fio) and len(employee_fio) <= 50:
            self.model.set_employee_fio(employee_fio)
    def set_employee_job(self, employee_job):
        if self.is_string(employee_job) and not self.is_empty(employee_job) and len(employee_job) <= 100:
            self.model.set_employee_job(employee_job)
    # add EMPLOYEE
    def add_employee(self):
        self.model.add_employee()
    def remove_employee(self, number):
        self.model.remove_employee(number)


    def delete_emp(self):
        self.model.delete_employee()
    def update_employee(self):
        self.model.update_employee()

    # ------------- EQUIPMENT ---------------
    def set_equipment_number(self, number):
        self.model.set_equipment_number(number)
    def set_equipment_old_number(self, number):
        self.model.set_equipment_old_number(number)
    def set_equipment_name(self, name):
        self.model.set_equipment_name(name)
    def set_equipment_type(self, type):
        self.model.set_equipment_type(type)
    def add_equipment(self):
        self.model.add_equipment()
    def remove_equipment(self, number):
        self.model.remove_equipment(number)
    def update_equipment(self):
        self.model.update_equipment()

    # ------------- WORK AREA --------------------
    def set_work_area_number(self, number):
        self.model.set_work_area_number(number)
    def set_work_area_old_number(self, number):
        self.model.set_work_area_old_number(number)
    def set_work_area_name(self, name):
        self.model.set_work_area_name(name)
    def add_work_area(self):
        self.model.add_work_area()
    def remove_work_area(self, number):
        self.model.remove_work_area(number)
    def update_work_area(self):
        self.model.update_work_area()


    # -------------- TECH INSPECTION ------------
    def set_tech_inspection_date(self, date):
        self.model.set_tech_inspection_date(date)
    def set_tech_inspection_old_date(self, date):
        self.model.set_tech_inspection_old_date(date)
    def set_tech_inspection_result(self, result):
        self.model.set_tech_inspection_result(result)
    def set_tech_inspection_worker_fio(self, worker_fio):
        self.model.set_tech_inspection_worker_fio(worker_fio)
    def set_tech_inspection_reason(self, reason):
        self.model.set_tech_inspection_reason(reason)
    def add_tech_inspection(self):
        self.model.add_tech_inspection()
    def remove_tech_inspection(self, date):
        self.model.remove_tech_inspection(date)
    def update_tech_inspection(self):
        self.model.update_tech_inspection()


    # ---------------------------------------------------------
    # returns True if str, False if it is not
    def is_string(self, string):
        numbers = '1234567890*+-/|,:;_&^%$#@=\'\"'
        for i in string:
            for j in numbers:
                if i == j:
                    return False
        return True

    # returns True if empty, False if it is not
    def is_empty(self, string):
        if len(string) == 0:
            return True
        else:
            return False



    def get_table_work_area(self):
        return self.model.get_table_work_area()
    def get_table_tech_inspection(self):
        return self.model.get_table_tech_inspection()
    def get_table_equipment(self):
        return self.model.get_table_equipment()
    def get_table_emp(self):
        return self.model.get_table_emp()
    def get_screen(self):
        return self.main_view