create  database conexion_py;
use conexion_py;

CREATE TABLE Airlines (
    AirlineID INT PRIMARY KEY,
    AirlineName VARCHAR(100),
    Country VARCHAR(100)
);

CREATE TABLE Airports (
    AirportID INT PRIMARY KEY,
    AirportName VARCHAR(100),
    City VARCHAR(100),
    Country VARCHAR(100)
);

CREATE TABLE Flights (
    FlightID INT PRIMARY KEY,
    AirlineID INT,
    DepartureAirportID INT,
    ArrivalAirportID INT,
    DepartureTime DATETIME,
    ArrivalTime DATETIME,
    Status VARCHAR(50),
    FOREIGN KEY (AirlineID) REFERENCES Airlines(AirlineID),
    FOREIGN KEY (DepartureAirportID) REFERENCES Airports(AirportID),
    FOREIGN KEY (ArrivalAirportID) REFERENCES Airports(AirportID)
);

CREATE TABLE Passengers (
    PassengerID INT PRIMARY KEY,
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    PassportNumber VARCHAR(50),
    Nationality VARCHAR(100)
);

CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY,
    PassengerID INT,
    FlightID INT,
    BookingDate DATETIME,
    SeatNumber VARCHAR(10),
    FOREIGN KEY (PassengerID) REFERENCES Passengers(PassengerID),
    FOREIGN KEY (FlightID) REFERENCES Flights(FlightID)
);

CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    Position VARCHAR(100),
    HireDate DATE
);

CREATE TABLE Luggage (
    LuggageID INT PRIMARY KEY,
    PassengerID INT,
    FlightID INT,
    Weight DECIMAL(5, 2),
    TagNumber VARCHAR(50),
    FOREIGN KEY (PassengerID) REFERENCES Passengers(PassengerID),
    FOREIGN KEY (FlightID) REFERENCES Flights(FlightID)
);

-- Airlines
INSERT INTO Airlines (AirlineID, AirlineName, Country) VALUES
(1, 'Delta Air Lines', 'USA'),
(2, 'British Airways', 'UK'),
(3, 'Qatar Airways', 'Qatar'),
(4, 'Air France', 'France'),
(5, 'Lufthansa', 'Germany'),
(6, 'Emirates', 'UAE'),
(7, 'American Airlines', 'USA'),
(8, 'Singapore Airlines', 'Singapore'),
(9, 'Turkish Airlines', 'Turkey'),
(10, 'ANA All Nippon Airways', 'Japan');

-- Airports
INSERT INTO Airports (AirportID, AirportName, City, Country) VALUES
(1, 'John F. Kennedy International Airport', 'New York', 'USA'),
(2, 'Heathrow Airport', 'London', 'UK'),
(3, 'Hamad International Airport', 'Doha', 'Qatar'),
(4, 'Charles de Gaulle Airport', 'Paris', 'France'),
(5, 'Frankfurt Airport', 'Frankfurt', 'Germany'),
(6, 'Dubai International Airport', 'Dubai', 'UAE'),
(7, 'Los Angeles International Airport', 'Los Angeles', 'USA'),
(8, 'Changi Airport', 'Singapore', 'Singapore'),
(9, 'Istanbul Airport', 'Istanbul', 'Turkey'),
(10, 'Tokyo Haneda Airport', 'Tokyo', 'Japan');




INSERT INTO Flights (FlightID, AirlineID, DepartureAirportID, ArrivalAirportID, DepartureTime, ArrivalTime, Status) VALUES
(1, 1, 1, 2, '2024-08-20 14:30:00', '2024-08-20 18:00:00', 'Scheduled'),
(2, 2, 2, 3, '2024-08-21 09:00:00', '2024-08-21 15:00:00', 'Scheduled'),
(3, 3, 3, 1, '2024-08-22 01:00:00', '2024-08-22 06:30:00', 'Scheduled'),
(4, 4, 4, 5, '2024-08-23 12:00:00', '2024-08-23 14:30:00', 'Scheduled'),
(5, 5, 5, 6, '2024-08-24 07:00:00', '2024-08-24 10:00:00', 'Scheduled'),
(6, 6, 6, 7, '2024-08-25 19:00:00', '2024-08-25 23:00:00', 'Scheduled'),
(7, 7, 7, 8, '2024-08-26 10:00:00', '2024-08-26 15:00:00', 'Scheduled'),
(8, 8, 8, 9, '2024-08-27 16:00:00', '2024-08-27 20:30:00', 'Scheduled'),
(9, 9, 9, 10, '2024-08-28 03:00:00', '2024-08-28 07:00:00', 'Scheduled'),
(10, 10, 10, 1, '2024-08-29 05:00:00', '2024-08-29 09:30:00', 'Scheduled');


INSERT INTO Passengers (PassengerID, FirstName, LastName, PassportNumber, Nationality) VALUES
(1, 'John', 'Doe', 'A1234567', 'USA'),
(2, 'Jane', 'Smith', 'B9876543', 'UK'),
(3, 'Ahmed', 'Khan', 'C1122334', 'Qatar'),
(4, 'Emily', 'Clark', 'D2233445', 'France'),
(5, 'Michael', 'Müller', 'E3344556', 'Germany'),
(6, 'Fatima', 'Ali', 'F4455667', 'UAE'),
(7, 'Robert', 'Brown', 'G5566778', 'USA'),
(8, 'Ling', 'Wang', 'H6677889', 'Singapore'),
(9, 'Yusuf', 'Demir', 'I7788990', 'Turkey'),
(10, 'Hiroshi', 'Tanaka', 'J8899001', 'Japan');



INSERT INTO Bookings (BookingID, PassengerID, FlightID, BookingDate, SeatNumber) VALUES
(1, 1, 1, '2024-08-10 12:00:00', '12A'),
(2, 2, 2, '2024-08-11 14:00:00', '7B'),
(3, 3, 3, '2024-08-12 16:00:00', '3C'),
(4, 4, 4, '2024-08-13 18:00:00', '14D'),
(5, 5, 5, '2024-08-14 20:00:00', '9E'),
(6, 6, 6, '2024-08-15 22:00:00', '2F'),
(7, 7, 7, '2024-08-16 08:00:00', '5G'),
(8, 8, 8, '2024-08-17 10:00:00', '10H'),
(9, 9, 9, '2024-08-18 12:00:00', '1A'),
(10, 10, 10, '2024-08-19 14:00:00', '6B');



INSERT INTO Employees (EmployeeID, FirstName, LastName, Position, HireDate) VALUES
(1, 'Alice', 'Brown', 'Pilot', '2015-03-01'),
(2, 'Bob', 'Johnson', 'Flight Attendant', '2018-07-15'),
(3, 'Charlie', 'Davis', 'Ground Staff', '2020-10-23'),
(4, 'David', 'Martinez', 'Security Officer', '2017-01-05'),
(5, 'Eva', 'Wilson', 'Customer Service', '2019-06-12'),
(6, 'Frank', 'Lopez', 'Technician', '2021-02-18'),
(7, 'Grace', 'Lee', 'Pilot', '2014-11-08'),
(8, 'Henry', 'Taylor', 'Flight Attendant', '2016-05-20'),
(9, 'Irene', 'Nguyen', 'Ground Staff', '2022-03-14'),
(10, 'Jack', 'Wright', 'Customer Service', '2022-03-14')




SELECT host, user FROM mysql.user WHERE user = 'root';


GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost';

GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost';
ALTER USER 'root'@'localhost' IDENTIFIED BY 'newpassword';
FLUSH PRIVILEGES;





