lexer grammar SpaceBattleLexer;

PLAYER_SHIP: 'PlayerShip';
NPC_SHIP: 'NPCShip';
SHIELDS: 'shields';
ENERGY: 'energy';
FUEL: 'fuel';
WEAPONS: 'weapons';
CURRENCY: 'currency';
ROLE: 'role';
BEHAVIOR: 'behavior';
DAMAGE: 'damage';
PRICE: 'price';
COLLISION: 'collision';

AND: 'and';
OR: 'or';
FROM: 'from';
BY: 'by';
TO: 'to';
FOR: 'for';
WITH: 'with';

CAN: 'can';
INCLUDES: 'includes';
MUST: 'must';
CHECK: 'check';
SPEND: 'spend';
WHEN: 'when';
PURCHASE: 'purchase';
AT: 'at';

GAME: 'game';
END_GAME: 'end_game';

LBRACE: '{';
RBRACE: '}';
LBRACKET: '[';
RBRACKET: ']';
COMMA: ',';
COLON: ':';
SEMICOLON: ';';


WEAPON
    : 'Laser_Cannon'
    | 'Plasma_Torpedo'
    | 'Quantum_Disruptor'
    ;

CAPABILITY
    : 'Move'
    | 'Rotate_Left' 
    | 'Rotate_Right'
    | 'Shoot'
    | 'Warp_Jump'
    | 'Stealth_Mode'
    | 'Summon_Drones'
    | 'Trade'
    ;

NPC_ROLE
    : 'Trader'
    | 'Fighter'
    | 'Guard'
    ;

NPC_BEHAVIOR
    : 'Aggressive'
    | 'Defensive'
    | 'Neutral'
    ;


COMPARE: '<' | '<=' | '==' | '>=' | '>' | '!=';
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+ ('.' [0-9]+)?;
WS: [ \t\n\r\f]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;
