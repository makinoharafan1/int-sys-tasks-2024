_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN COMMA DIV EQ FALSE GE GT ID LBRACE LE LPAREN LT MINUS MUL NEQ NOT NUMBER OR PLUS RBRACE RPAREN TRUEprogram : expressionexpression : assignment\n                  | logical_exprassignment : ID ASSIGN expressionlogical_expr : logical_expr OR logical_term\n                    | logical_termlogical_term : logical_term AND logical_factor\n                    | logical_factorlogical_factor : NOT logical_factor\n                      | relational_exprrelational_expr : relational_expr EQ additive_expr\n                       | relational_expr NEQ additive_expr\n                       | relational_expr LT additive_expr\n                       | relational_expr LE additive_expr\n                       | relational_expr GT additive_expr\n                       | relational_expr GE additive_expr\n                       | additive_expradditive_expr : additive_expr PLUS multiplicative_expr\n                     | additive_expr MINUS multiplicative_expr\n                     | multiplicative_exprmultiplicative_expr : multiplicative_expr MUL unary_expr\n                            | multiplicative_expr DIV unary_expr\n                            | unary_exprunary_expr : MINUS unary_expr\n                  | primary_exprprimary_expr : LPAREN expression RPAREN\n                    | ID\n                    | NUMBER\n                    | TRUE\n                    | FALSE\n                    | function_definition\n                    | function_callfunction_definition : ID LPAREN argument_list RPAREN LBRACE expression RBRACEfunction_call : ID LPAREN argument_list RPARENargument_list : argument_list COMMA expression\n                     | expression'
    
_lr_action_items = {'ID':([0,8,12,15,21,22,23,24,27,28,29,30,31,32,33,34,35,36,56,57,],[5,26,26,5,26,5,5,26,26,26,26,26,26,26,26,26,26,26,5,5,]),'NOT':([0,8,15,21,22,23,24,56,57,],[8,8,8,8,8,8,8,8,8,]),'MINUS':([0,5,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,27,28,29,30,31,32,33,34,35,36,37,44,45,46,47,48,49,50,51,52,53,54,55,56,57,60,],[12,-27,12,34,-20,12,-23,-25,12,-28,-29,-30,-31,-32,12,12,12,12,-27,12,12,12,12,12,12,12,12,12,12,-24,34,34,34,34,34,34,-18,-19,-21,-22,-26,-34,12,12,-33,]),'LPAREN':([0,5,8,12,15,21,22,23,24,26,27,28,29,30,31,32,33,34,35,36,56,57,],[15,23,15,15,15,15,15,15,15,23,15,15,15,15,15,15,15,15,15,15,15,15,]),'NUMBER':([0,8,12,15,21,22,23,24,27,28,29,30,31,32,33,34,35,36,56,57,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'TRUE':([0,8,12,15,21,22,23,24,27,28,29,30,31,32,33,34,35,36,56,57,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'FALSE':([0,8,12,15,21,22,23,24,27,28,29,30,31,32,33,34,35,36,56,57,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'$end':([1,2,3,4,5,6,7,9,10,11,13,14,16,17,18,19,20,25,26,37,39,40,43,44,45,46,47,48,49,50,51,52,53,54,55,60,],[0,-1,-2,-3,-27,-6,-8,-10,-17,-20,-23,-25,-28,-29,-30,-31,-32,-9,-27,-24,-5,-4,-7,-11,-12,-13,-14,-15,-16,-18,-19,-21,-22,-26,-34,-33,]),'RPAREN':([3,4,5,6,7,9,10,11,13,14,16,17,18,19,20,25,26,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,58,60,],[-2,-3,-27,-6,-8,-10,-17,-20,-23,-25,-28,-29,-30,-31,-32,-9,-27,-24,54,-5,-4,55,-36,-7,-11,-12,-13,-14,-15,-16,-18,-19,-21,-22,-26,-34,-35,-33,]),'COMMA':([3,4,5,6,7,9,10,11,13,14,16,17,18,19,20,25,26,37,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,58,60,],[-2,-3,-27,-6,-8,-10,-17,-20,-23,-25,-28,-29,-30,-31,-32,-9,-27,-24,-5,-4,56,-36,-7,-11,-12,-13,-14,-15,-16,-18,-19,-21,-22,-26,-34,-35,-33,]),'RBRACE':([3,4,5,6,7,9,10,11,13,14,16,17,18,19,20,25,26,37,39,40,43,44,45,46,47,48,49,50,51,52,53,54,55,59,60,],[-2,-3,-27,-6,-8,-10,-17,-20,-23,-25,-28,-29,-30,-31,-32,-9,-27,-24,-5,-4,-7,-11,-12,-13,-14,-15,-16,-18,-19,-21,-22,-26,-34,60,-33,]),'OR':([4,5,6,7,9,10,11,13,14,16,17,18,19,20,25,26,37,39,43,44,45,46,47,48,49,50,51,52,53,54,55,60,],[21,-27,-6,-8,-10,-17,-20,-23,-25,-28,-29,-30,-31,-32,-9,-27,-24,-5,-7,-11,-12,-13,-14,-15,-16,-18,-19,-21,-22,-26,-34,-33,]),'ASSIGN':([5,],[22,]),'MUL':([5,11,13,14,16,17,18,19,20,26,37,50,51,52,53,54,55,60,],[-27,35,-23,-25,-28,-29,-30,-31,-32,-27,-24,35,35,-21,-22,-26,-34,-33,]),'DIV':([5,11,13,14,16,17,18,19,20,26,37,50,51,52,53,54,55,60,],[-27,36,-23,-25,-28,-29,-30,-31,-32,-27,-24,36,36,-21,-22,-26,-34,-33,]),'PLUS':([5,10,11,13,14,16,17,18,19,20,26,37,44,45,46,47,48,49,50,51,52,53,54,55,60,],[-27,33,-20,-23,-25,-28,-29,-30,-31,-32,-27,-24,33,33,33,33,33,33,-18,-19,-21,-22,-26,-34,-33,]),'EQ':([5,9,10,11,13,14,16,17,18,19,20,26,37,44,45,46,47,48,49,50,51,52,53,54,55,60,],[-27,27,-17,-20,-23,-25,-28,-29,-30,-31,-32,-27,-24,-11,-12,-13,-14,-15,-16,-18,-19,-21,-22,-26,-34,-33,]),'NEQ':([5,9,10,11,13,14,16,17,18,19,20,26,37,44,45,46,47,48,49,50,51,52,53,54,55,60,],[-27,28,-17,-20,-23,-25,-28,-29,-30,-31,-32,-27,-24,-11,-12,-13,-14,-15,-16,-18,-19,-21,-22,-26,-34,-33,]),'LT':([5,9,10,11,13,14,16,17,18,19,20,26,37,44,45,46,47,48,49,50,51,52,53,54,55,60,],[-27,29,-17,-20,-23,-25,-28,-29,-30,-31,-32,-27,-24,-11,-12,-13,-14,-15,-16,-18,-19,-21,-22,-26,-34,-33,]),'LE':([5,9,10,11,13,14,16,17,18,19,20,26,37,44,45,46,47,48,49,50,51,52,53,54,55,60,],[-27,30,-17,-20,-23,-25,-28,-29,-30,-31,-32,-27,-24,-11,-12,-13,-14,-15,-16,-18,-19,-21,-22,-26,-34,-33,]),'GT':([5,9,10,11,13,14,16,17,18,19,20,26,37,44,45,46,47,48,49,50,51,52,53,54,55,60,],[-27,31,-17,-20,-23,-25,-28,-29,-30,-31,-32,-27,-24,-11,-12,-13,-14,-15,-16,-18,-19,-21,-22,-26,-34,-33,]),'GE':([5,9,10,11,13,14,16,17,18,19,20,26,37,44,45,46,47,48,49,50,51,52,53,54,55,60,],[-27,32,-17,-20,-23,-25,-28,-29,-30,-31,-32,-27,-24,-11,-12,-13,-14,-15,-16,-18,-19,-21,-22,-26,-34,-33,]),'AND':([5,6,7,9,10,11,13,14,16,17,18,19,20,25,26,37,39,43,44,45,46,47,48,49,50,51,52,53,54,55,60,],[-27,24,-8,-10,-17,-20,-23,-25,-28,-29,-30,-31,-32,-9,-27,-24,24,-7,-11,-12,-13,-14,-15,-16,-18,-19,-21,-22,-26,-34,-33,]),'LBRACE':([55,],[57,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'expression':([0,15,22,23,56,57,],[2,38,40,42,58,59,]),'assignment':([0,15,22,23,56,57,],[3,3,3,3,3,3,]),'logical_expr':([0,15,22,23,56,57,],[4,4,4,4,4,4,]),'logical_term':([0,15,21,22,23,56,57,],[6,6,39,6,6,6,6,]),'logical_factor':([0,8,15,21,22,23,24,56,57,],[7,25,7,7,7,7,43,7,7,]),'relational_expr':([0,8,15,21,22,23,24,56,57,],[9,9,9,9,9,9,9,9,9,]),'additive_expr':([0,8,15,21,22,23,24,27,28,29,30,31,32,56,57,],[10,10,10,10,10,10,10,44,45,46,47,48,49,10,10,]),'multiplicative_expr':([0,8,15,21,22,23,24,27,28,29,30,31,32,33,34,56,57,],[11,11,11,11,11,11,11,11,11,11,11,11,11,50,51,11,11,]),'unary_expr':([0,8,12,15,21,22,23,24,27,28,29,30,31,32,33,34,35,36,56,57,],[13,13,37,13,13,13,13,13,13,13,13,13,13,13,13,13,52,53,13,13,]),'primary_expr':([0,8,12,15,21,22,23,24,27,28,29,30,31,32,33,34,35,36,56,57,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'function_definition':([0,8,12,15,21,22,23,24,27,28,29,30,31,32,33,34,35,36,56,57,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'function_call':([0,8,12,15,21,22,23,24,27,28,29,30,31,32,33,34,35,36,56,57,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'argument_list':([23,],[41,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S -> program","S",1,None,None,None),
  ('program -> expression','program',1,'p_program','ply_setup.py',67),
  ('expression -> assignment','expression',1,'p_expression','ply_setup.py',70),
  ('expression -> logical_expr','expression',1,'p_expression','ply_setup.py',71),
  ('assignment -> ID ASSIGN expression','assignment',3,'p_assignment','ply_setup.py',74),
  ('logical_expr -> logical_expr OR logical_term','logical_expr',3,'p_logical_expr','ply_setup.py',77),
  ('logical_expr -> logical_term','logical_expr',1,'p_logical_expr','ply_setup.py',78),
  ('logical_term -> logical_term AND logical_factor','logical_term',3,'p_logical_term','ply_setup.py',81),
  ('logical_term -> logical_factor','logical_term',1,'p_logical_term','ply_setup.py',82),
  ('logical_factor -> NOT logical_factor','logical_factor',2,'p_logical_factor','ply_setup.py',85),
  ('logical_factor -> relational_expr','logical_factor',1,'p_logical_factor','ply_setup.py',86),
  ('relational_expr -> relational_expr EQ additive_expr','relational_expr',3,'p_relational_expr','ply_setup.py',89),
  ('relational_expr -> relational_expr NEQ additive_expr','relational_expr',3,'p_relational_expr','ply_setup.py',90),
  ('relational_expr -> relational_expr LT additive_expr','relational_expr',3,'p_relational_expr','ply_setup.py',91),
  ('relational_expr -> relational_expr LE additive_expr','relational_expr',3,'p_relational_expr','ply_setup.py',92),
  ('relational_expr -> relational_expr GT additive_expr','relational_expr',3,'p_relational_expr','ply_setup.py',93),
  ('relational_expr -> relational_expr GE additive_expr','relational_expr',3,'p_relational_expr','ply_setup.py',94),
  ('relational_expr -> additive_expr','relational_expr',1,'p_relational_expr','ply_setup.py',95),
  ('additive_expr -> additive_expr PLUS multiplicative_expr','additive_expr',3,'p_additive_expr','ply_setup.py',98),
  ('additive_expr -> additive_expr MINUS multiplicative_expr','additive_expr',3,'p_additive_expr','ply_setup.py',99),
  ('additive_expr -> multiplicative_expr','additive_expr',1,'p_additive_expr','ply_setup.py',100),
  ('multiplicative_expr -> multiplicative_expr MUL unary_expr','multiplicative_expr',3,'p_multiplicative_expr','ply_setup.py',103),
  ('multiplicative_expr -> multiplicative_expr DIV unary_expr','multiplicative_expr',3,'p_multiplicative_expr','ply_setup.py',104),
  ('multiplicative_expr -> unary_expr','multiplicative_expr',1,'p_multiplicative_expr','ply_setup.py',105),
  ('unary_expr -> MINUS unary_expr','unary_expr',2,'p_unary_expr','ply_setup.py',108),
  ('unary_expr -> primary_expr','unary_expr',1,'p_unary_expr','ply_setup.py',109),
  ('primary_expr -> LPAREN expression RPAREN','primary_expr',3,'p_primary_expr','ply_setup.py',112),
  ('primary_expr -> ID','primary_expr',1,'p_primary_expr','ply_setup.py',113),
  ('primary_expr -> NUMBER','primary_expr',1,'p_primary_expr','ply_setup.py',114),
  ('primary_expr -> TRUE','primary_expr',1,'p_primary_expr','ply_setup.py',115),
  ('primary_expr -> FALSE','primary_expr',1,'p_primary_expr','ply_setup.py',116),
  ('primary_expr -> function_definition','primary_expr',1,'p_primary_expr','ply_setup.py',117),
  ('primary_expr -> function_call','primary_expr',1,'p_primary_expr','ply_setup.py',118),
  ('function_definition -> ID LPAREN argument_list RPAREN LBRACE expression RBRACE','function_definition',7,'p_function_definition','ply_setup.py',121),
  ('function_call -> ID LPAREN argument_list RPAREN','function_call',4,'p_function_call','ply_setup.py',124),
  ('argument_list -> argument_list COMMA expression','argument_list',3,'p_argument_list','ply_setup.py',127),
  ('argument_list -> expression','argument_list',1,'p_argument_list','ply_setup.py',128),
]
