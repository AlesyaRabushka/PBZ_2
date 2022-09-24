class Model:
    def __init__(self, controller, cursor, connection):
        self.controller = controller
        self.cursor = cursor
        self.connection = connection


        # WORK AREA
        self.work_area_name = ''
        self.work_area_number = 0
        # EQUIPMENT
        self.equipment_number = 0
        self.equipment_name = ''
        self.equipment_type = ''
        # TECH INSPECTION
        self.tech_inspection_date = ''
        self.tech_inspection_result = ''
        self.tech_inspection_worker_fio = ''
        self.tech_inspection_reason = ''
        # EMPLOYEE
        self.emp_number = 6493
        self.emp_fio = ''
        self.emp_job = ''


    # ------------- EMPLOYEE --------
    def set_emp_number(self, emp_number):
        self.emp_number = emp_number
    def set_emp_fio(self, emp_fio):
        self.emp_fio = emp_fio
    def set_emp_job(self, emp_job):
        self.emp_job = emp_job

    # add EMPLOYEE info
    def add_emp(self):
        if self.emp_number != '':
            self.cursor.execute(f"insert into сотрудник(табельный_номер, фио, должность)"
                                f" values({self.emp_number},'{self.emp_fio}','{self.emp_job}')")
            self.connection.commit()
    # delete EMPLOYEE info
    def remove_employee(self, number):
        self.cursor.execute(f"delete from сотрудник"
                            f" where табельный_номер = {int(number)}")
        self.connection.commit()
    # update EMPLOYEE info
    def update_emp(self, column_name, new_data):
        print(column_name)
        self.cursor.execute(f"update сотрудник"
                            f" set {column_name} = '{new_data}'"
                            f" where табельный_номер = {self.emp_number}")
        self.connection.commit()



    # ------------ WORK AREA ------------
    def set_work_area_number(self, number):
        self.work_area_number = number
    def set_work_area_name(self, name):
        self.work_area_name = name
    def add_work_area(self):
        if self.work_area_number != '':
            self.cursor.execute(f"insert into производственный_участок(номер, название)"
                                f" values({self.work_area_number},'{self.work_area_name}')")
            self.connection.commit()
    def remove_work_area(self, number):
        self.cursor.execute(f"delete from производственный_участок"
                            f" where номер = {int(number)}")
        self.connection.commit()

    # ------------ EQUIPMENT -------------
    def set_equipment_number(self, number):
        self.equipment_number = number
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

    # ------------ TECH INSPECTION --------
    def set_tech_inspection_date(self, date):
        self.tech_inspection_date = date
    def set_tech_inspection_result(self, result):
        self.tech_inspection_result = result
    def set_tech_inspection_worker_fio(self, fio):
        self.tech_inspection_worker_fio = fio
    def set_tech_inspection_reason(self, reason):
        self.tech_inspection_reason = reason
    def add_tech_inspection(self):
        self.cursor.execute(f"insert into технический_осмотр(дата, результат, сотрудник, причина)"
                            f" values('{self.tech_inspection_date}','{self.tech_inspection_result}','{self.tech_inspection_worker_fio}','{self.tech_inspection_reason}')")
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