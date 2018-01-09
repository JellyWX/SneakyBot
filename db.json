I just thought I'd give you examples of the code for the database.




## New Table
import sqlite3

conn = sqlite3.connect('Database.db')
c = conn.cursor()

def create_table():
  c.execute("CREATE TABLE IF NOT EXISTS TableName(normaltext TEXT, number INTEGER)")
create_table()
##



## Inserting Into The DB

def insert(stl):
  c.execute(stl)
  conn.commit()
  
stl = "INSERT INTO TableName (column1, stuff, anotherone) VALUES ('" + use-this-if-it's-an-defined-value +"', use-this-if-not)
insert(stl) #This inserts it.
##

## Selecting from the DB

def select(sel):
  c.execute(sel)
  conn.commit()
  
sel = "SELECT * FROM TableName"
#* to select everything
sel = "SELECT stuff FROM TableName"
#stuff will be only selected
sel = "SELECT stuff FROM TableName WHERE user_id = '" + ctx.message.author.id + "'"
#stuff will be selected where the user_id is equals to the author of the message.

select(sel)
##


## Deleting from the DB

def delete(del):
  c.execute(del)
  conn.commit()
  
del = "DELETE * FROM TableName"
#* will delete everything
del = "DELETE stuff FROM TableName"
#stuff will get deleted
del = "DELETE stuff FROM TableName WHERE state = california"
#stuff will get deleted where the state is california
##


## Using it in commands

def use(us):
  c.execute(us)
  conn.commit()

@bot.command()
async def test():
  us = "SELECT * FROM TableName"
  use(us)
  await bot.say(us)
##




### That's the basic stuff, have fun.
