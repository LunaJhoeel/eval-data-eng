--Query para obtener todos los regs de la tabla 'usuarios' mayores a 30 anhos de Madrid
SELECT *
FROM usuarios
WHERE ciudad = 'Madrid' AND edad > 30;
