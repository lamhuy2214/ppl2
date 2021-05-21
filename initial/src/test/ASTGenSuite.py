import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_var_1(self):
        """Simple program: int main() {} """
        input = """Let x:Number;"""
        expect = Program([VarDecl(Id("x"), None, NumberType(), None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_var_2(self):
        """Simple program: int main() {} """
        input = """Let x=5;"""
        expect = Program(
            [VarDecl(Id("x"), [], NoneType(), NumberLiteral(5.0))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_var_3(self):
        """Simple program: int main() {} """
        input = """Let x=True;"""
        expect = Program(
            [VarDecl(Id("x"), [], NoneType(), BooleanLiteral(True))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_var_4(self):
        """Simple program: int main() {} """
        input = """Let x:String="5";"""
        expect = Program(
            [VarDecl(Id("x"), [], StringType(), StringLiteral('5'))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_var_5(self):
        """Simple program: int main() {} """
        input = """Let x=[True,1,[2,5]];"""
        expect = Program([VarDecl(Id("x"), [], NoneType(), ArrayLiteral([BooleanLiteral(
            'true'), NumberLiteral(1.0), ArrayLiteral([NumberLiteral(2.0), NumberLiteral(5.0)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_var_6(self):
        """Simple program: int main() {} """
        input = """Let x[2]="5";"""
        expect = Program(
            [VarDecl(Id("x"), [NumberLiteral(2.0)], NoneType(), StringLiteral("5"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_var_7(self):
        """Simple program: int main() {} """
        input = """Let x[3,2]=[True,1,[2,5]];"""
        expect = Program([VarDecl(Id("x"), [NumberLiteral(3.0), NumberLiteral(2.0)], NoneType(), ArrayLiteral(
            [BooleanLiteral("True"), NumberLiteral("1.0"), ArrayLiteral([NumberLiteral("2.0"), NumberLiteral(5.0)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_var_8(self):
        """Simple program: int main() {} """
        input = """Let x:String="5";"""
        expect = Program(
            [VarDecl(Id("x"), [], StringType(), StringLiteral("5"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_var_9(self):
        """Simple program: int main() {} """
        input = """Let x:String="5",y;"""
        expect = Program([VarDecl(Id("x"), [], StringType(), StringLiteral(
            "5")), VarDecl(Id("y"), [], NoneType(), None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))
    # def test_var_10(self):
    #     """Simple program: int main() {} """
    #     input = """Let x[3,2]={name:"hao",age:21};"""
    #     expect = """Program([VarDecl(Id(x),[NumberLiteral(3),NumberLiteral(2)],NoneType,JSONLiteral((Key=name,Value=hao),(Key=age,Value=21))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_const_1(self):
        """Simple program: int main() {} """
        input = """Constant $x:Number=5;"""
        expect = Program(
            [ConstDecl(Id("$x"), [], NumberType(), NumberLiteral(5.0))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_const_2(self):
        """Simple program: int main() {} """
        input = """Constant $x=5;"""
        expect = Program(
            [ConstDecl(Id("$x"), [], NoneType(), NumberLiteral(5.0))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_const_3(self):
        """Simple program: int main() {} """
        input = """Constant $x=True;"""
        expect = Program(
            [ConstDecl(Id("$x"), [], NoneType(), BooleanLiteral("True"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_const_4(self):
        """Simple program: int main() {} """
        input = """Constant $x:String="5";"""
        expect = Program(
            [ConstDecl(Id("$x"), [], StringType(), StringLiteral("5"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_const_5(self):
        """Simple program: int main() {} """
        input = """Constant $x=[True,1,[2,5]];"""
        expect = Program([ConstDecl(Id("$x"), [], NoneType(), ArrayLiteral([BooleanLiteral(
            "True"), NumberLiteral("1.0"), ArrayLiteral([NumberLiteral("2.0"), NumberLiteral(5.0)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_const_6(self):
        """Simple program: int main() {} """
        input = """Constant $x[2]="5";"""
        expect = Program(
            [ConstDecl(Id("$x"), [NumberLiteral(2.0)], NoneType(), StringLiteral("5"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_const_7(self):
        """Simple program: int main() {} """
        input = """Constant $x[3,2]=[True,1,[2,5]];"""
        expect = Program([ConstDecl(Id("$x"), [NumberLiteral(3.0), NumberLiteral(2.0)], NoneType(), ArrayLiteral(
            [BooleanLiteral("True"), NumberLiteral(1.0), ArrayLiteral([NumberLiteral(2.0), NumberLiteral(5.0)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_const_8(self):
        """Simple program: int main() {} """
        input = """Constant $x:String="5";"""
        expect = Program(
            [ConstDecl(Id("$x"), [], StringType(), StringLiteral("5"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_const_9(self):
        """Simple program: int main() {} """
        input = """Constant $x:String="5",$y=[2,1];"""
        expect = Program([ConstDecl(Id("$x"), [], StringType(), StringLiteral("5")), ConstDecl(
            Id("$y"), [], NoneType(), ArrayLiteral([NumberLiteral(2.0), NumberLiteral(1.0)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_func_1(self):
        """Simple program: int main() {} """
        input = """Function main() {
            Let a;
            Constant $b = 12;
            a = 12;
        }"""
        expect = "Program([FuncDecl(Id(main)[],[VarDecl(Id(a),NoneType),ConstDecl(Id($b),NoneType,NumberLiteral(12.0))]),FuncDecl(Id(ma)[],[VarDecl(Id(c),NoneType),ConstDecl(Id($bds),NoneType,NumberLiteral(12.0))])])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))
