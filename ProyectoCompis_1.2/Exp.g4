grammar Exp;


prog: (stat)* EOF ;

stat
    : declaracion
    | expr
    | if_real
    ;

declaracion
    : tipo IDENTIFICADOR '=' valor ';'
    ;

if_real
    : 'if' '(' cond ')' '{' (stat)* '}'  
    ;

cond
    : expr op_rel expr  
    ;

op_rel
    : '>'
    | '<'
    | '=='
    ;


tipo
    : 'bin' 
    | 'oct' 
    | 'hex' 
    | 'dec'
    ;

valor
    : LIT_NUM
    | LIT_HEX
    ;

expr
    : expr ('*' | '/') expr    # MulDiv
    | expr ('+' | '-') expr    # SumRes
    | '(' expr ')'             # Parentesis
    | IDENTIFICADOR            # Variable
    | LIT_NUM                  # Numero
    | LIT_HEX                  # NumeroHex
    ;


TYPE_BIN : 'bin';
TYPE_OCT : 'oct';
TYPE_HEX : 'hex';
TYPE_DEC : 'dec';

// Identificadores (Variables, también pusimos que la variable inicie con minucula porque sino se confunde con hexadecimal)

IDENTIFICADOR : [a-z_][a-zA-Z0-9_]* ;

// Literales (Números)

LIT_NUM : [0-9]+ ;
LIT_HEX : [0-9A-F]+ ;

// Ignorar espacios

WS : [ \t\r\n]+ -> skip ;