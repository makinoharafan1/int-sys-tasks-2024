parser grammar SpaceBattleParser;
options { tokenVocab=SpaceBattleLexer; }

program
    : (statement)* EOF
    ;

statement
    : shipDefinitions
    | actionRules
    | damageRules
    | gameRules
    | SEMICOLON
    ;

shipDefinitions
    : playerShipDefinition
    | npcShipDefinition
    ;

playerShipDefinition
    : PLAYER_SHIP IDENTIFIER LBRACE 
        shipAttribute*
        playerCurrency?
        shipCapabilities
      RBRACE
    ;

npcShipDefinition
    : NPC_SHIP IDENTIFIER LBRACE 
        shipAttribute*
        npcRole?
        npcBehavior?
        shipCapabilities
      RBRACE
    ;

shipAttribute
    : SHIELDS NUMBER
    | ENERGY NUMBER
    | FUEL NUMBER
    | WEAPONS LBRACKET WEAPON (COMMA WEAPON)* RBRACKET
    ;
    
playerCurrency: CURRENCY NUMBER;
shipCapabilities: CAN CAPABILITY (COMMA CAPABILITY)*;
npcRole: ROLE NPC_ROLE;
npcBehavior: BEHAVIOR NPC_BEHAVIOR;


actionRules
    : CAPABILITY INCLUDES commandSequence
    | CAPABILITY MUST CHECK COLLISION
    | CAPABILITY MUST SPEND resource (COMMA resource)*
    | CAPABILITY WITH (CAPABILITY | WEAPON) MUST SPEND resource (COMMA resource)*
    | IDENTIFIER CAN PURCHASE (SHIELDS | FUEL) AT PRICE NUMBER FROM IDENTIFIER
    ;

damageRules
    : DAMAGE FROM WEAPON BY NUMBER (TO SHIELDS | TO ENERGY)
    ;

gameRules
    : GAME MUST CHECK commandSequence
    | END_GAME WHEN conditionSequence
    ;


commandSequence
    : IDENTIFIER (COMMA IDENTIFIER)*
    ;

resource
    : (ENERGY | FUEL | CURRENCY) (NUMBER)?
    ;

conditionSequence
    : conditionExpression ( (OR | AND) conditionExpression )*
    ;

conditionExpression
    : IDENTIFIER (SHIELDS | ENERGY | FUEL | CURRENCY) COMPARE NUMBER
    ;
    