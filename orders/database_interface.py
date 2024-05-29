import sqlite3




def get_order(id: int) -> tuple:
        '''gets name, pickUpTime, items from orders'''
        query = "select name, pickUpTime, items from orders where id = ?"
        with sqlite3.connect('main.db') as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, (id)).fetchone()
        return result
    
    
def create_order(name: str, pickUpTime: str, pickUpTimeInt: int, items: str) -> int:
        '''inserts name, pickUpTime, items into orders'''
        query = "insert into orders (name, pickUpTime, pickUpTimeNumber, items) values (?, ?, ?, ?)"
        with sqlite3.connect('main.db') as conn:
            cursor = conn.cursor()
            cursor.execute(query, (name, pickUpTime, pickUpTimeInt, items))
        return cursor.lastrowid
    
    
def update_order(name: str, pickUpTime: int, items: str, id: int) -> int:
        '''updates name, pickUpTime, items in orders table'''
        query = "update orders set name = ?, pickUpTime = ?, items = ? where id = ?"
        with sqlite3.connect('main.db') as conn:
            cursor = conn.cursor()
            cursor.execute(query, name, pickUpTime, items, id)
    
    
def delete_order(id: int):
        query = "delete from orders where id = ?"
        with sqlite3.connect('main.db') as conn:
            cursor = conn.cursor()
            cursor.execute(query, (id))
                
    

def get_all_orders() -> list[tuple[int, str, int, str]]:
    '''gets all orders from orders table'''
    query = "select * from orders"
    with sqlite3.connect('main.db') as conn:
        cursor = conn.cursor()
        result = cursor.execute(query).fetchall()
    return result



