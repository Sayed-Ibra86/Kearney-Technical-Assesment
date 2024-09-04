/*
Considering the database schema displayed in the SQL Server - style diagram below,
 write a SQL query to return a list of all the invoices. For each invoice, show the Invoice ID,
 the billing date, the customer’s name, and the name of the customer who referred to that customer (if any).
 The list should be ordered by billing date.
*/
SELECT
    i.Id AS Invoice_ID,
    i.BillingDate,
    c.Name AS Customer_Name,
    r.Name AS Referring_Customer_Name
FROM
    Invoices i
LEFT JOIN Customers c ON i.CustomerId = c.Id
LEFT JOIN Customers r ON c.ReferredBy = r.Id
ORDER BY
    i.BillingDate;