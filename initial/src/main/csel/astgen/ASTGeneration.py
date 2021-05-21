from CSELVisitor import CSELVisitor
from CSELParser import CSELParser
from AST import *
from main.csel.utils.AST import ArrayAccess, BooleanType, ForIn, ForOf, NumberType, StringType


class ASTGeneration(CSELVisitor):

    def visitProgram(self, ctx: CSELParser.ProgramContext):
        return Program(self.visit(ctx.many_var_declare()) + self.visit(ctx.many_const_declare()) + self.visit(ctx.many_func_declare()))

    def visitMany_var_declare(self, ctx: CSELParser.Many_var_declareContext):
        if ctx.getChildCount() == 0:
            return []
        elif ctx.getChildCount() == 1:
            return self.visit(ctx.one_var_declare())
        else:
            return self.visit(ctx.one_var_declare()) + self.visit(ctx.many_var_declare())

    def visitOne_var_declare(self, ctx: CSELParser.One_var_declareContext):
        return self.visit(ctx.id_list())

    def visitMany_const_declare(self, ctx: CSELParser.Many_const_declareContext):
        if ctx.getChildCount() == 0:
            return []
        elif ctx.getChildCount() == 1:
            return self.visit(ctx.one_const_declare())
        else:
            return self.visit(ctx.one_const_declare()) + self.visit(ctx.many_const_declare())

    def visitOne_const_declare(self, ctx: CSELParser.One_const_declareContext):
        return self.visit(ctx.id_list_const())

    def visitId_list_const(self, ctx: CSELParser.Id_list_constContext):
        if ctx.id_list_const():
            return self.visit(ctx.id_list_element_const()) + self.visit(ctx.id_list_const())
        else:
            return self.visit(ctx.id_list_element_const())

    def visitId_list_element_const(self, ctx: CSELParser.Id_list_element_constContext):
        id = Id(ctx.ID_const().getText())
        if ctx.composit():
            dimen = self.visit(ctx.composit())
        else:
            dimen = []
        if ctx.Typ():
            typq = ctx.Typ().getText()
            if typq == 'Number':
                typ = NumberType()
            elif typq == 'Boolean':
                typ = BooleanType()
            elif typq == 'String':
                typ = StringType()
            elif typq == 'JSON':
                typ = JSONType()
        else:
            typ = NoneType()
        if ctx.ASSIGN():
            if ctx.array_literal():
                literal = self.visit(ctx.array_literal())
            else:
                literal = self.visit(ctx.literal())
        else:
            literal = []
        return [ConstDecl(id, dimen, typ, literal)]

    def visitId_list(self, ctx: CSELParser.Id_listContext):
        if ctx.id_list():
            return self.visit(ctx.id_list_element()) + self.visit(ctx.id_list())
        else:
            return self.visit(ctx.id_list_element())

    def visitId_list_element(self, ctx: CSELParser.Id_list_elementContext):
        id = Id(ctx.ID().getText())
        if ctx.composit():
            dimen = self.visit(ctx.composit())
        else:
            dimen = []
        if ctx.Typ():
            typq = ctx.Typ().getText()
            if typq == 'Number':
                typ = NumberType()
            elif typq == 'Boolean':
                typ = BooleanType()
            elif typq == 'String':
                typ = StringType()
            elif typq == 'JSON':
                typ = JSONType()
        else:
            typ = NoneType()
        if ctx.ASSIGN():
            if ctx.array_literal():
                literal = self.visit(ctx.array_literal())
            else:
                literal = self.visit(ctx.literal())
        else:
            literal = []
        return [VarDecl(id, dimen, typ, literal)]

    def visitComposit(self, ctx: CSELParser.CompositContext):
        if ctx.NUM_LITERAL():
            intlist = ctx.NUM_LITERAL()
            lst = []
            for j in intlist:
                i = j.getText()
                lst += [i]
            dimen = list(map(lambda x: NumberLiteral(float(x)), lst))
        else:
            dimen = []
        return dimen

    def visitMany_func_declare(self, ctx: CSELParser.Many_func_declareContext):
        if ctx.one_func_declare():
            if ctx.many_func_declare():
                return self.visit(ctx.one_func_declare()) + self.visit(ctx.many_func_declare())
            return self.visit(ctx.one_func_declare())
        else:
            return []

    def visitOne_func_declare(self, ctx: CSELParser.One_func_declareContext):
        func_name = Id(ctx.ID().getText())
        if ctx.parameter_name():
            param_list = self.visit(ctx.parameter_name())
        else:
            param_list = []
        var_list = self.visit(ctx.many_var_declare())
        const_list = self.visit(ctx.many_const_declare())
        stm_list = self.visit(ctx.many_stm())
        body = var_list + const_list + stm_list
        return [FuncDecl(func_name, param_list, body)]

    def visitParameter_name(self, ctx: CSELParser.Parameter_nameContext):
        if ctx.parameter_name():
            return self.visit(ctx.param_list_element()) + self.visit(ctx.parameter_name())
        else:
            return self.visit(ctx.param_list_element())

    def visitParam_list_element(self, ctx: CSELParser.Param_list_elementContext):
        id = Id(ctx.ID().getText())
        dimen = []

        typ = NoneType()
        if ctx.composit():
            dimen = self.visit(ctx.composit())
        return [VarDecl(id, dimen, typ, None)]

    def visitMany_stm(self, ctx: CSELParser.Many_stmContext):
        if ctx.stm():
            if ctx.many_stm():
                return self.visit(ctx.stm()) + self.visit(ctx.many_stm())
            return self.visit(ctx.stm())
        return []

    def visitStm(self, ctx: CSELParser.StmContext):
        if ctx.assign_stm():
            return self.visit(ctx.assign_stm())
        if ctx.call_stm():
            return self.visit(ctx.call_stm())
        if ctx.return_stm():
            return self.visit(ctx.return_stm())
        if ctx.if_stm():
            return self.visit(ctx.if_stm())
        if ctx.break_stm():
            return self.visit(ctx.break_stm())
        if ctx.continue_stm():
            return self.visit(ctx.continue_stm())
        if ctx.while_stm():
            return self.visit(ctx.while_stm())
        if ctx.forin_stm():
            return self.visit(ctx.forin_stm())
        if ctx.forof_stm():
            return self.visit(ctx.forof_stm())

    def visitAssign_stm(self, ctx: CSELParser.Assign_stmContext):
        lhs = []
        rhs = []
        if (ctx.array_cell()):
            lhs = self.visit(ctx.array_cell())
        elif ctx.json_cell():
            lhs = self.visit(ctx.json_cell())
        else:
            lhs = Id(ctx.ID().getText())
        rhs = self.visit(ctx.exp())
        return [Assign(lhs, rhs)]

    def visitCall_stm(self, ctx: CSELParser.Call_stmContext):
        id = Id(ctx.ID().getText())
        lst = []
        if ctx.exp():
            for i in range(len(ctx.exp())):
                lst += [self.visit(ctx.exp(i))]
        else:
            lst = []

        return [CallStmt(id, lst)]

    def visitFunction_call(self, ctx: CSELParser.Function_callContext):
        id = Id(ctx.ID().getText())
        param = []
        if ctx.exp():
            for i in range(len(ctx.exp())):
                param += [self.visit(ctx.exp(i))]
        else:
            param = []

        return CallExpr(id, param)

    def visitReturn_stm(self, ctx: CSELParser.Return_stmContext):
        if ctx.exp():
            return [Return(self.visit(ctx.exp()))]
        else:
            return [Return(None)]

    def visitBreak_stm(self, ctx: CSELParser.Break_stmContext):
        return [Break()]

    def visitContinue_stm(self, ctx: CSELParser.Continue_stmContext):
        return [Continue()]

    def visitIf_stm(self, ctx: CSELParser.If_stmContext):
        manyelseif = []
        if ctx.many_elseif():

            for i in range(len(ctx.many_elseif())):

                manyelseif += [self.visit(ctx.many_elseif(i))]
            ifthenStm = [self.visit(ctx.if_then())] + manyelseif
        else:
            ifthenStm = [self.visit(ctx.if_then())]
        if ctx.else_part():
            elseStm = self.visit(ctx.else_part())
        else:
            elseStm = ([], [])

        return [If(ifthenStm, elseStm)]

    def visitIf_then(self, ctx: CSELParser.If_thenContext):
        exp = self.visit(ctx.exp())
        list_var_decleare = self.visit(ctx.many_var_declare())
        list_stm = self.visit(ctx.many_stm())
        return (exp, list_var_decleare, list_stm)

    def visitMany_elseif(self, ctx: CSELParser.Many_elseifContext):
        exp = self.visit(ctx.exp())
        list_var_decleare = self.visit(ctx.many_var_declare())
        list_stm = self.visit(ctx.many_stm())
        return (exp, list_var_decleare, list_stm)

    def visitElse_part(self, ctx: CSELParser.Else_partContext):
        return (self.visit(ctx.many_var_declare()), self.visit(ctx.many_stm()))

    def visitWhile_stm(self, ctx: CSELParser.While_stmContext):
        exp = self.visit(ctx.exp())
        sl = (self.visit(ctx.many_var_declare()), self.visit(ctx.many_stm()))
        return [While(exp, sl)]

    def visitForin_stm(self, ctx: CSELParser.Forin_stmContext):
        id = Id(ctx.ID().getText())
        expr = self.visit(ctx.exp())
        loop = (self.visit(ctx.many_var_declare()), self.visit(ctx.many_stm()))
        return [ForIn(id, expr, loop)]

    def visitForof_stm(self, ctx: CSELParser.Forof_stmContext):
        id = Id(ctx.ID().getText())
        expr = self.visit(ctx.exp())
        loop = (self.visit(ctx.many_var_declare()), self.visit(ctx.many_stm()))
        return [ForOf(id, expr, loop)]

    def visitExp(self, ctx: CSELParser.ExpContext):
        # BinaryOP:
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp1(0))
        else:
            left = self.visit(ctx.exp1(0))
            right = self.visit(ctx.exp1(1))
            return BinaryOp(ctx.getChild(1).getText(), left, right)

    def visitExp1(self, ctx: CSELParser.Exp1Context):
        # BinaryOP:
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp2(0))
        else:
            left = self.visit(ctx.exp2(0))
            right = self.visit(ctx.exp2(1))
            return BinaryOp(ctx.getChild(1).getText(), left, right)

    def visitExp2(self, ctx: CSELParser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp3())
        else:
            left = self.visit(ctx.exp2())
            right = self.visit(ctx.exp3())
            return BinaryOp(ctx.getChild(1).getText(), left, right)

    def visitExp3(self, ctx: CSELParser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4())
        else:
            left = self.visit(ctx.exp3())
            right = self.visit(ctx.exp4())
            return BinaryOp(ctx.getChild(1).getText(), left, right)

    def visitExp4(self, ctx: CSELParser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5())
        else:
            left = self.visit(ctx.exp4())
            right = self.visit(ctx.exp5())
            return BinaryOp(ctx.getChild(1).getText(), left, right)

    def visitExp5(self, ctx: CSELParser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5())
        return UnaryOp(ctx.NEGATION().getText(), self.visit(ctx.exp5()))

    def visitExp6(self, ctx: CSELParser.Exp6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp7())
        return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.exp6()))

    def visitExp7(self, ctx: CSELParser.Exp7Context):
        if ctx.array_literal():
            return self.visit(ctx.array_literal())
        if ctx.literal():
            return self.visit(ctx.literal())
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.function_call():
            return self.visit(ctx.function_call())
        if ctx.array_cell():
            return self.visit(ctx.array_cell())
        if ctx.exp():
            return self.visit(ctx.exp())
        if ctx.ID_const():
            return Id(ctx.ID_const().getText())
        if ctx.json_cell():
            return self.visit(ctx.json_cell())

    def visitArray_cell(self, ctx: CSELParser.Array_cellContext):
        lelf = []
        if ctx.ID():
            lelf = Id(ctx.ID().getText())
        if ctx.function_call():
            lelf = self.visit(ctx.function_call())
        if ctx.exp():
            lelf = self.visit(ctx.exp())
        return ArrayAccess(lelf, self.visit(ctx.index_exp()))

    def visitJson_cell(self, ctx: CSELParser.Json_cellContext):
        lelf = []
        if ctx.ID():
            lelf = Id(ctx.ID().getText())
        if ctx.function_call():
            lelf = self.visit(ctx.function_call())
        if ctx.exp():
            lelf = self.visit(ctx.exp())
        return ArrayCell(lelf, self.visit(ctx.index_exp()))

    def visitIndex_exp(self, ctx: CSELParser.Index_expContext):
        if ctx.index_exp():
            return [self.visit(ctx.exp())] + self.visit(ctx.index_exp())
        else:
            return [self.visit(ctx.exp())]

    # LITERAL_______________________________________________________________________

    def visitArray_literal(self, ctx: CSELParser.Array_literalContext):
        lst = []
        for i in range(len(ctx.array_literal_element())):
            lst += self.visit(ctx.array_literal_element(i))
        return ArrayLiteral(lst)

    def visitArray_literal_element(self, ctx: CSELParser.Array_literal_elementContext):
        if ctx.literal():
            return [self.visit(ctx.literal())]
        else:
            return [self.visit(ctx.array_literal())]

    def visitLiteral(self, ctx: CSELParser.LiteralContext):
        if ctx.NUM_LITERAL():
            return NumberLiteral(float(ctx.NUM_LITERAL().getText()))
        if ctx.BOOLEAN_LITERAL():
            return BooleanLiteral(ctx.BOOLEAN_LITERAL().getText())
        if ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        if ctx.json():
            return JSONLiteral(ctx.json().getText())
