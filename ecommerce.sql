use `ecommerce`;

CREATE TABLE Address (ID int(10) NOT NULL AUTO_INCREMENT, UserID int(10) NOT NULL, City varchar(255), District varchar(255), Ward varchar(255), Description varchar(255), PRIMARY KEY (ID));
CREATE TABLE Cart (ID int(10) NOT NULL AUTO_INCREMENT, UserID int(10) NOT NULL, PRIMARY KEY (ID));
CREATE TABLE Cart_Item (CartID int(10) NOT NULL, ItemID int(10) NOT NULL, PRIMARY KEY (CartID, ItemID));
CREATE TABLE Custom (ID int(10) NOT NULL AUTO_INCREMENT, UserID int(10) NOT NULL, Birthday date, Email varchar(255), Phonenumber varchar(255), PRIMARY KEY (ID));
CREATE TABLE Fullname (ID int(10) NOT NULL AUTO_INCREMENT, FirstName varchar(255), LastName varchar(255), PRIMARY KEY (ID));
CREATE TABLE Item (ID int(10) NOT NULL AUTO_INCREMENT, Name varchar(255), Image varchar(255), Description varchar(255), Price float, Quantity int(10), PRIMARY KEY (ID));
CREATE TABLE `Order` (ID int(10) NOT NULL AUTO_INCREMENT, PaymentID int(10) NOT NULL, UserID int(10) NOT NULL, Total float, Discount float, PRIMARY KEY (ID));
CREATE TABLE Order_Item (OrderID int(10) NOT NULL, ItemID int(10) NOT NULL, PRIMARY KEY (OrderID, ItemID));
CREATE TABLE Payment (ID int(10) NOT NULL AUTO_INCREMENT, Name varchar(255), Description varchar(255), PRIMARY KEY (ID));
CREATE TABLE `User` (ID int(10) NOT NULL AUTO_INCREMENT, FullnameID int(10) NOT NULL, Username varchar(255), Password varchar(255), PRIMARY KEY (ID));
ALTER TABLE Custom ADD CONSTRAINT FKCustom230901 FOREIGN KEY (UserID) REFERENCES `User` (ID);
ALTER TABLE Cart_Item ADD CONSTRAINT FKCart_Item220265 FOREIGN KEY (ItemID) REFERENCES Item (ID);
ALTER TABLE Cart_Item ADD CONSTRAINT FKCart_Item904313 FOREIGN KEY (CartID) REFERENCES Cart (ID);
ALTER TABLE Order_Item ADD CONSTRAINT FKOrder_Item101392 FOREIGN KEY (ItemID) REFERENCES Item (ID);
ALTER TABLE Order_Item ADD CONSTRAINT FKOrder_Item365630 FOREIGN KEY (OrderID) REFERENCES `Order` (ID);
ALTER TABLE `Order` ADD CONSTRAINT FKOrder92191 FOREIGN KEY (PaymentID) REFERENCES Payment (ID);
ALTER TABLE `Order` ADD CONSTRAINT FKOrder63439 FOREIGN KEY (UserID) REFERENCES `User` (ID);
ALTER TABLE Cart ADD CONSTRAINT FKCart424327 FOREIGN KEY (UserID) REFERENCES `User` (ID);
ALTER TABLE Address ADD CONSTRAINT FKAddress555440 FOREIGN KEY (UserID) REFERENCES `User` (ID);
ALTER TABLE `User` ADD CONSTRAINT FKUser481364 FOREIGN KEY (FullnameID) REFERENCES Fullname (ID);