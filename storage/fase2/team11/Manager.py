from storage.avl import avlMode as avl
from storage.b import BMode as b
from storage.bplus import BPlusMode as bPlus
from storage.dict import DictMode as diccionario
from storage.isam import ISAMMode as isam
from storage.hash import HashMode as hash
from storage.json import jsonMode as json
from Binary import verify_string
from checksum import checksum_database, checksum_table
import criptografia as crypt
from estruct.blockChain import BlockChain
from metadata import Database, Table, FK

metadata_db_list = list()
flag_block = False
block_list = list()

mode_dict = {'avl': 1, 'b': 2, 'bplus': 3, 'dict': 4, 'hash': 5, 'isam': 6, 'json': 7}


def save_database_db(database, mode, encondig):
    new_mode = Database(database, mode, encondig)
    metadata_db_list.append(new_mode)


def get_metadata_db(database: str):
    index = 0
    for db in metadata_db_list:
        if db.get_name_database() == database:
            return db, index
        index += 1
    return None, None


def get_metadata_dbmode(database: str, mode: str):
    for db in metadata_db_list:
        if db.get_name_database() == database and db.get_mode() == mode:
            return db
    return None


# -------------------------------------------- --> Get Struct <-- ----------------------------------------------------
# Metodo que retorna la estructura correspondiente al modo
def get_struct(mode: str):
    if mode.lower().strip() == "avl":
        return avl
    elif mode.lower().strip() == "b":
        return b
    elif mode.lower().strip() == "bplus":
        return bPlus
    elif mode.lower().strip() == "dict":
        return diccionario
    elif mode.lower().strip() == "hash":
        return hash
    elif mode.lower().strip() == "isam":
        return isam
    elif mode.lower().strip() == "json":
        return json


# -------------------------------------------- --> <-> <-- -----------------------------------------------------------
# Revisar para Metadata
def createDatabase(database: str, mode: str, encoding: str):
    if verify_string(database):  # Metodo que verifica el nombre si cumple con las condiciones
        metadata, index = get_metadata_db(database)
        if metadata: return 2  # Verifica que no haya repetidos en el listado de metadata database
        if str(encoding.lower().strip()) == "ascii" or str(encoding.lower().strip()) == "iso-8859-1" \
                or str(encoding.lower().strip()) == "utf8":  # Revisa que cumpla con la codificacion
            if mode_dict.get(mode) is None: return 3  # Revisa que el modo este en el diccionario  si no esta retorno 3
            mode_struct = get_struct(mode)  # Retorna el objeto avl,b,bplus, etc dependiendo el modo
            status = mode_struct.createDatabase(database)  # Crea base de datos de la estructura correspondiente(avl,b)
            if status == 0:  # Si el estatus es el correcto guarda en la lista metadata_db_list
                save_database_db(database, mode.lower().strip(), encoding)  # Guarda en la lista metada_db_list
            return status
        else:
            return 4
    else:
        return 1




def alterDatabaseMode(database: str, mode: str):
    ModeDB, indexDB = exist_Alter(database)
    mode_list.pop(indexDB)
    createDatabase(database, mode, ModeDB.get_encondig())
    if ModeDB:

        oldMode = ModeDB.get_mode()
        if oldMode.lower().strip() == "avl":
            tables = avl.showTables(database)
            for tabla in tables:
                listaDatos = get_Data(database, tabla, oldMode)
                numberColumns = len(listaDatos[0])
                insertAlter(database, tabla, numberColumns, mode, listaDatos)
            avl.dropDatabase(database)
        elif oldMode.lower().strip() == "b":
            tables = b.showTables(database)
            for tabla in tables:
                listaDatos = get_Data(database, tabla, oldMode)
                numberColumns = len(listaDatos[0])
                insertAlter(database, tabla, numberColumns, mode, listaDatos)
            b.dropDatabase(database)
        elif oldMode.lower().strip() == "bPlus".lower():
            tables = bPlus.showTables(database)
            for tabla in tables:
                listaDatos = get_Data(database, tabla, oldMode)
                numberColumns = len(listaDatos[0])
                insertAlter(database, tabla, numberColumns, mode, listaDatos)
            bPlus.dropDatabase(database)
        elif oldMode.lower().strip() == "dict":
            tables = diccionario.showTables(database)
            for tabla in tables:
                listaDatos = get_Data(database, tabla, oldMode)
                numberColumns = len(listaDatos[0])
                insertAlter(database, tabla, numberColumns, mode, listaDatos)
            diccionario.dropDatabase(database)
        elif oldMode.lower().strip() == "isam":
            tables = isam.showTables(database)
            for tabla in tables:
                listaDatos = get_Data(database, tabla, oldMode)
                numberColumns = len(listaDatos[0])
                insertAlter(database, tabla, numberColumns, mode, listaDatos)
            isam.dropDatabase(database)
        elif oldMode.lower().strip() == "hash":
            tables = hash.showTables(database)
            for tabla in tables:
                listaDatos = get_Data(database, tabla, oldMode)
                numberColumns = len(listaDatos[0])
                insertAlter(database, tabla, numberColumns, mode, listaDatos)
            hash.dropDatabase(database)
        elif oldMode.lower().strip() == "json":
            tables = json.showTables(database)
            for tabla in tables:
                listaDatos = get_Data(database, tabla, oldMode)
                numberColumns = len(listaDatos[0])
                insertAlter(database, tabla, numberColumns, mode, listaDatos)
            json.dropDatabase(database)


def insertAlter(database, tabla, numberColumns, mode, listaDatos):
    if mode.lower().strip() == "avl":
        avl.createTable(database, tabla, numberColumns)
        for data in listaDatos:
            avl.insert(database, tabla, data)
    elif mode.lower().strip() == "b":
        b.createTable(database, tabla, numberColumns)
        for data in listaDatos:
            b.insert(database, tabla, data)
    elif mode.lower().strip() == "bPlus".lower():
        bPlus.createTable(database, tabla, numberColumns)
        for data in listaDatos:
            bPlus.insert(database, tabla, data)
    elif mode.lower().strip() == "dict":
        diccionario.createTable(database, tabla, numberColumns)
        for data in listaDatos:
            diccionario.insert(database, tabla, data)
    elif mode.lower().strip() == "isam":
        isam.createTable(database, tabla, numberColumns)
        for data in listaDatos:
            isam.insert(database, tabla, data)
    elif mode.lower().strip() == "hash":
        hash.createTable(database, tabla, numberColumns)
        for data in listaDatos:
            hash.insert(database, tabla, data)
    elif mode.lower().strip() == "json":
        json.createTable(database, tabla, numberColumns)
        for data in listaDatos:
            json.insert(database, tabla, data)


def get_Data(database: str, table: str, mode: str):
    if mode.lower().strip() == "avl":
        return avl.extractTable(database, table)
    elif mode.lower().strip() == "b":
        return b.extractTable(database, table)
    elif mode.lower().strip() == "bPlus".lower():
        return bPlus.extractTable(database, table)
    elif mode.lower().strip() == "dict":
        return diccionario.extractTable(database, table)
    elif mode.lower().strip() == "isam":
        return isam.extractTable(database, table)
    elif mode.lower().strip() == "hash":
        return hash.extractTable(database, table)
    elif mode.lower().strip() == "json":
        return json.extractTable(database, table)


def alterTableMode(database: str, table: str, mode: str):
    metadata_db, index_metadata = get_metadata_db(database) 
    metadata_db = Database() 
    if metadata_db:
        oldMode = metadata_db.get_mode()
        encoding = metadata_db.get_encondig()
        if mode not in ["avl","b","bPlus","dict","isam","hash","json"]: return 4
        struct = get_struct(metadata_db.get_mode())
        tables = struct.showTables(database)
        for tabla in tables:
            if tabla == table:
                listaDatos = get_Data(database, tabla, oldMode)  # UNA LISTA VACIA NO EJECUTA EL FOR
                numberColumns = len(listaDatos[0])
                #insertAlter(database+"_"+mode, tabla, numberColumns, mode, listaDatos)
                if metadata_db.get_table(table).get_pk_list() != []:
                    alterAddPK(database, table,metadata_db.get_table(table).get_pk_list())
                createDatabase(database+"_"+mode, mode, encoding)
                createTable(database+"_"+mode, table, numberColumns)
                for i in listaDatos:
                    insert(database, table,i)
                struct.dropTable(database, table)
                return 0
        return 3
    else:
        return 2


# Revisar para Metadata
def alterDatabase(old_db, new_db):
    metadata_db, index_md_db = get_metadata_db(old_db)
    metadata_db_new, index_new_md_db = get_metadata_db(new_db)
    if metadata_db and metadata_db_new is None:
        struct = get_struct(metadata_db.get_mode())
        status = struct.alterDatabase(old_db, new_db)
        if status == 0:
            metadata_db.set_name_database(new_db)
        return status
    return 1



# Revisar Para Metadata
def dropDatabase(name_db):
    metadata_db, index_metadata = get_metadata_db(name_db)
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        status = struct.dropDatabase(name_db)
        if status == 0:
            metadata_db_list.pop(index_metadata)
        return status
    else:
        return 1



# Revisar para Metadata
def createTable(database, name_table, number_columns):
    metadata_db, index_metadata = get_metadata_db(database)
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        status = struct.createTable(database, name_table, number_columns)
        if status == 0:
            metadata_db.create_table(name_table, number_columns, metadata_db.get_mode())
        return status
    else:
        return 1


def showTables(database):
    metadata_db, index_md_db = get_metadata_db(database)
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        status = struct.showTables(database)
        return status
    return 1


def extractTable(database, name_table):
    metadata_db, index_md_db = get_metadata_db(database)
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        status = struct.extractTable(database, name_table)
        return status
    return 1


def extractRangeTable(database, name_table, number_column, lower, upper):
    metadata_db, index_md_db = get_metadata_db(database)
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        status = struct.extractRangeTable(database, name_table, number_column, lower, upper)
        return status
    return 1


def alterAddPK(database, name_table, columns):
    metadata_db: Database
    metadata_db, index_md_db = get_metadata_db(database)
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        status = struct.alterAddPK(database, name_table, columns)
        if status == 0:
            tabla: Table = metadata_db.get_table(name_table)
            tabla.add_pk_list(columns)
        return status
    return 1


def alterDropPK(database, name_table):
    metadata_db, index_md_db = get_metadata_db(database)
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        status = struct.alterDropPK(database, name_table)
        if status == 0:
            tabla: Table = metadata_db.get_table(name_table)
            tabla.add_pk_list([])
        return status
    return 1


def alterTable(database, old_table, new_table):
    metadata_db, index_metadata = get_metadata_db(database)  
    if metadata_db:
        retorno = metadata_db.alter_table(old_table, new_table) 
        if retorno==0:
            struct = get_struct(metadata_db.get_mode())
            status = struct.alterTable(database, old_table, new_table)
            return status
    else:
        return 2

def alterAddColumn(database, name_table, default):
    metadata_db, index_metadata = get_metadata_db(database)  # verificar metadata
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        status = struct.alterAddColumn(database, name_table, default)
        return status
    else:
        return 2

def alterDropColumn(database, name_table, number_column): # verificar metadata
    metadata_db, index_metadata = get_metadata_db(database)
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        status = struct.alterDropColumn(database, name_table, number_column)
        return status
    else:
        return 2

def dropTable(database, name_table):
    metadata_db, index_metadata = get_metadata_db(database)
    if metadata_db:
        retorno = metadata_db.drop_table(name_table)
        if retorno!=1:
            struct = get_struct(metadata_db.get_mode())
            status = struct.dropTable(database, name_table)
            return status
    else:
        return 2

def insert(database, name_table, register: list):
    metadata_db, index_metadata = get_metadata_db(database)
    if metadata_db:
        if name_table in metadata_db.get_tab():
            struct = get_struct(metadata_db.get_mode())
            if metadata_db.get_encondig().lower().strip() == "ascii":
                if encodi_ascii_decod(register,"ascii") != 1:
                    status = struct.insert(database, name_table, register)
                    return status
                else:
                    return 1
            elif metadata_db.get_encondig().lower().strip() == "utf-8":
                if encodi_utf_decod(register,"utf-8") !=1:
                    status = struct.insert(database, name_table, register)
                    return status
                else:
                    return 1
            elif metadata_db.get_encondig().lower().strip() == "iso-8859-1":
                if encodi_iso_decod(register,"iso-8859-1") !=1:
                    status = struct.insert(database, name_table, register)
                    return status
                else:
                    return 1
            else:
                None
        else:
            return 3
    else:
        return 2

#-------------------ENCODING--------------------------------
def alterDatabaseEncoding(database: str, encoding: str):
    metadata_db, index_metadata = get_metadata_db(database)
    if metadata_db:
        struct = get_struct(metadata_db.get_mode())
        tables = struct.showTables(database)
        state = 0
        if encoding not in ["ascii","utf-8","iso-8859-1"]: return 3
        for e in tables:
            tuplas = struct.extractTable(database,e)
            for n in tuplas:
                if encoding == "ascii" and encodi_ascii_decod(n,encoding) !=1:
                    pass
                elif encoding == "utf-8" and encodi_utf_decod(n,encoding) !=1:
                    pass
                elif encoding == "iso-8859-1" and encodi_iso_decod(n,encoding) !=1:
                    pass
                else:
                    return 1
        if state == 0:
             metadata_db.set_encondig(encoding)
             return 0
    else:
        return 2



def encodi_ascii_decod(lista: list ,encoding: str):
    try:
        for i in lista:
            str(i).encode(f'{encoding}').decode(f'{encoding}')
        return 0
    except:
        return 1

def encodi_utf_decod(lista: list ,encoding: str):
    try:
        for i in lista:
            str(i).encode('utf-8').decode('utf-8')
        return 0
    except:
        return 1

def encodi_iso_decod(lista: list ,encoding: str):
    try:
        for i in lista:
            str(i).encode('iso-8859-1').decode('iso-8859-1')
        return lista
    except:
        return 1


def extractRow(database, name_table, columns):
    ModeDB, indexDB = exist_Alter(database)
    if ModeDB:
        mode = ModeDB.get_mode()
        if mode.lower().strip() == "avl":
            return avl.extractRow(database, name_table, columns)
        elif mode.lower().strip() == "b":
            return b.extractRow(database, name_table, columns)
        elif mode.lower().strip() == "bPlus".lower():
            return bPlus.extractRow(database, name_table, columns)
        elif mode.lower().strip() == "dict":
            return diccionario.extractRow(database, name_table, columns)
        elif mode.lower().strip() == "hash":
            return hash.extractRow(database, name_table, columns)
        elif mode.lower().strip() == "isam":
            return isam.extractRow(database, name_table, columns)
        elif mode.lower().strip() == "json":
            return json.extractRow(database, name_table, columns)
    # return db.extractRow(database, name_table, columns) Revisar persona quien lo realizo
    return None


def update(database, name_table, register, columns):
    ModeDB, indexDB = exist_Alter(database)
    if ModeDB:
        mode = ModeDB.get_mode()
        if mode.lower().strip() == "avl":
            return avl.update(database, name_table, register, columns)
        elif mode.lower().strip() == "b":
            return b.update(database, name_table, register, columns)
        elif mode.lower().strip() == "bPlus".lower():
            return bPlus.update(database, name_table, register, columns)
        elif mode.lower().strip() == "dict":
            return diccionario.update(database, name_table, register, columns)
        elif mode.lower().strip() == "hash":
            return hash.update(database, name_table, register, columns)
        elif mode.lower().strip() == "isam":
            return isam.update(database, name_table, register, columns)
        elif mode.lower().strip() == "json":
            return json.update(database, name_table, register, columns)


def loadCSV(file, database, name_table):
    ModeDB, indexDB = exist_Alter(database)
    if ModeDB:
        mode = ModeDB.get_mode()
        if mode.lower().strip() == "avl":
            return avl.loadCSV(file, database, name_table)
        elif mode.lower().strip() == "b":
            return b.loadCSV(file, database, name_table)
        elif mode.lower().strip() == "bPlus".lower():
            return bPlus.loadCSV(file, database, name_table)
        elif mode.lower().strip() == "dict":
            return diccionario.loadCSV(file, database, name_table)
        elif mode.lower().strip() == "hash":
            return hash.loadCSV(file, database, name_table)
        elif mode.lower().strip() == "isam":
            return isam.loadCSV(file, database, name_table)
        elif mode.lower().strip() == "json":
            return json.loadCSV(file, database, name_table)


def delete(database, name_table, columns):
    ModeDB, indexDB = exist_Alter(database)
    if ModeDB:
        mode = ModeDB.get_mode()
        if mode.lower().strip() == "avl":
            return avl.delete(database, name_table, columns)
        elif mode.lower().strip() == "b":
            return b.delete(database, name_table, columns)
        elif mode.lower().strip() == "bPlus".lower():
            return bPlus.delete(database, name_table, columns)
        elif mode.lower().strip() == "dict":
            return diccionario.delete(database, name_table, columns)
        elif mode.lower().strip() == "hash":
            return hash.delete(database, name_table, columns)
        elif mode.lower().strip() == "isam":
            return isam.delete(database, name_table, columns)
        elif mode.lower().strip() == "json":
            return json.delete(database, name_table, columns)


def truncate(database, name_table):
    ModeDB, indexDB = exist_Alter(database)
    if ModeDB:
        mode = ModeDB.get_mode()
        if mode.lower().strip() == "avl":
            return avl.truncate(database, name_table)
        elif mode.lower().strip() == "b":
            return b.truncate(database, name_table)
        elif mode.lower().strip() == "bPlus".lower():
            return bPlus.truncate(database, name_table)
        elif mode.lower().strip() == "dict":
            return diccionario.truncate(database, name_table)
        elif mode.lower().strip() == "hash":
            return hash.truncate(database, name_table)
        elif mode.lower().strip() == "isam":
            return isam.truncate(database, name_table)
        elif mode.lower().strip() == "json":
            return json.truncate(database, name_table)


#  ------------------------------------------ -> Metodos del checksum <- -----------------------------------------------
def get_object_mode(database: str):
    index = 0
    for mode in mode_list:
        if mode.get_name_database() == database:
            return mode, index
        index += 1
    return None, None


def checksumDatabase(database, mode: str):
    objet_mode, index = get_object_mode(database)
    if objet_mode is None: return None
    mode_db = objet_mode.get_mode()
    # sha256 -> 1
    if mode.lower().strip() == "sha256":
        data = ""
        if mode_db.lower().strip() == "avl":
            data = avl.showTables(database)
        elif mode_db.lower().strip() == "b":
            data = list()
            for tables in b.showTables(database):
                data.append(b.extractTable(database, tables))
        elif mode_db.lower().strip() == "bPlus".lower():
            data = bPlus.showTables(database)
        elif mode_db.lower().strip() == "dict":
            data = diccionario.showTables(database)
        elif mode_db.lower().strip() == "hash":
            data = hash.showTables(database)
        elif mode_db.lower().strip() == "isam":
            data = isam.showTables(database)
        elif mode_db.lower().strip() == "json":
            data = json.showTables(database)
        return checksum_database(1, database, mode_db, data)
    # md5 -> 2
    elif mode.lower().strip() == "md5":
        data = ""
        if mode_db.lower().strip() == "avl":
            data = avl.showTables(database)
        elif mode_db.lower().strip() == "b":
            data = list()
            for tables in b.showTables(database):
                data.append(b.extractTable(database, tables))

        elif mode_db.lower().strip() == "bPlus".lower():
            data = bPlus.showTables(database)
        elif mode_db.lower().strip() == "dict":
            data = diccionario.showTables(database)
        elif mode_db.lower().strip() == "hash":
            data = hash.showTables(database)
        elif mode_db.lower().strip() == "isam":
            data = isam.showTables(database)
        elif mode_db.lower().strip() == "json":
            data = json.showTables(database)
        return checksum_database(2, database, mode_db, data)
    else:
        return None


def checksumTable(database, table: str, mode: str):
    object_mode, index = get_object_mode(database)
    if object_mode:
        mode_db = object_mode.get_mode()
        if mode.lower().strip() == "sha256":
            data = ""
            if mode_db.lower().strip() == "avl":
                if table.strip() in avl.showTables(database):
                    data = table
                else:
                    return None
            elif mode_db.lower().strip() == "b":
                if table.strip() in b.showTables(database):
                    data = b.extractTable(database, table)
                else:
                    return None
            elif mode_db.lower().strip() == "bPlus".lower():
                if table.strip() in bPlus.showTables(database):
                    data = table
                else:
                    return None
            elif mode_db.lower().strip() == "dict":
                if table.strip() in diccionario.showTables(database):
                    data = table
                else:
                    return None
            elif mode_db.lower().strip() == "hash":
                if table.strip() in hash.showTables(database):
                    data = table
                else:
                    return None
            elif mode_db.lower().strip() == "isam":
                if table.strip() in isam.showTables(database):
                    data = table
                else:
                    return None
            elif mode_db.lower().strip() == "json":
                if table.strip() in json.showTables(database):
                    data = table
                else:
                    return None
            return checksum_table(1, database, mode_db, data)
        elif mode.lower().strip() == "md5":
            data = ""
            if mode_db.lower().strip() == "avl":
                if table.strip() in avl.showTables(database):
                    data = table
                else:
                    return None
            elif mode_db.lower().strip() == "b":
                if table.strip() in b.showTables(database):
                    data = b.extractTable(database, table)
                else:
                    return None
            elif mode_db.lower().strip() == "bPlus".lower():
                if table.strip() in bPlus.showTables(database):
                    data = table
                else:
                    return None
            elif mode_db.lower().strip() == "dict":
                if table.strip() in diccionario.showTables(database):
                    data = table
                else:
                    return None
            elif mode_db.lower().strip() == "hash":
                if table.strip() in hash.showTables(database):
                    data = table
                else:
                    return None
            elif mode_db.lower().strip() == "isam":
                if table.strip() in isam.showTables(database):
                    data = table
                else:
                    return None
            elif mode_db.lower().strip() == "json":
                if table.strip() in json.showTables(database):
                    data = table
                else:
                    return None
            return checksum_table(2, database, mode_db, data)
        else:
            return None
    else:
        return None

#  ------------------------------------------ -> -------------------- <- -----------------------------------------------


# if mode.lower().strip() == "avl":
#     pass
# elif mode.lower().strip() == "b":
#     pass
# elif mode.lower().strip() == "bPlus".lower():
#     pass
# elif mode.lower().strip() == "dict":
#     pass
# elif mode.lower().strip() == "hash":
#     pass
# elif mode.lower().strip() == "isam":
#     pass
# elif mode.lower().strip() == "json":
#     pass
