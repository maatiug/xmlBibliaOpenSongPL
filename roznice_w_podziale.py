#################################################
# Pozwala na znalezienie roznic w ilosci ksiag,
# rozdzialow i wersetow.
#
# Napisano w Python3
#
# Autor: Górka Mateusz
################################################

from lxml import etree

# Tutaj ustaw nazwy plików:
plikA = "PBW"
plikB = "KJV"

# Wczytywanie XML
xmlA_tree = etree.parse( plikA )
xmlB_tree = etree.parse( plikB )

xmlB = xmlB_tree.getroot()
xmlA = xmlA_tree.getroot()

# Porowynwanie plikow
if len( xmlB ) == len( xmlA ):

    for b in range( 0, len(xmlB) ):

        if len( xmlB[b] ) != len( xmlA[b] ):
            print("")
            print("------------Rozna ilosc rozdzialow!------------------")
            print( plikB, " | ", xmlB[b].attrib, " | ",  len( xmlB[b] ) )
            print( plikA, " | ", xmlA[b].attrib, " | ",  len( xmlA[b] ) )
            continue

        for c in range( 0, len(xmlB[b]) ):

            if len(xmlB[b][c]) != len(xmlA[b][c]) :
                print("")
                if len(xmlB[b][c]) < len(xmlA[b][c]) :
                    print("--- Rozna ilosc wersetow! ---   ", plikB, " < ", plikA )
                else:
                    print("--- Rozna ilosc wersetow! ---   ", plikB, " > ", plikA )

                print( plikB, " | ", xmlB[b].attrib, " | ", xmlB[b][c].attrib, " | ", len( xmlB[b][c] ) )
                print( plikA, " | ", xmlA[b].attrib, " | ", xmlA[b][c].attrib, " | ", len( xmlA[b][c] ) )

else:
    print("Rozna ilosc ksiag!")

