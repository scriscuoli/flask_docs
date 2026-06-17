-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS docs;

-- Create the user 'docs' that can connect from any host ('%')
-- Replace 'your_strong_password' with a secure password
CREATE USER 'docs'@'%' IDENTIFIED BY '!QAZ2wsx#EDC4rfv';

-- Grant all privileges on the 'docs' database to the 'docs' user
GRANT ALL PRIVILEGES ON docs.* TO 'docs'@'%';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;

-- Optional: To verify the grants for the user
SHOW GRANTS FOR 'docs'@'%';
