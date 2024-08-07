-- 코드를 작성해주세요
SELECT A.ID, A.GENOTYPE, B.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA AS A -- A 자식 / B 부모 테이블.
JOIN ECOLI_DATA AS B
ON B.ID = A.PARENT_ID
WHERE B.GENOTYPE & A.GENOTYPE = B.GENOTYPE
ORDER BY A.ID