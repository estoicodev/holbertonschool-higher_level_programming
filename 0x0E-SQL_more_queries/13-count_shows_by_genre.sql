-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record should display:
-- <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by
-- the number of shows linked
SELECT tvs_g.name AS genre, COUNT(tvs_g.show_id) AS number_of_shows
FROM tv_show_genres AS tvs_g INNER JOIN tv_shows AS tvs
ON tvs_g.show_id = tvs.id
ORDER BY number_of_shows DESC;