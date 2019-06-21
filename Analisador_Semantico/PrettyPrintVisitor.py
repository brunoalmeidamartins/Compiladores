#import Syntaxtree
# Visitor Interface
class statement():
    def accept(self):
        pass
    def type_accept(self):
        pass

class exp():
    def accept(self, v):
        pass
    def type_accept(self, v):
        pass


class type():
    def accept(self, v):
        pass
    def type_accept(self, v):
        pass

class andjava(exp):
    def __init__(self, ae1, ae2):
        self.e1 = ae1
        self.e2 = ae2

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class arrayassign(statement):
    def __init__(self, ai, ae1, ae2):
        self.i = ai
        self.e1 = ae1
        self.e2 = ae2

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class arraylength(exp):
    def __init__(self, ae):
        self.e = ae

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class arraylookup(exp):
    def __init__(self, ae1, ae2):
        self.e1 = ae1
        self.e2 = ae2

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class assing(statement):
    def __init__(self, ai, ae):
        self.i = ai
        self.e = ae

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class block(statement):
    def __init__(self, asl):
        self.sl = asl

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class booleantype(type):
    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
         return v.visit(self)


class call(exp):
    def __init__(self, ae, ai, ael):
        self.e = ae
        self.i = ai
        self.el = ael

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class classdecl():
    def accept(self, v):
        pass
    def type_accept(self, v):
        pass


class cassdeclextends(classdecl):
    def __init__(self, ai, aj, avl, aml):
        self.i = ai
        self.j = aj
        self.vl = avl
        self.ml = aml

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class classdecllist():
    def __init__(self):
        self.lista = []

    def addElement(self, n):
        self.lista.append(n)

    def elementAt(self, i):
        return self.elementAt(i)

    def size(self):
        return len(self.lista)


class classdeclsimple(classdecl):
    def __init__(self, ai, avl, aml):
        self.i = ai
        self.vl = avl
        self.ml = aml

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)

class explist():
    def __init__(self):
        self.lista = []

    def addElement(self, n):
        self.lista.append(n)

    def elementAt(self, i):
        return self.elementAt(i)

    def size(self):
        return len(self.lista)


class false(exp):
    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class formal():
    def __init__(self, at, ai):
        self.t = at
        self.i = ai

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class formallist():
    def __init__(self):
        self.lista = []

    def addElement(self, n):
        self.lista.append(n)

    def elementAt(self, i):
        return self.elementAt(i)

    def size(self):
        return len(self.lista)


class identifier():
    def __init__(self, asf):
        self.s = asf

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)

    def toString(self):
        return self.s


class identifierexp(exp):
    def __init__(self, asf):
        self.s = asf

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class identifiertype(type):
    def __init__(self, asf):
        self.s = asf

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class ifjava(statement):
    def __init__(self, ae, as1, as2):
        self.e = ae
        self.s1 = as1
        self.s2 = as2

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class intarraytype(type):
    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class intergerliteral(exp):
    def __init__(self, ai):
        self.i = ai

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class integertype(type):
    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class lessthan(exp):
    def __init__(self, ae1, ae2):
        self.e1 = ae1
        self.e2 = ae2

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class mainclass():
    def __init__(self, ai1, ai2, asf):
        self.i1 = ai1
        self.i2 = ai2
        self.s = asf

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class methoddecl():
    def __init__(self, at, ai, afl, avl, asl, ae):
        self.t = at
        self.i = ai
        self.fl = afl
        self.vl = avl
        self.sl = asl
        self.e = ae

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class methoddecllist():
    def __init__(self):
        self.lista = []

    def addElement(self, n):
        self.lista.append(n)

    def elementAt(self, i):
        return self.elementAt(i)

    def size(self):
        return len(self.lista)


class minus(exp):
    def __init__(self, ae1, ae2):
        self.e1 = ae1
        self.e2 = ae2

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class newarray(exp):
    def __init__(self, ae):
        self.e = ae

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class newobject(exp):
    def __init__(self, ai):
        self.i = ai

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class notjava(exp):
    def __init__(self, ae):
        self.e = ae

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class plus(exp):
    def __init__(self, ae1, ae2):
        self.e1 = ae1
        self.e2 = ae2

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class printjava(statement):
    def __init__(self, ae):
        self.e = ae

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class program():
    def __init__(self, am, acl):
        self.m = am
        self.cl = acl

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)

class statementList():
    def __init__(self):
        self.lista = []

    def addElement(self, n):
        self.lista.append(n)

    def elementAt(self, i):
        return self.elementAt(i)

    def size(self):
        return len(self.lista)


class this(exp):
    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class times(exp):
    def __init__(self, ae1, ae2):
        self.e1 = ae1
        self.e2 = ae2

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class true(exp):
    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)

class vardecl():
    def __init__(self, at, ai):
        self.t = at
        self.i = ai

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)


class vardecllist():
    def __init__(self):
        self.lista = []

    def addElement(self, n):
        self.lista.append(n)

    def elementAt(self, i):
        return self.elementAt(i)

    def size(self):
        return len(self.lista)


class whilejava(statement):
    def __init__(self, ae, asf):
        self.e = ae
        self.s = asf

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)

class Visitor():
  def mainclass_visit(self, mainclass):
      pass
  def classdeclsimple_visit(self, classdeclsimple):
      pass
  def classdeclextends_visit(self, classdeclextends):
      pass
  def vardecl_visit(self, vardecl):
      pass
  def methoddecl_visit(self, methoddecl):
      pass
  def formal_visit(self, formal):
      pass
  def intarraytype_visit(self, intarraytype):
      pass
  def booleantype_visit(self, booleantype):
      pass
  def integertype_visit(self, integertype):
      pass
  def identifiertype_visit(self, identifiertype):
      pass
  def block_visit(self, block):
      pass
  def ifjava_visit(self, ifjava):
      pass
  def whilejava_visit(self, whilejava):
      pass
  def printjava_visit(self, printjava):
      pass
  def assign_visit(self, assign):
      pass
  def arrayassign_visit(self, arrayassign):
      pass
  def andjava_visit(self, andjava):
      pass
  def lessthan_visit(self, lessthan):
      pass
  def plus_visit(self, plus):
      pass
  def minus_visit(self, minus):
      pass
  def times_visit(self, times):
      pass
  def arraylookup_visit(self, arraylookup):
      pass
  def arraylength_visit(self, arraylength):
      pass
  def call_visit(self, call):
      pass
  def integerliteral_visit(self, integerliteral):
      pass
  def true_visit(self, true):
      pass
  def false_visit(self, false):
      pass
  def identifierexp_visit(self, identifierexp):
      pass
  def this_visit(self, this):
      pass
  def newarray_visit(self, newarray):
      pass
  def newobject_visit(self, newobject):
      pass
  def notjava_visit(self, notjava):
      pass
  def identifier_visit(self, identifier):
      pass


#Visitor implements
class PrettyPrintVisitor(Visitor):

  # MainClass m;
  # ClassDeclList cl;
  def program_visit(self, program):
      n=program
      n.m.accept(self)
      for i in n.cl.elementAt:
        print()
        i.accept(self)
    
  

  # Identifier i1,i2;
  # Statement s;
  def mainclass_visit(self, mainclass):
    n=mainclass
    print("class ")
    n.i1.accept(self)
    print(" ")
    print("  public static void main (String [] ")
    n.i2.accept(self)
    print(") ")
    print("    ")
    n.s.accept(self)
    print("  ")
    print("")
  

  # Identifier i;
  # VarDeclList vl;
  # MethodDeclList ml;
  def classdeclsimple_visit(self, classdeclsimple):
      n=classdeclsimple
      print("class ")
      n.i.accept(self)
      print("  ")
      cont = 0
      for i in n.vl.elementAt:
          print("  ")
          i.accept(self)
          if cont+1 < n.vl.size():
              print()
          cont +=1
    
      for i in n.ml.elementAt:
          print()
          i.accept(self)
    
      print()
      print("")
  

  # Identifier i;
  # Identifier j;
  # VarDeclList vl;
  # MethodDeclList ml;
  def classdeclextends_visit(self, classdeclextends):
      n=classdeclextends
      print("class ")
      n.i.accept(self)
      print(" extends ")
      n.j.accept(self)
      print("  ")
      cont = 0
      for i in n.vl.elementAt:
          print("  ")
          i.accept(self)
          if cont+1 < n.vl.size():
              print()
          cont +=1
    
      for i in n.ml.elementAt:
          print()
          i.accept(self)
    
      print()
      print("")
  

  # Type t;
  # Identifier i;
  def vardecl_visit(self, vardecl):
      n = vardecl
      n.t.accept(self)
      print(" ")
      n.i.accept(self)
      print(";")
  

  # Type t;
  # Identifier i;
  # FormalList fl;
  # VarDeclList vl;
  # StatementList sl;
  # Exp e;
  def methoddecl_visit(self, methoddecl):
      n=methoddecl
      print("  public ")
      n.t.accept(self)
      print(" ")
      n.i.accept(self)
      print(" (")
      cont = 0
      for i in n.fl.elementAt:
          i.accept(self)
          if cont+1 < n.fl.size():
              print(", ")
          cont +=1
    
      print(")  ")
      for i in n.vl.elementAt:
          print("    ")
          i.accept(self)
          print("")
      cont = 0
      for i in n.sl.elementAt:
          print("    ")
          i.accept(self)
          if cont < n.sl.size():
             print("")
          cont +=1
      print("    return ")
      n.e.accept(self)
      print("")
      print("  ")
  

  # Type t
  # Identifier i;
  def formal_visit(self, formal):
      n = formal
      n.t.accept(self)
      print(" ")
      n.i.accept(self)
  

  def intarraytype_visit(self, intarraytype):
      print("int []")
  

  def booleantype_visit(self, booleantype):
      print("boolean")
  

  def integertype_visit(self, integertype):
      print("int")
  

  # String s;
  def identifiertype_visit(self, identifiertype):
      n = identifiertype
      print(n.s)
  

  # StatementList sl;
  def block_visit(self, block):
      n=block
      print(" ")
      for i in n.sl.elementAt:
           print("      ")
           i.accept(self)
           print()
      print("     ")
  

  # Exp e;
  # Statement s1,s2;
  def ifjava_visit(self, ifjava):
      n = ifjava
      print("if (")
      n.e.accept(self)
      print(") ")
      print("    ")
      n.s1.accept(self)
      print();
      print("    else ")
      n.s2.accept(self)
  

  # Exp e;
  # Statement s;
  def whilejava_visit(self, whilejava):
      n=whilejava
      print("while (")
      n.e.accept(self)
      print(") ")
      n.s.accept(self)
  

  # Exp e;
  def printjava_visit(self, printjava):
      n = printjava
      print("System.out.prinln(")
      n.e.accept(self)
      print(");")
  

  # Identifier i;
  # Exp e;
  def assign_visit(self, assign):
      n = assign
      n.i.accept(self)
      print(" = ")
      n.e.accept(self)
      print(";")
  

  # Identifier i;
  # Exp e1,e2;
  def arrayassign_visit(self, arrayassign):
      n = arrayassign
      n.i.accept(self)
      print("[")
      n.e1.accept(self)
      print("] = ")
      n.e2.accept(self)
      print(";")
  

  # Exp e1,e2;
  def andjava_visit(self, andjava):
      n = andjava
      print("(")
      n.e1.accept(self)
      print(" && ")
      n.e2.accept(self)
      print(")")
  

  # Exp e1,e2;
  def lessthan_visit(self, lessthan):
      n = lessthan
      print("(")
      n.e1.accept(self)
      print(" < ")
      n.e2.accept(self)
      print(")")
  

  # Exp e1,e2;
  def plus_visit(self, plus):
      n = plus
      print("(")
      n.e1.accept(self)
      print(" + ")
      n.e2.accept(self)
      print(")")
  

  # Exp e1,e2;
  def minus_visit(self, minus):
      n = minus
      print("(")
      n.e1.accept(self)
      print(" - ")
      n.e2.accept(self)
      print(")")
  

  # Exp e1,e2;
  def times_visit(self, times):
      n=times
      print("(")
      n.e1.accept(self)
      print(" * ")
      n.e2.accept(self)
      print(")")
  

  # Exp e1,e2;
  def arraylookup_visit(self, arraylookup):
      n = arraylookup
      n.e1.accept(self)
      print("[")
      n.e2.accept(self)
      print("]")
  

  # Exp e;
  def arraylength_visit(self, arraylength):
      n=arraylength
      n.e.accept(self)
      print(".length")
  

  # Exp e;
  # Identifier i;
  # ExpList el;
  def call_visit(self, call):
      n=call
      n.e.accept(self)
      print(".")
      n.i.accept(self)
      print("(")
      cont = 0
      for i in n.el.elementAt:
          i.accept(self)
          if cont+1 < n.el.size():
              print(", ")
          cont +=1
    
      print(")")
  

  # int i;
  def integerliteral_visit(self, integerliteral):
      n=integerliteral
      print(n.i)
  

  def true_visit(self, true):
      print("true")
  

  def false_visit(self, false):
      print("false")
  

  # String s;
  def identifierexp_visit(self, identifierexp):
      n=identifierexp
      print(n.s);
  

  def this_visit(self, this):
    print("this")
  

  # Exp e;
  def newarray_visit(self, newarray):
      n=newarray
      print("new int [")
      n.e.accept(self)
      print("]")
  

  # Identifier i;
  def newobject_visit(self, newobject):
      n=newobject
      print("new ")
      print(n.i.s)
      print("()")
  

  # Exp e;
  def notjava_visit(self, notjava):
      n=notjava
      print("!")
      n.e.accept(self)

  # String s;
  def identifier_visit(self, identifier):
      n=identifier
      print(n.s)