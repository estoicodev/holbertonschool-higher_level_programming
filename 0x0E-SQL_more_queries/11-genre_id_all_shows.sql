-- lists all shows contained in the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by
-- tv_shows.title and tv_show_genres.genre_id
-- If a show doesn’t have a genre, display NULL
SELECT tvs.title, tvs_g.genre_id
FROM tv_shows AS tvs RIGHT JOIN tv_show_genres AS tvs_g
ON tvs.id = tvs_g.show_id
ORDER BY tvs.title ASC, tvs_g.genre_id ASC;