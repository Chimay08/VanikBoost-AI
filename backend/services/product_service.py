from backend.database import get_connection


def create_product(product):
    connection = get_connection()
    query = """
        INSERT INTO products
        (store_id, name, category, cost_price, selling_price, stock)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id, name, category, cost_price, selling_price, stock;
    """

    with connection.cursor() as cursor:
        cursor.execute(
            query,
            (
                1,
                product.name,
                product.category,
                product.cost_price,
                product.selling_price,
                product.stock,
            )
        )

        result = cursor.fetchone()
        connection.commit()

    return result


def get_products():
    connection = get_connection()
    query = """
        SELECT id, name, category, cost_price, selling_price, stock
        FROM products
        WHERE store_id = %s;
    """

    with connection.cursor() as cursor:
        cursor.execute(query, (1,))
        result = cursor.fetchall()

    return result
