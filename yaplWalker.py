
import sys
import ctypes
from antlr4 import *
from symbolTable import SymbolTable
from build.yaplParser import yaplParser
from build.yaplVisitor import yaplVisitor

# This class defines a custom visitor for a parse tree.

BOOL_MAX_SIZE = 28
MAX_SIZE = 1234567890

class yaplWalker(yaplVisitor):

    def __init__(self) -> None:
        self.basic_types = ["Int", "String", "Bool"]
        self.errors = []
        self.main_class_count = 0
        self.main_method_count = 0
        self.current_class = None
        self.current_method = None
        super().__init__()

    def initSymbolTable(self):
        self.symbolTable = SymbolTable()

    def getSymbolTable(self):
        return  self.symbolTable

    def find_or_create_type_id(self, ctx):

        if not ctx.TYPE_ID():
            return None

        symbol = self.symbolTable.find("TYPE_ID", ctx.TYPE_ID())

        if ctx.TYPE_ID():
            payload_value = ctx.TYPE_ID().getPayload()
        else:
            payload_value = None

        if not symbol:
            self.errors.append({
                "msg": "Undefined: {id}".format(id=ctx.TYPE_ID()),
                "payload": ctx.TYPE_ID().getPayload()
            })

            self.errors.append({
            "msg": "...",
            "payload": payload_value
            })

            self.symbolTable.add(
                "TYPE_ID",
                ctx.TYPE_ID(),
                line=ctx.TYPE_ID().getPayload().line,
                column=ctx.TYPE_ID().getPayload().column
            )

    def find_or_create_object_id(self, ctx):
        symbol = self.symbolTable.find("OBJECT_ID", ctx.OBJECT_ID())

        if not symbol:
            self.errors.append({
                "msg": "Undefined: {id}".format(id=ctx.OBJECT_ID()),
                "payload": ctx.OBJECT_ID().getPayload()
            })

            self.symbolTable.add(
                "OBJECT_ID",
                ctx.OBJECT_ID(),
                line=ctx.OBJECT_ID().getPayload().line,
                column=ctx.OBJECT_ID().getPayload().column
            )

    # Visit a parse tree produced by yaplParser#prog.
    def visitProg(self, ctx:yaplParser.ProgContext):

        # Defining Int
        self.symbolTable.add(
            "TYPE_ID",
            "Int",
            "class",
        )

        # Defining Bool
        self.symbolTable.add(
            "TYPE_ID",
            "Bool",
            "class",
        )

        # Defining String
        self.symbolTable.add(
            "TYPE_ID",
            "String",
            "class",
        )

        # Defining IO
        self.symbolTable.add(
            "TYPE_ID",
            "IO",
            "class",
        )

        self.symbolTable.add(
            "OBJECT_ID",
            "in_string",
            "Object",
            numParams=1,
            paramTypes=["String"],
            scope="IO",
            scope_type="global",
        )

        self.symbolTable.add(
            "OBJECT_ID",
            "out_string",
            "Object",
            numParams=1,
            paramTypes=["String"],
            scope="IO",
            scope_type="global",
        )

        self.symbolTable.add(
            "OBJECT_ID",
            "in_int",
            "Object",
            numParams=1,
            paramTypes=["Int"],
            scope="IO",
            scope_type="global",
        )

        self.symbolTable.add(
            "OBJECT_ID",
            "out_int",
            "Object",
            numParams=1,
            paramTypes=["Int"],
            scope="IO",
            scope_type="global",
        )

        self.visitChildren(ctx)

        # Checking the amount of Main classes
        if self.main_class_count != 1:
            self.errors.append({
                "msg": "Solo una clase Main debe existir",
                # "payload": ctx.TYPE_ID()[0].getPayload()
            })

        # Checking the amount of main methods
        if self.main_method_count != 1:
            self.errors.append({
                "msg": "Solo un metodo main en la clase Main debe existir",
                # "payload": feat_child_ctx.OBJECT_ID().getPayload()
            })

        return ctx


    # Visit a parse tree produced by yaplParser#class_def.
    def visitClass_def(self, ctx:yaplParser.Class_defContext):

        self.current_class = str(ctx.TYPE_ID()[0])

        # Checking Main Class errors
        if self.current_class == "Main":
            self.main_class_count += 1
            if len(ctx.TYPE_ID()) > 1:
                self.errors.append({
                    "msg": "Clase Main no debe heredar de ninguna",
                    "payload": ctx.TYPE_ID()[1].getPayload()
                })

        self.symbolTable.add(
            "TYPE_ID",
            self.current_class,
            ctx.CLASS(),
            line=ctx.CLASS().getPayload().line,
            column=ctx.CLASS().getPayload().column
        )

        # Class inheritance validations
        if ctx.INHERITS():
            # Inherit from a basic type is not possible
            if str(ctx.TYPE_ID()[1]) in self.basic_types:
                self.errors.append({
                    "msg": "No se puede heredar de un tipo basico",
                    "payload": ctx.TYPE_ID()[1].getPayload()
                })

            # Recursive inheritance is not possible
            if self.current_class == str(ctx.TYPE_ID()[1]):
                self.errors.append({
                    "msg": "No se puede heredar recursivamente",
                    "payload": ctx.TYPE_ID()[1].getPayload()
                })

            # Multiple inheritance is not possible
            if len(ctx.TYPE_ID()) >= 3 and ctx.TYPE_ID()[2]:
                self.errors.append({
                    "msg": "No se puede tener multiple herencia",
                    "payload": ctx.TYPE_ID()[2].getPayload()
                })

        self.visitChildren(ctx)
        return ctx


    # Visit a parse tree produced by yaplParser#feat_def.
    def visitFeat_def(self, ctx:yaplParser.Feat_defContext):
        self.current_method = str(ctx.OBJECT_ID())

        # Checking the amount of main methods
        if str(ctx.OBJECT_ID()) == "main":
            self.main_method_count += 1

            if len(ctx.formal()) > 0:
                self.errors.append({
                    "msg": "Metodo main no debe tener parametros formales",
                    "payload": ctx.OBJECT_ID().getPayload()
                })

        self.symbolTable.add(
            "OBJECT_ID",
            ctx.OBJECT_ID(),
            ctx.TYPE_ID(),
            line=ctx.OBJECT_ID().getPayload().line,
            column=ctx.OBJECT_ID().getPayload().column,
            numParams=len(ctx.formal()),
            paramTypes=[],
            scope="{class_scope}".format(class_scope=self.current_class),
            scope_type="global",
        )

        self.visitChildren(ctx)
        return ctx


    # Visit a parse tree produced by yaplParser#feat_asgn.
    def visitFeat_asgn(self, ctx:yaplParser.Feat_asgnContext):
        self.symbolTable.add(
            "OBJECT_ID",
            ctx.OBJECT_ID(),
            ctx.TYPE_ID(),
            line=ctx.OBJECT_ID().getPayload().line,
            column=ctx.OBJECT_ID().getPayload().column,
            scope="{class_scope}".format(class_scope=self.current_class),
            scope_type="global",
        )

        self.visitChildren(ctx)
        return ctx


    # Visit a parse tree produced by yaplParser#formal.
    def visitFormal(self, ctx:yaplParser.FormalContext):
        global_scope = "{class_scope}".format(class_scope=self.current_class)
        scope = "{method_scope}".format(method_scope=self.current_method)

        # Adding the current formal to the feature which belongs
        feature_symbol = self.symbolTable.find("OBJECT_ID", self.current_method, global_scope, "global")

        if feature_symbol:
            feature_symbol.paramTypes.append(str(ctx.TYPE_ID()))

        # Checking if already exists this formal on the current_scope
        symbol = self.symbolTable.find("OBJECT_ID", ctx.OBJECT_ID(), scope, "local")

        if symbol:
            self.errors.append({
                "msg": "{id} already exists".format(id=ctx.OBJECT_ID()),
                "payload": ctx.OBJECT_ID().getPayload()
            })

        self.symbolTable.add(
            "OBJECT_ID",
            ctx.OBJECT_ID(),
            ctx.TYPE_ID(),
            line=ctx.OBJECT_ID().getPayload().line,
            column=ctx.OBJECT_ID().getPayload().column,
            scope=scope,
            scope_type="local",
        )

        self.visitChildren(ctx)
        return ctx


    # ========================================================================================
    # Expressions
    # ========================================================================================


    # Visit a parse tree produced by yaplParser#expr_asgn.
    def visitExpr_asgn(self, ctx:yaplParser.Expr_asgnContext):
        self.find_or_create_object_id(ctx)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_class_call.
    def visitExpr_class_call(self, ctx:yaplParser.Expr_class_callContext):
        self.find_or_create_type_id(ctx)
        self.find_or_create_object_id(ctx)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_call.
    def visitExpr_call(self, ctx:yaplParser.Expr_callContext):
        self.find_or_create_object_id(ctx)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_if.
    def visitExpr_if(self, ctx:yaplParser.Expr_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_while.
    def visitExpr_while(self, ctx:yaplParser.Expr_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_brackets.
    def visitExpr_brackets(self, ctx:yaplParser.Expr_bracketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_decl.
    def visitExpr_decl(self, ctx:yaplParser.Expr_declContext):

        # TODO: revisar
        self.symbolTable.add(
            "OBJECT_ID",
            ctx.OBJECT_ID()[0],
            ctx.TYPE_ID()[0],
            line=ctx.LET().getPayload().line,
            column=ctx.LET().getPayload().column
        )

        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_instance.
    def visitExpr_instance(self, ctx:yaplParser.Expr_instanceContext):
        self.find_or_create_type_id(ctx)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_isvoid.
    def visitExpr_isvoid(self, ctx:yaplParser.Expr_isvoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_suma.
    def visitExpr_suma(self, ctx:yaplParser.Expr_sumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_mult.
    def visitExpr_mult(self, ctx:yaplParser.Expr_multContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_negative.
    def visitExpr_negative(self, ctx:yaplParser.Expr_negativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_negado.
    def visitExpr_negado(self, ctx:yaplParser.Expr_negadoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_less_than.
    def visitExpr_less_than(self, ctx:yaplParser.Expr_less_thanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_equal.
    def visitExpr_equal(self, ctx:yaplParser.Expr_equalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_not.
    def visitExpr_not(self, ctx:yaplParser.Expr_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_parenthesis.
    def visitExpr_parenthesis(self, ctx:yaplParser.Expr_parenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_id.
    def visitExpr_id(self, ctx:yaplParser.Expr_idContext):
        self.find_or_create_type_id(ctx)
        self.find_or_create_object_id(ctx)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_int.
    def visitExpr_int(self, ctx:yaplParser.Expr_intContext):
        # x = 14
        # print(id(x))
        # print(hex(id(x)))
        # print(ctypes.string_at(id(x), sys.getsizeof(x)))

        self.symbolTable.add(
            "INT",
            ctx.INT(),
            line=ctx.INT().getPayload().line,
            column=ctx.INT().getPayload().column,
            size=sys.getsizeof(int(ctx.INT().getText())),
            max_size=MAX_SIZE,
            address_id=id(int(ctx.INT().getText()))
        )
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_str.
    def visitExpr_str(self, ctx:yaplParser.Expr_strContext):
        self.symbolTable.add(
            "STRING",
            ctx.STRING(),
            line=ctx.STRING().getPayload().line,
            column=ctx.STRING().getPayload().column,
            size=sys.getsizeof(str(ctx.STRING().getText())),
            max_size=MAX_SIZE,
            address_id=id(str(ctx.STRING().getText()))
        )
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_true.
    def visitExpr_true(self, ctx:yaplParser.Expr_trueContext):
        self.symbolTable.add(
            "TRUE",
            ctx.TRUE(),
            line=ctx.TRUE().getPayload().line,
            column=ctx.TRUE().getPayload().column,
            size=sys.getsizeof(bool(ctx.TRUE().getText())),
            max_size=BOOL_MAX_SIZE,
            address_id=id(bool(ctx.TRUE().getText()))
        )
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_false.
    def visitExpr_false(self, ctx:yaplParser.Expr_falseContext):
        self.symbolTable.add(
            "FALSE",
            ctx.FALSE(),
            line=ctx.FALSE().getPayload().line,
            column=ctx.FALSE().getPayload().column,
            size=sys.getsizeof(bool(ctx.FALSE().getText())),
            max_size=BOOL_MAX_SIZE,
            address_id=id(bool(ctx.FALSE().getText()))
        )
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_self.
    def visitExpr_self(self, ctx:yaplParser.Expr_selfContext):
        return self.visitChildren(ctx)


del yaplParser
