# Generated from main/csel/parser/CSEL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u01f3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\3\3\3\5\3\u0096")
        buf.write("\n\3\3\4\3\4\3\4\5\4\u009b\n\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\5\5\u00a3\n\5\3\6\3\6\5\6\u00a7\n\6\3\7\6\7\u00aa\n\7")
        buf.write("\r\7\16\7\u00ab\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u00b6")
        buf.write("\n\b\f\b\16\b\u00b9\13\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\7\t\u00c4\n\t\f\t\16\t\u00c7\13\t\3\t\3\t\3\n\3")
        buf.write("\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\5\17\u00d9\n\17\3\20\3\20\3\20\3\20\3\20\7\20\u00e0")
        buf.write("\n\20\f\20\16\20\u00e3\13\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\7\21\u00eb\n\21\f\21\16\21\u00ee\13\21\3\22\3\22")
        buf.write("\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3$")
        buf.write("\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\3*\3*\3*\3*\3*\3*\3+\3+\3+\3,\3,\3-\3-\3-\3.\3.\3/\3")
        buf.write("/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67")
        buf.write("\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3")
        buf.write("@\3A\3A\5A\u01a5\nA\3A\3A\3A\5A\u01aa\nA\5A\u01ac\nA\3")
        buf.write("B\3B\5B\u01b0\nB\3B\6B\u01b3\nB\rB\16B\u01b4\3C\3C\7C")
        buf.write("\u01b9\nC\fC\16C\u01bc\13C\3D\6D\u01bf\nD\rD\16D\u01c0")
        buf.write("\3E\3E\3E\3E\3E\3E\7E\u01c9\nE\fE\16E\u01cc\13E\3E\3E")
        buf.write("\3E\3F\3F\3F\3F\3F\3F\7F\u01d7\nF\fF\16F\u01da\13F\3F")
        buf.write("\3F\3F\3F\5F\u01e0\nF\3F\3F\3G\3G\3G\3G\3G\3G\7G\u01ea")
        buf.write("\nG\fG\16G\u01ed\13G\3G\3G\3H\3H\3H\3\u00c5\2I\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\2\25\2\27\2\31\2\33\2\35")
        buf.write("\13\37\f!\r#\16%\17\'\20)\21+\22-\23/\24\61\25\63\26\65")
        buf.write("\27\67\309\31;\32=\33?\34A\35C\36E\37G I!K\"M#O$Q%S&U")
        buf.write("\'W(Y)[*]+_,a-c.e/g\60i\61k\62m\63o\64q\65s\66u\67w8y")
        buf.write("9{:};\177<\u0081=\u0083\2\u0085\2\u0087\2\u0089>\u008b")
        buf.write("?\u008d@\u008fA\3\2\r\5\2\13\f\17\17\"\"\3\2%%\3\2C\\")
        buf.write("\3\2c|\3\2\62;\3\2\63;\4\2GGgg\4\2--//\t\2))^^ddhhppt")
        buf.write("tvv\6\2\f\f$$))^^\3\2$$\2\u0214\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\2\u0081\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2")
        buf.write("\u008d\3\2\2\2\2\u008f\3\2\2\2\3\u0091\3\2\2\2\5\u0095")
        buf.write("\3\2\2\2\7\u009a\3\2\2\2\t\u00a2\3\2\2\2\13\u00a6\3\2")
        buf.write("\2\2\r\u00a9\3\2\2\2\17\u00af\3\2\2\2\21\u00bf\3\2\2\2")
        buf.write("\23\u00ca\3\2\2\2\25\u00cc\3\2\2\2\27\u00ce\3\2\2\2\31")
        buf.write("\u00d0\3\2\2\2\33\u00d2\3\2\2\2\35\u00d8\3\2\2\2\37\u00da")
        buf.write("\3\2\2\2!\u00e4\3\2\2\2#\u00ef\3\2\2\2%\u00f1\3\2\2\2")
        buf.write("\'\u00f3\3\2\2\2)\u00f5\3\2\2\2+\u00f7\3\2\2\2-\u00f9")
        buf.write("\3\2\2\2/\u00fc\3\2\2\2\61\u0100\3\2\2\2\63\u0105\3\2")
        buf.write("\2\2\65\u010b\3\2\2\2\67\u0110\3\2\2\29\u0114\3\2\2\2")
        buf.write(";\u011d\3\2\2\2=\u0126\3\2\2\2?\u012b\3\2\2\2A\u0130\3")
        buf.write("\2\2\2C\u0137\3\2\2\2E\u013e\3\2\2\2G\u0146\3\2\2\2I\u014b")
        buf.write("\3\2\2\2K\u014f\3\2\2\2M\u0155\3\2\2\2O\u015e\3\2\2\2")
        buf.write("Q\u0161\3\2\2\2S\u0168\3\2\2\2U\u016e\3\2\2\2W\u0171\3")
        buf.write("\2\2\2Y\u0173\3\2\2\2[\u0176\3\2\2\2]\u0178\3\2\2\2_\u017b")
        buf.write("\3\2\2\2a\u017e\3\2\2\2c\u0180\3\2\2\2e\u0183\3\2\2\2")
        buf.write("g\u0186\3\2\2\2i\u0188\3\2\2\2k\u018a\3\2\2\2m\u018d\3")
        buf.write("\2\2\2o\u0190\3\2\2\2q\u0192\3\2\2\2s\u0194\3\2\2\2u\u0196")
        buf.write("\3\2\2\2w\u0198\3\2\2\2y\u019a\3\2\2\2{\u019c\3\2\2\2")
        buf.write("}\u019e\3\2\2\2\177\u01a0\3\2\2\2\u0081\u01a2\3\2\2\2")
        buf.write("\u0083\u01ad\3\2\2\2\u0085\u01b6\3\2\2\2\u0087\u01be\3")
        buf.write("\2\2\2\u0089\u01c2\3\2\2\2\u008b\u01d0\3\2\2\2\u008d\u01e3")
        buf.write("\3\2\2\2\u008f\u01f0\3\2\2\2\u0091\u0092\7$\2\2\u0092")
        buf.write("\4\3\2\2\2\u0093\u0096\5]/\2\u0094\u0096\5_\60\2\u0095")
        buf.write("\u0093\3\2\2\2\u0095\u0094\3\2\2\2\u0096\6\3\2\2\2\u0097")
        buf.write("\u009b\5\'\24\2\u0098\u009b\5)\25\2\u0099\u009b\5+\26")
        buf.write("\2\u009a\u0097\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u0099")
        buf.write("\3\2\2\2\u009b\b\3\2\2\2\u009c\u00a3\5c\62\2\u009d\u00a3")
        buf.write("\5e\63\2\u009e\u00a3\5g\64\2\u009f\u00a3\5i\65\2\u00a0")
        buf.write("\u00a3\5k\66\2\u00a1\u00a3\5m\67\2\u00a2\u009c\3\2\2\2")
        buf.write("\u00a2\u009d\3\2\2\2\u00a2\u009e\3\2\2\2\u00a2\u009f\3")
        buf.write("\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a1\3\2\2\2\u00a3\n")
        buf.write("\3\2\2\2\u00a4\u00a7\5\61\31\2\u00a5\u00a7\5\63\32\2\u00a6")
        buf.write("\u00a4\3\2\2\2\u00a6\u00a5\3\2\2\2\u00a7\f\3\2\2\2\u00a8")
        buf.write("\u00aa\t\2\2\2\u00a9\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2")
        buf.write("\u00ab\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad\3")
        buf.write("\2\2\2\u00ad\u00ae\b\7\2\2\u00ae\16\3\2\2\2\u00af\u00b0")
        buf.write("\7%\2\2\u00b0\u00b1\7%\2\2\u00b1\u00b7\3\2\2\2\u00b2\u00b6")
        buf.write("\n\3\2\2\u00b3\u00b4\7,\2\2\u00b4\u00b6\n\3\2\2\u00b5")
        buf.write("\u00b2\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00b9\3\2\2\2")
        buf.write("\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00ba\3")
        buf.write("\2\2\2\u00b9\u00b7\3\2\2\2\u00ba\u00bb\7%\2\2\u00bb\u00bc")
        buf.write("\7%\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00be\b\b\2\2\u00be")
        buf.write("\20\3\2\2\2\u00bf\u00c0\7%\2\2\u00c0\u00c1\7%\2\2\u00c1")
        buf.write("\u00c5\3\2\2\2\u00c2\u00c4\13\2\2\2\u00c3\u00c2\3\2\2")
        buf.write("\2\u00c4\u00c7\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c5\u00c3")
        buf.write("\3\2\2\2\u00c6\u00c8\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c8")
        buf.write("\u00c9\b\t\3\2\u00c9\22\3\2\2\2\u00ca\u00cb\7a\2\2\u00cb")
        buf.write("\24\3\2\2\2\u00cc\u00cd\t\4\2\2\u00cd\26\3\2\2\2\u00ce")
        buf.write("\u00cf\t\5\2\2\u00cf\30\3\2\2\2\u00d0\u00d1\t\6\2\2\u00d1")
        buf.write("\32\3\2\2\2\u00d2\u00d3\t\7\2\2\u00d3\34\3\2\2\2\u00d4")
        buf.write("\u00d9\5A!\2\u00d5\u00d9\5C\"\2\u00d6\u00d9\5E#\2\u00d7")
        buf.write("\u00d9\5G$\2\u00d8\u00d4\3\2\2\2\u00d8\u00d5\3\2\2\2\u00d8")
        buf.write("\u00d6\3\2\2\2\u00d8\u00d7\3\2\2\2\u00d9\36\3\2\2\2\u00da")
        buf.write("\u00e1\5\27\f\2\u00db\u00e0\5\23\n\2\u00dc\u00e0\5\25")
        buf.write("\13\2\u00dd\u00e0\5\27\f\2\u00de\u00e0\5\31\r\2\u00df")
        buf.write("\u00db\3\2\2\2\u00df\u00dc\3\2\2\2\u00df\u00dd\3\2\2\2")
        buf.write("\u00df\u00de\3\2\2\2\u00e0\u00e3\3\2\2\2\u00e1\u00df\3")
        buf.write("\2\2\2\u00e1\u00e2\3\2\2\2\u00e2 \3\2\2\2\u00e3\u00e1")
        buf.write("\3\2\2\2\u00e4\u00e5\7&\2\2\u00e5\u00ec\5\27\f\2\u00e6")
        buf.write("\u00eb\5\23\n\2\u00e7\u00eb\5\25\13\2\u00e8\u00eb\5\27")
        buf.write("\f\2\u00e9\u00eb\5\31\r\2\u00ea\u00e6\3\2\2\2\u00ea\u00e7")
        buf.write("\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea\u00e9\3\2\2\2\u00eb")
        buf.write("\u00ee\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2")
        buf.write("\u00ed\"\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ef\u00f0\7/\2")
        buf.write("\2\u00f0$\3\2\2\2\u00f1\u00f2\7-\2\2\u00f2&\3\2\2\2\u00f3")
        buf.write("\u00f4\7,\2\2\u00f4(\3\2\2\2\u00f5\u00f6\7\61\2\2\u00f6")
        buf.write("*\3\2\2\2\u00f7\u00f8\7\'\2\2\u00f8,\3\2\2\2\u00f9\u00fa")
        buf.write("\7-\2\2\u00fa\u00fb\7\60\2\2\u00fb.\3\2\2\2\u00fc\u00fd")
        buf.write("\7?\2\2\u00fd\u00fe\7?\2\2\u00fe\u00ff\7\60\2\2\u00ff")
        buf.write("\60\3\2\2\2\u0100\u0101\7V\2\2\u0101\u0102\7t\2\2\u0102")
        buf.write("\u0103\7w\2\2\u0103\u0104\7g\2\2\u0104\62\3\2\2\2\u0105")
        buf.write("\u0106\7H\2\2\u0106\u0107\7c\2\2\u0107\u0108\7n\2\2\u0108")
        buf.write("\u0109\7u\2\2\u0109\u010a\7g\2\2\u010a\64\3\2\2\2\u010b")
        buf.write("\u010c\7E\2\2\u010c\u010d\7c\2\2\u010d\u010e\7n\2\2\u010e")
        buf.write("\u010f\7n\2\2\u010f\66\3\2\2\2\u0110\u0111\7N\2\2\u0111")
        buf.write("\u0112\7g\2\2\u0112\u0113\7v\2\2\u01138\3\2\2\2\u0114")
        buf.write("\u0115\7E\2\2\u0115\u0116\7q\2\2\u0116\u0117\7p\2\2\u0117")
        buf.write("\u0118\7v\2\2\u0118\u0119\7k\2\2\u0119\u011a\7p\2\2\u011a")
        buf.write("\u011b\7w\2\2\u011b\u011c\7g\2\2\u011c:\3\2\2\2\u011d")
        buf.write("\u011e\7E\2\2\u011e\u011f\7q\2\2\u011f\u0120\7p\2\2\u0120")
        buf.write("\u0121\7u\2\2\u0121\u0122\7v\2\2\u0122\u0123\7c\2\2\u0123")
        buf.write("\u0124\7p\2\2\u0124\u0125\7v\2\2\u0125<\3\2\2\2\u0126")
        buf.write("\u0127\7G\2\2\u0127\u0128\7n\2\2\u0128\u0129\7u\2\2\u0129")
        buf.write("\u012a\7g\2\2\u012a>\3\2\2\2\u012b\u012c\7G\2\2\u012c")
        buf.write("\u012d\7n\2\2\u012d\u012e\7k\2\2\u012e\u012f\7h\2\2\u012f")
        buf.write("@\3\2\2\2\u0130\u0131\7P\2\2\u0131\u0132\7w\2\2\u0132")
        buf.write("\u0133\7o\2\2\u0133\u0134\7d\2\2\u0134\u0135\7g\2\2\u0135")
        buf.write("\u0136\7t\2\2\u0136B\3\2\2\2\u0137\u0138\7U\2\2\u0138")
        buf.write("\u0139\7v\2\2\u0139\u013a\7t\2\2\u013a\u013b\7k\2\2\u013b")
        buf.write("\u013c\7p\2\2\u013c\u013d\7i\2\2\u013dD\3\2\2\2\u013e")
        buf.write("\u013f\7D\2\2\u013f\u0140\7q\2\2\u0140\u0141\7q\2\2\u0141")
        buf.write("\u0142\7n\2\2\u0142\u0143\7g\2\2\u0143\u0144\7c\2\2\u0144")
        buf.write("\u0145\7p\2\2\u0145F\3\2\2\2\u0146\u0147\7L\2\2\u0147")
        buf.write("\u0148\7U\2\2\u0148\u0149\7Q\2\2\u0149\u014a\7P\2\2\u014a")
        buf.write("H\3\2\2\2\u014b\u014c\7H\2\2\u014c\u014d\7q\2\2\u014d")
        buf.write("\u014e\7t\2\2\u014eJ\3\2\2\2\u014f\u0150\7D\2\2\u0150")
        buf.write("\u0151\7t\2\2\u0151\u0152\7g\2\2\u0152\u0153\7c\2\2\u0153")
        buf.write("\u0154\7m\2\2\u0154L\3\2\2\2\u0155\u0156\7H\2\2\u0156")
        buf.write("\u0157\7w\2\2\u0157\u0158\7p\2\2\u0158\u0159\7e\2\2\u0159")
        buf.write("\u015a\7v\2\2\u015a\u015b\7k\2\2\u015b\u015c\7q\2\2\u015c")
        buf.write("\u015d\7p\2\2\u015dN\3\2\2\2\u015e\u015f\7K\2\2\u015f")
        buf.write("\u0160\7h\2\2\u0160P\3\2\2\2\u0161\u0162\7T\2\2\u0162")
        buf.write("\u0163\7g\2\2\u0163\u0164\7v\2\2\u0164\u0165\7w\2\2\u0165")
        buf.write("\u0166\7t\2\2\u0166\u0167\7p\2\2\u0167R\3\2\2\2\u0168")
        buf.write("\u0169\7Y\2\2\u0169\u016a\7j\2\2\u016a\u016b\7k\2\2\u016b")
        buf.write("\u016c\7n\2\2\u016c\u016d\7g\2\2\u016dT\3\2\2\2\u016e")
        buf.write("\u016f\7K\2\2\u016f\u0170\7p\2\2\u0170V\3\2\2\2\u0171")
        buf.write("\u0172\7\60\2\2\u0172X\3\2\2\2\u0173\u0174\7Q\2\2\u0174")
        buf.write("\u0175\7h\2\2\u0175Z\3\2\2\2\u0176\u0177\7#\2\2\u0177")
        buf.write("\\\3\2\2\2\u0178\u0179\7(\2\2\u0179\u017a\7(\2\2\u017a")
        buf.write("^\3\2\2\2\u017b\u017c\7~\2\2\u017c\u017d\7~\2\2\u017d")
        buf.write("`\3\2\2\2\u017e\u017f\7?\2\2\u017fb\3\2\2\2\u0180\u0181")
        buf.write("\7?\2\2\u0181\u0182\7?\2\2\u0182d\3\2\2\2\u0183\u0184")
        buf.write("\7#\2\2\u0184\u0185\7?\2\2\u0185f\3\2\2\2\u0186\u0187")
        buf.write("\7>\2\2\u0187h\3\2\2\2\u0188\u0189\7@\2\2\u0189j\3\2\2")
        buf.write("\2\u018a\u018b\7>\2\2\u018b\u018c\7?\2\2\u018cl\3\2\2")
        buf.write("\2\u018d\u018e\7@\2\2\u018e\u018f\7?\2\2\u018fn\3\2\2")
        buf.write("\2\u0190\u0191\7=\2\2\u0191p\3\2\2\2\u0192\u0193\7<\2")
        buf.write("\2\u0193r\3\2\2\2\u0194\u0195\7.\2\2\u0195t\3\2\2\2\u0196")
        buf.write("\u0197\7}\2\2\u0197v\3\2\2\2\u0198\u0199\7\177\2\2\u0199")
        buf.write("x\3\2\2\2\u019a\u019b\7*\2\2\u019bz\3\2\2\2\u019c\u019d")
        buf.write("\7+\2\2\u019d|\3\2\2\2\u019e\u019f\7]\2\2\u019f~\3\2\2")
        buf.write("\2\u01a0\u01a1\7_\2\2\u01a1\u0080\3\2\2\2\u01a2\u01ab")
        buf.write("\5\u0087D\2\u01a3\u01a5\5\u0085C\2\u01a4\u01a3\3\2\2\2")
        buf.write("\u01a4\u01a5\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01ac\5")
        buf.write("\u0083B\2\u01a7\u01a9\5\u0085C\2\u01a8\u01aa\5\u0083B")
        buf.write("\2\u01a9\u01a8\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ac")
        buf.write("\3\2\2\2\u01ab\u01a4\3\2\2\2\u01ab\u01a7\3\2\2\2\u01ab")
        buf.write("\u01ac\3\2\2\2\u01ac\u0082\3\2\2\2\u01ad\u01af\t\b\2\2")
        buf.write("\u01ae\u01b0\t\t\2\2\u01af\u01ae\3\2\2\2\u01af\u01b0\3")
        buf.write("\2\2\2\u01b0\u01b2\3\2\2\2\u01b1\u01b3\5\31\r\2\u01b2")
        buf.write("\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b2\3\2\2\2")
        buf.write("\u01b4\u01b5\3\2\2\2\u01b5\u0084\3\2\2\2\u01b6\u01ba\5")
        buf.write("W,\2\u01b7\u01b9\5\31\r\2\u01b8\u01b7\3\2\2\2\u01b9\u01bc")
        buf.write("\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb")
        buf.write("\u0086\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd\u01bf\5\31\r")
        buf.write("\2\u01be\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01be")
        buf.write("\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u0088\3\2\2\2\u01c2")
        buf.write("\u01ca\7$\2\2\u01c3\u01c4\7)\2\2\u01c4\u01c9\7$\2\2\u01c5")
        buf.write("\u01c6\7^\2\2\u01c6\u01c9\t\n\2\2\u01c7\u01c9\n\13\2\2")
        buf.write("\u01c8\u01c3\3\2\2\2\u01c8\u01c5\3\2\2\2\u01c8\u01c7\3")
        buf.write("\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8\3\2\2\2\u01ca\u01cb")
        buf.write("\3\2\2\2\u01cb\u01cd\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cd")
        buf.write("\u01ce\7$\2\2\u01ce\u01cf\bE\4\2\u01cf\u008a\3\2\2\2\u01d0")
        buf.write("\u01d8\7$\2\2\u01d1\u01d2\7)\2\2\u01d2\u01d7\7$\2\2\u01d3")
        buf.write("\u01d4\7^\2\2\u01d4\u01d7\t\n\2\2\u01d5\u01d7\n\13\2\2")
        buf.write("\u01d6\u01d1\3\2\2\2\u01d6\u01d3\3\2\2\2\u01d6\u01d5\3")
        buf.write("\2\2\2\u01d7\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8\u01d9")
        buf.write("\3\2\2\2\u01d9\u01df\3\2\2\2\u01da\u01d8\3\2\2\2\u01db")
        buf.write("\u01dc\7^\2\2\u01dc\u01e0\n\n\2\2\u01dd\u01de\7)\2\2\u01de")
        buf.write("\u01e0\n\f\2\2\u01df\u01db\3\2\2\2\u01df\u01dd\3\2\2\2")
        buf.write("\u01e0\u01e1\3\2\2\2\u01e1\u01e2\bF\5\2\u01e2\u008c\3")
        buf.write("\2\2\2\u01e3\u01eb\7$\2\2\u01e4\u01e5\7)\2\2\u01e5\u01ea")
        buf.write("\7$\2\2\u01e6\u01e7\7^\2\2\u01e7\u01ea\t\n\2\2\u01e8\u01ea")
        buf.write("\n\13\2\2\u01e9\u01e4\3\2\2\2\u01e9\u01e6\3\2\2\2\u01e9")
        buf.write("\u01e8\3\2\2\2\u01ea\u01ed\3\2\2\2\u01eb\u01e9\3\2\2\2")
        buf.write("\u01eb\u01ec\3\2\2\2\u01ec\u01ee\3\2\2\2\u01ed\u01eb\3")
        buf.write("\2\2\2\u01ee\u01ef\bG\6\2\u01ef\u008e\3\2\2\2\u01f0\u01f1")
        buf.write("\13\2\2\2\u01f1\u01f2\bH\7\2\u01f2\u0090\3\2\2\2\36\2")
        buf.write("\u0095\u009a\u00a2\u00a6\u00ab\u00b5\u00b7\u00c5\u00d8")
        buf.write("\u00df\u00e1\u00ea\u00ec\u01a4\u01a9\u01ab\u01af\u01b4")
        buf.write("\u01ba\u01c0\u01c8\u01ca\u01d6\u01d8\u01df\u01e9\u01eb")
        buf.write("\b\b\2\2\3\t\2\3E\3\3F\4\3G\5\3H\6")
        return buf.getvalue()


class CSELLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    LOGICAL_OP = 2
    MULTIPLYING = 3
    RL_OP = 4
    BOOLEAN_LITERAL = 5
    WS = 6
    COMMENT = 7
    UNTERMINATED_COMMENT = 8
    Typ = 9
    ID = 10
    ID_const = 11
    SUB = 12
    ADD = 13
    MUL = 14
    DIV = 15
    MOD = 16
    SADD = 17
    SEQ = 18
    TRUE = 19
    FALSE = 20
    CALL = 21
    LET = 22
    CONTINUE = 23
    CONSTANT = 24
    ELSE = 25
    ELSEIF = 26
    Number = 27
    String = 28
    Boolean = 29
    JSON = 30
    FOR = 31
    BREAK = 32
    FUNCTION = 33
    IF = 34
    RETURN = 35
    WHILE = 36
    IN = 37
    DOT = 38
    OF = 39
    NEGATION = 40
    CONJUNCTION = 41
    DISJUNCTION = 42
    ASSIGN = 43
    EQUAL = 44
    NOTEQUAL = 45
    LESSTHAN = 46
    GREATERTHAN = 47
    LESSTHAN_EQUAL = 48
    GREATERTHAN_EQUAL = 49
    SEMI = 50
    COLON = 51
    COMMA = 52
    LB = 53
    RB = 54
    LP = 55
    RP = 56
    LSB = 57
    RSB = 58
    NUM_LITERAL = 59
    STRING_LITERAL = 60
    ILLEGAL_ESCAPE = 61
    UNCLOSE_STRING = 62
    ERROR_CHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\"'", "'-'", "'+'", "'*'", "'/'", "'%'", "'+.'", "'==.'", 
            "'True'", "'False'", "'Call'", "'Let'", "'Continue'", "'Constant'", 
            "'Else'", "'Elif'", "'Number'", "'String'", "'Boolean'", "'JSON'", 
            "'For'", "'Break'", "'Function'", "'If'", "'Return'", "'While'", 
            "'In'", "'.'", "'Of'", "'!'", "'&&'", "'||'", "'='", "'=='", 
            "'!='", "'<'", "'>'", "'<='", "'>='", "';'", "':'", "','", "'{'", 
            "'}'", "'('", "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "LOGICAL_OP", "MULTIPLYING", "RL_OP", "BOOLEAN_LITERAL", "WS", 
            "COMMENT", "UNTERMINATED_COMMENT", "Typ", "ID", "ID_const", 
            "SUB", "ADD", "MUL", "DIV", "MOD", "SADD", "SEQ", "TRUE", "FALSE", 
            "CALL", "LET", "CONTINUE", "CONSTANT", "ELSE", "ELSEIF", "Number", 
            "String", "Boolean", "JSON", "FOR", "BREAK", "FUNCTION", "IF", 
            "RETURN", "WHILE", "IN", "DOT", "OF", "NEGATION", "CONJUNCTION", 
            "DISJUNCTION", "ASSIGN", "EQUAL", "NOTEQUAL", "LESSTHAN", "GREATERTHAN", 
            "LESSTHAN_EQUAL", "GREATERTHAN_EQUAL", "SEMI", "COLON", "COMMA", 
            "LB", "RB", "LP", "RP", "LSB", "RSB", "NUM_LITERAL", "STRING_LITERAL", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "LOGICAL_OP", "MULTIPLYING", "RL_OP", "BOOLEAN_LITERAL", 
                  "WS", "COMMENT", "UNTERMINATED_COMMENT", "UNDERSCORES", 
                  "UPPER", "LOWER", "DIGIT", "DIGIT_EX0", "Typ", "ID", "ID_const", 
                  "SUB", "ADD", "MUL", "DIV", "MOD", "SADD", "SEQ", "TRUE", 
                  "FALSE", "CALL", "LET", "CONTINUE", "CONSTANT", "ELSE", 
                  "ELSEIF", "Number", "String", "Boolean", "JSON", "FOR", 
                  "BREAK", "FUNCTION", "IF", "RETURN", "WHILE", "IN", "DOT", 
                  "OF", "NEGATION", "CONJUNCTION", "DISJUNCTION", "ASSIGN", 
                  "EQUAL", "NOTEQUAL", "LESSTHAN", "GREATERTHAN", "LESSTHAN_EQUAL", 
                  "GREATERTHAN_EQUAL", "SEMI", "COLON", "COMMA", "LB", "RB", 
                  "LP", "RP", "LSB", "RSB", "NUM_LITERAL", "EXPONENT_PART", 
                  "DECIMAL_PART", "INT_PART", "STRING_LITERAL", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "CSEL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[7] = self.UNTERMINATED_COMMENT_action 
            actions[67] = self.STRING_LITERAL_action 
            actions[68] = self.ILLEGAL_ESCAPE_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[70] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    raise UnterminatedComment()
                    
     

    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:


                            self.text = self.text[1:-1]
                    
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                                    raise IllegalEscape(self.text[1:])
                            
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                                    raise UncloseString(self.text[1:])
                            
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                    raise ErrorToken(self.text)
                    
     


