grammar MiniJava;

goal    : main_class=mainClass ( main_class_decl=classDeclaration )* EOF
        ;

mainClass   : 'class' Identifier '{' 'public' 'static' 'void' 'main' '(' 'String' '[' ']' Identifier ')' '{' main_class_stmt=statement '}' '}'
            #mainclass
            ;

classDeclaration    : 'class' Identifier ('extends' Identifier)? '{' (class_Decl_var=varDeclaration)* (class_meth_decl=methodDeclaration)* '}'
                    #dec_class
                    ;

varDeclaration  : mtype Identifier ';'
                #dec_var
                ;

methodDeclaration	:	'public' meth_mtype=mtype Identifier '(' ( tipoP1=mtype nomeP1=Identifier ( ',' listaTipoPs+=mtype listaNomePs+=Identifier )* )? ')' '{' ( met_var_decl=varDeclaration )* ( meth_stmt_decl=statement )* 'return' exp_retorno=expression ';' '}'
					#dec_method
					;

//methodDeclaration   : 'public' mtype Identifier '(' parameters ')' '{' (varDeclaration)* (statement)* 'return' expression ';' '}'
//                    #dec_method
//                    ;

//parameters  : (parameterDeclaration (',' parameterDeclaration)*)?
//            ;

//parameterDeclaration    : mtype Identifier
//                        ;

mtype   : 'int' '[' ']'
        | 'boolean'
        | 'int'
        | Identifier
        ;

statement   : '{' (stmt=statement)* '}'
                #state_lrparents
            | 'if' '(' expIf=expression ')' statementIF1=statement 'else' statementIF2=statement
                #state_if
            | 'while' '(' expWhile=expression ')' statementWhile=statement
                #state_while
            | 'System.out.println' '(' expPrint=expression ')' ';'
                #state_print
            | Identifier '=' expIdt=expression ';'
                #state_assign
            | Identifier '[' expArrayAssign1=expression ']' '=' expArrayAssign2=expression ';'
                #state_array_assign
            ;

expression  : //expression ('&&' | '<' | '+' | '-' | '*') expression
                //#expr_op
            exp1=expression '&&' exp2=expression
                #expr_op_and
            | exp3=expression '<' exp4=expression
                #expr_op_less
            | exp5=expression '+' exp6=expression
                #expr_op_plus
            | exp7=expression '-' exp8=expression
                #expr_op_minus
            | exp9=expression '*' exp10=expression
                #expr_op_multi
            | expArray1=expression '[' expArray2=expression ']'
                #expr_array
            | expLegth=expression '.' 'length'
                #expr_length
            | exp_chamador=expression '.' Identifier '(' (listaExpCamadaFuncao1=expression (',' listaExpCamadaFuncao2+=expression)* )? ')'
                #expr_method_calling
            | Integer
                #expr_int
            | Boolean
                #expr_bool
            | Identifier
                #expr_id
            | 'this'
                #expr_this
            | 'new' 'int' '[' exp12=expression ']'
                #expr_int_array
            | 'new' Identifier '(' ')'
                #expr_new_array
            | '!' exp_not=expression
                #expr_not
            | '(' exp_lr=expression ')'
                #expr_lrparents
            | expression ('&&' | '<' | '+' | '-' | '*')
                {self.notifyErrorListeners('Erro: Faltando o RHS do operador')}
                #err_miss_RHS
            | ('&&' | '<' | '+' | '-' | '*') expression
                {self.notifyErrorListeners('Erro: Faltando o LHS do operador')}
                #err_miss_LHS
            | '(' expression ')' ')'
                {self.notifyErrorListeners("Erro: Muitos ')'s")}
                #err_many_rparents
            | '(' '(' expression ')'
                {self.notifyErrorListeners("Erro: Muitos '('s")}
                #err_many_lparents
            //| '(' expression
            //    {self.notifyErrorListeners('Erro: Falta parentese a direita')}
            //    #err_rparent_closing
            //| expression ')'
            //    {self.notifyErrorListeners('Erro: Falta parentese a esquerda')}
            //    #err_lparent_closing
            ;

Boolean : 'true'
        | 'false'
        ;

Identifier  : [a-zA-Z_][a-zA-Z0-9_]*
            | [0-9]+[a-zA-Z_][a-zA-Z0-9_]*
                {self.notifyErrorListeners('Erro: Identificador começando com digito')}
            ;

Integer : [0-9]+
        ;
//Espaco em Branco
WS  : [ \t\r\n]+ -> skip
    ;
//Comentarios de multiplas linhas
LineComment : '//' .*? ('\r')? '\n' -> skip
            ;

//Comentarios de uma linha so
Comment : '/*' .*? '*/' -> skip
        ;