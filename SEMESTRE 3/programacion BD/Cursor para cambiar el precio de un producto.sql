/* -----------------------------------------
-- Crear un procedimiento almacenado que utiliza un cursor para cambiar el precio de los productos.
-- Declarar el Cursor
-- -----------------------------------------
*/

DELIMITER //
CREATE PROCEDURE CambiarPrecioProductos()
BEGIN
    -- Declarar el cursor
    DECLARE cursor_productos CURSOR FOR
    SELECT idProducto, valorVenta
    FROM productos;

    -- Variables para mantener el estado del producto
    DECLARE ing_producto_id INT;
    DECLARE ing_nuevo_precio INT;

    -- Abrir el cursor
    OPEN cursor_productos;

    -- Iniciar bucle para recorrer los productos
    FETCH cursor_productos INTO ing_producto_id, ing_nuevo_precio;
    WHILE @@FETCH_STATUS = 0 DO
        -- Realizar la modificación del precio (aumentar en un 10%)
        SET nuevo_precio = nuevo_precio * 1.10;

        -- Actualizar el precio en la tabla de productos
        UPDATE productos
        SET valorVenta = ing_nuevo_precio
        WHERE idProducto = ing_producto_id;

        -- Obtener el siguiente producto
        FETCH cursor_productos INTO ing_producto_id, ing_nuevo_precio;
    END WHILE;

    -- Cerrar y liberar el cursor
    CLOSE cursor_productos;

END //
DELIMITER ;
-- -----------------------------------------
-- Paso 5: Liberar el Cursor
-- Libera el cursor cuando hayas terminado de usarlo.
-- -----------------------------------------
CALL CambiarPrecioProductos();
