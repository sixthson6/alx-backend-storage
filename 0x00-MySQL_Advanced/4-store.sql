-- create trigger
-- when new order is added
-- item reduces
CREATE TRIGGER decrease_quantity
AFTER INSERT ON item
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END $$

DELIMETER;