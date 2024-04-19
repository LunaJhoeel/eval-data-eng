-- Query para calcular monto total de venta por día combinando dos tablas y filtrando ventas del 1 de enero de 2024
SELECT DiaVenta, SUM(MontoVenta) AS TotalMontoVenta
FROM (
    SELECT DiaVenta, MontoVenta
    FROM proyecto_prd
    WHERE DiaVenta >= date '2024-01-01'
    UNION ALL
    SELECT DiaVenta, MontoVenta
    FROM proyecto_dev
    WHERE DiaVenta >= date '2024-01-01'
) AS ventas_combinadas
GROUP BY DiaVenta
ORDER BY DiaVenta;
