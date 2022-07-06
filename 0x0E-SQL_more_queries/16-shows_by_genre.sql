-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
SELECT tv_s.title, tv_g.name
FROM tv_shows AS tv_s
LEFT JOIN tv_show_genres AS tv_sg
ON tv_s.id = tv_sg.show_id
LEFT JOIN tv_genres AS tv_g
ON tv_g.id = tv_sg.genre_id
ORDER BY tv_s.title ASC, tv_g.name ASC;