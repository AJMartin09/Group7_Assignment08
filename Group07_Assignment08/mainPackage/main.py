#main.py
#*************************************************************************************************************************************
# Names: Trevor Hunt, Andrew Martin, Anna Bowers                                                                                     *
# emails: huntt3@mail.uc.edu, marti6aj@mail.uc.edu, bowersas@mail.uc.edu                                                                                                *
# Assignment Number: Assignment 08                                                                                                   *
# Due Date: 03/28/2024                                                                                                               *
# Course/Section: IS4010-001                                                                                                         *
# Semester/Year: Spring 2024                                                                                                         *
# Brief Description of the assignment: Demonstrates techniques for working with an SQL server using pyodbc                           *
#                                                                                                                                    *
# Brief Description of what this module does: Calls functions to retrieve data from SQL server and prints interesting fact about data*
# Citations: https://stackoverflow.com/questions/26098102/how-to-use-count-with-sql-joins                                            *
# Anything else that's relevant:                                                                                                     *
#*************************************************************************************************************************************\
import pyodbc

# Connect to the database
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                      'Database=IS4010;'
                      'uid=IS4010Login;'
                      'pwd=P@ssword2;')
cursor = conn.cursor()
'''
# Example from class
cursor.execute("SELECT GroceryStoreSimulator.dbo.tProduct.[UPC-A], GroceryStoreSimulator.dbo.tTransactionDetail.QtyOfProduct \
                FROM GroceryStoreSimulator.dbo.tProduct INNER JOIN \
                     GroceryStoreSimulator.dbo.tTransactionDetail ON GroceryStoreSimulator.dbo.tProduct.ProductID = GroceryStoreSimulator.dbo.tTransactionDetail.ProductID \
                WHERE (GroceryStoreSimulator.dbo.tTransactionDetail.QtyOfProduct> 100)")
first_query_result = cursor.fetchone()
print(first_query_result)
'''

# Corrected Option 1
'''
    Fetches the total number of coupons with a discount greater than a specified amount.
    
    Parameters:
    - cursor: The database cursor for executing SQL queries.
    - amount_off: The minimum discount amount of the coupon.
    - coupon_source_id: The source ID of the coupon.
    
    Returns:
    The total number of coupons matching the criteria.
'''
cursor.execute("SELECT count(GroceryStoreSimulator.dbo.tCoupon.[CouponSourceID]) \
                FROM GroceryStoreSimulator.dbo.tCoupon INNER JOIN \
                     GroceryStoreSimulator.dbo.tCouponDetail ON GroceryStoreSimulator.dbo.tCoupon.CouponID = GroceryStoreSimulator.dbo.tCouponDetail.CouponID INNER JOIN \
                     GroceryStoreSimulator.dbo.tCouponSource ON GroceryStoreSimulator.dbo.tCoupon.CouponSourceID = GroceryStoreSimulator.dbo.tCouponSource.CouponSourceID \
                WHERE (GroceryStoreSimulator.dbo.tCouponDetail.Amountoff> 10) and (GroceryStoreSimulator.dbo.tCouponSource.CouponSourceID = 6)")
results_option_1 = cursor.fetchone()
print("The total number of coupons with a value of more than $10.00 off is " + str(results_option_1[0]) + ".")

# Corrected Option 2 (Same as 1)
cursor.execute("""
    SELECT COUNT(GroceryStoreSimulator.dbo.tCoupon.CouponSourceID)
    FROM GroceryStoreSimulator.dbo.tCoupon
    INNER JOIN GroceryStoreSimulator.dbo.tCouponDetail
        ON GroceryStoreSimulator.dbo.tCoupon.CouponID = GroceryStoreSimulator.dbo.tCouponDetail.CouponID
    INNER JOIN GroceryStoreSimulator.dbo.tCouponSource
        ON GroceryStoreSimulator.dbo.tCoupon.CouponSourceID = GroceryStoreSimulator.dbo.tCouponSource.CouponSourceID
    WHERE (GroceryStoreSimulator.dbo.tCouponDetail.Amountoff > 10)
        AND (GroceryStoreSimulator.dbo.tCouponSource.CouponSourceID = 6)
""")
results = cursor.fetchone()
print("The total number of coupons with a value of more than $10.00 off and from 'Penny Saver' is " + str(results[0]) + ".")