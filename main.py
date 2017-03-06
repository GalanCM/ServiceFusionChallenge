#!/usr/bin/env python

import sqlite3
import json
from flask import Flask, request

app = Flask(__name__)

# page for the main app
@app.route("/")
def main():
  with open( "views/index.html" ) as file:
    view = file.read()
  return view

# handles ajax for the persons manager
@app.route("/persons", methods=['GET', 'PUT', 'POST', 'DELETE'])
def persons():
  db = sqlite3.connect('data.db')
  db_cursor = db.cursor()
  
  if request.method == 'GET':
    persons = db_cursor.execute('SELECT * FROM persons;')

    # make dictionary of results
    results = []
    for row in persons.fetchall():
      row_result = {}
      for i in range( 0, len(row) ):
        row_result[ persons.description[i][0] ] = row[i]
        
      results.append ( row_result )
      
      db.close()
        
    return json.dumps( results )
  
  
  elif request.method == "PUT":
    db_cursor = db.cursor()
    data = json.loads( request.data.decode() )
    
    db_cursor.execute("UPDATE persons SET first_name=?, last_name=?, date_of_birth=?, zip_code=? WHERE id=?", ( data['first_name'], data['last_name'], data['date_of_birth'], data['zip_code'], str(data['id']) ) )
    update = db_cursor.execute( "SELECT * FROM persons WHERE id=?;", str(data['id']) )
    
    # make dictionary of results
    row = update.fetchone()
    result = {}
    for i in range( 0, len(row) ):
      result[ update.description[i][0] ] = row[i]
      
    db.commit()
    db.close()
      
    return json.dumps( result )
    
  elif request.method == "POST":
    db_cursor = db.cursor()
    data = json.loads( request.data.decode() )
    
    db_cursor.execute("INSERT INTO persons (first_name, last_name, date_of_birth, zip_code) VALUES (?, ?, ?, ?)", ( data['first_name'], data['last_name'], data['date_of_birth'], data['zip_code']) )
    update = db_cursor.execute( "SELECT * FROM persons WHERE id=?;", str(db_cursor.lastrowid) )
    
    # make dictionary of results
    row = update.fetchone()
    result = {}
    for i in range( 0, len(row) ):
      result[ update.description[i][0] ] = row[i]
    
    db.commit()
    db.close()
    
    return json.dumps( result )
    
  elif request.method == 'DELETE':
    db_cursor = db.cursor()
    data = json.loads( request.data.decode() )
    
    db_cursor.execute("DELETE FROM persons WHERE id=?", ( str( data['id'] ) ) )
    
    db.commit()
    db.close()
    
    return json.dumps( { 'id': data['id'] } )

if __name__ == "__main__":
  app.run()
