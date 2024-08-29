import psycopg2
import os
class InventoryDal:
    
    def get_inventory(self, sku_code):
        user =  os.getenv('DATABASE_USER')
        db_name =  os.getenv('DATABASE_NAME')
        password=  os.getenv('DATABASE_PASSWORD')
        host =  os.getenv('DATABASE_HOST', 'localhost')
        print("TTTT", user, db_name, password, host)
        conn = psycopg2.connect(dbname=db_name, user=user, password=password, host=host, port=5432)
        cur = conn.cursor()
        cur.execute("""
                    SELECT sku, edd, quantity, status
                    FROM api_inventory
                    WHERE sku = %s
                    AND quantity > 0
                        """, 
                        (sku_code,))
        results = cur.fetchall()
        print("res", results)
        return results
        