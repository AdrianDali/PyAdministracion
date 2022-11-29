from cmath import e
#from DBmysql import create_
import numpy as np
from datetime   import datetime
from database.connection import create_connection
from random import randrange


class DBProceso():

    @property
    def id_proceso(self):
        return self._id_proceso

    @property
    def id_maquina(self):
        return self._id_maquina

    @property
    def id_pieza(self):
        return self._id_pieza

    @property
    def id_nombre(self):
        return self._id_nombre

    @property
    def nombre(self):
        return self._nombre

    @property
    def hora_inicio(self):
        return self._hora_inicio

    @property
    def observaciones(self):
        return self._observaciones

    @property
    def hora_inicio(self):
        return self._hora_inicio

    def __init__(self, mode='', id_maquina=0, id_pieza=0, id_nombre=0,
                 nombre="", hora_inicio='', observaciones='', proceso_terminado=0,
                 numero_piezas=0, peso_merma=0, id_proceso=0):
        self._id_proceso = id_proceso
        self._id_maquina = id_maquina
        self._id_pieza = id_pieza
        self._id_nombre = id_nombre
        self._nombre = nombre
        self._hora_inicio = hora_inicio
        self._observaciones = observaciones
        self._proceso_terminado = proceso_terminado
        self._numero_piezas = numero_piezas
        self._peso_merma = peso_merma

        if self._nombre != '' and mode == 'new':
            self._id_pieza = randrange(111111, 999999, 1)
            sql = 'INSERT INTO proceso(id_maquina,id_pieza,id_nombre ,nombre,hora_inicio,observaciones)VALUES({},{},{},"{}","{}","{}")'.format(
                id_maquina, id_pieza, id_nombre, nombre, hora_inicio, observaciones)
            try:
                connection = create_connection()
                cursor = connection.cursor()
                cursor.execute(sql)
                connection.commit()
                cursor.close()
                print("logrado proceso iniciado")
            except Exception as e:
                print(e)
                raise
        elif self._id_proceso != '' and mode == 'select':
            #print("select id proceso  ")
            self.select_proceso()
        elif self._nombre != '' and mode == 'update':
            self.update_proceso()
        else:
            print("Objeto proceso vacio")

    def filter_procesos(self, user, machine, part):


        if user != "Seleccione un usuario"and machine != 'Seleccione una maquina' and part != 'Seleccione una pieza':

             sql = 'SELECT p.id_proceso, u.nombre as nombre_usuario,p.nombre, m.nombre_maquina, i.nombre_pieza, p.hora_inicio, p.hora_termino ,p.numero_piezas ,p.peso_merma,p.observaciones, p.piezas_neto FROM proceso as p join maquina as m on m.id_maquina = p.id_maquina  join pieza as i on p.id_pieza = i.id_pieza join usuarios as u on u.id_usuario = p.id_nombre where  m.nombre_maquina = "{}" and i.nombre_pieza = "{}" and  u.nombre = "{}"  ;'.format(machine, part, user)
        
        elif machine == "Seleccione una maquina" and part == "Seleccione una pieza":
            sql = 'SELECT p.id_proceso, u.nombre as nombre_usuario,p.nombre, m.nombre_maquina, i.nombre_pieza, p.hora_inicio, p.hora_termino ,p.numero_piezas ,p.peso_merma,p.observaciones, p.piezas_neto FROM proceso as p join maquina as m on m.id_maquina = p.id_maquina  join pieza as i on p.id_pieza = i.id_pieza join usuarios as u on u.id_usuario = p.id_nombre where u.nombre = "{}";'.format(user)
        elif machine == "Seleccione una maquina" and user == "Seleccione un usuario":
            sql = 'SELECT p.id_proceso, u.nombre as nombre_usuario,p.nombre, m.nombre_maquina, i.nombre_pieza, p.hora_inicio, p.hora_termino ,p.numero_piezas , p.peso_merma,p.observaciones, p.piezas_neto FROM proceso as p join maquina as m on m.id_maquina = p.id_maquina  join pieza as i on p.id_pieza = i.id_pieza join usuarios as u on u.id_usuario = p.id_nombre where i.nombre_pieza = "{}" ;'.format(part)
        elif part == "Seleccione una pieza" and user == "Seleccione un usuario":
            sql = 'SELECT p.id_proceso, u.nombre as nombre_usuario,p.nombre, m.nombre_maquina, i.nombre_pieza, p.hora_inicio, p.hora_termino ,p.numero_piezas , p.peso_merma,p.observaciones, p.piezas_neto FROM proceso as p join maquina as m  on m.id_maquina = p.id_maquina  join pieza as i on p.id_pieza = i.id_pieza join usuarios as u on u.id_usuario = p.id_nombre where  m.nombre_maquina = "{}" ;'.format(machine)
        elif machine == "Seleccione una maquina":
            sql = 'SELECT p.id_proceso, u.nombre as nombre_usuario,p.nombre, m.nombre_maquina, i.nombre_pieza, p.hora_inicio, p.hora_termino ,p.numero_piezas , p.peso_merma,p.observaciones, p.piezas_neto FROM proceso as p join maquina as m on m.id_maquina = p.id_maquina  join pieza as i on p.id_pieza = i.id_pieza join usuarios as u on u.id_usuario = p.id_nombre where i.nombre_pieza = "{}" and u.nombre = "{}";'.format(part, user)
        elif part == "Seleccione una pieza":
            sql = 'SELECT p.id_proceso, u.nombre as nombre_usuario,p.nombre, m.nombre_maquina, i.nombre_pieza, p.hora_inicio, p.hora_termino ,p.numero_piezas , p.peso_merma,p.observaciones, p.piezas_neto FROM proceso as p join maquina as m on m.id_maquina = p.id_maquina  join pieza as i on p.id_pieza = i.id_pieza join usuarios as u on u.id_usuario = p.id_nombre where  m.nombre_maquina = "{}" and u.nombre = "{}";'.format(machine, user)
        elif user == "Seleccione un usuario":
            sql = 'SELECT p.id_proceso, u.nombre as nombre_usuario,p.nombre, m.nombre_maquina, i.nombre_pieza, p.hora_inicio, p.hora_termino ,p.numero_piezas ,p.peso_merma,p.observaciones, p.piezas_neto FROM proceso as p join maquina as m on m.id_maquina = p.id_maquina  join pieza as i on p.id_pieza = i.id_pieza join usuarios as u on u.id_usuario = p.id_nombre where  m.nombre_maquina = "{}" and i.nombre_pieza = "{}" ;'.format(machine, part)
        
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            procesos = cursor.fetchall()
            cursor.close()
            print(procesos)
            return procesos

        except Exception as e:
            print(e)
            raise

    def select_name_maquinas_enabled(self):
        sql = 'SELECT nombre_maquina from maquina where disponible = 1 '
        try:
            conn = create_connection()
            cur = conn.cursor()
            cur.execute(sql)
            maquinas = cur.fetchall()
            lista = []
            for maquina in maquinas:
                lista.append(maquina[0])
            cur.close()
            return lista
        except Exception as e:
            print(e)
            raise

    def select_procesos_user(self,id_usuario):
        sql = 'select nombre from proceso where id_nombre  = {};'.format(id_usuario)
        try:
            conn = create_connection()
            cur = conn.cursor()
            cur.execute(sql)
            maquinas = cur.fetchall()
            lista = []
            for maquina in maquinas:
                lista.append(maquina[0])
            cur.close()
            return lista
        except Exception as e:
            print(e)
            raise

    def select_all_users_name(self):
        sql = 'SELECT nombre from usuarios' 

    def select_historial(self, u_nombre , p_nombre):
        sql = ' select u.nombre, p.nombre ,pu.hora, p.peso_merma from proceso as p join proceso_usuario as pu on p.id_proceso = pu.id_proceso join usuarios as u on u.id_usuario = pu.id_usuario where u.nombre = "{}" and p.nombre = "{}"; '.format(u_nombre, p_nombre)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            procesos = cursor.fetchall()
            cursor.close()
            print("##############PROCESO##############")
            print(procesos)
            print("##############PROCESO##############")
            return procesos

        except Exception as e:
            print(e)
            raise

    def select_procesos_unfinish(self):
        sql = 'SELECT p.id_proceso, u.nombre as nombre_usuario,p.nombre, m.nombre_maquina, i.nombre_pieza, p.hora_inicio,p.numero_piezas , p.peso_merma,p.observaciones FROM proceso as p join maquina as m on m.id_maquina = p.id_maquina  join pieza as i on p.id_pieza = i.id_pieza join usuarios as u on u.id_usuario = p.id_nombre  where p.proceso_terminado = 1;'
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            procesos = cursor.fetchall()
            cursor.close()
            return procesos

        except Exception as e:
            print(e)
            raise

    def select_piezas_neto_fecha(self,day):
        now = datetime.now().strftime("%m")        
        print(now + "mes")
        sql = "SELECT piezas_neto FROM proceso  WHERE hora_inicio BETWEEN '2022-{}-{} 00:00:00' AND '2022-{}-{} 23:59:00';".format(now,day, now,day)
        try:
            conn = create_connection()
            cur = conn.cursor()
            cur.execute(sql)
            maquinas = cur.fetchall()
            lista = []
            for maquina in maquinas:
                lista.append(maquina[0])
            cur.close()

            sum_lista = 0

            for i in lista:
                sum_lista += i
            return sum_lista
        except Exception as e:
            print(e)
            raise

    def select_peso_fecha(self,day):
        now = datetime.now().strftime("%m")        
        print(now + "mes")
        sql = "SELECT peso_merma FROM proceso WHERE hora_inicio BETWEEN '2022-{}-{} 00:00:00' AND '2022-{}-{} 23:59:00';".format(now,day, now,day)
        try:
            conn = create_connection()
            cur = conn.cursor()
            cur.execute(sql)
            maquinas = cur.fetchall()
            lista = []
            for maquina in maquinas:
                lista.append(maquina[0])
            cur.close()

            sum_lista = 0

            for i in lista:
                sum_lista += i
            return int(sum_lista)
        except Exception as e:
            print(e)
            raise

    def select_peso_fecha(self,day):
        now = datetime.now().strftime("%m")        
        print(now + "mes")
        sql = "SELECT peso_merma FROM proceso WHERE hora_inicio BETWEEN '2022-{}-{} 00:00:00' AND '2022-{}-{} 23:59:00';".format(now,day, now,day)
        try:
            conn = create_connection()
            cur = conn.cursor()
            cur.execute(sql)
            maquinas = cur.fetchall()
            lista = []
            for maquina in maquinas:
                lista.append(maquina[0])
            cur.close()

            sum_lista = 0

            for i in lista:
                sum_lista += i
            return int(sum_lista)
        except Exception as e:
            print(e)
            raise


    def select_peso_neto_fecha_user(self,day,user):
        date = day.split(" ")

        #print("dia" + date[0])
        now = datetime.now().strftime("%m")        
        #print(now + "mes")
        sql = "SELECT p.peso_merma FROM proceso AS p JOIN usuarios AS u WHERE u.nombre = '{}' AND hora_inicio BETWEEN '{} 00:00:00' AND '{} 23:59:00';".format(user,date[0],date[0])
        try:
            conn = create_connection()
            cur = conn.cursor()
            cur.execute(sql)
            maquinas = cur.fetchall()
            lista = []
            for maquina in maquinas:
                lista.append(maquina[0])
            cur.close()

            sum_lista = 0

            for i in lista:
                sum_lista += i

            print("LISTA PESOOOO::  ")
            print(lista)
            return int(sum_lista)
        except Exception as e:
            print(e)
            raise

    def select_piezas_neto_fecha_user(self,day,user):
        date = day.split(" ")

        #print("dia" + date[0])
        now = datetime.now().strftime("%m")        
        #print(now + "mes")
        sql = "SELECT p.piezas_neto FROM proceso AS p JOIN usuarios AS u WHERE u.nombre = '{}' AND hora_inicio BETWEEN '{} 00:00:00' AND '{} 23:59:00';".format(user,date[0],date[0])
        try:
            conn = create_connection()
            cur = conn.cursor()
            cur.execute(sql)
            maquinas = cur.fetchall()
            lista = []
            for maquina in maquinas:
                lista.append(maquina[0])
            cur.close()

            sum_lista = 0

            for i in lista:
                sum_lista += i

            #print("LISTA::  ")
            #print(lista)
            return sum_lista
        except Exception as e:
            print(e)
            raise

    def select_all_procesos(self):
        sql = 'SELECT p.id_proceso, u.nombre as nombre_usuario,p.nombre, m.nombre_maquina, i.nombre_pieza, p.hora_inicio, p.hora_termino ,p.numero_piezas , p.peso_merma,p.observaciones, p.piezas_neto FROM proceso as p join maquina as m on m.id_maquina = p.id_maquina  join pieza as i on p.id_pieza = i.id_pieza join usuarios as u on u.id_usuario = p.id_nombre'
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            procesos = cursor.fetchall()
            cursor.close()
            return procesos

        except Exception as e:
            print(e)
            raise

    def insertar_monitoreo_proceso(idProceso, idUsuario):
        fecha = datetime.datetime.now()
        print(idProceso)
        print(str(fecha.strftime("%Y-%m-%d %H:%M:%S")))
        sql = "insert into proceso_usuario(id_proceso, id_usuario,hora) values({},{},'{}')".format(
            idProceso, idUsuario, str(fecha.strftime("%H:%M:%S")))
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            print("logrado ")
            cursor.close()
        except Exception as e:
            raise

    def actualizar_piezas_proceso(contador, idProceso):
        sql = "update proceso set numero_piezas = {} where id_proceso = {}".format(
            contador, idProceso)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            print("logrado")
            cursor.close()
        except Exception as e:
            raise

    def update_proceso(self):
        sql = "UPDATE proceso SET id_maquina = {}, id_pieza = {}, id_nombre = {}, nombre = '{}' WHERE id_proceso = {}".format(
            self._id_maquina, self._id_pieza, self._id_nombre, self._nombre, self._id_proceso)
        print("idprceosd  ")
        print(self._id_proceso)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            print("logrado")
            cursor.close()
        except Exception as e:
            raise

    def finish_proceso(self):
        sql = "UPDATE proceso SET hora_termino = '2022-07-14 23:35:10' , proceso_terminado = 1 WHERE id_proceso = 1;".format(self._id_maquina,
                                                                                                                             self._id_pieza, self._id_nombre, self._nombre, self._id_proceso)
        print("idprceosd  ")
        print(self._id_proceso)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            print("logrado")
            cursor.close()
        except Exception as e:
            raise

    def actualizar_peso_proceso(contador, idProceso):
        sql = "update proceso set peso_merma = {} where id_proceso = {}".format(
            contador, idProceso)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            print("logrado")
            cursor.close()
        except Exception as e:
            raise

    def select_id_proceso(self):
        sql = 'SELECT * from proceso where nombre = "{}" '.format(
            self.nombre_proceso)
        objeto_usuario = []
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            self.nombre_proceso = cursor.fetchall()
            user = self.nombre_proceso
            print(user)
            cursor.close()
            return user
        except Exception as e:
            print(e)
            raise

    def select_proceso(self):
        sql = 'SELECT * from proceso where id_proceso = {} '.format(
            self._id_proceso)
        objeto_usuario = []
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            self.nombre_proceso = []
            self.nombre_proceso = cursor.fetchall()

            user = self.nombre_proceso
            if (user == []):
                print("no existe nada en la DB")

            else:
                self._nombre = user[0][4]
                self._id_proceso = user[0][0]
                self._id_maquina = user[0][1]
                self._id_pieza = user[0][2]
                self._id_nombre = user[0][3]
                self._hora_inicio = user[0][5]
                # print(self.hora_inicio)
                print(user)
                cursor.close()
                return user
        except Exception as e:
            print(e)
            raise


#print("obejto medicina ")
#maquina  = DBProceso(mode = "select" , id_proceso = 43)
#print("select proceso")
# maquina.select_proceso()
#list = maquina.select_name_maquinas_enabled()
# print(list)

# print(select_procesos_unfinish())
# print(insertar_monitoreo_proceso(43,2))
# print(actualizar_piezas_proceso(1,43))
# print(actualizar_peso_proceso(88,43))
# print(select_id_proceso("proceso00"))
#processs = DBProceso(2,2,2,"proceso00","2020-12-12 12:12:12","observaciones")
