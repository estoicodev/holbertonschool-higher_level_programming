-- Import the database dump from hbtn_0d_tvshows to your MySQL server
-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT tvs.title, tvs_g.genre_id FROM tv_show_genres AS tvs_g INNER JOIN tv_shows AS tvs ON tvs_g.show_id = tvs.id
ORDER BY tvs.title ASC, tvs_g.genre_id ASC;