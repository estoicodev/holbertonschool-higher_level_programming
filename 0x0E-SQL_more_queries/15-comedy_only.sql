-- lists all Comedy shows in the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
SELECT tv_s.title
FROM tv_shows AS tv_s INNER JOIN tv_show_genres AS tv_sg INNER JOIN tv_genres AS tv_g
ON tv_g.name = "Comedy"
AND tv_sg.show_id = tv_s.id AND tv_sg.genre_id = tv_g.id
GROUP BY tv_s.title
ORDER BY tv_s.title ASC;