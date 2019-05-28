palavras_reservadas = ['ABSTRACT', 'ASSERT', 'BOOLEAN', 'BREAK', 'BYTE', 'CASE', 'CATCH',
          'CHAR', 'CLASS', 'CONST', 'CONTINUE', 'DEFAULT', 'DO', 'DOUBLE', 'ELSE',
          'ENUM', 'EXTENDS', 'FINAL', 'FINALLY', 'FLOAT', 'FOR', 'IF', 'GOTO',
          'IMPLEMENTS', 'IMPORT', 'INSTANCEOF', 'INT', 'INTERFACE', 'LONG', 'NATIVE',
          'NEW', 'PACKAGE', 'PRIVATE', 'PROTECTED', 'PUBLIC', 'RETURN', 'SHORT', 'STATIC',
          'STRICTFP', 'SUPER', 'SWITCH', 'SYNCHRONIZED', 'THIS', 'THROW', 'THROWS', 'TRANSIENT',
          'TRY', 'VOID', 'VOLATILE', 'WHILE', 'MAIN', 'STRING', 'LENGTH', 'SYSTEM', 'OUT',
          'PRINTLN', 'SYSTEM.OUT.PRINTLN']


'''
#Palavras Reservadas
t_ABSTRACT = r'\abstract'
t_ASSERT = r'\assert'
t_BOOLEAN = r'\boolean'
t_BREAK = r'\break'
t_BYTE = r'\byte'
t_CASE = r'\case'
t_CATCH = r'\catch'
t_CHAR = r'\char'
t_CLASS = r'\class'
t_CONST = r'\const'
t_CONTINUE = r'\continue'
t_DEFAULT = r'\default'
t_DO = r'\do'
t_DOUBLE = r'\double'
t_ELSE = r'\else'
t_ENUM = r'\enum'
t_EXTENDS = r'\extends'
t_FINAL = r'\final'
t_FINALLY = r'\finally'
t_FLOAT = r'\float'
t_FOR = r'\for'
t_IF = r'\if'
t_GOTO = r'\goto'
t_IMPLEMENTS = r'\implements'
t_IMPORT = r'\import'
t_INSTANCEOF = r'\instanceof'
t_INT = r'\int'
t_INTERFACE = r'\interface'
t_LONG = r'\long'
t_NATIVE = r'\native'
t_NEW = r'\new'
t_PACKAGE = r'\package'
t_PRIVATE = r'\private'
t_PROTECTED = r'\protected'
t_PUBLIC = r'\public'
t_RETURN = r'\return'
t_SHORT = r'\short'
t_STATIC = r'\static'
t_STRICTFP = r'\strictfp'
t_SUPER = r'\super'
t_SWITCH = r'\switch'
t_SYNCHRONIZED = r'\synchronized'
t_THIS = r'\this'
t_THROW = r'\throw'
t_THROWS = r'\throws'
t_TRANSIENT = r'\transient'
t_TRY = r'\try'
t_VOID = r'\void'
t_VOLATILE = r'\volatile'
t_WHILE = r'\while'
t_MAIN = r'\main'
t_STRING = r'\string'
t_LENGTH = r'\length'
t_SYSTEM = r'\system'
t_OUT = r'\out'
t_PRINTLN = r'\println'
t_SYSTEM_OUT_PRINTLN = r'\system.out.println'
'''



for palavra in palavras_reservadas:
    print("'"+palavra.lower()+"':'"+palavra+"',")