# From MrCopperrrr
import unittest
from TestUtils import TestUtils
from SymbolTable import simulate # import để debug print(simulate(input))


class TestSymbolTable(unittest.TestCase):

    def test_1(self):
        input = ["INSERT a number"] 
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 101))

    def test_2(self):
        input = ["INSERT a number", 
                "INSERT b string"
        ]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 102))

    def test_3(self):
        input = ["INSERT a number",
                 "INSERT a number" 
        ]
        expected = ["Redeclared: INSERT a number"]
        self.assertTrue(TestUtils.check(input, expected, 103))

    def test_4(self):
        input = ["INSERT x number", 
                "BEGIN", 
                "INSERT x number", 
                "END"
        ]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 104))

    def test_5(self):
        input = ["INSERT x number", 
                 "INSERT x string"
        ]
        expected = ["Redeclared: INSERT x string"]
        self.assertTrue(TestUtils.check(input, expected, 105))

    def test_6(self):
        input = ["INSERT a1 number", 
                 "INSERT b2 string", 
                 "INSERT c3 number", 
                 "INSERT d4 string"
        ]
        expected = ["success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 106))

    def test_7(self):
        input = ["INSERT a_B1 number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 107))

    def test_8(self):
        input = ["INSERT x number", 
                 "BEGIN", 
                 "INSERT x number", 
                 "END"
        ]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 108))

    def test_9(self):
        input = [
            "INSERT y string", 
            "INSERT y string"
        ]
        expected = ["Redeclared: INSERT y string"]
        self.assertTrue(TestUtils.check(input, expected, 109))

    def test_10(self):
        input = [
            "INSERT a number",
            "BEGIN",
            "INSERT b string",
            "BEGIN",
            "INSERT c number",
        ]
        expected = ["UnclosedBlock: 2"]
        self.assertTrue(TestUtils.check(input, expected, 110))

    def test_11(self):
        input = [
            "INSERT x number",
            "INSERT x string"
        ]
        expected = ["Redeclared: INSERT x string"]
        self.assertTrue(TestUtils.check(input, expected, 111))

    def test_12(self):
        input = [
            "INSERT x number",
            "BEGIN",
            "INSERT x string"
        ]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 112))

    def test_13(self):
        input = [
            "INSERT x number",
            "BEGIN",
            "BEGIN",
            "INSERT x string",
            "END"
        ]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 113))

    def test_14(self):
        input = [
            "INSERT x number",
            "INSERT y number",
            "INSERT z number"
        ]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 114))

    def test_15(self):
        input = [
            "BEGIN",
            "INSERT x number",
            "END"
        ]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 115))

    def test_16(self):
        input = [
            "BEGIN",
            "INSERT x number"
        ]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 116))

    def test_17(self):
        input = [
            "ASSIGN x 10"
        ]
        expected = ["Undeclared: ASSIGN x 10"]
        self.assertTrue(TestUtils.check(input, expected, 117))

    def test_18(self):
        input = [
            "INSERT x number",
            "ASSIGN x 100"
        ]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 118))

    def test_19(self):
        input = [
            "INSERT x number",
            "ASSIGN x 'hello'"
        ]
        expected = ["TypeMismatch: ASSIGN x 'hello'"]
        self.assertTrue(TestUtils.check(input, expected, 119))

    def test_20(self):
        input = [
            "INSERT s string",
            "ASSIGN s 'abc'"
        ]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 120))

    def test_21(self):
        input = [
            "INSERT s string",
            "ASSIGN s 123"
        ]
        expected = ["TypeMismatch: ASSIGN s 123"]
        self.assertTrue(TestUtils.check(input, expected, 121))

    def test_22(self):
        input = [
            "ASSIGN y 'hello'"
        ]
        expected = ["Undeclared: ASSIGN y 'hello'"]
        self.assertTrue(TestUtils.check(input, expected, 122))

    def test_23(self):
        input = [
            "INSERT a number",
            "INSERT b number",
            "ASSIGN a 10",
            "ASSIGN b a"
        ]
        expected = ["success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 123))

    def test_24(self):
        input = [
            "INSERT a string",
            "INSERT z number",
            "ASSIGN a 123"
        ]
        expected = ["TypeMismatch: ASSIGN a 123"]
        self.assertTrue(TestUtils.check(input, expected, 124))

    def test_25(self):
        input = [
            "INSERT a number",
            "ASSIGN a 'b'"
        ]
        expected = ["TypeMismatch: ASSIGN a 'b'"]
        self.assertTrue(TestUtils.check(input, expected, 125))

    def test_26(self):
        input = [
            "INSERT x number",
            "BEGIN",
            "ASSIGN x 5"
        ]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 126))

    def test_27(self):
        input = [
            "INSERT x string",
            "BEGIN",
            "BEGIN",
            "ASSIGN x 'a'"
        ]
        expected = ["UnclosedBlock: 2"]
        self.assertTrue(TestUtils.check(input, expected, 127))

    def test_28(self):
        input = [
            "INSERT s string",
            "ASSIGN s ''"
        ]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 128))

    def test_29(self):
        input = [
            "INSERT n number",
            "ASSIGN n 999"
        ]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 129))

    def test_30(self):
        input = [
            "BEGIN",
            "END"
        ]
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 130))

    def test_31(self):
        input = [
            "BEGIN",
            "BEGIN",
            "END",
            "END"
        ]
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 131))

    def test_32(self):
        input = [
            "BEGIN",
            "INSERT x number"
        ]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 132))

    def test_33(self):
        input = [
            "BEGIN",
            "BEGIN",
            "END"
        ]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 133))

    def test_34(self):
        input = [
            "END"
        ]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 134))

    def test_35(self):
        input = [
            "BEGIN",
            "INSERT x number",
            "END"
        ]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 135))

    def test_36(self):
        input = [
            "INSERT x number",
            "INSERT x string"
        ]
        expected = ["Redeclared: INSERT x string"]
        self.assertTrue(TestUtils.check(input, expected, 136))

    def test_37(self):
        input = [
            "INSERT x number",
            "BEGIN",
            "INSERT x number"
        ]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 137))

    def test_38(self):
        input = [
            "BEGIN",
            "INSERT y string",
            "INSERT y string"
        ]
        expected = ["Redeclared: INSERT y string"]
        self.assertTrue(TestUtils.check(input, expected, 138))

    def test_39(self):
        input = [
            "BEGIN",
            "INSERT tmp number",
            "END",
            "LOOKUP tmp"
        ]
        expected = ["Undeclared: LOOKUP tmp"]
        self.assertTrue(TestUtils.check(input, expected, 139))

    def test_40(self):
        input = [
            "INSERT a number",
            "LOOKUP a"
        ]
        expected = ["success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 140))

    def test_41(self):
        input = [
            "LOOKUP b"
        ]
        expected = ["Undeclared: LOOKUP b"]
        self.assertTrue(TestUtils.check(input, expected, 141))

    def test_42(self):
        input = [
            "BEGIN",
            "INSERT x number",
            "LOOKUP x"
        ]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 142))

    def test_43(self):
        input = [
            "INSERT x number",
            "BEGIN",
            "LOOKUP x"
        ]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 143))

    def test_44(self):
        input = [
            "INSERT a number",
            "BEGIN",
            "INSERT a number",
            "INSERT b string",
            "PRINT",
            "END"
        ]
        expected = ["success", "success", "success", "a//1 b//1"]
        self.assertTrue(TestUtils.check(input, expected, 144))

    def test_45(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "PRINT"
        ]
        expected = ["success", "success", "x//0 y//0"]
        self.assertTrue(TestUtils.check(input, expected, 145))

    def test_46(self):
        input = [
            "INSERT a number",
            "BEGIN",
            "INSERT a string",
            "INSERT b number",
            "RPRINT",
            "END"
        ]
        expected = ["success", "success", "success", "b//1 a//1"]
        self.assertTrue(TestUtils.check(input, expected, 146))

    def test_47(self):
        input = [
            "PRINT"
        ]
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 147))

    def test_48(self):
        input = [
            "RPRINT"
        ]
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 148))

    def test_49(self):
        input = [
            "BEGIN",
            "INSERT x number",
            "END",
            "LOOKUP x"
        ]
        expected = ["Undeclared: LOOKUP x"]
        self.assertTrue(TestUtils.check(input, expected, 149))

    def test_50(self):
        input = [
            "INSERT s string",
            "ASSIGN s 'abc" 
        ]
        expected = ["Invalid: ASSIGN s 'abc"]
        self.assertTrue(TestUtils.check(input, expected, 150))

    def test_51(self):
        input = [
            "INSERT s string",
            "ASSIGN s 'abc_1'"
        ]
        expected = ["Invalid: ASSIGN s 'abc_1'"]
        self.assertTrue(TestUtils.check(input, expected, 151))

    def test_52(self):
        input = [
            "INSERT s string",
            "ASSIGN s ''"
        ]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 152))

    def test_53(self):
        input = [
            "INSERT s string",
            "ASSIGN s abc'" 
        ]
        expected = ["Invalid: ASSIGN s abc'"]
        self.assertTrue(TestUtils.check(input, expected, 153))

    def test_54(self):
        input = [
            "INSERT s string",
            "ASSIGN s abc" 
        ]
        expected = ["Undeclared: ASSIGN s abc"]
        self.assertTrue(TestUtils.check(input, expected, 154))

    def test_55(self):
        input = []
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 155))

    def test_56(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "INSERT z number",
            "PRINT",
            "END" 
        ]
        expected = ["success", "success", "success", "success", "y//0 x//1 z//1"]
        self.assertTrue(TestUtils.check(input, expected, 156))

    def test_57(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN", 
            "INSERT x number",
            "INSERT z number",
            "RPRINT",
            "END" 
        ]
        expected = ["success", "success", "success", "success", 
                    "z//1 x//1 y//0"]
        self.assertTrue(TestUtils.check(input, expected, 157))

    def test_58(self):
        input = [
            "INSERT a number", 
            "BEGIN",
            "INSERT b string", 
            "BEGIN",
            "INSERT c number", 
            "INSERT a string", 
            "PRINT", 
            "END",
            "END"
        ]
        expected = ["success", "success", "success", "success", "b//1 c//2 a//2"]
        self.assertTrue(TestUtils.check(input, expected, 158))

    def test_59(self):
        input = [
            "INSERT a number", 
            "BEGIN",
            "INSERT b string", 
            "BEGIN",
            "INSERT c number", 
            "INSERT a string", 
            "RPRINT", 
            "END",
            "END"
        ]
        expected = ["success", "success", "success", "success", "a//2 c//2 b//1"]
        self.assertTrue(TestUtils.check(input, expected, 159))

    def test_60(self):
        input = [
            "BEGIN",
            "PRINT",
            "END"
        ]
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 160))

    def test_61(self):
        input = [
            "INSERT s string",
            "ASSIGN s 'HelloWorld'"
        ]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 161))

    def test_62(self):
        input = [
            "INSERT x number", # success
            "BEGIN",
            "INSERT y string", # success
            "BEGIN",
            "INSERT x string", # success
            "PRINT", # y//1 x//2
            "END",
            "END"
        ]
        expected = ["success", "success", "success", "y//1 x//2"]
        self.assertTrue(TestUtils.check(input, expected, 162))

    def test_63(self):
        input = [
            "INSERT x number",
            "BEGIN",
            "BEGIN",
            "BEGIN",
            "LOOKUP x"
        ]
        expected = ["UnclosedBlock: 3"]
        self.assertTrue(TestUtils.check(input, expected, 163))

    def test_64(self):
        input = [
            "BEGIN",
            "BEGIN",
            "BEGIN",
            "END",
            "END",
            "END"
        ]
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 164))

    def test_65(self):
        input = [
            "INSERT x number", # success
            "INSERT y string", # success
            "BEGIN",
            "INSERT z number", # success
            "PRINT", # x//0 y//0 z//1
            "RPRINT", # z//1 y//0 x//0
            "END"
        ]
        expected = ["success", "success", "success", 
                    "x//0 y//0 z//1", "z//1 y//0 x//0"]
        self.assertTrue(TestUtils.check(input, expected, 165))
    
    def test_66(self):
        input = [
            "INSERT a number", #09198210923
            "INSERT b string", 
            "ASSIGN a 100", 
            "ASSIGN b 'hello'", 
            "BEGIN", 
            "INSERT c number", 
            "ASSIGN c a", 
            "LOOKUP b", 
            "BEGIN", 
            "INSERT a string", 
            "ASSIGN a b", 
            "BEGIN", 
            "INSERT d string", 
            "ASSIGN d 'data123'", 
            "PRINT", 
            "END", 
            "RPRINT", 
            "END", 
            "PRINT", 
            "END", 
            "LOOKUP c", 
            "INSERT b number", 
            "ASSIGN a 'oops'", 
            "ASSIGN x 123", 
            "END", 
            "BEGIN", 
            "INSERT e number", 
            "LOOKUP a", 
            "ASSIGN e a", 
        ]

        expected = ["Undeclared: LOOKUP c"]
        self.assertTrue(TestUtils.check(input, expected, 166))
        
    def test_67(self):
            input = [
                "INSERT x number",
                "BEGIN",
                "INSERT y string",
                "END",
                "END"  
            ]
            expected = ["UnknownBlock"]

            self.assertTrue(TestUtils.check(input, expected, 167))

    def test_68(self):
        input = [
            "INSERT a number",          
            "INSERT a string",          
            "INSERT b string",
            "BEGIN",
            "INSERT b string",
            "ASSIGN b 'hello'",
            "ASSIGN a 10",
            "BEGIN",
            "INSERT c number",
            "ASSIGN c a",
            "PRINT",
            "END",
            "RPRINT",
            "END"
        ]

        expected = ["Redeclared: INSERT a string"]  

        self.assertTrue(TestUtils.check(input, expected, 168))


    def test_69(self):
        input = ["INSERT gEYw_Z9dS_TW string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 169))

    def test_70(self):
        input = ["INSERT oD4QoA9Kyn6IsU number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 170))

    def test_71(self):
        input = ["INSERT oD4QoA9Kyn6IsU number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 171))

    def test_72(self):
        input = ["INSERT eCQXt1gIyNqbXtz string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 172))

    def test_73(self):
        input = ["INSERT psjLO string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 173))
    
    def test_74(self):
        input = ["INSERT w2AylIT9NNZwhp string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 174))

    def test_75(self):
        input = ["INSERT ckUuS_lU string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 175))
    
    def test_76(self):
        input = ["INSERT oyHj9kv string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 176))

    def test_77(self):
        input = ["INSERT njdi number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 177))

    def test_78(self):
        input = ["INSERT nUDUsbsTaj3 number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 178))
    
    def test_79(self):
        input = ["INSERT ^m0RvWt-adq<7l$ string"]
        expected = ["Invalid: INSERT ^m0RvWt-adq<7l$ string"]
        self.assertTrue(TestUtils.check(input, expected, 179))

    def test_80(self):
        input = ["INSERT M78 string"]
        expected = ["Invalid: INSERT M78 string"]
        self.assertTrue(TestUtils.check(input, expected, 180))
    
    def test_81(self):
        input = ["INSERT - number"]
        expected = ["Invalid: INSERT - number"]
        self.assertTrue(TestUtils.check(input, expected, 181))
    
    def test_82(self):
        input = ["INSERT ~7pQ number"]
        expected = ["Invalid: INSERT ~7pQ number"]
        self.assertTrue(TestUtils.check(input, expected, 182))
    
    def test_83(self):
        input = ["INSERT M string"]
        expected = ["Invalid: INSERT M string"]
        self.assertTrue(TestUtils.check(input, expected, 183))
    
    def test_84(self):
        input = ["INSERT ~?R number"]
        expected = ["Invalid: INSERT ~?R number"]
        self.assertTrue(TestUtils.check(input, expected, 184))

    def test_85(self):
        input = ["INSERT S5vK6!Y'-(fP)S string"]
        expected = ["Invalid: INSERT S5vK6!Y'-(fP)S string"]
        self.assertTrue(TestUtils.check(input, expected, 185))
    
    def test_86(self):
        input = ["INSERT ~eKB number"]
        expected = ["Invalid: INSERT ~eKB number"]
        self.assertTrue(TestUtils.check(input, expected, 186))
    
    def test_87(self):
        input = ["INSERT <Cf=M7vCk string"]
        expected = ["Invalid: INSERT <Cf=M7vCk string"]
        self.assertTrue(TestUtils.check(input, expected, 187))
    
    def test_88(self):
        input = ["INSERT K string"]
        expected = ["Invalid: INSERT K string"]
        self.assertTrue(TestUtils.check(input, expected, 188))

    def test_89(self):
        input = ["INSERT x hETJM"]
        expected = ["Invalid: INSERT x hETJM"]
        self.assertTrue(TestUtils.check(input, expected, 189))

    def test_90(self):
        input = ["INSERT x MxjccZfOrp"]
        expected = ["Invalid: INSERT x MxjccZfOrp"]
        self.assertTrue(TestUtils.check(input, expected, 190))

    def test_91(self):
        input = ["INSERT x XXtCa"]
        expected = ["Invalid: INSERT x XXtCa"]
        self.assertTrue(TestUtils.check(input, expected, 191))

    def test_92(self):
        input = ["INSERT x bnGfrGE"]
        expected = ["Invalid: INSERT x bnGfrGE"]
        self.assertTrue(TestUtils.check(input, expected, 192))

    def test_93(self):
        input = ["INSERT x dvZXsLCgp"]
        expected = ["Invalid: INSERT x dvZXsLCgp"]
        self.assertTrue(TestUtils.check(input, expected, 193))

    def test_94(self):
        input = ["INSERT x VUC"]
        expected = ["Invalid: INSERT x VUC"]
        self.assertTrue(TestUtils.check(input, expected, 194))

    def test_95(self):
        input = ["INSERT x aVZvILOR"]
        expected = ["Invalid: INSERT x aVZvILOR"]
        self.assertTrue(TestUtils.check(input, expected, 195))

    def test_96(self):
        input = ["INSERT x XtU"]
        expected = ["Invalid: INSERT x XtU"]
        self.assertTrue(TestUtils.check(input, expected, 196))

    def test_97(self):
        input = ["INSERT x hUxxjMZUC"]
        expected = ["Invalid: INSERT x hUxxjMZUC"]
        self.assertTrue(TestUtils.check(input, expected, 197))

    def test_98(self):
        input = ["INSERT x zoxVzp"]
        expected = ["Invalid: INSERT x zoxVzp"]
        self.assertTrue(TestUtils.check(input, expected, 198))

    def test_99(self):
        input = ["DNSERT x string"]
        expected = ["Invalid: DNSERT x string"]
        self.assertTrue(TestUtils.check(input, expected, 199))

    def test_100(self):
        input = ["INSEUT x number"]
        expected = ["Invalid: INSEUT x number"]
        self.assertTrue(TestUtils.check(input, expected, 200))

    def test_101(self):
        input = ["INSERW x number"]
        expected = ["Invalid: INSERW x number"]
        self.assertTrue(TestUtils.check(input, expected, 201))

    def test_102(self):
        input = ["INSQRT x string"]
        expected = ["Invalid: INSQRT x string"]
        self.assertTrue(TestUtils.check(input, expected, 202))

    def test_103(self):
        input = ["IWSERT x string"]
        expected = ["Invalid: IWSERT x string"]
        self.assertTrue(TestUtils.check(input, expected, 203))

    def test_104(self):
        input = ["INSEKT x string"]
        expected = ["Invalid: INSEKT x string"]
        self.assertTrue(TestUtils.check(input, expected, 204))

    def test_105(self):
        input = ["PNSERT x string"]
        expected = ["Invalid: PNSERT x string"]
        self.assertTrue(TestUtils.check(input, expected, 205))

    def test_106(self):
        input = ["INYERT x string"]
        expected = ["Invalid: INYERT x string"]
        self.assertTrue(TestUtils.check(input, expected, 206))

    def test_107(self):
        input = ["IYSERT x string"]
        expected = ["Invalid: IYSERT x string"]
        self.assertTrue(TestUtils.check(input, expected, 207))

    def test_108(self):
        input = ["BNSERT x number"]
        expected = ["Invalid: BNSERT x number"]
        self.assertTrue(TestUtils.check(input, expected, 208))

    def test_109(self):
        input = [
                "INSERT p number", "INSERT n number", 
                "INSERT x number", "INSERT x number", 
                "INSERT u string", "INSERT u number", 
                "INSERT u number", "INSERT o number", 
                "INSERT n string"
                ]
        expected = ['Redeclared: INSERT x number']
        self.assertTrue(TestUtils.check(input, expected, 209))

    def test_110(self):
        input = [
                "INSERT m number", "INSERT n number", 
                "INSERT x number", "INSERT p number", 
                "INSERT x number", "INSERT u string", 
                "INSERT v string", "INSERT m number", 
                "INSERT y number", "INSERT t number"]
        expected = ['Redeclared: INSERT x number']
        self.assertTrue(TestUtils.check(input, expected, 210))

    def test_111(self):
        input = [
                "INSERT u string", "INSERT a string", 
                "INSERT v number", "INSERT p string", 
                "INSERT p number", "INSERT u number", 
                "INSERT n string", "INSERT p number", 
                "INSERT t string"]
        expected = ['Redeclared: INSERT p number']
        self.assertTrue(TestUtils.check(input, expected, 211))

    def test_112(self):
        input = [
                "INSERT p number", "INSERT p string", 
                "INSERT z number", "INSERT o number", 
                "INSERT y string", "INSERT c string", 
                "INSERT z number"]
        expected = ['Redeclared: INSERT p string']
        self.assertTrue(TestUtils.check(input, expected, 212))

    def test_113(self):
        input = [
                "INSERT v number", "INSERT y number", 
                "INSERT t string", "INSERT b string", 
                "INSERT c number", "INSERT z number", 
                "INSERT m number", "INSERT v string", 
                "INSERT a number", "INSERT x string"]
        expected = ['Redeclared: INSERT v string']
        self.assertTrue(TestUtils.check(input, expected, 213))

    def test_114(self):
        input = [
               "INSERT m number", "INSERT m string", 
               "INSERT a number", "INSERT m number", 
               "INSERT y string", "INSERT y string", 
               "INSERT m number", "INSERT t number", 
               "INSERT z string"]
        expected = ['Redeclared: INSERT m string']
        self.assertTrue(TestUtils.check(input, expected, 214))

    def test_115(self):
        input = [
                "INSERT x number", "INSERT u number", 
                "INSERT u string", "INSERT b number", 
                "INSERT y string", "INSERT u string", 
                "INSERT u string", "INSERT b string",
                "INSERT p string"]
        expected = ['Redeclared: INSERT u string']
        self.assertTrue(TestUtils.check(input, expected, 215))

    def test_116(self):
        input = [
                "INSERT o string", "INSERT c number", 
                "INSERT n number", "INSERT v string", 
                "INSERT p string", "INSERT c number", 
                "INSERT p number", "INSERT v number"]
        expected = ['Redeclared: INSERT c number']
        self.assertTrue(TestUtils.check(input, expected, 216))

    def test_117(self):
        input = [
                "INSERT p string", "INSERT y number", 
                "INSERT x number", "INSERT n string", 
                "INSERT m string", "INSERT u string", 
                "INSERT n number", "INSERT c string", 
                "INSERT p number", "INSERT z number"]
        expected = ['Redeclared: INSERT n number']
        self.assertTrue(TestUtils.check(input, expected, 217))

    def test_118(self):
        input = [
                "INSERT y string", "INSERT u string", 
                "INSERT y number", "INSERT t number", 
                "INSERT z string", "INSERT z string", 
                "INSERT z number"]
        expected = ['Redeclared: INSERT y number']
        self.assertTrue(TestUtils.check(input, expected, 218))

    def test_119(self):
        input = [
                "BEGIN", "INSERT x number", 
                "BEGIN", "INSERT x string", "INSERT y number", 
                "END", "INSERT y string", 
                "END", "INSERT x string", 
                "END"]
        expected = ['UnknownBlock']
        self.assertTrue(TestUtils.check(input, expected, 219))

    def test_120(self):
        input = [  
                "BEGIN", "INSERT a string", 
                "BEGIN", "INSERT b string", 
                "BEGIN", "INSERT a number", 
                "END", "INSERT b number", 
                "END", "INSERT c string", 
                "END"]
        expected = ['Redeclared: INSERT b number']
        self.assertTrue(TestUtils.check(input, expected, 220))

    def test_121(self):
        input = [
                "INSERT x number", 
                "BEGIN", "INSERT x string", 
                "BEGIN", "INSERT y string", 
                "END", "INSERT z number", 
                "END", "INSERT y string", "END"]
        expected = ['UnknownBlock']
        self.assertTrue(TestUtils.check(input, expected, 221))

    def test_122(self):
        input = [
                "BEGIN", "INSERT m string", 
                "BEGIN", "INSERT m string", 
                "END", "INSERT m number", 
                "BEGIN", "INSERT m string", 
                "END", "END", 
                "INSERT m number"]
        expected = ['Redeclared: INSERT m number']
        self.assertTrue(TestUtils.check(input, expected, 222))

    def test_123(self):
        input = [
                "INSERT a number", 
                "BEGIN", "INSERT b string", 
                "BEGIN", "INSERT a string", 
                "END", "INSERT c number", 
                "BEGIN", "INSERT b number", 
                "END", "END"]
        expected = [
                'success', 'success', 'success', 
                'success', 'success']
        self.assertTrue(TestUtils.check(input, expected, 223))

    def test_124(self):
        input = [
                "BEGIN", "INSERT x string", 
                "BEGIN", "INSERT x string", "INSERT x number", 
                "END", "END", 
                "INSERT y string", "INSERT y string", "END"]
        expected = ['Redeclared: INSERT x number']
        self.assertTrue(TestUtils.check(input, expected, 224))

    def test_125(self):
        input = [
                "INSERT z number", 
                "BEGIN", "INSERT y string", 
                "BEGIN", "INSERT z string", 
                "END", "INSERT y number", 
                "END", "INSERT x string", "END"]
        expected = ['Redeclared: INSERT y number']
        self.assertTrue(TestUtils.check(input, expected, 225))

    def test_126(self):
        input = [
                "BEGIN", "BEGIN", "BEGIN", "INSERT a string", 
                "END", "INSERT a number", 
                "END", "INSERT a string", 
                "END", "INSERT a number"]
        expected = ['success', 'success', 'success', 'success']
        self.assertTrue(TestUtils.check(input, expected, 226))

    def test_127(self):
        input = [
                "BEGIN", "INSERT m string", 
                "BEGIN", "INSERT n string", 
                "BEGIN", "INSERT m string", "INSERT m string", 
                "END", "END", "END", "INSERT m string"]
        expected = ['Redeclared: INSERT m string']
        self.assertTrue(TestUtils.check(input, expected, 227))

    def test_128(self):
        input = [
                "INSERT p number", 
                "BEGIN", "INSERT p string", 
                "BEGIN", "INSERT q string", 
                "END", "INSERT r number", 
                "BEGIN", "INSERT s number", "END", "END"]
        expected = ['success', 'success', 'success', 
                    'success', 'success']
        self.assertTrue(TestUtils.check(input, expected, 228))

    def test_129(self):
        input = ["INSERT x number", "ASSIGN x -10i+10"]
        expected = ["Invalid: ASSIGN x -10i+10"]
        self.assertTrue(TestUtils.check(input, expected, 229))

    def test_130(self):
        input = ["INSERT x number", "ASSIGN x -24/2"]
        expected = ["Invalid: ASSIGN x -24/2"]
        self.assertTrue(TestUtils.check(input, expected, 230))

    def test_131(self):
        input = ["INSERT x number", "ASSIGN x -655126"]
        expected = ["Invalid: ASSIGN x -655126"]
        self.assertTrue(TestUtils.check(input, expected, 231))

    def test_132(self):
        input = ["INSERT x number", "ASSIGN x 342a"]
        expected = ["Invalid: ASSIGN x 342a"]
        self.assertTrue(TestUtils.check(input, expected, 232))

    def test_133(self):
        input = ["INSERT x number", "ASSIGN x -542953"]
        expected = ["Invalid: ASSIGN x -542953"]
        self.assertTrue(TestUtils.check(input, expected, 233))

    def test_134(self):
        input = ["INSERT x number", "ASSIGN x 935.4"]
        expected = ["Invalid: ASSIGN x 935.4"]
        self.assertTrue(TestUtils.check(input, expected, 234))

    def test_135(self):
        input = ["INSERT x number", "ASSIGN x -47i+9"]
        expected = ["Invalid: ASSIGN x -47i+9"]
        self.assertTrue(TestUtils.check(input, expected, 235))

    def test_136(self):
        input = ["INSERT x number", "ASSIGN x 669a"]
        expected = ["Invalid: ASSIGN x 669a"]
        self.assertTrue(TestUtils.check(input, expected, 236))

    def test_137(self):
        input = ["INSERT x number", "ASSIGN x -81i+3"]
        expected = ["Invalid: ASSIGN x -81i+3"]
        self.assertTrue(TestUtils.check(input, expected, 237))

    def test_138(self):
        input = ["INSERT x number", "ASSIGN x 172a"]
        expected = ["Invalid: ASSIGN x 172a"]
        self.assertTrue(TestUtils.check(input, expected, 238))

    def test_139(self):
        input = ["INSERT x string", "ASSIGN x 'n7zBTVu'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 239))

    def test_140(self):
        input = ["INSERT x string", "ASSIGN x 'u8v'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 240))

    def test_141(self):
        input = ["INSERT x string", "ASSIGN x 'dK8bp5'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 241))

    def test_142(self):
        input = ["INSERT x string", "ASSIGN x 'EhTP'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 242))

    def test_143(self):
        input = ["INSERT x string", "ASSIGN x 'EfJ'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 243))

    def test_144(self):
        input = ["INSERT x string", "ASSIGN x 'xLnDzDMB0w'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 244))

    def test_145(self):
        input = ["INSERT x string", "ASSIGN x 'z2ni9a4'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 245))

    def test_146(self):
        input = ["INSERT x string", "ASSIGN x 'KnNGXO0'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 246))

    def test_147(self):
        input = ["INSERT x string", "ASSIGN x 'IIr'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 247))

    def test_148(self):
        input = ["INSERT x string", "ASSIGN x 'dWE'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 248))

    def test_149(self):
        input = ["INSERT x string", "ASSIGN x 774617"]
        expected = ["TypeMismatch: ASSIGN x 774617"]
        self.assertTrue(TestUtils.check(input, expected, 249))

    def test_150(self):
        input = ["INSERT x string", "ASSIGN x 550830"]
        expected = ["TypeMismatch: ASSIGN x 550830"]
        self.assertTrue(TestUtils.check(input, expected, 250))

    def test_151(self):
        input = ["INSERT x string", "ASSIGN x 156753"]
        expected = ["TypeMismatch: ASSIGN x 156753"]
        self.assertTrue(TestUtils.check(input, expected, 251))

    def test_152(self):
        input = ["INSERT x string", "ASSIGN x 958949"]
        expected = ["TypeMismatch: ASSIGN x 958949"]
        self.assertTrue(TestUtils.check(input, expected, 252))

    def test_153(self):
        input = ["INSERT x string", "ASSIGN x 256981"]
        expected = ["TypeMismatch: ASSIGN x 256981"]
        self.assertTrue(TestUtils.check(input, expected, 253))

    def test_154(self):
        input = ["INSERT x string", "ASSIGN x 991507"]
        expected = ["TypeMismatch: ASSIGN x 991507"]
        self.assertTrue(TestUtils.check(input, expected, 254))

    def test_155(self):
        input = ["INSERT x string", "ASSIGN x 186932"]
        expected = ["TypeMismatch: ASSIGN x 186932"]
        self.assertTrue(TestUtils.check(input, expected, 255))

    def test_156(self):
        input = ["INSERT x string", "ASSIGN x 428017"]
        expected = ["TypeMismatch: ASSIGN x 428017"]
        self.assertTrue(TestUtils.check(input, expected, 256))

    def test_157(self):
        input = ["INSERT x string", "ASSIGN x 634993"]
        expected = ["TypeMismatch: ASSIGN x 634993"]
        self.assertTrue(TestUtils.check(input, expected, 257))

    def test_158(self):
        input = ["INSERT x string", "ASSIGN x 485940"]
        expected = ["TypeMismatch: ASSIGN x 485940"]
        self.assertTrue(TestUtils.check(input, expected, 258))

    def test_159(self):
        input = ["INSERT x number", "ASSIGN x 'dWE'"]
        expected = ["TypeMismatch: ASSIGN x 'dWE'"]
        self.assertTrue(TestUtils.check(input, expected, 259))

    def test_160(self):
        input = ["INSERT x number", "ASSIGN x 'IIr'"]
        expected = ["TypeMismatch: ASSIGN x 'IIr'"]
        self.assertTrue(TestUtils.check(input, expected, 260))

    def test_161(self):
        input = ["INSERT x number", "ASSIGN x 'KnNGXO0'"]
        expected = ["TypeMismatch: ASSIGN x 'KnNGXO0'"]
        self.assertTrue(TestUtils.check(input, expected, 261))

    def test_162(self):
        input = ["INSERT x number", "ASSIGN x 'z2ni9a4'"]
        expected = ["TypeMismatch: ASSIGN x 'z2ni9a4'"]
        self.assertTrue(TestUtils.check(input, expected, 262))

    def test_163(self):
        input = ["INSERT x number", "ASSIGN x 'xLnDzDMB0w'"]
        expected = ["TypeMismatch: ASSIGN x 'xLnDzDMB0w'"]
        self.assertTrue(TestUtils.check(input, expected, 263))

    def test_164(self):
        input = ["INSERT x number", "ASSIGN x 'EfJ'"]
        expected = ["TypeMismatch: ASSIGN x 'EfJ'"]
        self.assertTrue(TestUtils.check(input, expected, 264))

    def test_165(self):
        input = ["INSERT x number", "ASSIGN x 'EhTP'"]
        expected = ["TypeMismatch: ASSIGN x 'EhTP'"]
        self.assertTrue(TestUtils.check(input, expected, 265))

    def test_166(self):
        input = ["INSERT x number", "ASSIGN x 'dK8bp5'"]
        expected = ["TypeMismatch: ASSIGN x 'dK8bp5'"]
        self.assertTrue(TestUtils.check(input, expected, 266))

    def test_167(self):
        input = ["INSERT x number", "ASSIGN x 'u8v'"]
        expected = ["TypeMismatch: ASSIGN x 'u8v'"]
        self.assertTrue(TestUtils.check(input, expected, 267))

    def test_168(self):
        input = ["INSERT x number", "ASSIGN x 'n7zBTVu'"]
        expected = ["TypeMismatch: ASSIGN x 'n7zBTVu'"]
        self.assertTrue(TestUtils.check(input, expected, 268))

    def test_169(self):
        input = ["INSERT x number", "INSERT z string", "ASSIGN x y"]
        expected = ["Undeclared: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 269))

    def test_170(self):
        input = ["INSERT p string", "INSERT m string", "ASSIGN p 'ym'"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 270))

    def test_171(self):
        input = ["INSERT c string", "INSERT a number", "ASSIGN c 'p'"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 271))

    def test_172(self):
        input = ["INSERT t string", "INSERT t number", "ASSIGN t b"]
        expected = ["Redeclared: INSERT t number"]
        self.assertTrue(TestUtils.check(input, expected, 272))

    def test_173(self):
        input = ["INSERT t number", "INSERT p string", "ASSIGN t 614951"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 273))

    def test_174(self):
        input = ["INSERT v number", "INSERT v string", "ASSIGN v 'daAqcwYPj'"]
        expected = ["Redeclared: INSERT v string"]
        self.assertTrue(TestUtils.check(input, expected, 274))

    def test_175(self):
        input = ["INSERT b string", "INSERT a number", "ASSIGN b 'WJQKJOEX'"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 275))

    def test_176(self):
        input = ["INSERT o string", "INSERT z number", "ASSIGN o v"]
        expected = ["Undeclared: ASSIGN o v"]
        self.assertTrue(TestUtils.check(input, expected, 276))

    def test_177(self):
        input = ["INSERT z string", "INSERT z number", "ASSIGN z n"]
        expected = ["Redeclared: INSERT z number"]
        self.assertTrue(TestUtils.check(input, expected, 277))

    def test_178(self):
        input = ["INSERT y string", "INSERT x string", "ASSIGN y 'cscNJhc'"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 278))

    def test_179(self):
        input = ["ASSIGN p v", "INSERT n string", 
                 "INSERT y string", "INSERT m string", 
                 "INSERT y number", "INSERT m number", 
                 "ASSIGN c o", "INSERT p number", 
                 "ASSIGN b 1.2.3", "INSERT v number", 
                 "ASSIGN z #$", "ASSIGN m #$", "ASSIGN v 410236"]
        expected = ["Undeclared: ASSIGN p v"]
        self.assertTrue(TestUtils.check(input, expected, 279))

    def test_180(self):
        input = ["ASSIGN v @@@", "INSERT o string", 
                 "ASSIGN o 'a'","INSERT m string" ,"ASSIGN m 38425", 
                 "INSERT t number", "INSERT u string", 
                 "ASSIGN o 'v'", "ASSIGN u '()'", 
                 "INSERT y string", "ASSIGN y 'z'"]
        expected = ["Invalid: ASSIGN v @@@"]
        self.assertTrue(TestUtils.check(input, expected, 280))

    def test_181(self):
        input = ["ASSIGN n 439118", "ASSIGN y 712770", 
                 "ASSIGN v c", "INSERT y string", 
                 "ASSIGN o p", "ASSIGN x 441990", 
                 "INSERT o number", "INSERT z string", 
                 "INSERT z number", "INSERT y string", 
                 "INSERT z number", "INSERT m string", 
                 "INSERT x string"]
        expected = ["Undeclared: ASSIGN n 439118"]
        self.assertTrue(TestUtils.check(input, expected, 281))

    def test_182(self):
        input = ["ASSIGN y 530819", "ASSIGN b 663340", 
                 "INSERT c string", "ASSIGN v z", 
                 "INSERT b number", "INSERT o string", 
                 "ASSIGN b o", "INSERT v number", 
                 "ASSIGN t 123abc$", "INSERT y string"]
        expected = ["Undeclared: ASSIGN y 530819"]
        self.assertTrue(TestUtils.check(input, expected, 282))

    def test_183(self):
        input = ["INSERT p string", "ASSIGN v 420036", 
                 "ASSIGN c {}", "ASSIGN p ()", 
                 "INSERT y string", "INSERT p number", 
                 "INSERT x number", "INSERT p number", 
                 "INSERT b number", "INSERT b string", 
                 "INSERT z string", "ASSIGN m 1.2.3", 
                 "ASSIGN c #$", "INSERT n string"]
        expected = ["Undeclared: ASSIGN v 420036"]
        self.assertTrue(TestUtils.check(input, expected, 283))

    def test_184(self):
        input = ["ASSIGN o {}", "INSERT m number", 
                 "INSERT x number", "INSERT b number", 
                 "INSERT v string", "ASSIGN b a", 
                 "ASSIGN o ()", "ASSIGN y hello!", 
                 "ASSIGN v m", "ASSIGN p 538509", 
                 "INSERT b string", "ASSIGN c 123abc$"]
        expected = ["Invalid: ASSIGN o {}"]
        self.assertTrue(TestUtils.check(input, expected, 284))

    def test_185(self):
        input = ["ASSIGN t []", "ASSIGN x 282427", 
                 "INSERT n number", "INSERT z string", 
                 "INSERT p string", "INSERT u number", 
                 "INSERT b string", "ASSIGN b 235763", 
                 "ASSIGN x hello!", "ASSIGN z 45788"]
        expected = ["Invalid: ASSIGN t []"]
        self.assertTrue(TestUtils.check(input, expected, 285))

    def test_186(self):
        input = ["ASSIGN b hello!", "ASSIGN b ()", 
                 "INSERT m number", "ASSIGN u 303619", 
                 "ASSIGN v x", "ASSIGN m c", "ASSIGN y 859104", 
                 "INSERT z number", "INSERT t string", 
                 "INSERT a string", "ASSIGN b 864679", 
                 "INSERT t number", "INSERT t string", 
                 "INSERT y string", "ASSIGN b p"]
        expected = ["Invalid: ASSIGN b hello!"]
        self.assertTrue(TestUtils.check(input, expected, 286))

    def test_187(self):
        input = ["ASSIGN u 25472", "ASSIGN t ()", 
                 "ASSIGN t u", "ASSIGN c p", 
                 "ASSIGN p 698222", "ASSIGN t @@@", 
                 "ASSIGN u 984942", "INSERT v string", 
                 "ASSIGN c m", "ASSIGN t []", "ASSIGN p {}", 
                 "ASSIGN a hello!"]
        expected = ["Undeclared: ASSIGN u 25472"]
        self.assertTrue(TestUtils.check(input, expected, 287))

    def test_188(self):
        input = ["ASSIGN p 192874", "INSERT c number", 
                 "INSERT t string", "INSERT u string", 
                 "INSERT z number", "ASSIGN m 490226", 
                 "ASSIGN p 79497", "INSERT u number", 
                 "ASSIGN a #$", "INSERT v number"]
        expected = ["Undeclared: ASSIGN p 192874"]
        self.assertTrue(TestUtils.check(input, expected, 288))

    def test_189(self):
        input = ["INSERT z string", "INSERT u string", 
                 "INSERT b number", "ASSIGN b 583850", 
                 "INSERT v string", "INSERT p number", 
                 "ASSIGN x 168943", "INSERT b string", 
                 "INSERT z string", "INSERT o number", 
                 "INSERT m number"]
        expected = ["Undeclared: ASSIGN x 168943"]
        self.assertTrue(TestUtils.check(input, expected, 289))

    def test_190(self):
        input = [
                "BEGIN", "BEGIN", "BEGIN", 
                "INSERT a string", "LOOKUP a", 
                "END", "INSERT a number", "LOOKUP a", 
                "END", "INSERT a string", "LOOKUP a", 
                "END", "INSERT a number"]
        expected = [
                'success', '3', 
                'success', '2', 
                'success', '1', 
                'success']
        self.assertTrue(TestUtils.check(input, expected, 290))

    def test_191(self):
        input = [
                "BEGIN", "BEGIN", "BEGIN", 
                "INSERT a string", 
                "END", "INSERT a number", "LOOKUP a", 
                "END", "INSERT a string", "LOOKUP a", 
                "END", "INSERT a number"]
        expected = [
                'success', 
                'success', '2', 
                'success', '1', 
                'success']
        self.assertTrue(TestUtils.check(input, expected, 291))

    def test_192(self):
        input = [
                "INSERT p number", "LOOKUP p",
                "BEGIN", "INSERT p string", "LOOKUP p", 
                "BEGIN", "INSERT q string", "LOOKUP p", "LOOKUP q",
                "END", "INSERT r number", "LOOKUP q", "LOOKUP r", 
                "BEGIN", "INSERT s number", "LOOKUP r", 
                "LOOKUP s",
                "END", "END"
                ]
        expected = ['Undeclared: LOOKUP q']
        self.assertTrue(TestUtils.check(input, expected, 292))

    def test_193(self):
        input = [
                "INSERT a number", "LOOKUP a", 
                "BEGIN", "INSERT b string", "LOOKUP b", 
                "BEGIN", "INSERT a string", "LOOKUP a", "LOOKUP b", 
                "END", "INSERT c number", "LOOKUP a", "LOOKUP c",
                "BEGIN", "INSERT b number", "LOOKUP a", "LOOKUP c",
                "END", "END"
                ]
        expected = [
                "success", "0",        
                "success", "1",        
                "success", "2", "1",        
                "success", "0", "1",        
                "success", "0", "1"         
                ]        
        self.assertTrue(TestUtils.check(input, expected, 293))

    def test_194(self):
        input = [
                "BEGIN", "INSERT v number", 
                "INSERT c string", "LOOKUP v", "LOOKUP c",  
                "INSERT m string", "INSERT o number", 
                "LOOKUP m", "LOOKUP o", 
                "INSERT z string", "INSERT u string",
                "LOOKUP z", "LOOKUP u",
                "INSERT n string", "INSERT b string", 
                "LOOKUP n", "LOOKUP b",  
                "INSERT x number", "LOOKUP x",  "END"
                ]
        expected = ['success', 
                    'success', '1', '1', 
                    'success', 'success', 
                    '1', '1', 
                    'success', 'success', 
                    '1', '1', 
                    'success', 'success', 
                    '1', '1', 
                    'success', '1']
        self.assertTrue(TestUtils.check(input, expected, 294))

    def test_195(self):
        input = [
                "INSERT b string", 
                "BEGIN", "LOOKUP b", 
                "INSERT v number", "LOOKUP b", "LOOKUP v", 
                "END", 
                "BEGIN", "BEGIN", "INSERT m number", 
                "LOOKUP m", "LOOKUP v", 
                "END","INSERT t string", "INSERT z string", 
                "LOOKUP m", "LOOKUP t", 
                "END", "INSERT a string", 
                "BEGIN","INSERT p string", "LOOKUP t", "LOOKUP v", 
                "INSERT o number", 
                "END", "INSERT y string", "LOOKUP z", "LOOKUP o" 
                ]
        expected = ["Undeclared: LOOKUP v"]
        self.assertTrue(TestUtils.check(input, expected, 295))

    def test_196(self):
        input = [
                "INSERT x number", "INSERT y string", 
                "LOOKUP x", "LOOKUP y", 
                "BEGIN", "INSERT z string", "LOOKUP z", 
                "BEGIN", "INSERT m number", "LOOKUP m", 
                "LOOKUP z", "LOOKUP y", 
                "END", "INSERT n string", "LOOKUP n", "LOOKUP x", 
                "END", "INSERT o number", "LOOKUP o", "LOOKUP x"
        ]
        expected = ['success', 'success', 
                    '0', '0', 
                    'success', '1', 
                    'success', '2', 
                    '1', '0', 
                    'success', '1', '0', 
                    'success', '0', '0']
        self.assertTrue(TestUtils.check(input, expected, 296))


    def test_197(self):
        input = [
            "INSERT a number", "LOOKUP a", 
            "BEGIN", "INSERT b string", "LOOKUP b", 
            "BEGIN", "INSERT a string", "LOOKUP a", "LOOKUP b", 
            "END", "INSERT c number", "LOOKUP a", "LOOKUP c", 
            "BEGIN", "INSERT b number", "LOOKUP a", 
            "LOOKUP c", "LOOKUP b", 
            "END", "END"
            ]
        expected = ['success', '0', 
                    'success', '1', 
                    'success', '2', '1', 
                    'success', '0', '1', 
                    'success', '0', 
                    '1', '2' 
                    ]
        self.assertTrue(TestUtils.check(input, expected, 297))


    def test_198(self):
        input = [
            "INSERT x number", "LOOKUP x", 
            "BEGIN", "INSERT y string", "LOOKUP y", 
            "BEGIN", "INSERT z string", "LOOKUP z", 
            "LOOKUP x", "LOOKUP y", "LOOKUP z", 
            "END", "INSERT w number", 
            "LOOKUP w", "LOOKUP x", "LOOKUP y", "LOOKUP z", 
            "END"
        ]
        expected = ['Undeclared: LOOKUP z']
        self.assertTrue(TestUtils.check(input, expected, 298))


    def test_199(self):
        input = [
            "INSERT a string", 
            "BEGIN", "INSERT b number", "LOOKUP b", 
            "BEGIN", "INSERT c string", "LOOKUP a", 
            "LOOKUP b", "LOOKUP c", 
            "END", "INSERT d number", "LOOKUP d", "LOOKUP c", 
            "BEGIN", "INSERT e string", "LOOKUP d", "LOOKUP e", 
            "END", "END"
        ]
        expected = ['Undeclared: LOOKUP c']
        self.assertTrue(TestUtils.check(input, expected, 299))
    
    def test_200(self):
        input = [
            "BEGIN", "INSERT a string", "PRINT",
            "BEGIN", "INSERT b number", "PRINT",
            "END", "INSERT c string", "PRINT",
            "END", "INSERT d number", "PRINT"
        ]
        expected = ['success', 'a//1', 
                    'success', 'a//1 b//2', 
                    'success', 'a//1 c//1', 
                    'success', 'd//0']
        self.assertTrue(TestUtils.check(input, expected, 300))

    def test_201(self):
        input = [
            "INSERT x number", "PRINT",
            "BEGIN", "INSERT y string", "PRINT",
            "BEGIN", "INSERT z string", "PRINT",
            "END", "INSERT w number", "PRINT",
            "END", "INSERT v string", "PRINT"
        ]
        expected = ['success', 'x//0', 
                    'success', 'x//0 y//1', 
                    'success', 'x//0 y//1 z//2', 
                    'success', 'x//0 y//1 w//1', 
                    'success', 'x//0 v//0']
        self.assertTrue(TestUtils.check(input, expected, 301))

    def test_202(self):
        input = [
            "BEGIN", "INSERT a string", "PRINT",
            "BEGIN", "INSERT b number", "PRINT",
            "BEGIN", "INSERT c string", "PRINT",
            "END", "INSERT d number", "PRINT",
            "END", "INSERT e string", "PRINT",
            "END", "INSERT f number", "PRINT"
        ]
        expected = ['success', 'a//1', 
                    'success', 'a//1 b//2', 
                    'success', 'a//1 b//2 c//3', 
                    'success', 'a//1 b//2 d//2', 
                    'success', 'a//1 e//1', 
                    'success', 'f//0']
        self.assertTrue(TestUtils.check(input, expected, 302))

    def test_203(self):
        input = [
            "INSERT m number", "PRINT",
            "BEGIN", "INSERT n string", "PRINT",
            "BEGIN", "INSERT o string", "PRINT",
            "END", "INSERT p number", "PRINT",
            "END", "INSERT q string", "PRINT"
        ]
        expected = ['success', 'm//0', 
                    'success', 'm//0 n//1', 
                    'success', 'm//0 n//1 o//2', 
                    'success', 'm//0 n//1 p//1', 
                    'success', 'm//0 q//0']
        self.assertTrue(TestUtils.check(input, expected, 303))

    def test_204(self):
        input = [
            "BEGIN", "INSERT r string", "PRINT",
            "BEGIN", "INSERT s number", "PRINT",
            "INSERT t string",
            "END", "PRINT",
            "END", "PRINT" 
        ]
        expected = ['success', 'r//1', 
                    'success', 'r//1 s//2', 
                    'success', 
                    'r//1',''
                    ]
        self.assertTrue(TestUtils.check(input, expected, 304))

    def test_205(self):
        input = [
            "INSERT u number", "PRINT",
            "BEGIN", "INSERT v string", "PRINT",
            "INSERT w number",
            "BEGIN", "INSERT x string", "PRINT",
            "END", "PRINT",
            "END", "PRINT"
        ]
        expected = ['success', 'u//0', 
                    'success', 'u//0 v//1', 
                    'success', 
                    'success', 'u//0 v//1 w//1 x//2', 
                    'u//0 v//1 w//1', 
                    'u//0']
        self.assertTrue(TestUtils.check(input, expected, 305))

    def test_206(self):
        input = [
            "BEGIN", "INSERT y string", "PRINT",
            "BEGIN", "INSERT z number", "PRINT",
            "BEGIN", "INSERT a string", "PRINT",
            "END", "PRINT",
            "END", "PRINT",
            "END", "PRINT" 
        ]
        expected = ['success', 'y//1', 
                    'success', 'y//1 z//2', 
                    'success', 'y//1 z//2 a//3', 
                    'y//1 z//2', 
                    'y//1', ''
                    ]
        self.assertTrue(TestUtils.check(input, expected, 306))

    def test_207(self):
        input = [
            "INSERT b number", "PRINT",
            "BEGIN", "INSERT c string", "PRINT",
            "BEGIN", "INSERT d string", "PRINT",
            "END", "INSERT e number", "PRINT",
            "END", "INSERT f string", "PRINT"
        ]
        expected = ['success', 'b//0', 
                    'success', 'b//0 c//1', 
                    'success', 'b//0 c//1 d//2', 
                    'success', 'b//0 c//1 e//1', 
                    'success', 'b//0 f//0']
        self.assertTrue(TestUtils.check(input, expected, 307))

    def test_208(self):
        input = [
            "BEGIN", "INSERT g string", "PRINT",
            "BEGIN", "INSERT h number", "PRINT",
            "BEGIN", "INSERT i string", "PRINT",
            "END", "INSERT j number", "PRINT",
            "END", "INSERT k string", "PRINT",
            "END", "INSERT l number", "PRINT"
        ]
        expected = ['success', 'g//1', 
                    'success', 'g//1 h//2', 
                    'success', 'g//1 h//2 i//3', 
                    'success', 'g//1 h//2 j//2', 
                    'success', 'g//1 k//1', 
                    'success', 'l//0']
        self.assertTrue(TestUtils.check(input, expected, 308))

    def test_209(self):
        input = [
            "INSERT m string", "PRINT",
            "BEGIN", "INSERT n number", "PRINT",
            "INSERT o string",
            "BEGIN", "INSERT p number", "PRINT",
            "END", "PRINT",
            "END", "PRINT"
        ]
        expected = ['success', 'm//0', 
                    'success', 'm//0 n//1', 
                    'success', 
                    'success', 'm//0 n//1 o//1 p//2', 
                    'm//0 n//1 o//1', 
                    'm//0']
        self.assertTrue(TestUtils.check(input, expected, 309))

    def test_210(self):
        input = [
            "INSERT a string", "RPRINT",
            "BEGIN", "INSERT b number", "RPRINT",
            "BEGIN", "INSERT c string", "RPRINT",
            "END", "INSERT d number", "RPRINT",
            "END", "INSERT e string", "RPRINT"
        ]
        expected = ['success', 'a//0', 
                    'success', 'b//1 a//0', 
                    'success', 'c//2 b//1 a//0', 
                    'success', 'd//1 b//1 a//0', 
                    'success', 'e//0 a//0']
        self.assertTrue(TestUtils.check(input, expected, 310))

    def test_211(self):
        input = [
            "BEGIN", "INSERT f string", "RPRINT",
            "BEGIN", "INSERT g number", "RPRINT",
            "INSERT h string",
            "END", "RPRINT",
            "END", "RPRINT" 
        ]
        expected = ['success', 'f//1', 
                    'success', 'g//2 f//1', 
                    'success', 
                    'f//1', ''
                    ]
        self.assertTrue(TestUtils.check(input, expected, 311))

    def test_212(self):
        input = [
            "INSERT i number", "RPRINT",
            "BEGIN", "INSERT j string", "RPRINT",
            "BEGIN", "INSERT k string", "RPRINT",
            "END", "INSERT l number", "RPRINT",
            "END", "INSERT m string", "RPRINT"
        ]
        expected = ['success', 'i//0', 
                    'success', 'j//1 i//0', 
                    'success', 'k//2 j//1 i//0', 
                    'success', 'l//1 j//1 i//0', 
                    'success', 'm//0 i//0']
        self.assertTrue(TestUtils.check(input, expected, 312))

    def test_213(self):
        input = [
            "BEGIN", "INSERT n string", "RPRINT",
            "INSERT o number", 
            "BEGIN", "INSERT p string", "RPRINT",
            "END", "RPRINT",
            "END", "RPRINT" 
        ]
        expected = ['success', 'n//1', 
                    'success', 
                    'success', 'p//2 o//1 n//1', 
                    'o//1 n//1','' 
                    ] 
        self.assertTrue(TestUtils.check(input, expected, 313))

    def test_214(self):
        input = [
            "INSERT q number", "RPRINT",
            "BEGIN", "INSERT r string", "RPRINT",
            "BEGIN", "INSERT s string", "RPRINT",
            "END", "INSERT t number", "RPRINT",
            "END", "INSERT u string", "RPRINT"
        ]
        expected = ['success', 'q//0', 
                    'success', 'r//1 q//0', 
                    'success', 's//2 r//1 q//0', 
                    'success', 't//1 r//1 q//0', 
                    'success', 'u//0 q//0']
        self.assertTrue(TestUtils.check(input, expected, 314))

    def test_215(self):
        input = [
            "BEGIN", "INSERT v string", "RPRINT",
            "BEGIN", "INSERT w number", "RPRINT",
            "BEGIN", "INSERT x string", "RPRINT",
            "END", "INSERT y number", "RPRINT",
            "END", "INSERT z string", "RPRINT",
            "END", "INSERT aa number", "RPRINT"
        ]
        expected = ['success', 'v//1', 
                    'success', 'w//2 v//1', 
                    'success', 'x//3 w//2 v//1', 
                    'success', 'y//2 w//2 v//1', 
                    'success', 'z//1 v//1', 
                    'success', 'aa//0']
        self.assertTrue(TestUtils.check(input, expected, 315))

    def test_216(self):
        input = [
            "INSERT ab string", "RPRINT",
            "BEGIN", "INSERT ac number", "RPRINT",
            "BEGIN", "INSERT ad string", "RPRINT",
            "END", "INSERT ae number", "RPRINT",
            "END", "INSERT af string", "RPRINT"
        ]
        expected = ['success', 'ab//0', 
                    'success', 'ac//1 ab//0', 
                    'success', 'ad//2 ac//1 ab//0', 
                    'success', 'ae//1 ac//1 ab//0', 
                    'success', 'af//0 ab//0']
        self.assertTrue(TestUtils.check(input, expected, 316))

    def test_217(self):
        input = [
            "BEGIN", "INSERT ag string", "RPRINT",
            "INSERT ah number", 
            "BEGIN", "INSERT ai string", "RPRINT",
            "END", "INSERT aj number", "RPRINT",
            "END", "INSERT ak string", "RPRINT"
        ]
        expected = ['success', 'ag//1', 
                    'success', 
                    'success', 'ai//2 ah//1 ag//1',
                    'success', 'aj//1 ah//1 ag//1', 
                    'success', 'ak//0']
        self.assertTrue(TestUtils.check(input, expected, 317))

    def test_218(self):
        input = [
            "INSERT al number", "RPRINT",
            "BEGIN", "INSERT am string", "RPRINT",
            "INSERT an number",
            "BEGIN", "INSERT ao string", "RPRINT",
            "END", "RPRINT",
            "END", "RPRINT"
        ]
        expected = ['success', 'al//0', 
                    'success', 'am//1 al//0', 
                    'success', 
                    'success', 'ao//2 an//1 am//1 al//0', 
                    'an//1 am//1 al//0', 
                    'al//0']
        self.assertTrue(TestUtils.check(input, expected, 318))

    def test_219(self):
        input = [
            "BEGIN", "INSERT ap string", "RPRINT", 
            "BEGIN", "INSERT aq number", "RPRINT", 
            "BEGIN", "INSERT ar string", "RPRINT", 
            "END", "INSERT as number", "RPRINT",
            "END", "INSERT at string", "RPRINT", 
            "END", "INSERT au number", "RPRINT" 
        ]
        expected = [ 
            "success", "ap//1",   
            "success", "aq//2 ap//1",  
            "success", "ar//3 aq//2 ap//1",
            "success", "as//2 aq//2 ap//1",
            "success", "at//1 ap//1",   
            "success", "au//0"             
        ]
        self.assertTrue(TestUtils.check(input, expected, 319))
    
    def test_220(self):
        input = []
        expected = [""]
        self.assertTrue(TestUtils.check(input, expected, 320))

    def test_221(self):
        input = ["INSERT"]
        expected = ["Invalid: INSERT"]
        self.assertTrue(TestUtils.check(input, expected, 321))

    def test_222(self):
        input = ["ASSIGN"]
        expected = ["Invalid: ASSIGN"]
        self.assertTrue(TestUtils.check(input, expected, 322))

    def test_223(self):
        input = ["LOOKUP"]
        expected = ["Invalid: LOOKUP"]
        self.assertTrue(TestUtils.check(input, expected, 323))

    def test_224(self):
        input = ["PRINT"]
        expected = [""]
        self.assertTrue(TestUtils.check(input, expected, 324))

    def test_225(self):
        input = ["RPRINT"]
        expected = [""]
        self.assertTrue(TestUtils.check(input, expected, 325))

    def test_226(self):
        input = ["BEGIN", "BEGIN"]
        expected = ["UnclosedBlock: 2"]
        self.assertTrue(TestUtils.check(input, expected, 326))

    def test_227(self):
        input = ["END"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 327))

    def test_228(self):
        input = ["INSERT x number", 
                 "BEGIN", "INSERT x number" ,
                 "END", 
                 "BEGIN", "LOOKUP x", "END"]
        expected = ["success", "success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 328))

    def test_229(self):
        input = ["INSERT x string", "ASSIGN x ''"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 329))

    def test_230(self):
        input = ["BEGIN", "BEGIN", "BEGIN", "END"]
        expected = ["UnclosedBlock: 2"]
        self.assertTrue(TestUtils.check(input, expected, 330))

    def test_231(self):
        input = ["BEGIN", "BEGIN", "END", "END", "END"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 331))

    def test_232(self):
        input = ["INSERT a number", 
                 "BEGIN", "INSERT a string", 
                 "BEGIN", "INSERT a number", "ASSIGN a 'hello'", 
                 "END", "ASSIGN a 1"]
        expected = ["TypeMismatch: ASSIGN a 'hello'"]
        self.assertTrue(TestUtils.check(input, expected, 332))

    def test_233(self):
        input = ["INSERT a number", "ASSIGN a 'himom'", "LOOKUP a"]
        expected = ["TypeMismatch: ASSIGN a 'himom'"]
        self.assertTrue(TestUtils.check(input, expected, 333))

    def test_234(self):
        input = ["INSERT x number", "INSERT x number"]
        expected = ["Redeclared: INSERT x number"]
        self.assertTrue(TestUtils.check(input, expected, 334))

    def test_235(self):
        input = ["INSERT a string", "BEGIN", "ASSIGN b a"]
        expected = ["Undeclared: ASSIGN b a"]
        self.assertTrue(TestUtils.check(input, expected, 335))

    def test_236(self):
        input = ["INSERT a number", "ASSIGN a 1a"]
        expected = ["Invalid: ASSIGN a 1a"]
        self.assertTrue(TestUtils.check(input, expected, 336))

    def test_237(self):
        input = ["INSERT a number", "ASSIGN a 'abcxyz'"]
        expected = ["TypeMismatch: ASSIGN a 'abcxyz'"]
        self.assertTrue(TestUtils.check(input, expected, 337))

    def test_238(self):
        input = ["BEGIN", "BEGIN", "BEGIN", "END"]
        expected = ["UnclosedBlock: 2"]
        self.assertTrue(TestUtils.check(input, expected, 338))

    def test_239(self):
        input = ["INSERT a string", "LOOKUP a", "LOOKUP b"]
        expected = ["Undeclared: LOOKUP b"]
        self.assertTrue(TestUtils.check(input, expected, 339))

    def test_240(self):
        input = ["INSERT 1number string"]
        expected = ["Invalid: INSERT 1number string"]
        self.assertTrue(TestUtils.check(input, expected, 340))
    
    def test_241(self):
        input = ["INSERT a number", "PRINT", "RPRINT"]
        expected = ["success", "a//0", "a//0"]
        self.assertTrue(TestUtils.check(input, expected, 341))

    def test_242(self):
        input = ["INSERT a number", 
                 "BEGIN", "INSERT b string", 
                 "END",
                 "PRINT", "RPRINT"]
        expected = ["success", "success", "a//0", "a//0"]
        self.assertTrue(TestUtils.check(input, expected, 342))

    def test_243(self):
        input = ["INSERT a number", 
                 "BEGIN", "INSERT b string", "PRINT",
                 "END", "RPRINT"]
        expected = ["success", "success", "a//0 b//1", "a//0"]
        self.assertTrue(TestUtils.check(input, expected, 343))

    def test_244(self):
        input = ["INSERT a number", 
                 "BEGIN", "INSERT b string", "PRINT", "RPRINT", 
                 "END"]
        expected = ["success", "success", "a//0 b//1", "b//1 a//0"]
        self.assertTrue(TestUtils.check(input, expected, 344))    

    def test_245(self):
        input = ["BEGIN", "INSERT a string", 
                 "BEGIN", "INSERT a number", "PRINT",
                 "END", "PRINT",
                 "END"]
        expected = ["success", "success", "a//2", "a//1"]
        self.assertTrue(TestUtils.check(input, expected, 345))

    def test_246(self):
        input = ["BEGIN", "INSERT a string", 
                 "BEGIN", "INSERT a string", "PRINT",
                 "END", "PRINT",
                 "END"]
        expected = ["success", "success", "a//2", "a//1"]
        self.assertTrue(TestUtils.check(input, expected, 346))

    def test_247(self):
        input = ["BEGIN", "INSERT a number", 
                 "BEGIN", "INSERT a number", "RPRINT",
                 "END", "RPRINT",
                 "END"]
        expected = ["success", "success", "a//2", "a//1"]
        self.assertTrue(TestUtils.check(input, expected, 347))

    def test_248(self):
        input = ["BEGIN", "INSERT a number", 
                 "BEGIN", "INSERT a string", "RPRINT",
                 "END", "RPRINT",
                 "END"]
        expected = ["success", "success", "a//2", "a//1"]
        self.assertTrue(TestUtils.check(input, expected, 348))
    
    def test_249(self):
        input = ["BEGIN", "INSERT a number", 
                 "BEGIN", "INSERT a string", "PRINT",
                 "END", "RPRINT",
                 "END"]
        expected = ["success", "success", "a//2", "a//1"]
        self.assertTrue(TestUtils.check(input, expected, 349))

    def test_250(self):
        input = ["BEGIN", "INSERT a string", 
                 "BEGIN", "INSERT a number", "RPRINT",
                 "END", "PRINT",
                 "END"]
        expected = ["success", "success", "a//2", "a//1"]
        self.assertTrue(TestUtils.check(input, expected, 350))

    def test_251(self):
            input = [
                "BEGIN", "INSERT g string", "PRINT", "RPRINT", 
                "BEGIN", "INSERT h number", "PRINT", "RPRINT",
                "BEGIN", "INSERT i string", "PRINT", "RPRINT",
                "END", "INSERT j number", "PRINT", "RPRINT",
                "END", "INSERT k string", "PRINT", "RPRINT",
                "END", "INSERT l number", "PRINT", "RPRINT"
            ]
            expected = ['success', 'g//1', 'g//1',
                        'success', 'g//1 h//2', 'h//2 g//1',
                        'success', 'g//1 h//2 i//3', 'i//3 h//2 g//1',
                        'success', 'g//1 h//2 j//2', 'j//2 h//2 g//1',
                        'success', 'g//1 k//1', 'k//1 g//1',
                        'success', 'l//0', 'l//0']
            self.assertTrue(TestUtils.check(input, expected, 351))
    
    def test_252(self):
            input = ["PRINT", "RPRINT"]
            expected = ["", ""]
            self.assertTrue(TestUtils.check(input, expected, 352))

    def test_253(self):
            input = ["INSERT a number", "PRINT", "RPRINT"]
            expected = ["success", "a//0", "a//0"]
            self.assertTrue(TestUtils.check(input, expected, 353))

