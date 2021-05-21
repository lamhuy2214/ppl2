# Generated from main/csel/parser/CSEL.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CSELParser import CSELParser
else:
    from CSELParser import CSELParser

# This class defines a complete generic visitor for a parse tree produced by CSELParser.

class CSELVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSELParser#program.
    def visitProgram(self, ctx:CSELParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#many_var_declare.
    def visitMany_var_declare(self, ctx:CSELParser.Many_var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#one_var_declare.
    def visitOne_var_declare(self, ctx:CSELParser.One_var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#many_const_declare.
    def visitMany_const_declare(self, ctx:CSELParser.Many_const_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#one_const_declare.
    def visitOne_const_declare(self, ctx:CSELParser.One_const_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#id_list.
    def visitId_list(self, ctx:CSELParser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#id_list_element.
    def visitId_list_element(self, ctx:CSELParser.Id_list_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#id_list_const.
    def visitId_list_const(self, ctx:CSELParser.Id_list_constContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#id_list_element_const.
    def visitId_list_element_const(self, ctx:CSELParser.Id_list_element_constContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#composit.
    def visitComposit(self, ctx:CSELParser.CompositContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#array_literal.
    def visitArray_literal(self, ctx:CSELParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#array_literal_element.
    def visitArray_literal_element(self, ctx:CSELParser.Array_literal_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#literal.
    def visitLiteral(self, ctx:CSELParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#assign_stm.
    def visitAssign_stm(self, ctx:CSELParser.Assign_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#parameter_name.
    def visitParameter_name(self, ctx:CSELParser.Parameter_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#param_list_element.
    def visitParam_list_element(self, ctx:CSELParser.Param_list_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#many_func_declare.
    def visitMany_func_declare(self, ctx:CSELParser.Many_func_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#one_func_declare.
    def visitOne_func_declare(self, ctx:CSELParser.One_func_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#many_stm.
    def visitMany_stm(self, ctx:CSELParser.Many_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#stm.
    def visitStm(self, ctx:CSELParser.StmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#call_stm.
    def visitCall_stm(self, ctx:CSELParser.Call_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#function_call.
    def visitFunction_call(self, ctx:CSELParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#return_stm.
    def visitReturn_stm(self, ctx:CSELParser.Return_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#if_stm.
    def visitIf_stm(self, ctx:CSELParser.If_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#if_then.
    def visitIf_then(self, ctx:CSELParser.If_thenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#many_elseif.
    def visitMany_elseif(self, ctx:CSELParser.Many_elseifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#else_part.
    def visitElse_part(self, ctx:CSELParser.Else_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#forin_stm.
    def visitForin_stm(self, ctx:CSELParser.Forin_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#forof_stm.
    def visitForof_stm(self, ctx:CSELParser.Forof_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#while_stm.
    def visitWhile_stm(self, ctx:CSELParser.While_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#break_stm.
    def visitBreak_stm(self, ctx:CSELParser.Break_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#continue_stm.
    def visitContinue_stm(self, ctx:CSELParser.Continue_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp.
    def visitExp(self, ctx:CSELParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp1.
    def visitExp1(self, ctx:CSELParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp2.
    def visitExp2(self, ctx:CSELParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp3.
    def visitExp3(self, ctx:CSELParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp4.
    def visitExp4(self, ctx:CSELParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp5.
    def visitExp5(self, ctx:CSELParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp6.
    def visitExp6(self, ctx:CSELParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp7.
    def visitExp7(self, ctx:CSELParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#array_cell.
    def visitArray_cell(self, ctx:CSELParser.Array_cellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#index_exp.
    def visitIndex_exp(self, ctx:CSELParser.Index_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#json_cell.
    def visitJson_cell(self, ctx:CSELParser.Json_cellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#json_key.
    def visitJson_key(self, ctx:CSELParser.Json_keyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#json.
    def visitJson(self, ctx:CSELParser.JsonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#jsonlist.
    def visitJsonlist(self, ctx:CSELParser.JsonlistContext):
        return self.visitChildren(ctx)



del CSELParser