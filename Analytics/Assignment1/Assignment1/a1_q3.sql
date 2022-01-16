SELECT
    CONCAT(S.first_name, ' ', S.last_name) AS NAME,
    D.jee_rank
FROM
    Students AS S,
    Secondary_Details AS D
WHERE
    S.roll_number = D.roll_number
ORDER BY
    D.jee_rank
DESC
LIMIT 3;
