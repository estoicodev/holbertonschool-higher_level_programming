-- lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order
-- by tv_shows.title and tv_show_genres.genre_id
SELECT tvs.title, tvs_g.genre_id
FROM tv_shows AS tvs FULL OUTER JOIN tv_show_genres AS tvs_g
ON tvs.id = tvs_g.show_id
WHERE tvs.id IS NULL
OR tvs_g.show_id IS NULL
ORDER BY tvs.title ASC, tvs_g.genre_id ASC;