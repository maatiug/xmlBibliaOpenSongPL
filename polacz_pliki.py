#-*-coding: cp1250-*-
###########################################
# Plik łączy dwa pliki ze sobą łącząc każdy werset ze sobą
#
# - Jeśli w drugim przekladzie jest wiecej wersetow dopisuje je do ostatniego wersetu w rozdziale.
# -
# Autor: Górka Mateusz
###########################################

# Nazwy pliku
plikA = "PBW"       # Nazwa 1. pliku
plikB = "KJV"       # Nazwa 2. pliku

# Ograniczniki
znacznikPrzod = "|["    # Znacznik przed tekstem wersetu z 2. pliku ( | - wymusza przelamanie linii)
znacznikTyl = "]"       # Znacnzik po tekście wersetu z 2. pliku

###################################################################
from lxml import etree

# Wczytywanie XML
xmlA_tree = etree.parse( plikA )
xmlB_tree = etree.parse( plikB )

xmlB = xmlB_tree.getroot()
xmlA = xmlA_tree.getroot()

# XML wyjsciowy
plikOut = plikA + "_i_" + plikB
out = etree.Element('bible')

# Laczenie i porownywnaie plikow
if len( xmlB ) == len( xmlA ):

    # Petla po ksiegach --------------------------------------------
    for b in range( 0, len(xmlB) ):
        book = etree.SubElement( out, 'b', n=xmlA[b].attrib['n'] )

        if len( xmlB[b] ) != len( xmlA[b] ):
            print("Error: Rozna ilosc rozdzialow." )
            print(" | ", plikA, " | ", xmlA[b].attrib, " | ", len( xmlA[b] ) )
            print(" | ", plikB, " | ", xmlB[b].attrib, " | ", len( xmlB[b] ) )
            break

        # Petla po rozdzialach ------------------------------------
        for c in range( 0, len(xmlB[b]) ):
            chapter = etree.SubElement( book, 'c', n=xmlA[b][c].attrib['n'] )
            lenC_A = len( xmlA[b][c] )
            lenC_B = len( xmlB[b][c] )

            # TODO co jesli rozna ilosc rozdzialow

            # Petla po wersetach ----------------------------------
            for v in range( 0, lenC_A ) :
                verse = etree.SubElement( chapter, 'v', n=xmlA[b][c][v].attrib['n'] )

                if v < lenC_A : stringA = xmlA[b][c][v].text
                else: stringA = ""

                if v < lenC_B : stringB = znacznikPrzod + xmlB[b][c][v].text + znacznikTyl
                else: stringB = ""

                verse.text = stringA + stringB
            #_______________________________________________________

            if lenC_A != lenC_B :
                if lenC_B > lenC_A :             # Jesli w drugim przekladzie jest wiecej wersetow
                    stringB = ""
                    for v in range( lenC_A, lenC_B ) :
                        stringB = stringB + znacznikPrzod + xmlB[b][c][v].text + znacznikTyl
                    chapter[lenC_A-1].text = chapter[lenC_A-1].text + stringB
                else:                            # Jesli w pierwszym przekladzie jest wiecje werseotw
                    stringA = ""
                    for v in range( lenC_B, lenC_A ) :
                        stringA = stringA + znacznikPrzod + xmlA[b][c][v].text + znacznikTyl
                    chapter[lenC_B-1].text = chapter[lenC_B-1].text + stringA

                print("Warrning: Rozna ilosc wersetow.")
                print("| ", plikA, " | ", xmlA[b].attrib, xmlA[b][c].attrib, " | ", len( xmlA[b][c] ) )
                print("| ", plikB, " | ", xmlB[b].attrib, xmlB[b][c].attrib, " | ", len( xmlB[b][c] ) )
                print("| ", plikOut, " | ", book.attrib, chapter.attrib, " | ", len( chapter ) )

        #____________________________________________________________
else:
    print("Warrning: Rozna ilosc ksiag!")

# Zapis do pliku
etree.ElementTree(out).write( plikOut, pretty_print=True, xml_declaration=True, encoding="windows-1250")

