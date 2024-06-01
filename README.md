# DjangoTask


Question 1  
### `select_related`

- **Usage**: Uses SQL `JOIN` to perform a single complex query and fetch related objects in one go.
- **Relationships**: Suitable for one-to-one and many-to-one relationships.
- **Performance**: Reduces the number of database queries by combining them into one, but this query can become quite complex.

### `prefetch_related`

- **Usage**: Executes separate queries for each related object and performs the joining in Python.
- **Relationships**: Suitable for many-to-many and reverse foreign key relationships.
- **Performance**: More efficient when dealing with a large number of related objects as it avoids large JOIN operations in SQL.

Question 2

- **Q objects** allow for complex queries using the `&` (AND), `|` (OR), and `~` (NOT) operators.
- They are useful for constructing queries that involve conditional logic, enabling more flexible and powerful queries.

Question 3  
Step 1: Launch an EC2 instance by choosing an appropriate instance  
Step 2: Connect to the EC2 instance by using SSH  
Step 3: Install the required software      
Step 4: Set up the Django Application  
Step 5: Configure Gunicorn   
Step 6: Configure Nginx  
