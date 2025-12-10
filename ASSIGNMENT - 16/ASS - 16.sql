DROP DATABASE IF EXISTS library_db;
CREATE DATABASE library_db
  DEFAULT CHARACTER SET = utf8mb4
  DEFAULT COLLATE = utf8mb4_unicode_ci;
USE library_db;

-- 1) Create schema (tables)
DROP TABLE IF EXISTS Loans;
DROP TABLE IF EXISTS Books;
DROP TABLE IF EXISTS Members;

CREATE TABLE Members (
    member_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    join_date DATE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(200),
    author VARCHAR(100),
    available BOOLEAN
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE Loans (
    loan_id INT PRIMARY KEY,
    member_id INT,
    book_id INT,
    loan_date DATE,
    return_date DATE,
    CONSTRAINT fk_loans_member FOREIGN KEY (member_id) REFERENCES Members(member_id) ON DELETE RESTRICT,
    CONSTRAINT fk_loans_book   FOREIGN KEY (book_id)   REFERENCES Books(book_id)   ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 2) Insert sample data (parents first!)
INSERT INTO Members (member_id, name, email, join_date) VALUES
(1, 'anil', 'abc@123.gmail.com', '2025-10-16'),
(2, 'siri', 'def@gmail.com',       '2025-10-10'),
(3, 'nani', 'ghi@gmail.com',       '2025-10-24');

INSERT INTO Books (book_id, title, author, available) VALUES
(110, 'Atomic Habits',       'James Clear',     TRUE),
(120, 'Rich Dad Poor Dad',   'Robert Kiyosaki', TRUE),
(130, 'The Power of Habit',  'Charles Duhigg',  FALSE),
(140, 'The Alchemist',       'Paulo Coelho',    TRUE);

-- NOTE: Loans must reference the book_ids above (110,120,130,...).
-- Insert loans (children) AFTER parents exist:
INSERT INTO Loans (loan_id, member_id, book_id, loan_date, return_date) VALUES
(5001, 1, 130, '2025-10-10', NULL),   -- anil borrowed book 130 (Power of Habit)
(5002, 2, 110, '2025-10-12', '2025-10-20'),
(5003, 3, 120, '2025-10-15', NULL);

-- 3) TASK 3: queries
-- a) Members joined after a date
SELECT * FROM Members WHERE join_date > '2025-09-01';

-- b) Show all rows
SELECT * FROM Members;
SELECT * FROM Books;
SELECT * FROM Loans;

-- c) List books borrowed by a specific member (use member_id to avoid name/collation issues)
-- Change the member_id here to the desired member (e.g. 1)
SELECT
  L.loan_id,
  M.member_id,
  M.name AS member_name,
  B.book_id,
  B.title AS book_title,
  B.author AS book_author,
  L.loan_date,
  L.return_date
FROM Loans L
JOIN Members M ON L.member_id = M.member_id
JOIN Books   B ON L.book_id   = B.book_id
WHERE M.member_id = 1
ORDER BY L.loan_date DESC;

-- If you must filter by a name-string, force same collation:
-- WHERE M.name COLLATE utf8mb4_unicode_ci = 'anil';

-- 4) TASK 4:
-- Update a book's availability to FALSE when borrowed (example sets book 110 to FALSE)
UPDATE Books
SET available = FALSE
WHERE book_id = 110;

-- Safe delete: only delete member if they have NO outstanding loans (return_date IS NULL)
DELETE FROM Members
WHERE member_id = 3
  AND NOT EXISTS (
    SELECT 1 FROM Loans L WHERE L.member_id = 3 AND L.return_date IS NULL
  );

SELECT * FROM Loans WHERE member_id = 3 AND return_date IS NULL;
