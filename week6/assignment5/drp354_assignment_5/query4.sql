-- ################################################
-- #****CUSP Principle of urban informatic class**#
-- #-----Dimas R.Putro / drp354@nyu.edu-----------#
-- ################################################
-- Principle of urban informatics assignment 5

SELECT S.name, SUM((F2.ff)-(F1.ff)) AS diff_feb1_jan18 
FROM fares_jan18 F1 JOIN fares_feb1 F2 JOIN stations S 
WHERE F1.remote = F2.remote 
AND F1.station = S.name 
AND F2.station = S.name 
AND S.line = 'Broadway' 
GROUP BY S.name
ORDER BY S.name ASC
