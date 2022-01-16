CREATE DATABASE PROD2019;

CREATE TABLE Students(
    roll_number INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(20),
    section VARCHAR(1),
    PRIMARY KEY(roll_number)
);

CREATE TABLE Secodnary_Details(
    roll_number INT,
    contact_number VARCHAR(15),
    jee_rank NUMERIC(10),
    PRIMARY KEY(roll_number),
    FOREIGN KEY(roll_number) REFERENCES Students(roll_number)
);

INSERT INTO Students(
    roll_number,
    first_name,
    last_name,
    department,
    section
)
VALUES(1, 'fn-1-A', 'ln-1-A', 'dept-1-A', 'A');

INSERT INTO Students(
    roll_number,
    first_name,
    last_name,
    department,
    section
)
VALUES(2, 'fn-2-A', 'ln-2-A', 'dept-2-A', 'A'),(3, 'fn-3-A', 'ln-3-A', 'dept-3-A', 'B');

INSERT INTO Students(
    roll_number,
    first_name,
    last_name,
    department,
    section
)
VALUES(4, 'fn-4-A', 'ln-4-A', 'dept-4-A', 'A'),(5, 'fn-5-A', 'ln-5-A', 'dept-5-A', 'B'),(6, 'fn-6-A', 'ln-6-A', 'dept-6-A', 'B'),(7, 'fn-7-A', 'ln-7-A', 'dept-7-A', 'B'),(8, 'fn-8-A', 'ln-8-A', 'dept-8-A', 'B'),(9, 'fn-9-A', 'ln-9-A', 'dept-9-A', 'B'),(10, 'fn-10-A', 'ln-10-A', 'dept-10-A', 'A');

INSERT INTO Secondary_details(roll_number, contact_number, jee_rank) 
VALUES
(1,  -6381200121, FLOOR(RAND()*(50000)))
(2, -6381200122, FLOOR(RAND()*(50000))),
(3, -6381200123, FLOOR(RAND()*(50000))),
(4, -6381200124, FLOOR(RAND()*(50000))),
(5, -6381200125, FLOOR(RAND()*(50000))),
(6, -6381200126, FLOOR(RAND()*(50000))),
(7, -6381200127, FLOOR(RAND()*(50000))),
(8, -6381200128, FLOOR(RAND()*(50000))),
(9, -6381200129, FLOOR(RAND()*(50000))),
(10, -63812001210, FLOOR(RAND()*(50000)));
