-- Lists the numbers of records with the same score in the table second_table of
-- the database hbtn_0c_0 in a MySQL server.

SELECT score, count(*) as number FROM second_table GROUP BY score ORDER BY score DESC;
