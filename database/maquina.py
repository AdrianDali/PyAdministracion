from database.connection import create_connection
from random import randrange, choice



class DBMaquina():
    
    def __init__(self, mode = '' ,nombre = '',id_maquina = 0):
        self._id_maquina = id_maquina
        self._nombre = nombre
        self._disponible = 0
        
        if self._nombre != '' and mode == 'new':
            self._id_maquina = randrange(1111,9999,1)
            sql = 'INSERT INTO maquina(id_maquina,nombre_maquina,disponible) VALUES("{}","{}",1)'.format(self._id_maquina, self._nombre)
            try:
                connection = create_connection()
                cursor = connection.cursor()
                cursor.execute(sql)
                connection.commit()
                cursor.close()
                print("logrado")
            except Exception as e:
                print("************ERROR AL METER LA NUEVA MAQUINA******************")
                print(e)
                raise
        elif self._nombre != '' and mode == 'select':
            self.select_id_maquina()
        elif self.id_maquina != 0 and mode == 'select':
            self.select_maquina()
        
        else:
            print("Objeto vacio")

       



    def select_maquina(self):
        sql = 'SELECT id_maquina, nombre_maquina, disponible from maquina where id_maquina = {}'.format(self._id_maquina)
        objeto_maquina = []
        try: 
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            maquina = cursor.fetchone()
            objeto_maquina = [maquina[0],maquina[1],maquina[2]]
            cursor.close()
            self._nombre = maquina[1]
            self._disponible = maquina[2]
            return objeto_maquina
        except Exception as e:
            print(e)
            raise
    
    def select_name_maquinas_enabled(self):
        sql = 'SELECT nombre_maquina from maquina where disponible = 1 '
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            maquinas = cursor.fetchall()
            lista  = []
            for maquina in maquinas:
                lista.append(maquina[0])
                cursor.close()
            return lista
        except Exception as e:
            print(e)
            raise

    def select_name_maquinas(self):
        sql = 'SELECT nombre_maquina from maquina'
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            maquinas = cursor.fetchall()
            lista  = []
            for maquina in maquinas:
                lista.append(maquina[0])
                cursor.close()
            return lista
        except Exception as e:
            print(e)
            raise
    
    def select_id_maquina(self):
        print(self._nombre)
        sql = 'SELECT id_maquina from maquina where nombre_maquina = "{}"'.format(self._nombre)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            id = cursor.fetchone()
            self._id_maquina = id[0]
            #cursor.close()
        except Exception as e: 
            print(e)
            raise

    
    def select_maquina_info(self):
        print("select 222")
        sql = 'SELECT id_maquina, nombre_maquina, disponible from maquina where id_maquina = {}'.format(self._id_maquina)
        objeto_usuario = []
        try: 
            conn = create_connection()
            cur = conn.cursor()
            cur.execute(sql)
            usuario = cur.fetchone()
            #print(usuario)
            objeto_usuario = [usuario[0],usuario[1],usuario[2]]
            print("objeto usuario",objeto_usuario)
           
            self._nombre = usuario[1]
            self._disponible = usuario[2]
            print(self._nombre)
            #print("self nombre")
            #print(self._nombre)
            cur.close()
            return objeto_usuario
        except Exception as e:
            print(e)
            raise
    
    def update_maquina(self, name):
        sql = 'UPDATE maquina SET nombre_maquina = "{}" WHERE id_maquina = {}'.format(name, self._id_maquina)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            cursor.close()
        except Exception as e:
            print(e)
            raise

    
    @property 
    def id_maquina(self):
        return self._id_maquina
    
    @property
    def nombre(self):
        return self._nombre
            

    

#maquina  = DBMaquina("select", "MAQUINA1")
#print(maquina.id_maquina)
#print(maquina.nombre)
#list = select_name_maquinas_enabled()
#print(maquina.select_maquina(1))
#print(list)