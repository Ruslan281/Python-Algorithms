columns = ("8", "7", "6", "5", "4", "3", "2", "1")
rows = ("a", "b", "c", "d", "e", "f", "g", "h")

# Şahmat taxtasını yaradırıq
board = []

# Koordinantları yaradırıq.
for number in columns:
    row = []
    for letter in rows:
        coordinate = letter + number
        row.append(coordinate)
    board.append(row)

# Şahmat taxtasını yazdıraq.
for row in board:
    print(row)

    
# İndi ise Şahın ve Topun koordinatlarını teleb edek.
# Bunun üçün bir funksiya yazaq
def talep_et(message):
    _input = input(message)
    # Daxil edilen koordinant uygundurmu deye kontrol edek.
    if (_input[0] in rows) and (_input[1] in columns):
        
        row = rows.index(_input[0])
        column = columns.index(_input[1])
        return {"row": row, "column": column}
    else:
        # Uyğun deyilse mesaj verdirek.
        raise ValueError("Koordinant yalnışdır!")


king = talep_et("Şahın Koordinatı: ")
rook = talep_et("Topun Koordinatı: ")

# Son olaraq, tehdid veziyyetinin olub olmadığını kontrol edek.
# Bunun üçün yeni bir funksiya yazaq.
def kontrol_et(king, rook):
    # tehdid veziyyeti 0 ise "ROOK", 1 ise "KING", 2 ise "NOBODY" yazdıraq.
    threat = 2
    
    # Eger top ve şahın koordinat melumatlarindaki herf eynidirse
    # ve ya her ikisinin de sayı deyeri eynidirse şah üçün tehdid vardir.
    if king["row"] == rook["row"]:
        threat = 0
    elif king["column"] == rook["column"]:
        threat = 0
        
    # Eger şah ile top arasındaki max uzaqlıq 1 vahid ise top üçün tehdiddir.
    distance = max((abs(king["row"] - rook["row"]), abs(king["column"] - rook["column"])))
    if distance == 1:
        threat = 1

    output = ("ROOK", "KING", "NOBODY")
    
    print(output[threat])

kontrol_et(king, rook)
