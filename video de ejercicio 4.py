#video cuatro
100/5
20.0
type(100/5)
#<class "float">
7/2
3.5
7//2
3
7%2
1
type(7//2)
#<class"int">
"a"
"a"
type("a")
#<class "str">
"tiza"+"."
"tiza."
type ("tiza"+".")
#<class "str">
"hola "[1+1]
"1"
type ("hola"[1+1])
#<class "str">
len("hola")
4
type(len("hola"))
#<class"int">
int("145")
145
type(int("145"))
#<class "int">
float("145")
#<class"int>
float("145")
#145.0
float(145)
str(32)
"32"
type(str(32))
#<class "str"
1+2!=3
#false
177%2==0
#false
177%2
1
1==0
#false 
type(177%2==0)
#<class"bool">
len("nube")<=20
#true
len("nube")
#4
4<=20
#true

##¿que guardan las variables luego de cada operaciones?
#n=167/10
#n
#16.7
n=167//10
n
#16
n=167%10
n
7
167%100
67
167%1000
167
letra="a"
letra
"a"
type(letra)
#<class "str">
saludo="hola"+letra
saludo
"holaa"
c=saludo[0]
c
"h"
c=saludo[1+3]
c
"a"
L=len(saludo)
L
5
c=saludo[len(saludo)-1]
c
"a"
menor="a"<"b"
menor
#true
D=1!=1
D
#false
D="cinta">="canto"
D
#true
c="z"+"a"+"paz"[0]
c
"zap"
x=c[0]=="z"
x
#true

#¿CUALES DE LAS SIGUIENTES OPERACIONES ARROJAN ERROR?
11-(4%2+10)
1
"30"+2
"30"+"2"
#"302"
"hola"[len("hola")]
len(124)
"hola"[len("fin")]
"a"
"hola"[11-(4%2+10)]
"o"
int("4")
#4
int(4)
4
int("z")
int("4.")
4<"f"
"palabra"=="rama"
#false