from re import findall, sub

flag_candidate = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "1234567890"

first_command = '(case && (== $fEqInt (ord (!! first num0)) (I# 70)) (&& (== $fEqInt (ord (!! first num1)) (I# 108)) (&& (== $fEqInt (ord (!! first num2)) (I# 97)) (&& (== $fEqInt (ord (!! first num3)) (I# 103)) (&& (== $fEqInt (ord (!! first num4)) (I# 123)) (&& (== $fEqInt (ord (!! first num5)) (I# 83)) (&& (== $fEqInt (ord (!! first num6)) (I# 48)) (&& (== $fEqInt (ord (!! first num7)) (I# 109)) (&& (== $fEqInt (ord (!! first num8)) (I# 101)) (&& (== $fEqInt (ord (!! first num9)) (I# 48)) (&& (== $fEqInt (ord (!! first (I# 10))) (I# 102)) (&& (== $fEqInt (ord (!! first (I# 11))) (I# 85)) (== $fEqInt (ord (!! first (I# 12))) (I# 53))))))))))))) of'
second_command = 'c1ni_info_case_tag_DEFAULT_arg_0@_DEFAULT -> case == ($fEq[] $fEqChar) (reverse second) (: (C# 103) (: (C# 110) (: (C# 105) (: (C# 107) (: char0 (: char0 (: (C# 76) (: (C# 51) (: (C# 114) (: (C# 52) [])))))))))) of'
third_command = 'True -> case && (== $fEqChar (!! third num0) (!! uppercase num0)) (&& (== $fEqChar (!! third num1) (!! lowercase (I# 19))) (&& (== $fEqChar (!! third num2) (!! uppercase (I# 19))) (&& (== $fEqChar (!! third num3) (!! lowercase num7)) (&& (== $fEqChar (!! third num4) (!! digits num2)) (&& (== $fEqChar (!! third num5) (!! uppercase (I# 18))) (&& (== $fEqChar (!! third num6) (!! lowercase (I# 19))) (&& (== $fEqChar (!! third num7) (!! digits num3)) (&& (== $fEqChar (!! third num8) (!! lowercase (I# 17))) (== $fEqChar (!! third num9) (!! lowercase (I# 18))))))))))) of'

# (I# 'x')
m = findall(r'\)\)\s+\(I#\s+(\d+)\)', first_command)
first = ''.join(map(chr, map(int, m)))

# (C# 'x') / char0
m = findall(r'\(C#\s+(\d+)\)', second_command.replace('char0', '(C# 48)'))
second = ''.join(map(chr, map(int, m)))[::-1]

# (!! array1 index1) (!! 'array2' 'index2')
sub(r'num(\d)', r'\(I# \1\)', third_command)
m = findall(r'fEqChar\s+\(!![^!]+!!\s+([^\s]+)\s+\(I#\s+(\d+)\)\)', third_command)
third = ''.join([globals()[name][int(idx)] for (name, idx) in m])

print('#'.join([first, second, third]))