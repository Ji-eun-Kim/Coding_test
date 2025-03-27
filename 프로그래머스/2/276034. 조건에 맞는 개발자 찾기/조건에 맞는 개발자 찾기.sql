-- 코드를 작성해주세요
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME

FROM DEVELOPERS
# &: 특정 비트가 포함되어 있는지 확인하는 데 사용됨
# &: 하나의 값과만 비교!
WHERE SKILL_CODE & (SELECT CODE
                    FROM SKILLCODES
                    WHERE NAME ='Python')
     OR               
     SKILL_CODE & (SELECT CODE
                    FROM SKILLCODES
                    WHERE NAME ='C#')
                    

ORDER BY ID ASC;