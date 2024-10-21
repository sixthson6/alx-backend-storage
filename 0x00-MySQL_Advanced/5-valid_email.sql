-- create trigger to check
-- valid email
DELIMITER ;;
CREATE TRIGGER valid_email_check
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != email THEN
        SET NEW.email = 0
    END IF;
END;;
DELIMITER ;