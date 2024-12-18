from analyzer import LR1Analyzer
from tokenize import tokenize
from ply_tables.const import action_table, goto_table, rules


test_expressions = [
    # valid cases
    "x = 10",
    "x = 10",
    "a + b - c * d / e",
    "( x = 20 ) != ( y = 10 )",
    "foo ( 10 , 20 )",
    "function ( x , y ) { x + y }",
    "foo ( bar ( 10 , 20 ) , baz ( 30 ) )",
    "( x + ( y - z ) ) * ( a / b )",
    "function ( x , y ) { z = x + y }",

    # invalid cases
    "x = ",
    "x < 5 && y = 10",
    "x = > 10"
]

parser = LR1Analyzer(action_table, goto_table, rules)

for expr in test_expressions:
    print(f"Expression: {expr}")
    tokens = tokenize(expr)
    parser.parse(tokens)
    print()
