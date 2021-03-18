from PyQt5.QtCore import pyqtSignal, pyqtSlot
import fileFunctions
import tableFunctions
import forms

class Inventory:
    def __init__(self, home_window):
        self.part_list_file = "../Inventory/part_list.csv"
        self.product_list_file = "../Inventory/products.json"
        self.home_window = home_window
        self.balance_sheet = self.home_window.balance_sheet
        self.income_statement = self.home_window.income_statement
        self.inventory_table = self.home_window.inventory_table
        self.products_table = self.home_window.products_table
        self.add_part_btn = self.home_window.add_part_btn
        self.vendor_list = self.home_window.vendor_list
        self.build_robots_btn = self.home_window.build_robots_btn
        self.sell_robots_btn = self.home_window.sell_robots_btn
        self.purchase_inventory_btn = self.home_window.purchase_inventory_btn
        self.add_part_btn.clicked.connect(self.launchAddPartForm)
        self.build_robots_btn.clicked.connect(self.launchBuildRobotsForm)
        self.sell_robots_btn.clicked.connect(self.launchSellRobotsForm)
        self.purchase_inventory_btn.clicked.connect(self.launchPurchasePartsForm)
        self.readInParts()
        self.updateTable()

        self.products = fileFunctions.loadJSON(self.product_list_file)
        self.updateProductsTable()
    
        self.updateBalanceSheetInventory()

    def readInParts(self):
        self.inventory_df = fileFunctions.readCSV(self.part_list_file)
        self.headers = list(self.inventory_df.columns)
    
    def launchAddPartForm(self):
        #self.add_part_btn.setEnabled(False)
        vendor_name_list = self.vendor_list.getListOfNames()
        self.add_form = forms.AddPart(self, vendor_name_list)
        self.add_form.submit_signal.connect(self.updateTable)
        self.add_form.show()
    
    def launchBuildRobotsForm(self):
        product_list = self.products.keys()
        self.build_robots_form = forms.BuildRobots(self, product_list)
        self.build_robots_form.submit_signal.connect(self.updateAllTables)
        self.build_robots_form.show()

    def launchSellRobotsForm(self):
        product_list = self.products.keys()
        self.sell_robots_form = forms.SellRobots(self, product_list)
        self.sell_robots_form.submit_signal.connect(self.updateAllTables)
        self.sell_robots_form.show()
    
    def launchPurchasePartsForm(self):
        parts_list = self.inventory_df.part_name.to_list()
        self.purchase_parts_form = forms.PurchaseParts(self, parts_list)
        self.purchase_parts_form.submit_signal.connect(self.updateAllTables)
        self.purchase_parts_form.show()
    

    def addPart(self, part_name="", part_number="", unit_price="", vendor=""):
        new_part_dict = \
            {
                "part_name" : part_name,
                "count": 0,
                "part_number" : part_number,
                "unit_price" : unit_price,
                "vendor" : vendor
            }
        self.inventory_df = self.inventory_df.append(new_part_dict, ignore_index=True)
        return True
    
    def calculateCOGS(self, product):
        parts = self.products[product]["parts"]
        cogs = 0
        for part in parts:
            part_num = int(part) - 1
            quantity = float(parts[part])
            unit_price = self.inventory_df.unit_price[part_num]
            cogs += unit_price * quantity
        return cogs
    
    def checkCash(self, price):
        balance = self.balance_sheet["current assets"]["cash"]
        if price > balance:
            return False
        return True

    def purchaseParts(self, part_num=0, quantity=0):
        unit_price = self.inventory_df.unit_price[part_num]
        total_price = unit_price * quantity
        if self.checkCash(total_price) == False:
            return False
        
        self.inventory_df.at[part_num, "count"] += quantity
        self.balance_sheet["short term liabilities"]["payables"] += total_price
        self.updateBalanceSheetInventory()
        return True
    
    def checkInventory(self, product, quantity):
        parts = self.products[product]["parts"]
        for part in parts:
            part_num = int(part) - 1
            quantity_for_one = float(parts[part])
            available = self.inventory_df["count"][part_num]
            ask = quantity_for_one * quantity
            if ask > available:
                return False
        return True

    def subtractInventory(self, product, quantity):
        parts = self.products[product]["parts"]
        for part in parts:
            part_num = int(part) - 1
            available = self.inventory_df.at[part_num, "count"]
            ask = parts[part] * quantity
            new_quantity = available - ask
            self.inventory_df.at[part_num, "count"] = new_quantity
        
    def calculatePartsValue(self):
        value = 0
        for idx, part in self.inventory_df.iterrows():
            price = part.unit_price
            quantity = part["count"]
            value += price * quantity
        return value

    def calculateProductValue(self):
        value = 0
        for product in self.products:
            sale_price = self.products[product]["sale price"]
            quantity = self.products[product]["count"]
            value += sale_price * quantity
        return value
    
    def checkProductInventory(self, product, quantity):
        in_stock = self.products[product]["count"]
        if quantity > in_stock:
            return False
        return True

    def buildRobots(self, product="", quantity=0):
        if self.checkInventory(product, quantity) == False:
            return False
        
        self.products[product]["count"] += quantity
        self.subtractInventory(product, quantity)

        self.updateBalanceSheetInventory()
        return True

    def sellRobots(self, product="", quantity=0):
        if self.checkProductInventory(product, quantity) == False:
            return False
        
        self.products[product]["count"] -= quantity
        self.updateBalanceSheetInventory()

        total_sale = quantity * self.products[product]["sale price"]
        self.income_statement["revenue"][product] += total_sale
        self.balance_sheet["current assets"]["receivables"] = total_sale

        total_cogs = quantity * self.calculateCOGS(product)
        self.income_statement["cogs"][product] += total_cogs

        return True
    
    def updateBalanceSheetInventory(self):
        self.balance_sheet["current assets"]["inventory parts"] = self.calculatePartsValue()
        self.balance_sheet["current assets"]["inventory products"] = self.calculateProductValue()
        self.balance_sheet.updateAllInformation()
    
    def updateAllTables(self):
        self.updateTable()
        self.updateProductsTable()
        self.balance_sheet.updateAllInformation()
        self.income_statement.updateAllInformation()
    
    def updateTable(self):
        tableFunctions.setRowCount(self.inventory_table, self.inventory_df.shape[0])
        tableFunctions.setColumnCount(self.inventory_table, self.inventory_df.shape[1])
        tableFunctions.setHeaders(self.inventory_table, self.headers)
        for r, row in self.inventory_df.iterrows():
            for c, item in enumerate(row):
                tableFunctions.setItem(self.inventory_table, r, c, str(item))
        fileFunctions.writeCSV(self.inventory_df, self.part_list_file)
    
    def updateProductsTable(self):
        headers = ["name","count","sale price","cog"]
        tableFunctions.setRowCount(self.products_table, len(self.products))
        tableFunctions.setColumnCount(self.products_table, len(headers))
        tableFunctions.setHeaders(self.products_table, headers)
        for row, product in enumerate(self.products.keys()):
            count = self.products[product]["count"]
            sale_price = fileFunctions.formatCurrency(self.products[product]["sale price"])
            cog = fileFunctions.formatCurrency(self.calculateCOGS(product))
            tableFunctions.setItem(self.products_table, row, 0, product)
            tableFunctions.setItem(self.products_table, row, 1, str(count))
            tableFunctions.setItem(self.products_table, row, 2, sale_price)
            tableFunctions.setItem(self.products_table, row, 3, cog)
        fileFunctions.writeJSON(self.product_list_file, self.products)

            