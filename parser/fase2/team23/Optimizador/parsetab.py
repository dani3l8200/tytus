
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftCONCATleftMASMENOSleftPORDIVIDIDOrightUMENOSARROBA CADENA CONCAT DECIMAL DEF DIVIDIDO DOSPT ENTERO FROM GOTO ID IF IGUAL IGUALQUE IMPORT LABEL LLAVDER LLAVIZQ MAS MAYQUE MENOS MENQUE NIGUALQUE PARDER PARIZQ POR PTCOMA PUNTO WITH_GOTOinit            : instruccionesinstrucciones    : instrucciones instruccioninstrucciones    : instruccion instruccion      :  import import      : import_instr\n                        | definicion_instr\n                        | asignacion_instr\n                        | fromS\n                        | arrobas \n                        | llamada \n                        | ifI\n                        | gotoI \n                        | labels fromS     : FROM GOTO IMPORT WITH_GOTO   arrobas     : ARROBA WITH_GOTO  llamada     : ID PARIZQ PARDER   llamada     : ID PUNTO ID PARIZQ PARDER   ifI         : IF expression  DOSPT GOTO   PUNTO ID gotoI       : GOTO   PUNTO ID labels       : LABEL   PUNTO IDimport_instr     : IMPORT ID definicion_instr   : DEF ID PARIZQ PARDER DOSPTasignacion_instr   : ID IGUAL expression asignacion_instr   : ID PUNTO ID IGUAL expression expression : expression MAS expression\n                        | expression MENOS expression\n                        | expression POR expression\n                        | expression DIVIDIDO expressionexpression : expression MENQUE expression\n                        | expression MAYQUE expression\n                        | expression IGUALQUE expressionexpression : MENOS expression %prec UMENOSexpression : PARIZQ expression PARDERexpression : ENTERO\n                        | DECIMAL\n                        | CADENAexpression   : ID'
    
_lr_action_items = {'IMPORT':([0,2,3,4,5,6,7,8,9,10,11,12,13,22,23,28,30,32,35,36,37,39,41,44,53,55,59,61,62,63,64,65,66,67,68,69,70,71,73,],[14,14,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-2,-21,43,-15,-37,-34,-35,-36,-23,-16,-19,-32,-20,-14,-25,-26,-27,-28,-29,-30,-31,-33,-24,-17,-22,-18,]),'DEF':([0,2,3,4,5,6,7,8,9,10,11,12,13,22,23,30,32,35,36,37,39,41,44,53,55,59,61,62,63,64,65,66,67,68,69,70,71,73,],[16,16,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-2,-21,-15,-37,-34,-35,-36,-23,-16,-19,-32,-20,-14,-25,-26,-27,-28,-29,-30,-31,-33,-24,-17,-22,-18,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,20,22,23,24,25,29,30,32,33,34,35,36,37,38,39,41,44,46,47,48,49,50,51,52,53,55,56,59,61,62,63,64,65,66,67,68,69,70,71,72,73,],[15,15,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,23,27,32,-2,-21,32,40,44,-15,-37,32,32,-34,-35,-36,55,-23,-16,-19,32,32,32,32,32,32,32,-32,-20,32,-14,-25,-26,-27,-28,-29,-30,-31,-33,-24,-17,-22,73,-18,]),'FROM':([0,2,3,4,5,6,7,8,9,10,11,12,13,22,23,30,32,35,36,37,39,41,44,53,55,59,61,62,63,64,65,66,67,68,69,70,71,73,],[17,17,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-2,-21,-15,-37,-34,-35,-36,-23,-16,-19,-32,-20,-14,-25,-26,-27,-28,-29,-30,-31,-33,-24,-17,-22,-18,]),'ARROBA':([0,2,3,4,5,6,7,8,9,10,11,12,13,22,23,30,32,35,36,37,39,41,44,53,55,59,61,62,63,64,65,66,67,68,69,70,71,73,],[19,19,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-2,-21,-15,-37,-34,-35,-36,-23,-16,-19,-32,-20,-14,-25,-26,-27,-28,-29,-30,-31,-33,-24,-17,-22,-18,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,12,13,22,23,30,32,35,36,37,39,41,44,53,55,59,61,62,63,64,65,66,67,68,69,70,71,73,],[20,20,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-2,-21,-15,-37,-34,-35,-36,-23,-16,-19,-32,-20,-14,-25,-26,-27,-28,-29,-30,-31,-33,-24,-17,-22,-18,]),'GOTO':([0,2,3,4,5,6,7,8,9,10,11,12,13,17,22,23,30,32,35,36,37,39,41,44,45,53,55,59,61,62,63,64,65,66,67,68,69,70,71,73,],[18,18,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,28,-2,-21,-15,-37,-34,-35,-36,-23,-16,-19,60,-32,-20,-14,-25,-26,-27,-28,-29,-30,-31,-33,-24,-17,-22,-18,]),'LABEL':([0,2,3,4,5,6,7,8,9,10,11,12,13,22,23,30,32,35,36,37,39,41,44,53,55,59,61,62,63,64,65,66,67,68,69,70,71,73,],[21,21,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-2,-21,-15,-37,-34,-35,-36,-23,-16,-19,-32,-20,-14,-25,-26,-27,-28,-29,-30,-31,-33,-24,-17,-22,-18,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,22,23,30,32,35,36,37,39,41,44,53,55,59,61,62,63,64,65,66,67,68,69,70,71,73,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-2,-21,-15,-37,-34,-35,-36,-23,-16,-19,-32,-20,-14,-25,-26,-27,-28,-29,-30,-31,-33,-24,-17,-22,-18,]),'IGUAL':([15,40,],[24,56,]),'PUNTO':([15,18,21,60,],[25,29,38,72,]),'PARIZQ':([15,20,24,27,33,34,40,46,47,48,49,50,51,52,56,],[26,34,34,42,34,34,57,34,34,34,34,34,34,34,34,]),'WITH_GOTO':([19,43,],[30,59,]),'MENOS':([20,24,31,32,33,34,35,36,37,39,46,47,48,49,50,51,52,53,54,56,61,62,63,64,65,66,67,68,69,],[33,33,47,-37,33,33,-34,-35,-36,47,33,33,33,33,33,33,33,-32,47,33,-25,-26,-27,-28,47,47,47,-33,47,]),'ENTERO':([20,24,33,34,46,47,48,49,50,51,52,56,],[35,35,35,35,35,35,35,35,35,35,35,35,]),'DECIMAL':([20,24,33,34,46,47,48,49,50,51,52,56,],[36,36,36,36,36,36,36,36,36,36,36,36,]),'CADENA':([20,24,33,34,46,47,48,49,50,51,52,56,],[37,37,37,37,37,37,37,37,37,37,37,37,]),'PARDER':([26,32,35,36,37,42,53,54,57,61,62,63,64,65,66,67,68,],[41,-37,-34,-35,-36,58,-32,68,70,-25,-26,-27,-28,-29,-30,-31,-33,]),'DOSPT':([31,32,35,36,37,53,58,61,62,63,64,65,66,67,68,],[45,-37,-34,-35,-36,-32,71,-25,-26,-27,-28,-29,-30,-31,-33,]),'MAS':([31,32,35,36,37,39,53,54,61,62,63,64,65,66,67,68,69,],[46,-37,-34,-35,-36,46,-32,46,-25,-26,-27,-28,46,46,46,-33,46,]),'POR':([31,32,35,36,37,39,53,54,61,62,63,64,65,66,67,68,69,],[48,-37,-34,-35,-36,48,-32,48,48,48,-27,-28,48,48,48,-33,48,]),'DIVIDIDO':([31,32,35,36,37,39,53,54,61,62,63,64,65,66,67,68,69,],[49,-37,-34,-35,-36,49,-32,49,49,49,-27,-28,49,49,49,-33,49,]),'MENQUE':([31,32,35,36,37,39,53,54,61,62,63,64,65,66,67,68,69,],[50,-37,-34,-35,-36,50,-32,50,-25,-26,-27,-28,50,50,50,-33,50,]),'MAYQUE':([31,32,35,36,37,39,53,54,61,62,63,64,65,66,67,68,69,],[51,-37,-34,-35,-36,51,-32,51,-25,-26,-27,-28,51,51,51,-33,51,]),'IGUALQUE':([31,32,35,36,37,39,53,54,61,62,63,64,65,66,67,68,69,],[52,-37,-34,-35,-36,52,-32,52,-25,-26,-27,-28,52,52,52,-33,52,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,],[2,]),'instruccion':([0,2,],[3,22,]),'import':([0,2,],[4,4,]),'import_instr':([0,2,],[5,5,]),'definicion_instr':([0,2,],[6,6,]),'asignacion_instr':([0,2,],[7,7,]),'fromS':([0,2,],[8,8,]),'arrobas':([0,2,],[9,9,]),'llamada':([0,2,],[10,10,]),'ifI':([0,2,],[11,11,]),'gotoI':([0,2,],[12,12,]),'labels':([0,2,],[13,13,]),'expression':([20,24,33,34,46,47,48,49,50,51,52,56,],[31,39,53,54,61,62,63,64,65,66,67,69,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','gramatica.py',135),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','gramatica.py',139),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',145),
  ('instruccion -> import','instruccion',1,'p_fromfoto','gramatica.py',149),
  ('import -> import_instr','import',1,'p_instruccion','gramatica.py',152),
  ('import -> definicion_instr','import',1,'p_instruccion','gramatica.py',153),
  ('import -> asignacion_instr','import',1,'p_instruccion','gramatica.py',154),
  ('import -> fromS','import',1,'p_instruccion','gramatica.py',155),
  ('import -> arrobas','import',1,'p_instruccion','gramatica.py',156),
  ('import -> llamada','import',1,'p_instruccion','gramatica.py',157),
  ('import -> ifI','import',1,'p_instruccion','gramatica.py',158),
  ('import -> gotoI','import',1,'p_instruccion','gramatica.py',159),
  ('import -> labels','import',1,'p_instruccion','gramatica.py',160),
  ('fromS -> FROM GOTO IMPORT WITH_GOTO','fromS',4,'p_from','gramatica.py',176),
  ('arrobas -> ARROBA WITH_GOTO','arrobas',2,'p_arroba','gramatica.py',181),
  ('llamada -> ID PARIZQ PARDER','llamada',3,'p_funciones','gramatica.py',186),
  ('llamada -> ID PUNTO ID PARIZQ PARDER','llamada',5,'p_funciones_aux','gramatica.py',194),
  ('ifI -> IF expression DOSPT GOTO PUNTO ID','ifI',6,'p_ifS','gramatica.py',199),
  ('gotoI -> GOTO PUNTO ID','gotoI',3,'p_gotoS','gramatica.py',204),
  ('labels -> LABEL PUNTO ID','labels',3,'p_labelS','gramatica.py',209),
  ('import_instr -> IMPORT ID','import_instr',2,'p_instruccion_import','gramatica.py',215),
  ('definicion_instr -> DEF ID PARIZQ PARDER DOSPT','definicion_instr',5,'p_instruccion_definicion','gramatica.py',221),
  ('asignacion_instr -> ID IGUAL expression','asignacion_instr',3,'p_asignacion_instr','gramatica.py',227),
  ('asignacion_instr -> ID PUNTO ID IGUAL expression','asignacion_instr',5,'p_asignacion_instr_aux','gramatica.py',235),
  ('expression -> expression MAS expression','expression',3,'p_expresion_binaria','gramatica.py',240),
  ('expression -> expression MENOS expression','expression',3,'p_expresion_binaria','gramatica.py',241),
  ('expression -> expression POR expression','expression',3,'p_expresion_binaria','gramatica.py',242),
  ('expression -> expression DIVIDIDO expression','expression',3,'p_expresion_binaria','gramatica.py',243),
  ('expression -> expression MENQUE expression','expression',3,'p_expresion_binaria_aux','gramatica.py',262),
  ('expression -> expression MAYQUE expression','expression',3,'p_expresion_binaria_aux','gramatica.py',263),
  ('expression -> expression IGUALQUE expression','expression',3,'p_expresion_binaria_aux','gramatica.py',264),
  ('expression -> MENOS expression','expression',2,'p_expresion_unaria','gramatica.py',279),
  ('expression -> PARIZQ expression PARDER','expression',3,'p_expresion_agrupacion','gramatica.py',283),
  ('expression -> ENTERO','expression',1,'p_expresion_number','gramatica.py',288),
  ('expression -> DECIMAL','expression',1,'p_expresion_number','gramatica.py',289),
  ('expression -> CADENA','expression',1,'p_expresion_number','gramatica.py',290),
  ('expression -> ID','expression',1,'p_expresion_id','gramatica.py',295),
]