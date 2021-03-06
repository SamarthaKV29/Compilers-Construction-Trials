
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'LPAREN RPAREN INTEGER NEGATE PLUS EQUALS VAR BOOL WHILE PROGRAM LET PRINT SCAN ELSE TYPE IFEXP : LPAREN PROGRAM EXP MORE RPARENEXP : LPAREN EXP RPARENMORE : EXP MORE\n            | EXP : NEGATE EXPEXP : PLUS EXP EXPEXP : INTEGEREXP : BOOLEXP : SCANEXP : VAR EXPEXP : PRINT VAREXP : PRINT INTEGER'
    
_lr_action_items = {'RPAREN':([2,6,9,10,11,12,15,16,17,18,19,20,21,22,23,],[-9,-8,-7,-11,-12,-10,19,-5,-6,-4,-2,-4,23,-3,-1,]),'SCAN':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,23,],[2,-9,2,2,-8,2,2,-7,-11,-12,-10,2,2,-5,-6,2,-2,2,-1,]),'NEGATE':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,23,],[8,-9,8,8,-8,8,8,-7,-11,-12,-10,8,8,-5,-6,8,-2,8,-1,]),'VAR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,23,],[4,-9,10,4,4,-8,4,4,-7,-11,-12,-10,4,4,-5,-6,4,-2,4,-1,]),'PROGRAM':([7,],[14,]),'BOOL':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,23,],[6,-9,6,6,-8,6,6,-7,-11,-12,-10,6,6,-5,-6,6,-2,6,-1,]),'LPAREN':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,23,],[7,-9,7,7,-8,7,7,-7,-11,-12,-10,7,7,-5,-6,7,-2,7,-1,]),'INTEGER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,23,],[9,-9,11,9,9,-8,9,9,-7,-11,-12,-10,9,9,-5,-6,9,-2,9,-1,]),'PRINT':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,23,],[3,-9,3,3,-8,3,3,-7,-11,-12,-10,3,3,-5,-6,3,-2,3,-1,]),'PLUS':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,23,],[5,-9,5,5,-8,5,5,-7,-11,-12,-10,5,5,-5,-6,5,-2,5,-1,]),'$end':([1,2,6,9,10,11,12,16,17,19,23,],[0,-9,-8,-7,-11,-12,-10,-5,-6,-2,-1,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'EXP':([0,4,5,7,8,13,14,18,20,],[1,12,13,15,16,17,18,20,20,]),'MORE':([18,20,],[21,22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> EXP","S'",1,None,None,None),
  ('EXP -> LPAREN PROGRAM EXP MORE RPAREN','EXP',5,'p_program','c0parser.py',10),
  ('EXP -> LPAREN EXP RPAREN','EXP',3,'p_brackets','c0parser.py',18),
  ('MORE -> EXP MORE','MORE',2,'p_more','c0parser.py',22),
  ('MORE -> <empty>','MORE',0,'p_more','c0parser.py',23),
  ('EXP -> NEGATE EXP','EXP',2,'p_neg','c0parser.py',29),
  ('EXP -> PLUS EXP EXP','EXP',3,'p_add','c0parser.py',43),
  ('EXP -> INTEGER','EXP',1,'p_int_exp','c0parser.py',59),
  ('EXP -> BOOL','EXP',1,'p_bool_exp','c0parser.py',63),
  ('EXP -> SCAN','EXP',1,'p_scan','c0parser.py',67),
  ('EXP -> VAR EXP','EXP',2,'p_var','c0parser.py',74),
  ('EXP -> PRINT VAR','EXP',2,'p_print','c0parser.py',80),
  ('EXP -> PRINT INTEGER','EXP',2,'p_prr','c0parser.py',87),
]
