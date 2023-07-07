-- script that lists all bands with Glam rock as their main style
SELECT band_name, COALESCE(split, YEAR(NOW())) - formed AS lifespan
FROM metal_bands
WHERE BINARY style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
