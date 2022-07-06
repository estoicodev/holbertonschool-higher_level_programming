-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
SELECT tv_g.name
FROM tv_shows AS tv_s INNER JOIN tv_show_genres AS tv_sg INNER JOIN tv_genres AS tv_g
ON tv_s.title = "Dexter"
AND tv_sg.show_id = tv_s.id AND tv_sg.genre_id = tv_g.id
GROUP BY tv_g.name
ORDER BY tv_g.name ASC;