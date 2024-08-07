-- SELECT 절에는 GROUP BY에 쓰인 column만 사용가능하다.
WITH b_fish AS (
    SELECT FISH_TYPE,  MAX(LENGTH) AS LENGTH
    FROM FISH_INFO 
    GROUP BY FISH_TYPE
)

SELECT A.ID, C.FISH_NAME, B.LENGTH
FROM b_fish AS B
LEFT JOIN FISH_INFO AS A
ON A.FISH_TYPE = B.FISH_TYPE AND A.LENGTH = B.LENGTH
LEFT JOIN FISH_NAME_INFO AS C
ON B.FISH_TYPE = C.FISH_TYPE
ORDER BY A.ID