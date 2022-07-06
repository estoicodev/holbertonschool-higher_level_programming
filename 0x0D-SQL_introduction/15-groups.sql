-- lists the number of records with the same score in the table second_table
SELECT `score`, COUNT(`score`) AS `number`
FROM `second_table`
ORDER BY `score` DESC
HAVING COUNT(`score`) > 1;