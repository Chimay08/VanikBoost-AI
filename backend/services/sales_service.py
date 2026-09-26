from backend.database import get_connection


def create_sale(product_id: int, quantity: int):
    connection = get_connection()

    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT id, name, cost_price, selling_price, stock
            FROM products
            WHERE id = %s
            """,
            (product_id,),
        )
        product = cursor.fetchone()

    if product is None:
        return {
            "error": "Product not found"
        }
