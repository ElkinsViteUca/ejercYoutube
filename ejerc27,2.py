import unittest

def titulo(cadena):
    nueva=""
    inicioPalabra=True #indica el incicio de una palabra
    for caracter in cadena:
        if not caracter.isalpha():
            nueva=nueva+caracter
            inicioPalabra=True
        else:
            if inicioPalabra:
                nueva=nueva+caracter.upper()
                inicioPalabra=False # ya no es el incicio de una palabra
            else:
                nueva=nueva+caracter.lower()
    return nueva

class Pruebas(unittest.TestCase):
    def test_titulo(self):
        self.assertEqual(titulo("esto es una frase","Esto es una frase","Error al cpnvertir cadena minúscula"))
        self.assertEqual(titulo("ESTO ES UNA FRASE"),"Esto Es Una Frase")
        self. assertEqual(titulo('palabra'),"Palabra")
        self.assertEqual(titulo('esto es una frase'),"   Esto Es Una Frase")
        self.assertEqual(titulo ("esto  es  una  frase"),"Esto  Es  Una  Frase")
        self.assertEqual(titulo (""),"")
        self.assertEqual(titulo(' '), ' ') 
        self.assertEqual(titulo ("123"),'123')
        self.assertEqual(titulo('-lesto 2es 3una 4frase'), '-1Esto 2Es Una 4Frase' )
        self.assertEqual(titulo ('estol es2 una3 frase4---'), 'Estol Es2 Una3 Frase4---')

if __name__=="__main__":
    unittest.main()
        