-- seed.sql
INSERT INTO users (name, email, created_at) VALUES
('Amber Harris', 'amber@example.com', '2023-01-01'),
('Jane Doe', 'jane@example.com', '2023-01-15'),
('John Smith', 'john@example.com', '2023-02-01');

INSERT INTO products (name, price) VALUES
('Widget A', 10.99),
('Widget B', 14.99),
('Widget C', 7.49);

INSERT INTO orders (user_id, order_date) VALUES
(1, '2023-03-01'),
(2, '2023-03-02'),
(1, '2023-03-04');

INSERT INTO order_items (order_id, product_id, quantity) VALUES
(1, 1, 2),
(1, 3, 1),
(2, 2, 1),
(3, 1, 1),
(3, 2, 2);

