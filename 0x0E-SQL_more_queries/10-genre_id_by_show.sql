--Import the database dump from hbtn_0d_tvshows to your MySQL server: download
SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY title, genre_id ASC;
