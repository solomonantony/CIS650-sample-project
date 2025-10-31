# Overview
The purpose of this document is to inform the reader about the steps taken to develop software for a business application.  
# Source
The business example for this exercise was found in the case study 
Powell, A., & Barber, C. S. (2021). Teaching Case: Integrating Systems at We Build Stuff: Analysis and Design Case. Journal of Information Systems Education, 32(4), 244-248. 

The case study can be found at JISE - V32 - N4 - Teaching Case: Integrating Systems at We Build Stuff: Analysis and Design Case

# Contents
Based on an analysis of the requirements, we can work with two data files to address this user story
RawMaterials – RawMaterialID, Description, Current stock, Vendor information, Threshold, Minimum order quantity, Lead time, Purchase Order id, Reorder status
PurchaseOrders – PO_id, Date, RawMaterialID, Vendor information, Quantity ordered, Arrival date, Delivery Status, Stock update status
# User story
As the Director of the Financial Management Department, Veronica would like to create an automatic reorder of a raw material if its stock falls below a certain threshold so that she would have enough material in stock to complete an order. 

# Data model
Data model
Vendors - VendorID,  VendorName, Contact, Phone
RawMaterials – RawMaterialID, Description, Current stock, Vendor information, Threshold, Minimum order quantity, Lead time, Purchase Order id, Reorder status
PurchaseOrders – PO_id, Date, RawMaterialID, Vendor information, Quantity ordered, Arrival date, Delivery Status, Stock update status

# testing md

| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |

# Use case analysis

|Use case title| Update stock|
|------------------------------|
|Primary actor| Director of FIS|
|---|
|Secondary actor | None|
|---|
|Goal|Update the stock and create a purchase order|
|---|
|Scope|Financial Inforrmation System|
|---|
|Preconditions|Product inventory data is available|
|---|
||and Purchase order data are available|
|---|
|Post condition|Inventory updated|
|---|
||Purchase order created, if needed|
|---|
|Main success scenario|User enters valid product information|
|---|
||User enters valid data for stock update|
|---|
||Stock data is updated|
|---|
||If the current stock falls below Threshold, create as many purchase orders so that the resulting stock will be above the threshold|
|---|
||Add the purchase order to the dataset|
|---|


