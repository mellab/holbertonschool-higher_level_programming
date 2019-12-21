-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows.

SELECT DISTINCT
        title
FROM
	tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE
	title NOT IN (
SELECT
        title
FROM
	tv_genres
LEFT JOIN
tv_show_genres ON genre_id = tv_genres.id
LEFT JOIN
     	tv_shows
ON
	show_id = tv_shows.id
WHERE name = "Comedy") ORDER BY title ASC;
