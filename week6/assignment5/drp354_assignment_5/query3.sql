-- ################################################
-- #****CUSP Principle of urban informatic class**#
-- #-----Dimas R.Putro / drp354@nyu.edu-----------#
-- ################################################
-- Principle of urban informatics assignment 5

SELECT S.lat AS  'lat', S.lng AS  'lng', SUM( F.ff ) AS  'ff'
FROM fares_jan18 F
JOIN stations S ON F.station = S.name
WHERE S.line =  'Broadway'
GROUP BY F.station
ORDER BY ff DESC
