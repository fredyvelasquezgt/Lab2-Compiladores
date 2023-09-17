# Generated from yapl.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .yaplParser import yaplParser
else:
    from yaplParser import yaplParser

# This class defines a complete generic visitor for a parse tree produced by yaplParser.

class yaplVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by yaplParser#prog.
    def visitProg(self, ctx:yaplParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#class_def.
    def visitClass_def(self, ctx:yaplParser.Class_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#feat_def.
    def visitFeat_def(self, ctx:yaplParser.Feat_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#feat_asgn.
    def visitFeat_asgn(self, ctx:yaplParser.Feat_asgnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#formal.
    def visitFormal(self, ctx:yaplParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_parenthesis.
    def visitExpr_parenthesis(self, ctx:yaplParser.Expr_parenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_negado.
    def visitExpr_negado(self, ctx:yaplParser.Expr_negadoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_false.
    def visitExpr_false(self, ctx:yaplParser.Expr_falseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_mult.
    def visitExpr_mult(self, ctx:yaplParser.Expr_multContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_self.
    def visitExpr_self(self, ctx:yaplParser.Expr_selfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_instance.
    def visitExpr_instance(self, ctx:yaplParser.Expr_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_decl.
    def visitExpr_decl(self, ctx:yaplParser.Expr_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_isvoid.
    def visitExpr_isvoid(self, ctx:yaplParser.Expr_isvoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_call.
    def visitExpr_call(self, ctx:yaplParser.Expr_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_less_than.
    def visitExpr_less_than(self, ctx:yaplParser.Expr_less_thanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_int.
    def visitExpr_int(self, ctx:yaplParser.Expr_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_class_call.
    def visitExpr_class_call(self, ctx:yaplParser.Expr_class_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_equal.
    def visitExpr_equal(self, ctx:yaplParser.Expr_equalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_str.
    def visitExpr_str(self, ctx:yaplParser.Expr_strContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_asgn.
    def visitExpr_asgn(self, ctx:yaplParser.Expr_asgnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_while.
    def visitExpr_while(self, ctx:yaplParser.Expr_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_brackets.
    def visitExpr_brackets(self, ctx:yaplParser.Expr_bracketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_true.
    def visitExpr_true(self, ctx:yaplParser.Expr_trueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_negative.
    def visitExpr_negative(self, ctx:yaplParser.Expr_negativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_if.
    def visitExpr_if(self, ctx:yaplParser.Expr_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_not.
    def visitExpr_not(self, ctx:yaplParser.Expr_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_id.
    def visitExpr_id(self, ctx:yaplParser.Expr_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr_suma.
    def visitExpr_suma(self, ctx:yaplParser.Expr_sumaContext):
        return self.visitChildren(ctx)



del yaplParser