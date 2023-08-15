# Importamos las librerias que vamos a utilizar
import sqlite3
import csv
import datetime


# Generamos la tabla donde guardaremos la informacion
def create_news_table():
    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS noticias(
                   id INTEGER PRIMARY KEY,
                   titulo TEXT NOT NULL,
                   url_noticia TEXT NOT NULL,
                   medio TEXT NOT NULL
                   )
                   """)
    
    conn.commit()
    conn.close()

# Leemos el archivo CSV donde tenemos la informacion
def read_csv_file(csv_file):
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

# Guardamos la informacion en la base de datos
def insert_data_to_news_table(data):
    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()

    for row in data:
        cursor.execute("""
            INSERT INTO noticias (titulo, url_noticia, medio)
            VALUES (?, ?, ?)
        """, (row["Titulo"], row["Url"], row["Medio"]))

    conn.commit()
    conn.close()


# %%
if __name__ == "__main__":
    fecha_actual = datetime.datetime.now().strftime("%d-%m-%Y") 
    file_name = f"tiempocommx-{fecha_actual}.csv"
    data_to_insert = read_csv_file(file_name) # Se manda el nombre del archivo que se va a leer y se ponen los datos disponibles
    insert_data_to_news_table(data_to_insert) # Se guardan los datos en la base de datos

# %%
if __name__ == "__main__":
    create_news_table()
# %%
