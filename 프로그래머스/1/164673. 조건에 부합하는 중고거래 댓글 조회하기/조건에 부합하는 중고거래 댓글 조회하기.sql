-- 코드를 입력하세요
SELECT a.TITLE, a.BOARD_ID, b.REPLY_ID, b.WRITER_ID, b.CONTENTS,
date_format(b.CREATED_DATE,'%Y-%m-%d') AS CREATED_DATE

FROM USED_GOODS_BOARD AS a
INNER JOIN USED_GOODS_REPLY AS b
ON a.BOARD_ID = b.BOARD_ID
WHERE a.CREATED_DATE LIKE '2022-10%'
ORDER BY b.CREATED_DATE ASC, a.TITLE ASC;