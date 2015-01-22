-- ################################################
-- #****CUSP Principle of urban informatic class**#
-- #-----Dimas R.Putro / drp354@nyu.edu-----------#
-- ################################################
-- Principle of urban informatics assignment 6

SELECT RTRIM(F1.station) AS name
FROM fares_jan18 F1 JOIN fares_feb1 F2
WHERE F1.remote = F2.remote
GROUP BY F1.station
HAVING (SUM(F1.ff)-SUM(F2.ff))>1000
ORDER BY F1.station ASC
