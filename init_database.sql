-- Inefficient schema: no foreign keys or indexes on enrollments
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    description TEXT
);

CREATE TABLE enrollments (
    id SERIAL PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    status VARCHAR(16)
);

-- Sample students
INSERT INTO students (name, email) VALUES
('Alice Roberts', 'alice.roberts@example.com'),
('Brian Lee', 'brian.lee@example.com'),
('Cathy Smith', 'cathy.smith@example.com'),
('David King', 'david.king@example.com'),
('Eva Stone', 'eva.stone@example.com');

-- Sample courses
INSERT INTO courses (name, description) VALUES
('Mathematics', 'Fundamental concepts in calculus and algebra.'),
('History', 'Ancient and modern world history.'),
('Computer Science', 'Basics of programming and algorithms.');

-- Sample enrollments (not all students are enrolled in all courses)
INSERT INTO enrollments (student_id, course_id, status) VALUES
(1, 1, 'ENROLLED'),
(1, 2, 'COMPLETED'),
(2, 1, 'ENROLLED'),
(3, 2, 'ENROLLED'),
(4, 3, 'ENROLLED'),
(5, 2, 'DROPPED');
