import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
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
cursor.execute("SELECT    count(GroceryStoreSimulator.dbo.tCoupon.[CouponSourceID])\
                FROM      GroceryStoreSimulator.dbo.tCoupon INNER JOIN\
                GroceryStoreSimulator.dbo.tCouponDetail ON GroceryStoreSimulator.dbo.tCoupon.CouponID = GroceryStoreSimulator.dbo.tCouponDetail.CouponID INNER JOIN\
                GroceryStoreSimulator.dbo.tCouponSource ON GroceryStoreSImulator.dbo.tCoupon.CouponSourceID = GroceryStoreSimulator.dbo.tCouponSourceID.CouponSourceID\
                WHERE     (GroceryStoreSimulator.dbo.tCouponDetail.Amountoff> 10) and (GroceryStoreSimulator.dbo.tCouponSource.CouponSourceID = 6)" )
results = cursor.fetchone()
print("The total number of coupons with a value of more than $10.00 off is " + str(results[0]) + ".")
'''
for row in results:
    print(row[0],row[1])
'''


