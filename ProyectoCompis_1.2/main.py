import sys
from antlr4 import *
from antlr4.tree.Tree import TerminalNode
from ExpLexer import ExpLexer
from ExpParser import ExpParser
from ExpVisitor import ExpVisitor

def shunting_yard(infija):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}
    salida = []
    pila = []
    for token in infija:
        if token.isalnum(): 
            salida.append(token)
        elif token == '(':
            pila.append(token)
        elif token == ')':
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            pila.pop() 
        else: 
            while pila and pila[-1] != '(' and precedencia.get(pila[-1], 0) >= precedencia.get(token, 0):
                salida.append(pila.pop())
            pila.append(token)
    while pila:
        salida.append(pila.pop())
    return salida 

def evaluar_postfija(postfija, memoria):
    pila = []
    for token in postfija:
        if token in memoria: 
            pila.append(memoria[token])
        elif all(c in '0123456789ABCDEFabcdef' for c in token): 
            try:
                pila.append(int(token, 10))
            except ValueError:
                pila.append(int(token, 16))
        else:
            b = pila.pop()
            a = pila.pop()
            if token == '+': pila.append(a + b)
            elif token == '-': pila.append(a - b)
            elif token == '*': pila.append(a * b)
            elif token == '/': pila.append(a // b)
    return pila[0]

class MiVisitor(ExpVisitor):
    def __init__(self):
        self.memoria = {}

    def evaluar_nodo_expr(self, expr_ctx):
        infija = []
        def get_leaves(node):
            if isinstance(node, TerminalNode):
                infija.append(node.getText())
            else:
                for i in range(node.getChildCount()):
                    get_leaves(node.getChild(i))
        get_leaves(expr_ctx)
        postfija = shunting_yard(infija)
        return evaluar_postfija(postfija, self.memoria)

    def visitDeclaracion(self, ctx):
        tipo = ctx.tipo().getText()
        nombre = ctx.IDENTIFICADOR().getText()
        valor_str = ctx.valor().getText()

        try:
            if tipo == 'bin':
                if any(c not in '01' for c in valor_str): raise ValueError()
                valor = int(valor_str, 2)
            elif tipo == 'oct':
                if any(c not in '01234567' for c in valor_str): raise ValueError()
                valor = int(valor_str, 8)
            elif tipo == 'dec':
                if any(c not in '0123456789' for c in valor_str): raise ValueError()
                valor = int(valor_str, 10)
            elif tipo == 'hex':
                valor = int(valor_str, 16)
            
            self.memoria[nombre] = valor
            print(f"Log: var '{nombre}' guardada. Valor: {valor}")
            
        except ValueError:
            print(f"Error: Tipo incorrecto. '{valor_str}' no es {tipo}")
            sys.exit(1)

    def visitIf_real(self, ctx):
        #  Extrae la condicion
        cond_ctx = ctx.cond()
        
        #Se evalua el lado izquierdo y derecho de la condicion
        izq = self.evaluar_nodo_expr(cond_ctx.expr(0))
        der = self.evaluar_nodo_expr(cond_ctx.expr(1))
        
        # Se mira que operador es de los que definimos en g4 (>, <, ==)
        operador = cond_ctx.op_rel().getText()
        
        # Se verifica si la condificon que se puso es la correcta y se realiza la operacion 
        condicion_cumplida = False
        if operador == '>':  condicion_cumplida = (izq > der)
        elif operador == '<':  condicion_cumplida = (izq < der)
        elif operador == '==': condicion_cumplida = (izq == der)
        
        print(f"Log: Evaluando IF ({izq} {operador} {der}) -> {'VERDADERO' if condicion_cumplida else 'FALSO'}")
        
        # Si es verdadero, se realiza todo lo que este de ese lado, por ejemplo un axpresion 
        if condicion_cumplida:
            print("Log: Entrando al bloque IF...")
            for stat_ctx in ctx.stat():
                self.visit(stat_ctx)
        else:
            print("Log: Saltando bloque IF...")

    def visitStat(self, ctx):
        
        if ctx.declaracion():
            self.visitDeclaracion(ctx.declaracion())
        elif ctx.if_real():
            self.visitIf_real(ctx.if_real())
        elif ctx.expr():
            infija = []
            def get_leaves(node):
                if isinstance(node, TerminalNode):
                    infija.append(node.getText())
                else:
                    for i in range(node.getChildCount()):
                        get_leaves(node.getChild(i))
            
            get_leaves(ctx.expr())
            
            print("Infija encontrada:", infija)
            postfija = shunting_yard(infija)
            print("Postfija:", postfija)
            
            resultado = evaluar_postfija(postfija, self.memoria)
            print(f"RESULTADO: {resultado}")

def main():
    archivo = "programa.txt"
    
    input_stream = FileStream(archivo, encoding='utf-8')
    lexer = ExpLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExpParser(stream)
    
    print(f"Procesando: {archivo}")
    tree = parser.prog()
    
    print("----------------------\n")
    visitor = MiVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()