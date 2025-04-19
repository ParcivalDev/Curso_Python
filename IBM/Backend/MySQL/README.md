
# 🐘 Chuleta SQL – Guía Completa y Explicada

Esta chuleta es una guía rápida y explicativa de los comandos SQL más comunes para consultas, manipulación y análisis de datos. Ideal para estudiantes, desarrolladores y personas que trabajan con bases de datos.

---

## 🔍 Consultas Básicas

```sql
-- Selecciona todas las columnas de una tabla
SELECT * FROM pais;

-- Selecciona columnas específicas
SELECT id, nombre FROM ciudad;

-- Ordena los resultados ascendentemente por la columna 'clasificacion'
SELECT nombre FROM ciudad ORDER BY clasificacion ASC;
```

---

## 🏷️ Alias (AS)

```sql
-- Renombra una columna para mostrarla con un nombre más claro
SELECT nombre AS nombre_ciudad FROM ciudad;

-- Renombra tablas y columnas para mayor legibilidad en joins
SELECT pa.nombre AS nombre_pais, ci.nombre AS nombre_ciudad
FROM ciudad AS ci
JOIN pais AS pa ON ci.id_pais = pa.id;
```

---

## 🎯 Filtros con WHERE

```sql
-- Filtra filas donde la clasificación sea mayor a 3
SELECT nombre FROM ciudad WHERE clasificacion > 3;

-- Filtra filas que no sean ni 'Berlín' ni 'Madrid'
SELECT nombre FROM ciudad WHERE nombre != 'Berlín' AND nombre != 'Madrid';

-- Selecciona ciudades cuyo nombre empiece por 'P'
SELECT nombre FROM ciudad WHERE nombre LIKE 'P%';

-- Ciudades cuyo nombre termina en 's'
SELECT nombre FROM ciudad WHERE nombre LIKE '%s';

-- Ciudades cuyo nombre tiene un carácter antes de 'adrid'
SELECT nombre FROM ciudad WHERE nombre LIKE '_adrid';

-- Filtra ciudades cuya población esté entre 500.000 y 5.000.000
SELECT nombre FROM ciudad WHERE poblacion BETWEEN 500000 AND 5000000;

-- Filtra ciudades con clasificación no nula
SELECT nombre FROM ciudad WHERE clasificacion IS NOT NULL;

-- Selecciona ciudades cuyo país tiene ID 1, 4, 7 u 8
SELECT nombre FROM ciudad WHERE id_pais IN (1, 4, 7, 8);
```

---

## 🧾 Modificación de Datos

```sql
-- Inserta una nueva ciudad con sus atributos
INSERT INTO ciudad (id, nombre, id_pais, poblacion, clasificacion)
VALUES (999, 'NuevaCiudad', 1, 1000000, 4);

-- Actualiza la clasificación de una ciudad específica
UPDATE ciudad SET clasificacion = 5 WHERE nombre = 'París';

-- Elimina una ciudad de la tabla
DELETE FROM ciudad WHERE nombre = 'CiudadFantasma';
```

---

## 🔗 JOINs (Uniones de Tablas)

```sql
-- INNER JOIN: muestra sólo registros con coincidencias en ambas tablas
SELECT ciudad.nombre, pais.nombre
FROM ciudad
INNER JOIN pais ON ciudad.id_pais = pais.id;

-- LEFT JOIN: muestra todas las ciudades, incluso si no hay país relacionado
SELECT ciudad.nombre, pais.nombre
FROM ciudad
LEFT JOIN pais ON ciudad.id_pais = pais.id;

-- RIGHT JOIN: muestra todos los países, incluso si no hay ciudades asociadas
SELECT ciudad.nombre, pais.nombre
FROM ciudad
RIGHT JOIN pais ON ciudad.id_pais = pais.id;

-- FULL OUTER JOIN: muestra todos los registros de ambas tablas, con NULL donde no hay coincidencias
SELECT ciudad.nombre, pais.nombre
FROM ciudad
FULL OUTER JOIN pais ON ciudad.id_pais = pais.id;

-- CROSS JOIN: todas las combinaciones posibles entre ciudad y país
SELECT ciudad.nombre, pais.nombre
FROM ciudad CROSS JOIN pais;
```

---

## 🧮 Agregaciones y Agrupaciones

```sql
-- Cuenta el total de filas en la tabla
SELECT COUNT(*) FROM ciudad;

-- Cuenta cuántos países únicos hay en la tabla ciudad
SELECT COUNT(DISTINCT id_pais) FROM ciudad;

-- Calcula máximos, mínimos, promedio y suma
SELECT MAX(poblacion), MIN(poblacion), AVG(clasificacion), SUM(poblacion)
FROM ciudad;

-- Agrupa por país y suma la población por país
SELECT id_pais, SUM(poblacion)
FROM ciudad
GROUP BY id_pais;

-- Filtra los grupos según una condición sobre agregados
SELECT id_pais, AVG(clasificacion)
FROM ciudad
GROUP BY id_pais
HAVING AVG(clasificacion) > 3.0;
```

---

## 🧩 Subconsultas

```sql
-- Subconsulta: compara con un valor único
SELECT nombre
FROM ciudad
WHERE clasificacion = (
  SELECT clasificacion FROM ciudad WHERE nombre = 'París'
);

-- Subconsulta: compara con múltiples valores
SELECT nombre
FROM ciudad
WHERE id_pais IN (
  SELECT id FROM pais WHERE poblacion > 20000000
);

-- Subconsulta correlacionada: compara con datos del mismo grupo
SELECT *
FROM ciudad c1
WHERE poblacion > (
  SELECT AVG(poblacion)
  FROM ciudad c2
  WHERE c2.id_pais = c1.id_pais
);

-- Subconsulta en FROM (tabla derivada)
SELECT nombre, poblacion_promedio
FROM (
  SELECT nombre, AVG(poblacion) OVER() AS poblacion_promedio
  FROM ciudad
) AS sub;
```

---

## 📦 Operaciones de Conjuntos

```sql
-- UNION: combina resultados sin duplicados
SELECT nombre FROM ciclismo WHERE pais = 'DE'
UNION
SELECT nombre FROM patinaje WHERE pais = 'DE';

-- INTERSECT: muestra sólo los elementos comunes
SELECT nombre FROM ciclismo WHERE pais = 'DE'
INTERSECT
SELECT nombre FROM patinaje WHERE pais = 'DE';

-- EXCEPT: muestra los que están en la primera pero no en la segunda
SELECT nombre FROM ciclismo WHERE pais = 'DE'
EXCEPT
SELECT nombre FROM patinaje WHERE pais = 'DE';
```

---

## 🛠️ Gestión de Tablas

```sql
-- Crear tabla
CREATE TABLE ciudad (
  id INT PRIMARY KEY,
  nombre VARCHAR(100),
  id_pais INT,
  poblacion INT,
  clasificacion INT
);

-- Eliminar una tabla
DROP TABLE ciudad;

-- Agregar una columna a una tabla
ALTER TABLE ciudad ADD COLUMN area INT;

-- Cambiar el tipo de una columna
ALTER TABLE ciudad ALTER COLUMN poblacion TYPE BIGINT;
```
