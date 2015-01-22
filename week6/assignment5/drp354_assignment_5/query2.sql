-- ################################################
-- #****CUSP Principle of urban informatic class**#
-- #-----Dimas R.Putro / drp354@nyu.edu-----------#
-- ################################################
-- Principle of urban informatics assignment 5

SELECT S.name as 'name' 
FROM stations S 
WHERE S.line='Broadway'
ORDER BY S.name ASC
