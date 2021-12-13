Main_main_closure = >> $fMonadIO
    (putStrLn (unpackCString# "Input Serial Key >>> "))
    (>>= $fMonadIO
        getLine
        (\line ->
            >> $fMonadIO
                (putStrLn (++ (unpackCString# "your serial key >>> ") (++ first (++ (unpackCString# "_") (++ second (++ (unpackCString# "_") third))))))
                (case && (== $fEqInt (ord (!! first num0)) (I# 70)) (&& (== $fEqInt (ord (!! first num1)) (I# 108)) (&& (== $fEqInt (ord (!! first num2)) (I# 97)) (&& (== $fEqInt (ord (!! first num3)) (I# 103)) (&& (== $fEqInt (ord (!! first num4)) (I# 123)) (&& (== $fEqInt (ord (!! first num5)) (I# 83)) (&& (== $fEqInt (ord (!! first num6)) (I# 48)) (&& (== $fEqInt (ord (!! first num7)) (I# 109)) (&& (== $fEqInt (ord (!! first num8)) (I# 101)) (&& (== $fEqInt (ord (!! first num9)) (I# 48)) (&& (== $fEqInt (ord (!! first (I# 10))) (I# 102)) (&& (== $fEqInt (ord (!! first (I# 11))) (I# 85)) (== $fEqInt (ord (!! first (I# 12))) (I# 53))))))))))))) of
                    <tag 1> -> putStrLn (unpackCString# ":p"),
                    c1ni_info_case_tag_DEFAULT_arg_0@_DEFAULT -> case == ($fEq[] $fEqChar) (reverse second) (: (C# 103) (: (C# 110) (: (C# 105) (: (C# 107) (: char0 (: char0 (: (C# 76) (: (C# 51) (: (C# 114) (: (C# 52) [])))))))))) of
                        False -> putStrLn (unpackCString# ":p"),
                        True -> case && (== $fEqChar (!! third num0) (!! uppercase num0)) (&& (== $fEqChar (!! third num1) (!! lowercase (I# 19))) (&& (== $fEqChar (!! third num2) (!! uppercase (I# 19))) (&& (== $fEqChar (!! third num3) (!! lowercase num7)) (&& (== $fEqChar (!! third num4) (!! digits num2)) (&& (== $fEqChar (!! third num5) (!! uppercase (I# 18))) (&& (== $fEqChar (!! third num6) (!! lowercase (I# 19))) (&& (== $fEqChar (!! third num7) (!! digits num3)) (&& (== $fEqChar (!! third num8) (!! lowercase (I# 17))) (== $fEqChar (!! third num9) (!! lowercase (I# 18))))))))))) of
                            <tag 1> -> putStrLn (unpackCString# ":p"),
                            c1tb_info_case_tag_DEFAULT_arg_0@_DEFAULT -> putStrLn (unpackCString# "Correct Serial Key! Auth Flag!")
                )
        )
    )

lowercase = unpackCString# "abcdefghijklmnopqrstuvwxyz"
uppercase = unpackCString# "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = unpackCString# "1234567890"

num0 = I# 0
num1 = I# 1
num2 = I# 2
num3 = I# 3
num4 = I# 4
num5 = I# 5
num6 = I# 6
num7 = I# 7
num8 = I# 8
num9 = I# 9
char0 = C# 48

wordlist = splitOn $fEqChar (unpackCString# "#") line
first = !! wordlist num0
second = !! wordlist num1
third = !! wordlist num2
