from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from storageManager.jsonMode import *
from Optimizador.C3D import *
from Instrucciones.TablaSimbolos import Instruccion3D as c3d

class Truncate(Instruccion):
    def __init__(self, id, tipo, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = id

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        bd = arbol.getBaseDatos()
        if bd :
            operacion = truncate(str(bd), self.valor)
            if operacion == 0 :
                arbol.consola.append(f"Se ha eliminado los registros de la Tabla {self.valor} de la Base de Datos {str(bd)}")
            elif operacion == 1:
                error = Exception('XX000',"Semantico","Error Interno",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
            elif operacion == 2:
                error = Exception('XX000',"Semantico","La Base de datos no existe",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
            else :
                error = Exception('XX000',"Semantico","La tabla no existe",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())

    def generar3D(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        code = []
        code.append(c3d.asignacionH())
        code.append(c3d.aumentarP())
        t0 = c3d.getTemporal()
        code.append(c3d.asignacionString(t0, "TRUNCATE TABLE " + self.valor + ";"))
        code.append(c3d.asignacionTemporalStack(t0))
        code.append(c3d.LlamFuncion('call_funcion_intermedia'))
        
        return code

'''
instruccion = DropDatabase("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''