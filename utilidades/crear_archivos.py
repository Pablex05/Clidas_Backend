lista =[
    "Examen_Microscopico_Epitelial",
    "Examen_Microscopico_Leucocitos",
    "Examen_Microscopico_Hematies",
    "Examen_Microscopico_Cilindros",
    "Examen_Microscopico_Mucus",
    "Examen_Microscopico_Cristales",
    "Examen_Microscopico_Germenes",
    "Examen_Fisico_Reaccion",
    "Examen_Fisico_Aspecto",
    "Bilirrubina_Total",
    "Bilirrubina_Directa",
    "Bilirrubina_Indirecta",
    "Fosfatasa_Alcalina_Recien_Nacido",
    "Fosfatasa_Alcalina_Bebe",
    "Fosfatasa_Alcalina_Ninio",
    "Fosfatasa_Alcalina_Adulto",
    "Glutamico_Piruvica_Hombre",
    "Glutamico_Piruvica_Mujer",
    "Glutamico_Oxalacetica_Hombre",
    "Glutamico_Oxalacetica_Mujer",
    "Trigliceridos",
    "Colesterol_Total",
    "Hdl_Hombre",
    "Hdl_Mujer",
    "Ldl",
    "Creatinina",
    "Urea",
    "Glucosa",
    "Globulos_Rojos_Total_Mujer",
    "Globulos_Rojos_Total_Hombre",
    "Hematocritos_Hombre",
    "Hematocritos_Mujer",
    "Hemoglobina_G_Hombre",
    "Hemoglobina_G_Mujer",
    "Serie_Roja_Aspecto",
    "Leucocitos",
    "Neutrofilos_Cayado",
    "Neutrofilos_Segmentado",
    "Eosinofilos",
    "Basofilos",
    "Linfocitos",
    "Monocitos"
]

for i in lista:
    b = i.lower()
    a = open(f'{b}.py', "w")
    a.close()
"""
a = open(f'nombres.txt', "w")
for i in lista:
    b = i.lower()
    a.write(f'{b}')
    a.write('\n')
a.close()
"""