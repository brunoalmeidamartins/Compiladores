#Interface
class TypeVisitor():
  def program_visit(self, program):
      pass
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

class TypeDepthFirstVisitor(TypeVisitor):
    # MainClass m;
    # ClassDeclList cl;
    def program_visit(self, program):
        n = program
        n.m.accept(self)
        for i in n.cl.elementAt:
            i.accept(self)

    # Identifier i1,i2;
    # Statement s;
    def mainclass_visit(self, mainclass):
        n = mainclass
        n.i1.accept(self)
        n.i2.accept(self)
        n.s.accept(self)

    # Identifier i;
    # VarDeclList vl;
    # MethodDeclList ml;
    def classdeclsimple_visit(self, classdeclsimple):
        n = classdeclsimple
        n.i.accept(self)
        for i in n.vl.elementAt:
            i.accept(self)
        for i in n.ml.elementAt:
            i.accept(self)

    # Identifier i;
    # Identifier j;
    # VarDeclList vl;
    # MethodDeclList ml;
    def classdeclextends_visit(self, classdeclextends):
        n = classdeclextends
        n.i.accept(self)
        n.j.accept(self)
        for i in n.vl.elementAt:
            i.accept(self)

        for i in n.ml.elementAt:
            i.accept(self)

    # Type t;
    # Identifier i;
    def vardecl_visit(self, vardecl):
        n = vardecl
        n.t.accept(self)
        n.i.accept(self)

    # Type t;
    # Identifier i;
    # FormalList fl;
    # VarDeclList vl;
    # StatementList sl;
    # Exp e;
    def methoddecl_visit(self, methoddecl):
        n = methoddecl
        n.t.accept(self)
        n.i.accept(self)
        for i in n.fl.elementAt:
            i.accept(self)
        for i in n.vl.elementAt:
            i.accept(self)
        for i in n.sl.elementAt:
            i.accept(self)
        n.e.accept(self)

    # Type t
    # Identifier i;
    def formal_visit(self, formal):
        n = formal
        n.t.accept(self)
        n.i.accept(self)

    def intarraytype_visit(self, intarraytype):
        pass

    def booleantype_visit(self, booleantype):
        pass

    def integertype_visit(self, integertype):
        pass

    # String s;
    def identifiertype_visit(self, identifiertype):
        pass

    # StatementList sl;
    def block_visit(self, block):
        n = block
        for i in n.sl.elementAt:
            i.accept(self)

    # Exp e;
    # Statement s1,s2;
    def ifjava_visit(self, ifjava):
        n = ifjava
        n.e.accept(self)
        n.s1.accept(self)
        n.s2.accept(self)

    # Exp e;
    # Statement s;
    def whilejava_visit(self, whilejava):
        n = whilejava
        n.e.accept(self)
        n.s.accept(self)

    # Exp e;
    def printjava_visit(self, printjava):
        n = printjava
        n.e.accept(self)

    # Identifier i;
    # Exp e;
    def assign_visit(self, assign):
        n = assign
        n.i.accept(self)
        n.e.accept(self)

    # Identifier i;
    # Exp e1,e2;
    def arrayassign_visit(self, arrayassign):
        n = arrayassign
        n.i.accept(self)
        n.e1.accept(self)
        n.e2.accept(self)

    # Exp e1,e2;
    def andjava_visit(self, andjava):
        n = andjava
        n.e1.accept(self)
        n.e2.accept(self)

    # Exp e1,e2;
    def lessthan_visit(self, lessthan):
        n = lessthan
        n.e1.accept(self)
        n.e2.accept(self)

    # Exp e1,e2;
    def plus_visit(self, plus):
        n = plus
        n.e1.accept(self)
        n.e2.accept(self)

    # Exp e1,e2;
    def minus_visit(self, minus):
        n = minus
        n.e1.accept(self)
        n.e2.accept(self)

    # Exp e1,e2;
    def times_visit(self, times):
        n = times
        n.e1.accept(self)
        n.e2.accept(self)

    # Exp e1,e2;
    def arraylookup_visit(self, arraylookup):
        n = arraylookup
        n.e1.accept(self)
        n.e2.accept(self)

    # Exp e;
    def arraylength_visit(self, arraylength):
        n = arraylength
        n.e.accept(self)

    # Exp e;
    # Identifier i;
    # ExpList el;
    def call_visit(self, call):
        n = call
        n.e.accept(self)
        n.i.accept(self)
        for i in n.el.elementAt:
            i.accept(self)

    # int i;
    def integerliteral_visit(self, integerliteral):
        pass

    def true_visit(self, true):
        pass

    def false_visit(self, false):
        pass

    # String s;
    def identifierexp_visit(self, identifierexp):
        pass

    def this_visit(self, this):
        pass

    # Exp e;
    def newarray_visit(self, newarray):
        n = newarray
        n.e.accept(self)


    # Identifier i;
    def newobject_visit(self, newobject):
        pass

    # Exp e;
    def notjava_visit(self, notjava):
        n = notjava
        n.e.accept(self)

    # String s;
    def identifier_visit(self, identifier):
        pass