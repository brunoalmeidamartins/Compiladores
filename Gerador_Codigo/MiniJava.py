# -*- coding: utf-8 -*-

import os, sys, re
from antlr4 import *
from antlr4.error import ErrorListener
import argparse
import os

if __name__ is not None and "." in __name__:
	from .MiniJavaParser import MiniJavaParser
	from .MiniJavaLexer import MiniJavaLexer
	from .MiniJavaVisitor import MiniJavaVisitor
	from .MiniJavaListener import MiniJavaListener
	from .MiniJavaError_Presenter import MiniJava_ErrorListener
	from .MiniJavaSemanticAnalysis import *
	from .MiniJavaASTBuilder import *
	from .utilities import *
	from .AnaliseSemantica import *
else:
	from MiniJavaParser import MiniJavaParser
	from MiniJavaLexer import MiniJavaLexer
	from MiniJavaVisitor import MiniJavaVisitor
	from MiniJavaListener import MiniJavaListener
	from MiniJavaError_Presenter import MiniJava_ErrorListener
	from MiniJavaSemanticAnalysis import *
	from MiniJavaASTBuilder import *
	from utilities import *
	from AnaliseSemantica import *


def semantic_check(parser_ret):
	visitor4 = Visitor1()
	visitor4.visit(parser_ret)

	visitor5 = Visitor2(visitor4.retornaClassePronta())
	visitor5.visit(parser_ret)

	visitor6 = Visitor3()
	visitor6.visit(parser_ret)

	visitor7 = Visitor4(visitor6.retornaClassePronta())
	visitor7.visit(parser_ret)
	string = visitor7.devolveCodigoIntermediario()
	arq = open("03_SPIGLET/arquivo_spiglet_grupo.spg", 'w')
	arq.writelines(string)
	arq.close()

def geracao_codigo(path_arquivo):
	# Gera codigo par piglet
	resultado = os.popen('java -jar 01_MINIJAVA/minijava.jar ' + path_arquivo).read()
	arq = open("02_PIGLET/arquivo_piglet.pg", 'w')
	arq.writelines(resultado)
	arq.close()

	# Gera codigo para spiglet
	resultado = os.popen('java -jar 02_PIGLET/piglet.jar 02_PIGLET/arquivo_piglet.pg').read()
	arq = open("03_SPIGLET/arquivo_spiglet.spg", 'w')
	arq.writelines(resultado)
	arq.close()

	# Gera codigo para kanga
	resultado = os.popen('java -jar 03_SPIGLET/spiglet.jar 03_SPIGLET/arquivo_spiglet.spg').read()
	arq = open("04_KANGA/arquivo_kanga.kg", 'w')
	arq.writelines(resultado)
	arq.close()

	# Gera codigo para MIPS
	resultado = os.popen('java -jar 04_KANGA/kanga.jar 04_KANGA/arquivo_kanga.kg').read()
	arq = open("05_MIPS/arquivo_mips.s", 'w')
	arq.writelines(resultado)
	arq.close()

def draw(treelist, name):
	draw_pic(treelist, name)
	return treelist


def process(args):
	data = open(args.input_file).read()
	input = InputStream(data)
	lexer = MiniJavaLexer(input)
	stream = CommonTokenStream(lexer)
	parser = MiniJavaParser(stream)
	# setup the error listener
	parser.removeErrorListeners()
	parser.addErrorListener(MiniJava_ErrorListener())  # ()!!!
	tree = parser.goal()

	# semantic analysis
	try:
		semantic_check(tree)
		print("Semantica, Ok!!")
		try:
			geracao_codigo(args.input_file)
			print("Codigo MIPS gerado!!")
		except:
			print("Erro durante a geracao de codigo MIPS!!")
	except:
		print('Erro durante o processo na analise Semantica!!')



def main():

	aparser = argparse.ArgumentParser()

	aparser.add_argument('--input_file', '-i', type=str, default=None,
	                     help='minijava file for parsing')
	aparser.add_argument('--cst', action='store_true', default=False,
	                     help='show parse tree')
	aparser.add_argument('--ast', action='store_true', default=False,
	                     help='show ast')
	aparser.add_argument('--output_dir', '-o', type=str, default='output/',
	                     help='output directory of ast/cst trees')

	args = aparser.parse_args()

	print('* Compilando...')
	if os.path.exists(args.input_file) and os.path.isfile(args.input_file):
		process(args)
	else:
		print("[ERROR] arquivo: %s nao existe" % os.path.normpath(args.input_file))

	print('* Fim')


if __name__ == '__main__':
	main()
