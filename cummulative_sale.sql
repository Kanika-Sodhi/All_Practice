--Task SQL:

--QUESTION1:
with cte as(select r.good_name,s.s_date,amount
from [dbo].[ref_goods] r join [dbo].[sales] s  
on s.[id_good] = r.[id]),
CTE_YTD AS (
  SELECT good_name, SUM(amount) AS YTD
  FROM cte WHERE s_date >= DATEFROMPARTS(YEAR(GETDATE()), 1, 1) AND s_date <= GETDATE()
  GROUP BY good_name
),
CTE_MTD AS (
  SELECT good_name, SUM(amount) AS MTD
  FROM cte
  WHERE s_date >= DATEFROMPARTS(YEAR(GETDATE()), MONTH(GETDATE()), 1) 
  AND s_date <= GETDATE()
  GROUP BY good_name
),
CTE_QTD AS (
  SELECT good_name, SUM(amount) AS QTD
  FROM cte
  WHERE s_date >= DATEFROMPARTS(YEAR(GETDATE()), 1 + ((MONTH(GETDATE())-1) / 3) * 3, 1) 
  AND s_date <= GETDATE()
  GROUP BY good_name
),
CTE_PYTD AS (
  SELECT good_name, SUM(amount) AS PYTD
  FROM cte
  WHERE s_date >= DATEFROMPARTS(YEAR(DATEADD(year, -1, GETDATE())), 1, 1) 
  AND s_date <= DATEADD(year, -1, GETDATE())
  GROUP BY good_name
),
CTE_PMTD AS (
  SELECT good_name, SUM(amount) AS PMTD
  FROM cte
  WHERE s_date >= DATEFROMPARTS(YEAR(DATEADD(year, -1, GETDATE())), MONTH(GETDATE()), 1) 
  AND s_date <= DATEADD(year, -1, GETDATE())
  GROUP BY good_name
),
CTE_PQTD AS (
  SELECT good_name, SUM(amount) AS PQTD
  FROM cte
  WHERE s_date >= DATEFROMPARTS(YEAR(DATEADD(year, -1, GETDATE())), 1 + ((MONTH(GETDATE())-1) / 3) * 3, 1) 
  AND s_date <= DATEADD(year, -1, GETDATE())
  GROUP BY good_name
)
SELECT 
  CTE_YTD.good_name, 
  CTE_YTD.YTD, 
  CTE_MTD.MTD, 
  CTE_QTD.QTD, 
  CTE_PYTD.PYTD, 
  CTE_PMTD.PMTD, 
  CTE_PQTD.PQTD
FROM CTE_YTD
JOIN CTE_MTD ON CTE_YTD.good_name = CTE_MTD.good_name
JOin CTE_QTD on CTE_QTD.good_name = CTE_MTD.good_name
JOin CTE_PYTD on CTE_PYTD.good_name = CTE_MTD.good_name
JOin CTE_PMTD on CTE_PMTD.good_name = CTE_MTD.good_name
JOin CTE_PQTD on CTE_PQTD.good_name = CTE_MTD.good_name
--------------------------------------------------------------------------------
--QUESTION2:
WITH cte AS (
    SELECT 
        DATEPART(WEEK, s_date) as WeekNum, 
        d.id, 
        r.good_name, 
        g.good_group_name, 
        s_date, 
        d.amount, 
        d.rate,
        ROW_NUMBER() OVER (PARTITION BY r.good_name, DATEPART(WEEK, s_date) ORDER BY rate, s_date DESC) as rn
    FROM dbo.docs d join dbo.ref_goods r on d.id_good=r.id
	join dbo.ref_good_groups g on g.id = r.id_good_group
    WHERE DATEPART(MONTH, s_date) = 12 AND DATEPART(YEAR, s_date) = 2016
)
SELECT WeekNum, id, good_name, good_group_name, s_date, amount, rate
FROM cte
WHERE rn = 1
---------------------------------------------------------------------------------------------------------
--QUESTION 3:
declare @date_begin datetime = '2016-12-10 00:00:00';
declare @date_end datetime = '2016-12-20 00:00:00';

WITH theDates AS
     (SELECT @date_begin as theDate
      UNION ALL
      SELECT DATEADD(day, 1, theDate)
        FROM theDates
       WHERE DATEADD(day, 1, theDate) <= @date_end
     )
SELECT STUFF((SELECT ',' + QUOTENAME([theDate]) FROM theDates FOR XML PATH('')) ,1,1,'') as str into date_range

DECLARE @col nvarchar(max);
DECLARE @sql nvarchar(max);
SELECT @col = (select STR from date_range)
SELECT @sql = N'
select * from
(SELECT distinct r.good_name,s.amount,s.s_date
FROM sales s join ref_goods r on s.id_good = r.id) as src
PIVOT (
    sum([amount]) FOR [s_date] IN ('+@col+')
) as pvt'
EXEC sp_executesql @sql

