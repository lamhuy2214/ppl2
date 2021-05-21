grammar CSEL;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options {
	language = Python3;
}

//******* Parser ****************************** */
program: (many_var_declare) (many_const_declare) (
		many_func_declare
	) EOF;

many_var_declare:
	one_var_declare many_var_declare
	| one_var_declare
	|;
one_var_declare: LET id_list SEMI;
many_const_declare:
	one_const_declare many_const_declare
	| one_const_declare
	|;
one_const_declare: CONSTANT id_list_const SEMI;
id_list: (id_list_element) (COMMA id_list)?;

id_list_element: (ID | ID composit) (COLON Typ)? (
		ASSIGN (array_literal | literal)
	)?;
id_list_const: (id_list_element_const) (COMMA id_list_const)?;

id_list_element_const: (ID_const | ID_const composit) (COLON Typ)? (
		ASSIGN (array_literal | literal)
	)?;
composit: (LSB NUM_LITERAL* (COMMA NUM_LITERAL)* RSB)+;
array_literal:
	LSB (
		(array_literal_element) (COMMA (array_literal_element))*
	)? RSB;

array_literal_element: array_literal | literal;

//LITERAL ____________________________________________________
literal: NUM_LITERAL | BOOLEAN_LITERAL | STRING_LITERAL | json;

/*******************************************************************************func_declare */
/*Paser*/
assign_stm:
	(array_cell | json_cell) ASSIGN exp SEMI
	| ID ASSIGN exp SEMI;

parameter_name: (param_list_element) (COMMA parameter_name)?;

param_list_element: (ID | ID composit);

many_func_declare:
	one_func_declare many_func_declare
	| one_func_declare
	|;
one_func_declare:
	// FUNCTION COLON ID (PARAMETER COLON parameter_name)? ( BODY COLON ) (many_var_declare
	// many_stm) (ENDBODY DOT);
	FUNCTION ID LP (parameter_name)? RP LB (
		many_var_declare many_const_declare many_stm
	) RB;
many_stm: stm many_stm | stm |;

stm:
	assign_stm
	| call_stm
	| break_stm
	| continue_stm
	| if_stm
	| forof_stm
	| while_stm
	| forin_stm
	| return_stm;
call_stm: function_call SEMI;
function_call:
	CALL LP ID COMMA LSB RSB RP
	| CALL LP ID COMMA LSB (exp) (COMMA exp)* (
		COMMA function_call
	)* RSB RP;
return_stm: RETURN exp? SEMI;
if_stm: if_then many_elseif* else_part?;
if_then: IF LP exp RP LB (many_var_declare many_stm) RB;
many_elseif: ELSEIF LP exp RP LB (many_var_declare many_stm) RB;
else_part: ELSE LB (many_var_declare many_stm) RB;

forin_stm:
	FOR ID IN array_literal LB (many_var_declare many_stm) RB
	| FOR ID IN ID LB (many_var_declare many_stm) RB;
forof_stm: FOR ID OF ID LB (many_var_declare many_stm) RB;
while_stm: WHILE LP exp RP LB (many_var_declare many_stm) RB;
break_stm: BREAK SEMI;
continue_stm: CONTINUE SEMI;
LOGICAL_OP: CONJUNCTION | DISJUNCTION;
MULTIPLYING: MUL | DIV | MOD;
RL_OP:
	EQUAL
	| NOTEQUAL
	| LESSTHAN
	| GREATERTHAN
	| LESSTHAN_EQUAL
	| GREATERTHAN_EQUAL;

exp: exp1 SADD exp1 | exp1 SEQ exp1 | exp1;

exp1: exp2 RL_OP exp2 | exp2;
exp2: exp2 LOGICAL_OP exp3 | exp3;
exp3: exp3 ADD exp4 | exp3 SUB exp4 | exp4;
exp4: exp4 MULTIPLYING exp5 | exp5;
exp5: NEGATION exp5 | exp6;
exp6: SUB exp6 | exp7;
exp7:
	array_literal //1
	| json_cell
	| literal //1
	| ID //1
	| function_call //1
	| array_cell //1
	| ID_const
	| LP exp RP;
array_cell: (ID | function_call | LP exp RP) index_exp;
index_exp: (LSB exp (COMMA exp)* RSB)
	| ( LSB exp (COMMA exp)* RSB index_exp);
json_cell: (ID) json_key;
json_key: LB '"' exp '"' RB | LB '"' exp '"' RB json_key;
/* Bool */
json: LB jsonlist RB;
jsonlist: (ID COLON literal | array_literal) (COMMA jsonlist)?;
BOOLEAN_LITERAL: TRUE | FALSE;
//******** Lexer ******************************* Fragment:
WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
/* Comment */
COMMENT: '##' ((~'#') | ('*' ~'#'))* '##' -> skip;
UNTERMINATED_COMMENT:
	'##' .*? {
        raise UnterminatedComment()
        };
fragment UNDERSCORES: '_';
fragment UPPER: [A-Z];
fragment LOWER: [a-z];
fragment DIGIT: [0-9];
fragment DIGIT_EX0: [1-9];
Typ: Number | String | Boolean | JSON;
ID: LOWER (UNDERSCORES | UPPER | LOWER | DIGIT)*;
ID_const: '$' LOWER (UNDERSCORES | UPPER | LOWER | DIGIT)*;
//Operator:
SUB: '-';

ADD: '+';

MUL: '*';

DIV: '/';

MOD: '%';

SADD: '+.';

SEQ: '==.';
TRUE: 'True';
FALSE: 'False';
CALL: 'Call';
LET: 'Let';
CONTINUE: 'Continue';
CONSTANT: 'Constant';
ELSE: 'Else';
ELSEIF: 'Elif';

Number: 'Number';
String: 'String';
Boolean: 'Boolean';
JSON: 'JSON';
FOR: 'For';
BREAK: 'Break';
FUNCTION: 'Function';
IF: 'If';
RETURN: 'Return';

WHILE: 'While';

IN: 'In';
DOT: '.';
OF: 'Of';
//Boolean Operator:
NEGATION: '!';
CONJUNCTION: '&&';
DISJUNCTION: '||';
//Relational operator:
ASSIGN: '=';
EQUAL: '==';
NOTEQUAL: '!=';
LESSTHAN: '<';
GREATERTHAN: '>';
LESSTHAN_EQUAL: '<=';
GREATERTHAN_EQUAL: '>=';
//Separators: 
SEMI: ';';
COLON: ':';
COMMA: ',';
LB: '{';
RB: '}';
LP: '(';
RP: ')';
LSB: '[';
RSB: ']';
//literals:
// *******************************************************************************************
// **Integer** **Float**/
NUM_LITERAL:
	INT_PART (
		DECIMAL_PART? EXPONENT_PART
		| DECIMAL_PART EXPONENT_PART?
	)?;
fragment EXPONENT_PART: [eE] [+-]? DIGIT+;
fragment DECIMAL_PART: DOT DIGIT*;
fragment INT_PART: (DIGIT)+;

STRING_LITERAL:
	'"' (('\'"') | '\\' ([bfrnt\\']) | ~(["\n\\] | '\''))* '"' {

                self.text = self.text[1:-1]
        };

ILLEGAL_ESCAPE:
	'"' (('\'"') | '\\' ([bfrnt\\']) | ~(["\n\\] | '\''))* (
		'\\' ~[bfrnt'\\]
		| '\'' ~'"'
	) {
                        raise IllegalEscape(self.text[1:])
                };
UNCLOSE_STRING:
	'"' (('\'"') | '\\' ([bfrnt\\']) | ~(["\n\\] | '\''))* {
                        raise UncloseString(self.text[1:])
                };
ERROR_CHAR:
	.{
        raise ErrorToken(self.text)
        };