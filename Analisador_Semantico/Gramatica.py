#Gramatica do livro
collision_gramar = '''
            ?program: mainclass classdecl* -> Program
            ?mainclass: class id "{" public static void main "(" string colce colcd id ")" "{" statement "}" "}" -> MainClass
            ?classdecl: class id "{" vardecl* methoddecl* "}" -> ClassDeclSimple
                     | class id extends id "{" vardecl* methoddecl* "}" -> ClassDeclExtends
            ?vardecl: type id ";" -> VarDecl
            ?methoddecl: public type id "(" formallist ")" "{" vardecl* statement* return exp ";" "}" -> MethodDecl
            ?formallist: type id formalrest* -> Formal
                       | 
            ?formalrest: virgula type id
            ?type: int colce colcd -> IntArrayType
                | boolean ->BooleanType
                | int -> IntegerType
                | id -> IdentifierType
            ?statement: "{" statement* "}" -> Block
                     | if "(" exp ")" statement else statement -> If
                     | while "(" exp ")" statement -> While
                     | systemoutprintln "(" exp ")" ";" -> Print
                     | id igual exp ";" -> Assign
                     | id colce exp colcd igual exp ";" -> ArrayAssign
            ?exp: exp ecomercial exp -> And
               | exp menor exp -> LessThan
               | exp mais exp -> Plus
               | exp menos exp -> Minus
               | exp multiplica exp -> Times
               | exp colce exp colcd -> ArrayLooup
               | exp ponto length -> ArrayLength
               | exp ponto id "(" explist ")" -> Call
               | numero -> IntegerLiteral
               | true -> True
               | false -> False
               | id -> IdentifierExp
               | this -> This
               | new int colce exp colcd -> NewArray
               | new id "(" ")" -> NewObject
               | negacao exp -> Not
               | "(" exp ")"
            ?explist: exp exprest* -> ExpList
                   | 
            ?exprest: virgula exp
            
            //Tokens
            string: "STRING"
            systemoutprintln: "SYSTEMOUTPRINTLN"
            main: "MAIN"
            static: "STATIC"
            void: "VOID"
            class: "CLASS"
            extends: "EXTENDS"
            public: "PUBLIC"
            return: "RETURN"
            boolean: "BOOLEAN"
            int: "INT"
            if: "IF"
            else: "ELSE"
            while: "WHILE"
            true: "TRUE"
            false: "FALSE"
            null: "NULL"
            new: "NEW"
            length: "LENGTH"
            this: "THIS"
            mais: "MAIS"
            menos: "MENOS"
            multiplica: "MULTIPLICA"
            divide: "DIVIDE"
            igual: "IGUAL"
            comparacao: "COMPARACAO"
            //pe: "PE"
            //pd: "PD"
            colce: "COLCE" 
            colcd: "COLCD"
            menor: "MENOR"
            maior: "MAIOR"
            menorigual: "MENORIGUAL"
            maiorigual: "MAIORIGUAL"
            negacao: "NEGACAO"
            diferente: "DIFERENTE"
            ecomercial: "ECOMERCIAL"
            virgula: "VIRGULA"
            ponto: "PONTO"
            //pontovirgula: "PONTOVIRGULA"
            //pontoponto: "PONTOPONTO" 
            numero: /[0-9]+/
            //numero: "NUMERO"
            //ID: "[a-zA-Z_][a-zA-Z_0-9]*"
            //id: "ID"
            id: /[a-zA-Z_][a-zA-Z_0-9]*/ -> Identifier
            //WS: "[ \t]+" (%ignore)
            //%import commom.WS
            %ignore " "
        '''
#Gramatica Funcionando
collision_gramar = ''' 
    ?goal: mainclass ( classdeclaration )* 
            ?mainclass: class id "{" public static void main "(" string colce colcd id ")" "{" statement "}" "}" 
            ?classdeclaration: class id (extends id)? "{" ( vardeclaration )* ( methoddeclaration )* "}"
            ?vardeclaration: type id ";"
            ?methoddeclaration: public type id "(" (type id ( virgula type id )* )? ")" "{" ( vardeclaration )* ( statement )* return expression ";" "}" 
            ?type: int colce colcd 
                |	boolean 
                |	int
                |	id
            ?statement: "{"  statement* "}"
                         | if "(" expression ")" statement else statement
                         |	while "(" expression ")" statement
                         |	systemoutprintln "(" expression ")" ";"
                         |	id igual expression ";"
                         |	id colce expression colcd igual expression ";"
            ?expression: expression ( ecomercial | menor | mais | menos | multiplica ) expression
                       | expression colce expression colcd
                       | expression ponto length
                       | expression ponto id "(" ( expression ( virgula expression)* )? ")"
                       | numero
                       | true
                       | false
                       | id
                       | this
                       | new int colce expression colcd
                       | new id "(" ")"
                       | negacao expression
                       | "(" expression ")"
            //Tokens
                string: "STRING"
                systemoutprintln: "SYSTEMOUTPRINTLN"
                main: "MAIN"
                static: "STATIC"
                void: "VOID"
                class: "CLASS"
                extends: "EXTENDS"
                public: "PUBLIC"
                return: "RETURN"
                boolean: "BOOLEAN"
                int: "INT"
                if: "IF"
                else: "ELSE"
                while: "WHILE"
                true: "TRUE"
                false: "FALSE"
                null: "NULL"
                new: "NEW"
                length: "LENGTH"
                this: "THIS"
                mais: "MAIS"
                menos: "MENOS"
                multiplica: "MULTIPLICA"
                divide: "DIVIDE"
                igual: "IGUAL"
                comparacao: "COMPARACAO"
                //pe: "PE"
                //pd: "PD"
                colce: "COLCE" 
                colcd: "COLCD"
                menor: "MENOR"
                maior: "MAIOR"
                menorigual: "MENORIGUAL"
                maiorigual: "MAIORIGUAL"
                negacao: "NEGACAO"
                diferente: "DIFERENTE"
                ecomercial: "ECOMERCIAL"
                virgula: "VIRGULA"
                ponto: "PONTO"
                //pontovirgula: "PONTOVIRGULA"
                //pontoponto: "PONTOPONTO" 
                numero: /[0-9]+/
                //numero: "NUMERO"
                //ID: "[a-zA-Z_][a-zA-Z_0-9]*"
                //id: "ID"
                id: /[a-zA-Z_][a-zA-Z_0-9]*/
                //WS: "[ \t]+" (%ignore)
                //%import commom.WS
                %ignore " "
'''

# print(texto)
        # texto = retornaTokensArquivo(path)
        collision_gramar = '''
            ?program: mainclass classdecl*
            ?mainclass: class id "{" public static void main "(" string colce colcd id ")" "{" statement "}" "}"
            ?classdecl: class id "{" vardecl* methoddecl* "}"
                     | class id extends id "{" vardecl* methoddecl* "}" -> ClassDeclExtends
            ?vardecl: type id ";"
            ?methoddecl: public type id "(" formallist ")" "{" vardecl* statement* return exp ";" "}"
            ?formallist: type id formalrest*
                       | 
            ?formalrest: virgula type id
            ?type: int colce colcd
                | boolean -> BooleanType
                | int
                | id
            ?statement: "{" statement* "}" -> Block
                     | if "(" exp ")" statement else statement
                     | while "(" exp ")" statement
                     | systemoutprintln "(" exp ")" ";"
                     | id igual exp ";" -> Assign
                     | id colce exp colcd igual exp ";" ->ArrayAssign
            ?exp: exp op exp
               | exp colce exp colcd
               | exp ponto length -> ArrayLength
               | exp ponto id "(" explist ")" -> Call
               | numero
               | true
               | false
               | id
               | this
               | new int colce exp colcd
               | new id "(" ")"
               | negacao exp
               | "(" exp ")"
            ?explist: exp exprest*
                   | 
            ?exprest: virgula exp
            ?op: ecomercial
                | menor
                | mais
                | menos
                | multiplica
            //Tokens
            string: "STRING"
            systemoutprintln: "SYSTEMOUTPRINTLN"
            main: "MAIN"
            static: "STATIC"
            void: "VOID"
            class: "CLASS"
            extends: "EXTENDS"
            public: "PUBLIC"
            return: "RETURN"
            boolean: "BOOLEAN"
            int: "INT"
            if: "IF"
            else: "ELSE"
            while: "WHILE"
            true: "TRUE"
            false: "FALSE"
            null: "NULL"
            new: "NEW"
            length: "LENGTH"
            this: "THIS"
            mais: "MAIS"
            menos: "MENOS"
            multiplica: "MULTIPLICA"
            divide: "DIVIDE"
            igual: "IGUAL"
            comparacao: "COMPARACAO"
            //pe: "PE"
            //pd: "PD"
            colce: "COLCE" 
            colcd: "COLCD"
            menor: "MENOR"
            maior: "MAIOR"
            menorigual: "MENORIGUAL"
            maiorigual: "MAIORIGUAL"
            negacao: "NEGACAO"
            diferente: "DIFERENTE"
            ecomercial: "ECOMERCIAL"
            virgula: "VIRGULA"
            ponto: "PONTO"
            //pontovirgula: "PONTOVIRGULA"
            //pontoponto: "PONTOPONTO" 
            numero: /[0-9]+/
            //numero: "NUMERO"
            //ID: "[a-zA-Z_][a-zA-Z_0-9]*"
            //id: "ID"
            id: /[a-zA-Z_][a-zA-Z_0-9]*/
            //WS: "[ \t]+" (%ignore)
            //%import commom.WS
            %ignore " "
        '''