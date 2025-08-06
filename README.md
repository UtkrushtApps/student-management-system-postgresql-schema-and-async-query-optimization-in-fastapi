# Student Management System - PostgreSQL Async Optimization Task

## Task Overview

Utkrusht’s student management portal tracks students, courses, and enrollments. The FastAPI endpoints allow admins to see all students, courses, and the roster of students in each course as well as filter by enrollment status. API calls for listing students by course with status filters are unacceptably slow as data grows, leading to admin complaints and operational bottlenecks. Initial review points to an inefficient schema and slow database queries.

## Guidance

- The provided API works end-to-end but suffers delays listing students in courses (especially filtering by status)
- The database schema is missing foreign keys and indexes between enrollments and students/courses
- Left joins and filtering in the provided async query cause unnecessary full table scans
- You should analyze the schema, relationships, and query patterns; focus on the data layer and optimization logic
- You are NOT expected to write new endpoints or business features, only fix data access logic and database structure
- Use any PostgreSQL client and query tools for diagnosis (e.g., EXPLAIN (ANALYZE), pgAdmin, DBeaver)

## Database Access

- Host: <DROPLET_IP>
- Port: 5432
- Database: student_db
- Username: student_user
- Password: student_pass
- Use any preferred SQL client (e.g., pgAdmin, DBeaver, psql) to connect, inspect, and optimize the database

## Objectives

- Fix the schema to add missing relationships—define necessary foreign keys for enrollments
- Add indexes required to speed up LEFT JOINs and filtering on enrollment status
- Rewrite inefficient async SQL calls to return student rosters without unnecessary full table scans
- Achieve measurable performance increase for student-by-course listing and enrollment filtering endpoints

## How to Verify

- Use /courses/{course_id}/students?status=ENROLLED both before and after your changes to observe API response time (use curl, browser, or Postman)
- Run EXPLAIN (ANALYZE, BUFFERS) on the student-by-course query and compare row scan counts and execution time
- Confirm new indexes and foreign keys exist in the schema (describe tables in SQL client)
- Validate absence of timeouts, faster query returns, and overall improved user experience for enrollment filtering endpoints
