-- ################################################
-- #****CUSP Principle of urban informatic class**#
-- #-----Dimas R.Putro / drp354@nyu.edu-----------#
-- ################################################
-- Principle of urban informatics assignment 6


SELECT RTRIM(t1.name) AS  'station_with_largest_increase'
FROM (SELECT F1.station AS 'name', (SUM(F2.ff)-SUM(F1.ff)) as 'inc'
      FROM fares_jan18 F1 JOIN fares_feb1 F2
      WHERE F1.remote = F2.remote
      GROUP BY F1.station) t1
ORDER BY t1.inc DESC
LIMIT 1
