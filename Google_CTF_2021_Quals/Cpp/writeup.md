# Cpp - Google CTF 2021 Quals



#### 풀이

cpp.c 파일 하나가 주어진다. 파일을 살펴보면 6000줄이 넘는 코드가 #if, #ifdef, #define 등 전처리 지시자로 도배돼있다. 

파일 처음에 있는 FLAG_i를 define하는 부분을 적절히 수정하여, 파일 끝에 있는 main 함수가 전처리 이후에도 존재하게끔 만들면 되는 것 같았다. 

```c
#if __INCLUDE_LEVEL__ == 0
// Please type the flag:
#define FLAG_0 CHAR_C
#define FLAG_1 CHAR_T
#define FLAG_2 CHAR_F
#define FLAG_3 CHAR_LBRACE
#define FLAG_4 CHAR_w
#define FLAG_5 CHAR_r
#define FLAG_6 CHAR_i
#define FLAG_7 CHAR_t
#define FLAG_8 CHAR_e
#define FLAG_9 CHAR_UNDERSCORE
#define FLAG_10 CHAR_f
#define FLAG_11 CHAR_l
#define FLAG_12 CHAR_a
#define FLAG_13 CHAR_g
#define FLAG_14 CHAR_UNDERSCORE
#define FLAG_15 CHAR_h
#define FLAG_16 CHAR_e
#define FLAG_17 CHAR_r
#define FLAG_18 CHAR_e
#define FLAG_19 CHAR_UNDERSCORE
#define FLAG_20 CHAR_p
#define FLAG_21 CHAR_l
#define FLAG_22 CHAR_e
#define FLAG_23 CHAR_a
#define FLAG_24 CHAR_s
#define FLAG_25 CHAR_e
#define FLAG_26 CHAR_RBRACE

/* ... */

#if __INCLUDE_LEVEL__ == 0
#if S != -1
#error "Failed to execute program"
#endif
#include <stdio.h>
int main() {
printf("Key valid. Enjoy your program!\n");
printf("2+2 = %d\n", 2+2);
}
#endif
```



이대로는 읽기가 힘들어서 파이썬으로 들여쓰기와 줄바꿈을 적절히 추가했다. 

```python
with open('./cpp.c', 'r') as f:
	file = f.readlines()

with open('./indent.c', 'w') as f:
	indent = 0
	for line in file:
		if line[:5] == '#if S':
			f.write('\n')

		f.write('\t' * (indent - (line[:5] == '#else' or line[:6] == '#endif')) + line)
		
		if line[:3] == '#if':
			indent += 1
		elif line[:6] == '#endif':
			indent -= 1
```



이후 코드를 열심히 해석한다. 

- ROM_01XXXXXX_i: dump[0bXXXXXX]의 i번째 비트값이 0 또는 1로 정의된 매크로 상수
- ROM_00XXXXXX_i: FLAG[0bXXXXXX]의 i번째 비트값이 0 또는 1로 정의된 매크로 상수
- 매크로 상수 S는 프로그램 카운터 역할을 한다. S는 0부터 58까지의 값을 가질 수 있고 각각에 해당하는 코드가 있다. 
- S=0에서 시작하고, S=58이 되면 main 함수가 코드에 성공적으로 포함된다. 

S=i일 때 수행하는 코드의 내용을 분석할 때는 정규식 등을 사용해서 반복되는 부분을 단순화한다. 



S 값의 변화를 나타내보면 다음과 같다. 괄호 안의 X는 해당 코드에서 Xi 매크로 상수를 사용한다는 뜻이다. 

Xi가 define 되어 있으면 1, 그렇지 않으면 0을 저장하고 있는 것이다. Xi는 X의 i번째 비트값을 의미한다. 

```tex
0 -> 24~28 -> 29~31(B) -> 32 or 56
	32~37 -> 12~13 -> 14(X) -> 15 or 22
		15~17(Z) -> 18 or 19
			18 -> 19~21 -> 14
			19~21 -> 14

		22~23 -> 1~5(R) -> 6 or 38
			6~7(R) -> 8 or 59
				8~9(R) -> 10 or 59
					10~11 -> -1			10: BUG?
					59 -> NO
				59 -> NO
			
			38~55 -> 29~31(B) -> 32 or 56
				56(Q) -> 57 or 58
					57 -> NO
					58 -> YES

	56(Q) -> 57 or 58
		57 -> NO
		58 -> YES
```



S=i일 때의 전처리 지시자를 분석해서 위의 flow chart의 숫자 자리에 수도코드를 넣는다. 

```
// B += A
def f(B, A):
	_c = 0
	// N = 0 ~ 7
	if(_AN ^ _c) _c = _BN, _BN ^= 1

// 24~28
I = 0
M = 0
N = 1
P = 0
Q = 0

// 29~31
B = 0b11100101
f(B, I)

while(B) {
	// 32~37
	B = 0b10000000
	f(B, I)
	A = ROM[B]
	B = ROM[I]
	R = 1
	// jmp 12

	// 12~13
	X = 1
	Y = 0

	// 14(X) -> 15 -> ... -> 14
	while(X) {
		Z = X
		Z &= B
		if(Z)	f(Y, A)
		f(X, X)
		f(A, A)
	}

	// 22~23 -> 1~5
	A = Y
	R = ~R
	Z = 1
	f(R, Z)
	f(R, Z)

	// 5
	if(R) {
		// 6~

		f(R, Z)
		// 7
		if(R) {
			f(R, Z)
			// 9
			if(R) {
				// BUG
				// goto -1
			}
			else	// NO
		}
		else	// NO

		break
	}
	else {
		// 38
		O = M
		f(O, N)
		M = N
		N = O
		f(A, M)
		B = 0b00100000
		f(B, I)
		C = ROM[B]
		A ^= C
		f(P, A)
		B = 0b01000000
		f(B, I)
		A = ROM[B]
		A ^= P
		Q |= A
		A = 1
		f(I, A)

		B = 0b11100101
		f(B, I)
	}
}
// 56
if(!Q)	// YES
else	// NO
```



간결하게 정리한다. 

```
I = 0, M = 0, N = 1, P = 0, Q = 0
B = 0b11100101 + I

while(B) {
	A = ROM[0b10000000 + I]	// FLAG[I]
	B = ROM[I]

	X = 1
	Y = 0

	// Y = FLAG[I] * ROM[I]
	while(X) {
		if(B & X)	Y += A
		X += X
		A += A
	}

	A = Y
	Z = 1

	R = 1
	R = ~R
	R += 1
	R += 1
	// ~1 + 1 == -1
	// ~1 + 1 + 1 == 0
	if(R) {
		R += Z
		if(R) {
			R += Z
			if(R) {
				// BUG
				// goto -1
			}
			else	// NO
		}
		else	// NO

		break
	}
	else {
		O = M + N
		M = N
		N = O
		A += M

		B = 0b00100000 + I
		C = ROM[B]
		A ^= C
		P += A

		B = 0b01000000 + I
		A = ROM[B]
		A ^= P
		Q |= A
		A = 1
		I += 1

		B = 0b11100101 + I
	}
}
if(!Q)	// YES
else	// NO
```



FLAG를 한 글자씩 보면서 특정 조건을 만족하지 않는 순간 바로 결과가 NO가 되니 angr을 사용할 수 있다. 

실행 파일을 만들기 위해 수도코드를 바탕으로 c 코드를 작성하고 컴파일한다. (ROM 값은 파이썬으로 파싱하면 편하게 구할 수 있다)

```c
#include <stdio.h>
#include <string.h>

unsigned char FLAG[27];
unsigned ROM[] = {187, 85, 171, 197, 185, 157, 201, 105, 187, 55, 217, 205, 33, 179, 207, 207, 159, 9, 181, 61, 235, 127, 87, 161, 235, 135, 103, 35, 23, 37, 209, 27, 8, 100, 100, 53, 145, 100, 231, 160, 6, 170, 221, 117, 23, 157, 109, 92, 94, 25, 253, 233, 12, 249, 180, 131, 134, 34, 66, 30, 87, 161, 40, 98, 250, 123, 27, 186, 30, 180, 179, 88, 198, 243, 140, 144, 59, 186, 25, 110, 206, 223, 241, 37, 141, 64, 128, 112, 224, 77, 28, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
unsigned char I = 0, M = 0, N = 1, P = 0, Q = 0, A, B, O;

int main(void) {
	scanf("%s", FLAG);
	if(strlen(FLAG) != 27) {
		puts("NO");
		return 0;
	}
	B = 0b11100101 + I;
	while(B) {
		O = M + N;
		M = N;
		N = O;

		P += (FLAG[I] * ROM[I] + M) ^ ROM[0b00100000 + I];

		if(ROM[0b01000000 + I] ^ P) {
			puts("NO");
			return 0;
		}
		I += 1;
		B = 0b11100101 + I;
	}
	puts("YES");
	return 0;
}
```



angr을 사용해 FLAG를 구한다. 

```
import angr

proj = angr.Project('./c.exe', load_options = {'auto_load_libs': False})

find_addr = 0x00000000004016EF
avoid_addr = [0x0000000000401598, 0x00000000004016A7]

state = proj.factory.entry_state()
sm = proj.factory.simulation_manager(state)
sm.explore(find = find_addr, avoid = avoid_addr)

if len(sm.found) > 0:
	print(f'[{sm.found[0].posix.dumps(0)}]')
else:
	print('not found')
```



#### 요약

1. python으로 indent 넣기
2. 전체적인 코드 파악하기
3. 정규식으로 반복되는 구조 파악하기
4. S의 flow chart 만들기
5. flow chart 바탕으로 수도코드 짜고 정리하기
6. c 코드 짜기
7. angr 써서 flag 구하기
