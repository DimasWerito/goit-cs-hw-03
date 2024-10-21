# Отримати всі завдання певного користувача:
"""SELECT * 
FROM tasks 
WHERE user_id = 123; -- замінити 123 на потрібний user_id"""

# Вибрати завдання за певним статусом:
"""SELECT * 
FROM tasks 
WHERE status = 'new';"""

# Оновити статус конкретного завдання:
"""UPDATE tasks 
SET status = 'in progress' 
WHERE task_id = 456; -- замінити 456 на ідентифікатор завдання"""

# Отримати список користувачів, які не мають жодного завдання:
"""SELECT * 
FROM users 
WHERE user_id NOT IN (SELECT user_id FROM tasks);"""

# Додати нове завдання для конкретного користувача:
"""INSERT INTO tasks (user_id, task_name, status, description) 
VALUES (123, 'New Task', 'new', 'This is a new task.');""" # замінити 123 на потрібний user_id

# Отримати всі завдання, які ще не завершено:
"""SELECT * 
FROM tasks 
WHERE status != 'completed';"""

# Видалити конкретне завдання:
"""DELETE FROM tasks 
WHERE task_id = 789;""" # замінити 789 на ідентифікатор завдання"""

# Знайти користувачів з певною електронною поштою:
"""SELECT * 
FROM users 
WHERE email LIKE '%@gmail.com';""" # замінити на потрібну доменну частину

# Оновити ім'я користувача:
"""UPDATE users 
SET name = 'New Name' 
WHERE user_id = 123;""" # замінити 123 на потрібний user_id

# Отримати кількість завдань для кожного статусу:
"""SELECT status, COUNT(*) AS task_count 
FROM tasks 
GROUP BY status;"""

# Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти:
"""SELECT tasks.* 
FROM tasks 
JOIN users ON tasks.user_id = users.user_id 
WHERE users.email LIKE '%@example.com';""" # замінити на потрібну доменну частину

# Отримати список завдань, що не мають опису:
"""SELECT * 
FROM tasks 
WHERE description IS NULL;"""

# Вибрати користувачів та їхні завдання, які є у статусі 'in progress':
"""SELECT users.*, tasks.* 
FROM users 
INNER JOIN tasks ON users.user_id = tasks.user_id 
WHERE tasks.status = 'in progress';"""

# Отримати користувачів та кількість їхніх завдань:
"""SELECT users.name, COUNT(tasks.task_id) AS task_count 
FROM users 
LEFT JOIN tasks ON users.user_id = tasks.user_id 
GROUP BY users.name;"""
