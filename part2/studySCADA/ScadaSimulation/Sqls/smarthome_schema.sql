CREATE TABLE smarthomesensor (
  id int NOT NULL AUTO_INCREMENT,
  Home_Id varchar(20) NOT NULL,
  Room_Name varchar(20) NOT NULL,
  Sensing_DateTime datetime NOT NULL,
  Temp float NOT NULL,
  Humid float NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
