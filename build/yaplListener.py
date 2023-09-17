# Generated from yapl.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .yaplParser import yaplParser
else:
    from yaplParser import yaplParser

# This class defines a complete listener for a parse tree produced by yaplParser.
class yaplListener(ParseTreeListener):

    # Enter a parse tree produced by yaplParser#prog.
    def enterProg(self, ctx:yaplParser.ProgContext):
        pass

    # Exit a parse tree produced by yaplParser#prog.
    def exitProg(self, ctx:yaplParser.ProgContext):
        pass


    # Enter a parse tree produced by yaplParser#class_def.
    def enterClass_def(self, ctx:yaplParser.Class_defContext):
        pass

    # Exit a parse tree produced by yaplParser#class_def.
    def exitClass_def(self, ctx:yaplParser.Class_defContext):
        pass


    # Enter a parse tree produced by yaplParser#feat_def.
    def enterFeat_def(self, ctx:yaplParser.Feat_defContext):
        pass

    # Exit a parse tree produced by yaplParser#feat_def.
    def exitFeat_def(self, ctx:yaplParser.Feat_defContext):
        pass


    # Enter a parse tree produced by yaplParser#feat_asgn.
    def enterFeat_asgn(self, ctx:yaplParser.Feat_asgnContext):
        pass

    # Exit a parse tree produced by yaplParser#feat_asgn.
    def exitFeat_asgn(self, ctx:yaplParser.Feat_asgnContext):
        pass


    # Enter a parse tree produced by yaplParser#formal.
    def enterFormal(self, ctx:yaplParser.FormalContext):
        pass

    # Exit a parse tree produced by yaplParser#formal.
    def exitFormal(self, ctx:yaplParser.FormalContext):
        pass


    # Enter a parse tree produced by yaplParser#expr_parenthesis.
    def enterExpr_parenthesis(self, ctx:yaplParser.Expr_parenthesisContext):
        pass

    # Exit a parse tree produced by yaplParser#expr_parenthesis.
    def exitExpr_parenthesis(self, ctx:yaplParser.Expr_parenthesisContext):
        pass


    # Enter a parse tree produced by yaplParser#expr_negado.
    def enterExpr_negado(self, ctx:yaplParser.Expr_negadoContext):
        pass

    # Exit a parse tree produced by yaplParser#expr_negado.
    def exitExpr_negado(self, ctx:yaplParser.Expr_negadoContext):
        pass


    # Enter a parse tree produced by yaplParser#expr_false.
    def enterExpr_false(self, ctx:yaplParser.Expr_falseContext):
        pass

    # Exit a parse tree produced by yaplParser#expr_false.
    def exitExpr_false(self, ctx:yaplParser.Expr_falseContext):
        pass


    # Enter a parse tree produced by yaplParser#expr_mult.
    def enterExpr_mult(self, ctx:yaplParser.Expr_multContext):
        pass

    # Exit a parse tree produced by yaplParser#expr_mult.
    def exitExpr_mult(self, ctx:yaplParser.Expr_multContext):
        pass


    # Enter a parse tree produced by yaplParser#expr_self.
    def enterExpr_self(self, ctx:yaplParser.Expr_selfContext):
        pass

    # Exit a parse tree produced by yaplParser#expr_self.
    def exitExpr_self(self, ctx:yaplParser.Expr_selfContext):
        pass


    # Enter a parse tree produced by yaplParser#expr_instance.
    def enterExpr_instance(self, ctx:yaplParser.Expr_instanceContext):
        pass

    # Exit a parse tree produced by yaplParser#expr_instance.
    def exitExpr_instance(self, ctx:yaplParser.Expr_instanceContext):
        pass


    # Enter a parse tree produced by yaplParser#expr_decl.
    def enterExpr_decl(self, ctx:yaplParser.Expr_declContext):
        pass

    # Exit a parse tree produced by yaplParser#expr_decl.
    def exitExpr_decl(self, ctx:yaplParser.Expr_declContext):
        pass


    # Enter a parse tree produced by yaplParser#expr_isvoid.
    def enterExpr_isvoid(self, ctx:yaplParser.Expr_isvoidContext):
        pass

    # Exit a parse tree produced by yaplParser#expr_isvoid.
    def exitExpr_isvoid(self, ctx:yaplParser.Expr_isvoidContext):
        pass


    # Enter a parse tree produced by yaplParser#expr_call.
    def enterExpr_call(self, ctx:yaplParser.Expr_callContext):
        pass

    # Exit a parse tree produced by yaplParser#expr_call.
    def exitExpr_call(self, ctx:yaplParser.Expr_callContext):
        pass


    # Enter a parse tree produced by yaplParser#expr_less_than.
    def enterExpr_less_than(self, ctx:yaplParser.Expr_less_thanContext):
        pass

    # Exit a parse tree produced by yaplParser#expr_less_than.
    def exitExpr_less_than(self, ctx:yaplParser.Expr_less_thanContext):
        pass


    # Enter a parse tree produced by yaplParser#expr_int.
    def enterExpr_int(self, ctx:yaplParser.Expr_intContext):
        pass

    # Exit a parse tree produced by yaplParser#expr_int.
    def exitExpr_int(self, ctx:yaplParser.Expr_intContext):
        pass


    # Enter a parse tree produced by yaplParser#expr_class_call.
    def enterExpr_class_call(self, ctx:yaplParser.Expr_class_callContext):
        pass

    # Exit a parse tree produced by yaplParser#expr_class_call.
    def exitExpr_class_call(self, ctx:yaplParser.Expr_class_callContext):
        pass


    # Enter a parse tree produced by yaplParser#expr_equal.
    def enterExpr_equal(self, ctx:yaplParser.Expr_equalContext):
        pass

    # Exit a parse tree produced by yaplParser#expr_equal.
    def exitExpr_equal(self, ctx:yaplParser.Expr_equalContext):
        pass


    # Enter a parse tree produced by yaplParser#expr_str.
    def enterExpr_str(self, ctx:yaplParser.Expr_strContext):
        pass

    # Exit a parse tree produced by yaplParser#expr_str.
    def exitExpr_str(self, ctx:yaplParser.Expr_strContext):
        pass


    # Enter a parse tree produced by yaplParser#expr_asgn.
    def enterExpr_asgn(self, ctx:yaplParser.Expr_asgnContext):
        pass

    # Exit a parse tree produced by yaplParser#expr_asgn.
    def exitExpr_asgn(self, ctx:yaplParser.Expr_asgnContext):
        pass


    # Enter a parse tree produced by yaplParser#expr_while.
    def enterExpr_while(self, ctx:yaplParser.Expr_whileContext):
        pass

    # Exit a parse tree produced by yaplParser#expr_while.
    def exitExpr_while(self, ctx:yaplParser.Expr_whileContext):
        pass


    # Enter a parse tree produced by yaplParser#expr_brackets.
    def enterExpr_brackets(self, ctx:yaplParser.Expr_bracketsContext):
        pass

    # Exit a parse tree produced by yaplParser#expr_brackets.
    def exitExpr_brackets(self, ctx:yaplParser.Expr_bracketsContext):
        pass


    # Enter a parse tree produced by yaplParser#expr_true.
    def enterExpr_true(self, ctx:yaplParser.Expr_trueContext):
        pass

    # Exit a parse tree produced by yaplParser#expr_true.
    def exitExpr_true(self, ctx:yaplParser.Expr_trueContext):
        pass


    # Enter a parse tree produced by yaplParser#expr_negative.
    def enterExpr_negative(self, ctx:yaplParser.Expr_negativeContext):
        pass

    # Exit a parse tree produced by yaplParser#expr_negative.
    def exitExpr_negative(self, ctx:yaplParser.Expr_negativeContext):
        pass


    # Enter a parse tree produced by yaplParser#expr_if.
    def enterExpr_if(self, ctx:yaplParser.Expr_ifContext):
        pass

    # Exit a parse tree produced by yaplParser#expr_if.
    def exitExpr_if(self, ctx:yaplParser.Expr_ifContext):
        pass


    # Enter a parse tree produced by yaplParser#expr_not.
    def enterExpr_not(self, ctx:yaplParser.Expr_notContext):
        pass

    # Exit a parse tree produced by yaplParser#expr_not.
    def exitExpr_not(self, ctx:yaplParser.Expr_notContext):
        pass


    # Enter a parse tree produced by yaplParser#expr_id.
    def enterExpr_id(self, ctx:yaplParser.Expr_idContext):
        pass

    # Exit a parse tree produced by yaplParser#expr_id.
    def exitExpr_id(self, ctx:yaplParser.Expr_idContext):
        pass


    # Enter a parse tree produced by yaplParser#expr_suma.
    def enterExpr_suma(self, ctx:yaplParser.Expr_sumaContext):
        pass

    # Exit a parse tree produced by yaplParser#expr_suma.
    def exitExpr_suma(self, ctx:yaplParser.Expr_sumaContext):
        pass



del yaplParser