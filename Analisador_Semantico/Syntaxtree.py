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
