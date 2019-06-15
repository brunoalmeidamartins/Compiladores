start: goal;
goal: mainclass ( classdeclaration )*;
mainclass: class id ce public static void main pe string colce colcd id pd ce statement cd cd;
classdeclaration: class id (extends id)? ce ( vardeclaration )* ( methoddeclaration )* cd;
vardeclaration: type id pontovirgula;
methoddeclaration: public type id pe (type id ( virgula type id )* )? pd ce ( vardeclaration )* ( statement )* return expression pontovirgula cd;
type: int colce colcd
    |	boolean
    |	int
    |	id
    ;
statement: ce ( statement )* cd
         |	if pe expression pd statement else statement
         |	while pe expression pd statement
         |	systemoutprintln pe expression pd pontovirgula
         |	id igual expression pontovirgula
         |	id colce expression colcd igual expression pontovirgula
         ;
expression: expression ( ecomercial | menor | mais | menos | multiplica ) expression
          |	expression colce expression colcd
          |	expression ponto length
          |	expression ponto id pe ( expression ( virgula expression )* )? pd
          |	numero
          |	true
          |	false
          |	id
          |	this
          |	new int colce expression colcd
          |	new id pe pd
          |	negacao expression
          |	pe expression pd
          ;
//Tokens
string: 'STRING';
systemoutprintln: 'SYSTEMOUTPRINTLN';
main: 'MAIN';
static: 'STATIC';
void: 'VOID';
class: 'CLASS';
extends: 'EXTENDS';
public: 'PUBLIC';
return: 'RETURN';
boolean: 'BOOLEAN';
int: 'INT';
if: 'IF';
else: 'ELSE';
while: 'WHILE';
true: 'TRUE';
false: 'FALSE';
null: 'NULL';
new: 'NEW';
length: 'LENGTH';
this: 'THIS';
mais: 'MAIS';
menos: 'MENOS';
multiplica: 'MULTIPLICA';
divide: 'DIVIDE';
igual: 'IGUAL';
comparacao: 'COMPARACAO';
pe: 'PE';
pd: 'PD';
ce: 'CE';
cd: 'CD';
colce: 'COLCE';
colcd: 'COLCD';
menor: 'MENOR';
maior: 'MAIOR';
menorigual: 'MENORIGUAL';
maiorigual: 'MAIORIGUAL';
negacao: 'NEGACAO';
diferente: 'DIFERENTE';
ecomercial: 'ECOMERCIAL';
virgula: 'VIRGULA';
ponto: 'PONTO';
pontovirgula: 'PONTOVIRGULA';
pontoponto: 'PONTOPONTO';
numero: '\d+';
//numero: 'NUMERO';
//id: '[a-zA-Z_][a-zA-Z_0-9]*';
id: 'ID';
WS: '[ \t]+' (%ignore);
