SELECT
    S.*,
    D.*
FROM
    Students AS S,
    Secondary_Details AS D
WHERE
    S.roll_number = D.roll_number AND S.roll_number IN(
    SELECT
        MAX(S.roll_number)
    FROM
        S
);
