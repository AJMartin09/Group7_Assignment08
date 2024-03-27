#main.py
#*************************************************************************************************************************************
# Names: Trevor Hunt, Andrew Martin, Anna Bowers                                                                                     *
# emails: huntt3@mail.uc.edu, [], linneabowers@gmail.com                                                                                                 *
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
conn = pyodbc.connect('Driver={SQL Server};'    #connect to the database
                      'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                      'Database=IS4010;'
                      'uid=IS4010Login;'
                      'pwd=P@ssword2;')
cursor = conn.cursor()

# to run a query use:
# sql_string = "Select count(*) From GroceryStoreSimulator.dbo.tBrand;"
# results = conn.execute(sql_string)

#Below is example from class
'''
cursor.execute("SELECT    GroceryStoreSimulator.dbo.tProduct.[UPC-A], GroceryStoreSimulator.dbo.tTransactionDetail.QtyOfProduct\
                FROM      GroceryStoreSimulator.dbo.tProduct INNER JOIN\
                GroceryStoreSimulator.dbo.tTransactionDetail ON GroceryStoreSimulator.dbo.tProduct.ProductID = GroceryStoreSimulator.dbo.tTransactionDetail.ProductID\
                WHERE     (GroceryStoreSimulator.dbo.tTransactionDetail.QtyOfProduct> 100)" )
print(cursor.fetchone())
'''

# My own code
#GroceryStoreSimulator.dbo.tCoupon.[CouponSourceID], GroceryStoreSimulator.dbo.tCouponDetail.AmountOff\
#Option 1
'''
cursor.execute("SELECT    count(GroceryStoreSimulator.dbo.tCoupon.[CouponSourceID])\
                FROM      GroceryStoreSimulator.dbo.tCoupon INNER JOIN\
                GroceryStoreSimulator.dbo.tCouponDetail ON GroceryStoreSimulator.dbo.tCoupon.CouponID = GroceryStoreSimulator.dbo.tCouponDetail.CouponID INNER JOIN\
                GroceryStoreSimulator.dbo.tCouponSource ON GroceryStoreSImulator.dbo.tCoupon.CouponSourceID = GroceryStoreSimulator.dbo.tCouponSource.CouponSourceID\
                WHERE     (GroceryStoreSimulator.dbo.tCouponDetail.Amountoff> 10) and (GroceryStoreSimulator.dbo.tCouponSource.CouponSourceID = 6)" )
results = cursor.fetchone()
print("The total number of coupons with a value of more than $10.00 off is " + str(results[0]) + ".")
'''
'''
for row in results:
    print(row[0],row[1])
'''

#Option 2
cursor.execute("USE GroceryStoreSimulator\
Select DISTINCT COUNT(*) OVER () AS TotalRowCount--, tCoupon.CouponSourceID, tCouponDetail.Amountoff, tProductPriceHist.PricePerSellableUnit,\
        FROM tCoupon INNER JOIN\
               tCouponDetail ON tCoupon.CouponID = tCouponDetail.CouponID INNER JOIN\
               tCouponSource ON tCoupon.CouponSourceID = tCouponSource.CouponSourceID INNER JOIN\
                     tProduct ON tCouponDetail.ProductID = tProduct.ProductID INNER JOIN\
                     tProductPriceHist ON tProductPriceHist.ProductID = tProduct.ProductID\
               WHERE (tCouponDetail.Amountoff> 10) and (tCouponDetail.Amountoff > tProductPriceHist.PricePerSellableUnit)--and (tCouponSource.CouponSourceID = 6)")
results = cursor.fetchone()
'''
Using the GroceryStoreSimulator data set, this determines how many coupons have a value greater than the price of the product's sellable unit.
@returns: Total number of coupons with a value greater than the price per sellable unit
'''
print("The total number of coupons with a value greater than the price per sellable unit is " + str(results[0]) + ".")
