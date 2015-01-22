-- ################################################
-- #****CUSP Principle of urban informatic class**#
-- #-----Dimas R.Putro / drp354@nyu.edu-----------#
-- ################################################
-- Principle of urban informatics assignment 5

SELECT S.name AS 'stop_f' 
FROM stations S 
WHERE S.lines LIKE '%F%'
ORDER BY S.name
