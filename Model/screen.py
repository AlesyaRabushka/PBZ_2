from datetime import datetime


class Model:
    def __init__(self, controller, cursor, connection):
        self.controller = controller
        self.cursor = cursor
        self.connection = connection


        # WORK AREA
        self.work_area_name = ''
        self.work_area_number = 0
        self.work_area_old_number = 0
        self.work_area_equipment_type = ''
        # EQUIPMENT
        self.equipment_number = 0
        self.equipment_old_number = 0
        self.equipment_name = ''
        self.equipment_type = ''
        # TECH INSPECTION
        self.tech_inspection_date = ''
        self.tech_inspection_old_date = ''
        self.tech_inspection_equipment_number = 0
        self.tech_inspection_result = ''
        self.tech_inspection_worker_fio = ''
        self.tech_inspection_reason = ''
        # EMPLOYEE
        self.employee_number = 0
        self.employee_old_number = 0
        self.employee_fio = ''
        self.employee_job = ''

        #SEARCH
        self.search_tech_inspection_equipment_number = 0
        self.table_search_tech_inspection = []
        self.table_search = []
        self.search_employee_date = ''
        self.search_equipment_date = ''


    # ------------- EMPLOYEE --------
    def set_employee_number(self, emp_number):
        self.employee_number = emp_number
    def set_employee_old_number(self, emp_number):
        self.employee_old_number = emp_number
    def set_employee_fio(self, emp_fio):
        self.employee_fio = emp_fio
    def set_employee_job(self, emp_job):
        self.employee_job = emp_job

    # add EMPLOYEE info
    def add_employee(self):
        if self.employee_number != '':
            self.cursor.execute(f"insert into сотрудник(табельный_номер, фио, должность)"
                                f" values({self.employee_number},'{self.employee_fio}','{self.employee_job}')")
            self.connection.commit()
    # delete EMPLOYEE info
    def remove_employee(self, number):
        self.cursor.execute(f"delete from сотрудник"
                            f" where табельный_номер = {int(number)}")
        self.connection.commit()
    # update EMPLOYEE info
    def update_employee(self):
        print(self.employee_old_number, self.employee_fio, self.employee_job )
        self.cursor.execute(f"update сотрудник"
                            f" set табельный_номер = '{int(self.employee_number)}', фио = '{self.employee_fio}', должность = '{self.employee_job}'"
                            f" where табельный_номер = {self.employee_old_number}")
        self.connection.commit()



    # ------------ WORK AREA ------------
    def set_work_area_number(self, number):
        self.work_area_number = number
    def set_work_area_old_number(self, number):
        self.work_area_old_number = number
    def set_work_area_name(self, name):
        self.work_area_name = name
    def set_work_area_equipment_type(self, type):
        self.work_area_equipment_type = type
    def add_work_area(self):
        if self.work_area_number != '':
            self.cursor.execute(f"insert into производственный_участок(номер, название, тип_оборудования)"
                                f" values({self.work_area_number},'{self.work_area_name}', '{self.work_area_equipment_type}')")
            self.connection.commit()
    def remove_work_area(self, number):
        self.cursor.execute(f"delete from производственный_участок"
                            f" where номер = {int(number)}")
        self.connection.commit()

    def update_work_area(self):
        self.cursor.execute(f"update производственный_участок"
                            f" set название = '{self.work_area_name}', номер = '{self.work_area_number}', тип_оборудования = '{self.work_area_equipment_type}'"
                            f" where номер = {int(self.work_area_old_number)}")
        self.connection.commit()

    # ------------ EQUIPMENT -------------
    def set_equipment_number(self, number):
        self.equipment_number = number
    def set_equipment_old_number(self, number):
        self.equipment_old_number = number
    def set_equipment_name(self, name):
        self.equipment_name = name
    def set_equipment_type(self, type):
        self.equipment_type = type
    def add_equipment(self):
        self.cursor.execute(f"insert into оборудование(номер, название,тип)"
                            f" values({self.equipment_number},'{self.equipment_name}','{self.equipment_type}')")
        self.connection.commit()
    def remove_equipment(self, number):
        self.cursor.execute(f"delete from оборудование"
                            f" where номер = {int(number)}")
        self.connection.commit()
    def update_equipment(self):
        self.cursor.execute(f"update оборудование"
                            f" set название = '{self.equipment_name}', тип = '{self.equipment_type}', номер = '{int(self.equipment_number)}'"
                            f" where номер = {int(self.equipment_old_number)}")
        self.connection.commit()

    # ------------ TECH INSPECTION --------
    def set_tech_inspection_result(self, result):
        self.tech_inspection_result = result
    def set_tech_inspection_equipment_number(self, number):
        self.tech_inspection_equipment_number = number
    def set_tech_inspection_worker_fio(self, fio):
        self.tech_inspection_worker_fio = fio
    def set_tech_inspection_reason(self, reason):
        self.tech_inspection_reason = reason
    def add_tech_inspection(self):
        self.cursor.execute(f"insert into технический_осмотр(дата, номер_оборудования, результат, сотрудник, причина)"
                            f" values('{self.tech_inspection_date}',{self.tech_inspection_equipment_number},'{self.tech_inspection_result}','{self.tech_inspection_worker_fio}','{self.tech_inspection_reason}')")
        self.connection.commit()
    def set_tech_inspection_date(self, birth):
        self.tech_inspection_date = datetime.strptime(birth, '%Y-%m-%d')
    def set_tech_inspection_old_date(self, birth):
        self.tech_inspection_old_date = datetime.strptime(birth, '%Y-%m-%d')
    def remove_tech_inspection(self, date):
        self.cursor.execute(f" delete from технический_осмотр "
                            f"where дата = '{date}'::date")
        self.connection.commit()
    def update_tech_inspection(self):
        self.cursor.execute(f"update технический_осмотр"
                            f" set дата = '{self.tech_inspection_date}', номер_оборудования = '{self.tech_inspection_equipment_number}', результат = '{self.tech_inspection_result}', сотрудник = '{self.tech_inspection_worker_fio}', причина = '{self.tech_inspection_reason}'"
                            f" where дата = '{self.tech_inspection_old_date}'::date")
        self.connection.commit()


    # return table ПРОИЗВОДСТВЕННЫЙ_УЧАСТОК
    def get_table_work_area(self):
        table_work_are_list = []
        self.cursor.execute("select * from производственный_участок")
        rows = self.cursor.fetchall()
        for row in rows:
            work_area = []
            work_area.append(row[0])
            work_area.append(row[1])
            work_area.append(row[2])
            table_work_are_list.append(work_area)
        return table_work_are_list

    # return table ОБОРУДОВАНИЕ
    def get_table_equipment(self):
        table_equipment_list = []
        self.cursor.execute("select * from оборудование")
        rows = self.cursor.fetchall()
        for row in rows:
            equipment = []
            equipment.append(row[0])
            equipment.append(row[1])
            equipment.append(row[2])
            table_equipment_list.append(equipment)
        print(table_equipment_list)
        return table_equipment_list

    # return table ТЕХНИЧЕСКИЙ_ОСМОТР
    def get_table_tech_inspection(self):
        table_tech_inspection = []
        self.cursor.execute("select * from технический_осмотр")
        rows = self.cursor.fetchall()
        for row in rows:
            tech_inspection = []
            tech_inspection.append(row[0])
            tech_inspection.append(row[1])
            tech_inspection.append(row[2])
            tech_inspection.append(row[3])
            tech_inspection.append(row[4])
            table_tech_inspection.append(tech_inspection)
        return table_tech_inspection

    # return table СОТРУДНИК
    def get_table_emp(self):
        table_emp_list = []
        self.cursor.execute("select * from сотрудник")
        rows = self.cursor.fetchall()  # select all the rows
        for row in rows:
            employee = []
            employee.append(row[0])
            employee.append(row[1])
            employee.append(row[2])
            table_emp_list.append(employee)
        return table_emp_list


    # --------------------------- SEARCH ------------------------
    # SEARCH TECH INSPECTION
    def search_tech_inspection(self):
        self.table_search_tech_inspection = []
        self.cursor.execute(f"select технический_осмотр.дата, оборудование.номер,оборудование.название, оборудование.тип, технический_осмотр.результат "
                            f"from технический_осмотр "
                            f"inner join оборудование "
                            f"on технический_осмотр.номер_оборудования = оборудование.номер "
                            f"where оборудование.номер = {self.search_tech_inspection_equipment_number};")
        rows = self.cursor.fetchall()
        for row in rows:
            tech_inspection = []
            tech_inspection.append(row[0])
            tech_inspection.append(row[1])
            tech_inspection.append(row[2])
            tech_inspection.append(row[3])
            tech_inspection.append(row[4])
            self.table_search_tech_inspection.append(tech_inspection)
        self.controller.show_table_search_tech_inspection()

    def set_search_tech_inspection_equipment_number(self, number):
        self.search_tech_inspection_equipment_number = number
    def return_table_search_tech_inspection(self):
        return self.table_search_tech_inspection

    # SEARCH EMPLOYEE
    def search_employee(self):
        self.table_search = []
        self.cursor.execute(
            f"select сотрудник.фио, сотрудник.должность "
            f"from технический_осмотр "
            f"inner join сотрудник "
            f"on технический_осмотр.сотрудник = сотрудник.фио "
            f"where технический_осмотр.дата = '{self.search_employee_date}'::date")
        rows = self.cursor.fetchall()
        for row in rows:
            tech_inspection = []
            tech_inspection.append(row[0])
            tech_inspection.append(row[1])
            self.table_search.append(tech_inspection)
        self.controller.show_table_search_emeployee()

    def set_search_employee_date(self, date):
        self.search_employee_date = datetime.strptime(date, '%Y-%m-%d')

    def return_table_search_employee(self):
        return self.table_search

    # SEARCH EQUIPMENT
    def set_search_equipment_date(self, date):
        self.search_equipment_date = datetime.strptime(date, '%Y-%m-%d')
    def return_table_search_equipment(self):
        return self.table_search
    def search_equipment(self):
        self.table_search = []
        self.cursor.execute(
            f"select технический_осмотр.дата, оборудование.название, оборудование.тип, производственный_участок.название, технический_осмотр.причина "
            f"from производственный_участок "
            f"inner join оборудование "
            f"on производственный_участок.тип_оборудования = оборудование.тип "
            f"inner join технический_осмотр "
            f"on оборудование.номер = технический_осмотр.номер_оборудования "
            f"where технический_осмотр.дата = '{self.search_equipment_date}'::date")
        rows = self.cursor.fetchall()
        for row in rows:
            tech_inspection = []
            tech_inspection.append(row[0])
            tech_inspection.append(row[1])
            tech_inspection.append(row[2])
            tech_inspection.append(row[3])
            tech_inspection.append(row[4])
            self.table_search.append(tech_inspection)
        self.controller.show_table_search_equipment()

