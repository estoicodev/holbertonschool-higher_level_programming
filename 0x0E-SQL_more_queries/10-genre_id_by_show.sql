-- Import the database dump from hbtn_0d_tvshows to your MySQL server
-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT tvs_shows.title, tvs_g.genre_id FROM tv_shows AS `tvs` INNER JOIN tv_show_genres AS `tvs_g` ON tvs.id = tvs_g.show_id
ORDER BY tvs.title ASC, tvs_g.genre_id ASC;