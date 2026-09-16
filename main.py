# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

# print(pd.read_sql("""SELECT * FROM sqlite_master""", conn))

# STEP 1
# Replace None with your code
q = """
    SELECT firstName, lastName
    FROM employees
    JOIN offices
        USING (officeCode)
    WHERE city = "Boston"
"""
df_boston = pd.read_sql(q, conn)

# print(df_boston)

# STEP 2
# Replace None with your code
q = """
    SELECT officeCode
    FROM offices
    LEFT JOIN employees USING (officeCode)
    GROUP BY officeCode
    HAVING COUNT(employeeNumber) = 0
"""
df_zero_emp = pd.read_sql(q, conn)

# print(df_zero_emp)

# STEP 3
# Replace None with your code
q = """
    SELECT firstName, lastName, city, state
    FROM employees
    LEFT JOIN offices USING (officeCode)
    ORDER BY firstName, lastName
"""
df_employee = pd.read_sql(q, conn)

# print(df_employee)

# STEP 4
# Replace None with your code
q = """
    SELECT contactFirstName, contactLastName, phone, salesRepEmployeeNumber
    FROM customers
    LEFT JOIN orders USING (customerNumber)
    WHERE (orderNumber) IS NULL
    ORDER BY contactLastName
"""
df_contacts = pd.read_sql(q, conn)

# print(df_contacts)

# STEP 5
# Replace None with your code
q = """
    SELECT contactFirstName, contactLastName, paymentDate, amount
    FROM customers
    JOIN payments USING (customerNumber)
    ORDER BY CAST(amount AS INTEGER) DESC
"""

df_payment = pd.read_sql(q, conn)

# print(df_payment)

# STEP 6
# Replace None with your code
q = """
    SELECT employeeNumber, firstName, lastName, COUNT(customerNumber) AS n_customers
    FROM employees
    JOIN customers ON employees.employeeNumber = customers.salesRepEmployeeNumber
    GROUP BY employeeNumber
    HAVING AVG(creditLimit) > 90000
    ORDER BY n_customers DESC
"""

df_credit = pd.read_sql(q, conn)

# print(df_credit)

# STEP 7
# Replace None with your code
q = """
    SELECT productName, COUNT(orderNumber) AS numorders, SUM(quantityOrdered) AS totalunits
    FROM products
    JOIN orderDetails USING (productCode)
    GROUP BY productName
    ORDER BY totalunits DESC
"""

df_product_sold = pd.read_sql(q, conn)

# print(df_product_sold)

# STEP 8
# Replace None with your code
q = """
    SELECT
        productName,
        productCode,
        COUNT(DISTINCT customerNumber) AS numpurchasers
    FROM products
    JOIN orderDetails USING (productCode)
    JOIN orders USING (orderNumber)
    GROUP BY productCode
    ORDER BY numpurchasers DESC
"""

df_total_customers = pd.read_sql(q, conn)

# print(df_total_customers)

# STEP 9
# Replace None with your code
q = """
    SELECT
        offices.officeCode,
        offices.city,
        COUNT(customerNumber) AS n_customers

    FROM offices

    JOIN employees USING (officeCode)

    JOIN customers
        ON employees.employeeNumber = customers.salesRepEmployeeNumber

    GROUP BY offices.officeCode
"""

df_customers = pd.read_sql(q, conn)
print(df_customers)

# STEP 10
# Replace None with your code
q = """
    SELECT DISTINCT
        employees.employeeNumber,
        employees.firstName,
        employees.lastName,
        offices.city,
        offices.officeCode
    FROM employees
    JOIN offices USING (officeCode)
    JOIN customers
        ON employees.employeeNumber = customers.salesRepEmployeeNumber
    JOIN orders USING (customerNumber)
    JOIN orderDetails USING (orderNumber)
    WHERE productCode IN (
        SELECT productCode
        FROM orderDetails
        JOIN orders USING (orderNumber)
        GROUP BY productCode
        HAVING COUNT(DISTINCT customerNumber) < 20
    )
    ORDER BY employees.lastName
"""

df_under_20 = pd.read_sql(q, conn)
print(df_under_20.to_string(index=False))
print(df_under_20)

conn.close()