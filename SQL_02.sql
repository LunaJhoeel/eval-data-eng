-- Query para obtener los 3 prod mas vendidos por dia y local, mostrando dia, establecimiento, SKU y monto
SELECT dia, establecimiento, SKU, monto_venta
FROM (
    SELECT 
        dia, 
        establecimiento,
        SKU, 
        SUM(monto) AS monto_venta,
        ROW_NUMBER() OVER (PARTITION BY dia, establecimiento ORDER BY SUM(monto) DESC) as rn
    FROM ventas
    GROUP BY dia, establecimiento, SKU
) T
WHERE rn <= 3;

