#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3


def conectar():

    """Se conecta con la base de datos"""
    con = sqlite3.connect('movies.db')
    con.row_factory = sqlite3.Row
    return con


def obtener_peliculas():

    """Obtiene todos las peliculas de la base de datos"""
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM movies"
    resultado = c.execute(query)
    productos = resultado.fetchall()
    con.close()
    return productos

def obtener_una_pelicula(nombre):

    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM movies WHERE title = ?"
    resultado = c.execute(query, [nombre])
    peliculas = resultado.fetchall()
    return peliculas

def arriba_ranking(pelicula):

    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM movies WHERE title = ?"
    resultado = c.execute(query, [pelicula])
    pelicula_1 = resultado.fetchall() # Pelicula a la que quiero subir ranking
    ranking_pelicula_1 = pelicula_1[0][8]
    ranking_pelicula_2 = ranking_pelicula_1 - 1
    query = "SELECT * FROM movies WHERE ranking = ?"
    resultado_2 = c.execute(query, [ranking_pelicula_2])
    pelicula_2 = resultado_2.fetchall() # Pelicula a la que quiero bajar ranking
    query = "UPDATE movies SET ranking = \"{0}\" WHERE title = \"{1}\"".format(ranking_pelicula_2,pelicula_1[0][1])
    c.execute(query)
    query_2 = "UPDATE movies SET ranking = \"{0}\" WHERE title = \"{1}\"".format(ranking_pelicula_1,pelicula_2[0][1])
    c.execute(query_2)
    con.commit()
    con.close()

def abajo_ranking(pelicula):

    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM movies WHERE title = ?"
    resultado = c.execute(query, [pelicula])
    pelicula_1 = resultado.fetchall() # Pelicula a la que quiero subir ranking
    ranking_pelicula_1 = pelicula_1[0][8]
    ranking_pelicula_2 = ranking_pelicula_1 + 1
    query = "SELECT * FROM movies WHERE ranking = ?"
    resultado_2 = c.execute(query, [ranking_pelicula_2])
    pelicula_2 = resultado_2.fetchall() # Pelicula a la que quiero bajar ranking
    query = "UPDATE movies SET ranking = \"{0}\" WHERE title = \"{1}\"".format(ranking_pelicula_2,pelicula_1[0][1])
    c.execute(query)
    query_2 = "UPDATE movies SET ranking = \"{0}\" WHERE title = \"{1}\"".format(ranking_pelicula_1,pelicula_2[0][1])
    c.execute(query_2)
    con.commit()
    con.close()