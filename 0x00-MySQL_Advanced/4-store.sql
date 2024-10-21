-- create trigger
-- when new order is added
-- item reduces

DELIMITER $$

CREATE TRIGGER decrease_quantity
AFTER INSERT ON items
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.quantity
    WHERE name = NEW.name;
END $$

DELIMITER;