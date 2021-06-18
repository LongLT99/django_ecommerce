CREATE SCHEMA `boec` ;

use `boec`;

CREATE TABLE Address (
ID int(10) NOT NULL AUTO_INCREMENT,
City varchar(255), 
District varchar(255),
Ward varchar(255), 
`Description` varchar(255),
PRIMARY KEY (ID));

CREATE TABLE Fullname (
ID int(10) NOT NULL AUTO_INCREMENT, 
FirstName varchar(255), 
LastName varchar(255), 
PRIMARY KEY (ID));

CREATE TABLE `Account` (
ID int(10) NOT NULL AUTO_INCREMENT, 
Username varchar(255), 
`Password` varchar(255),
`Role` varchar(255),
PRIMARY KEY (ID));

CREATE TABLE Customer (
ID int(10) NOT NULL AUTO_INCREMENT, 
email varchar(255), 
tel varchar(11),
AccountID int(10) ,
FullnameID int(10) ,
AddressID int(10) ,
foreign key (AccountID) references `Account`(id),
foreign key (FullnameID) references Fullname(id),
foreign key (AddressID) references Address(id),
PRIMARY KEY (ID));

create table Cart (
ID int(10) NOT NULL AUTO_INCREMENT, 
price float(10),
CustomerID int(10),
`status` varchar(255),
foreign key (CustomerID) references Customer(id),
PRIMARY KEY (ID));

create table Product (
ID int(10) NOT NULL AUTO_INCREMENT, 
product_name varchar(255), 
product_type varchar(255), 
`description` text,
image varchar(255),
quantity int(10),
price float(10),
public boolean,
PRIMARY KEY (ID));

create table Item (
ID int(10) NOT NULL AUTO_INCREMENT, 
quantity int(10),
price float(10),
`status` boolean,
CartID int(10),
ProductID int(10),
foreign key (CartID) references Cart(id),
foreign key (ProductID) references Product(id),
PRIMARY KEY (ID));

create table Rating(
ID int(10)  NOT NULL AUTO_INCREMENT, 
Star int(10),
`comment` text,
ItemID int(10),
CustomerID int(10),
foreign key (CustomerID) references Customer(id),
foreign key (ItemID) references Item(id),
PRIMARY KEY (ID));

create table ProductRating (
ID int(10) NOT NULL AUTO_INCREMENT, 
RatingID int(10),
ProductID int(10),
foreign key (RatingID) references Rating(id),
foreign key (ProductID) references Product(id),
PRIMARY KEY (ID));

create table Payment (
ID int(10) NOT NULL AUTO_INCREMENT, 
price float(10),
payment_type varchar(255), 
PRIMARY KEY (ID));

create table Shipment (
ID int(10) NOT NULL AUTO_INCREMENT, 
fee float(10),
shipment_type varchar(255), 
AddressID int(10),
foreign key (AddressID) references Address(id),
PRIMARY KEY (ID));

create table `Order` (
ID int(10) NOT NULL AUTO_INCREMENT,
price float(10),
status varchar(255),
CartID int(10),
PaymentID int(10),
ShipmentID int(10),
foreign key (CartID) references Cart(id),
foreign key (PaymentID) references Payment(id),
foreign key (ShipmentID) references Shipment(id),
PRIMARY KEY (ID));

CREATE TABLE Employee (
ID int(10) NOT NULL AUTO_INCREMENT, 
`name` varchar(255), 
position varchar(11),
AccountID int(10) ,
foreign key (AccountID) references `Account`(id),
PRIMARY KEY (ID));

create table OrderProcess (
ID int(10) NOT NULL AUTO_INCREMENT, 
EmployeeID int(10),
OrderID int(10),
foreign key (EmployeeID) references Employee(id),
foreign key (OrderID) references `Order`(id),
PRIMARY KEY (ID));

create table RatingProcess (
ID int(10) NOT NULL AUTO_INCREMENT, 
feedback text,
EmployeeID int(10),
RatingID int(10),
foreign key (EmployeeID) references Employee(id),
foreign key (RatingID) references Rating(id),
PRIMARY KEY (ID));

INSERT INTO `boec`.`account` (`Username`, `Password`, `Role`) VALUES ('admin', '123456', '0');
INSERT INTO `boec`.`account` (`Username`, `Password`, `Role`) VALUES ('newguy', '123456', '1');

INSERT INTO `boec`.`fullname` (`FirstName`, `LastName`) VALUES ('Tran', 'Dan');
INSERT INTO `boec`.`address` (`City`, `District`, `Ward`, `Description`) VALUES ('Ha noi', 'Ha Dong ', 'Duong noi', 'so 100');
INSERT INTO `boec`.`customer` (`email`, `tel`, `AccountID`, `FullnameID`, `AddressID`) VALUES ('long@mail.com', '0987654321', '2', '1', '1');

INSERT INTO `boec`.`employee` (`name`, `position`, `AccountID`) VALUES ('Nguyen Tuan', 'admin', '1');

INSERT INTO `boec`.`product` (`product_name`, `product_type`, `description`, `image`, `quantity`, `price`, `public`) VALUES ('Harry Potter và hòn đá phù thủy', 'Book', 'Khi một lá thư được gởi đến cho cậu bé Harry Potter bình thường và bất hạnh, cậu khám phá ra một bí mật đã được che giấu suốt cả một thập kỉ. Cha mẹ cậu chính là phù thủy và cả hai đã bị lời nguyền của Chúa tể Hắc ám giết hại khi Harry mới chỉ là một đứa trẻ, và bằng cách nào đó, cậu đã giữ được mạng sống của mình. Thoát khỏi những người giám hộ Muggle không thể chịu đựng nổi để nhập học vào trường Hogwarts, một trường đào tạo phù thủy với những bóng ma và phép thuật, Harry tình cờ dấn thân vào một cuộc phiêu lưu đầy gai góc khi cậu phát hiện ra một con chó ba đầu đang canh giữ một căn phòng trên tầng ba. Rồi Harry nghe nói đến một viên đá bị mất tích sở hữu những sức mạnh lạ kì, rất quí giá, vô cùng nguy hiểm, mà cũng có thể là mang cả hai đặc điểm trên.', 'https://cdn0.fahasa.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/n/x/nxbtre_thumb_21542017_035423.jpg', '100', '108000', '1');
INSERT INTO `boec`.`product` (`product_name`, `product_type`, `description`,`image`, `quantity`, `price`, `public`) VALUES ('Harry Potter và căn phòng chứa bí mật', 'Book', 'Harry khổ sở mong ngóng cho kì nghỉ hè kinh khủng với gia đình Dursley kết thúc. Nhưng một con gia tinh bé nhỏ tội nghiệp đã cảnh báo cho Harry biết về mối nguy hiểm chết người đang chờ cậu ở trường Hogwarts. Trở lại trường học, Harry nghe một tin đồn đang lan truyền về phòng chứa bí mật, nơi cất giữ những bí ẩn đáng sợ dành cho giới phù thủy có nguồn gốc Muggle. Có kẻ nào đó đang phù phép làm tê liệt mọi người, khiến họ gần như đã chết, và một lời cảnh báo kinh hoàng được tìm thấy trên bức tường. Mối nghi ngờ hàng đầu – và luôn luôn sai lầm – là Harry. Nhưng một việc còn đen tối hơn thế đã được hé mở.', 'https://cdn0.fahasa.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/n/x/nxbtre_thumb_21472017_034753.jpg', '80', '	119250', '1');
INSERT INTO `boec`.`product` (`product_name`, `product_type`, `description`,`image`, `quantity`, `price`, `public`) VALUES ('Harry Potter Và Tên Tù Nhân Ngục Azkaban', 'Book', 'Harry Potter may mắn sống sót đến tuổi 13, sau nhiều cuộc tấn công của Chúa tể hắc ám. Nhưng hy vọng có một học kỳ yên ổn với Quidditch của cậu đã tiêu tan thành mây khói khi một kẻ điên cuồng giết người hàng loạt vừa thoát khỏi nhà tù Azkaban, với sự lùng sục của những cai tù là giám ngục. Dường như trường Hogwarts là nơi an toàn nhất cho Harry lúc này. Nhưng có phải là sự trùng hợp khi cậu luôn cảm giác có ai đang quan sát mình từ bóng đêm, và những điềm báo của giáo sư Trelawney liệu có chính xác?','https://cdn0.fahasa.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/8/9/8934974148050.jpg', '120', '147600', '1');
INSERT INTO `boec`.`product` (`product_name`, `product_type`, `description`,`image`, `quantity`, `price`, `public`) VALUES ('Harry Potter Và Chiếc Cốc Lửa', 'Book', 'Harry Potter may mắn sống sót đến tuổi 13, sau nhiều cuộc tấn công của Chúa tể hắc ám. Nhưng hy vọng có một học kỳ yên ổn với Quidditch của cậu đã tiêu tan thành mây khói khi một kẻ điên cuồng giết người hàng loạt vừa thoát khỏi nhà tù Azkaban, với sự lùng sục của những cai tù là giám ngục. Dường như trường Hogwarts là nơi an toàn nhất cho Harry lúc này. Nhưng có phải là sự trùng hợp khi cậu luôn cảm giác có ai đang quan sát mình từ bóng đêm, và những điềm báo của giáo sư Trelawney liệu có chính xác?','https://cdn0.fahasa.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/h/a/harrypottervachieccoclua.jpg', '70', '221400', '1');
INSERT INTO `boec`.`product` (`product_name`, `product_type`, `description`,`image`, `quantity`, `price`, `public`) VALUES ('Smart Tivi Samsung 4K 55 inch UA55TU8500', 'Electronic', 'Smart Tivi Samsung 4K 55 inch UA55TU8500 thu hút mọi ánh nhìn nhờ thiết kế phần chân đế phẳng chắc chắn, bên cạnh đó với thiết kế không viền 3 cạnh sẽ cho bạn những trải nghiệm giống như đang đứng trước một bức tranh sống động và chân thực.','//cdn.tgdd.vn/Products/Images/1942/219265/ua55tu8500-org.jpg', '50', '16900000', '1');
INSERT INTO `boec`.`product` (`product_name`, `product_type`, `description`,`image`, `quantity`, `price`, `public`) VALUES ('ÁO PHÔNG BÉ GÁI COTTON USA IN NHÂN VẬT', 'Clothes', 'áo phông cho bé gái chất lượng tốt hình ảnh đẹp','https://media.canifa.com/catalog/product/1/t/1ts21s013-sa534-120-1.jpg', '100', '149000', '1');

