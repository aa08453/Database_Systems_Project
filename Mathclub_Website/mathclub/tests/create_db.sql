
CREATE DATABASE CLUBS_DATABASE
GO 

USE CLUBS_DATABASE
GO



-- Check and create "Majors" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Majors')
BEGIN
    CREATE TABLE "Majors"(
        "Major_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Name" VARCHAR(255) NOT NULL
    );
END;

-- Check and create "Users" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Users')
BEGIN
    CREATE TABLE "Users"(
        "User_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Name" VARCHAR(255) NOT NULL,
        "Reg_Date" DATE NOT NULL,
        "Contact_Number" NVARCHAR(30) NOT NULL, 
        "Password" NVARCHAR(255) NOT NULL,
        "Address" VARCHAR(255) NULL,
        "CNIC" VARCHAR(255) NULL,
        "privilege" INT NOT NULL,
        "Year" INT NULL,
        "Major" INT NULL,
        "HUID" INT NULL,
        FOREIGN KEY ("Major") REFERENCES "Majors" ("Major_ID")
    );
END;


INSERT INTO Users (Name, Reg_Date, Contact_Number, Privilege, Password)
VALUES 
    ('admin', CAST('2024-01-01' AS DATE), 3001234567, 1, '123'),
    ('user', CAST('2024-01-02' AS DATE), 3007654321, 2, '123');


-- Check and create "Teams" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Teams')
BEGIN
    CREATE TABLE "Teams"(
        "Team_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Team_Name" NVARCHAR(255) NOT NULL,
        "Team_Lead" INT NOT NULL,
        "Date_Created" DATE NOT NULL,
        FOREIGN KEY ("Team_Lead") REFERENCES "Users"("User_ID")
    );
END;

-- Check and create "Team_Roles" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Team_Roles')
BEGIN
    CREATE TABLE "Team_Roles"(
        "Role_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Role_Name" VARCHAR(255) NOT NULL,
        "Role_Description" TEXT NOT NULL
    );
END;

-- Check and create "Team_Members" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Team_Members')
BEGIN
    CREATE TABLE "Team_Members"(
        "Member_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "User_ID" INT NOT NULL,
        "Team_ID" INT NOT NULL,
        "Role" INT NOT NULL,
        "Date_Started" DATE NOT NULL,
        "Date_Ended" DATE,
        FOREIGN KEY ("User_ID") REFERENCES "Users"("User_ID"),
        FOREIGN KEY ("Team_ID") REFERENCES "Teams"("Team_ID"),
        FOREIGN KEY ("Role") REFERENCES "Team_Roles"("Role_ID")
    );
END;

-- Check and create "Locations" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Locations')
BEGIN
    CREATE TABLE "Locations"(
        "Location_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Location_Name" NVARCHAR(255) NOT NULL
    );
END;

-- Check and create "Events" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Events')
BEGIN
    CREATE TABLE "Events"(
        "Event_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Event_Lead" INT NOT NULL,
        "Event_Name" NVARCHAR(255) NOT NULL,
        "Start_Date" DATE NOT NULL,
        "End_Date" DATE NOT NULL,
        "Location" INT NOT NULL,
        "Scale" INT NOT NULL,
        "Description" NVARCHAR(255) NOT NULL,
        FOREIGN KEY ("Event_Lead") REFERENCES "Users"("User_ID"),
        FOREIGN KEY ("Location") REFERENCES "Locations"("Location_ID")
    );
END;

-- Check and create "Attendee_Type" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Attendee_Type')
BEGIN
    CREATE TABLE "Attendee_Type"(
        "Type_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Type_Name" VARCHAR(255) NOT NULL
    );
END;

-- Check and create "Attendees" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Attendees')
BEGIN
    CREATE TABLE "Attendees"(
        "Attendee_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Event_ID" INT NOT NULL,
        "Attendee" INT NOT NULL,
        "Type_ID" INT NOT NULL,
        FOREIGN KEY ("Type_ID") REFERENCES "Attendee_Type" ("Type_ID"),
        FOREIGN KEY ("Event_ID") REFERENCES "Events"("Event_ID"),
        FOREIGN KEY ("Attendee") REFERENCES "Users"("User_ID"),
        CONSTRAINT event_attendee UNIQUE ("Event_ID", "Attendee")
    );
END;

-- Check and create "Event_Teams" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Event_Teams')
BEGIN
    CREATE TABLE "Event_Teams"(
        "Event_Team_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Event_ID" INT NOT NULL,
        "Team_ID" INT NOT NULL,
        FOREIGN KEY ("Team_ID") REFERENCES "Teams"("Team_ID"),
        FOREIGN KEY ("Event_ID") REFERENCES "Events"("Event_ID"),
        CONSTRAINT event_team UNIQUE ("Event_ID", "Team_ID")
    );
END;

-- Check and create "Orders" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Orders')
BEGIN
    CREATE TABLE "Orders"(
        "Order_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Customer_ID" INT NOT NULL,
        "Order_Date" DATE NOT NULL,
        "Delivery_Date" DATE NOT NULL,
        FOREIGN KEY ("Customer_ID") REFERENCES "Users"("User_ID")
    );
END;

-- Check and create "Products" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Products')
BEGIN
    CREATE TABLE "Products"(
        "Product_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Product_Name" NVARCHAR(255) NOT NULL,
        "Price" INT NOT NULL,
        "Items_In_Stock" INT NOT NULL
    );
END;

-- Check and create "Order_Details" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Order_Details')
BEGIN
        CREATE TABLE "Order_Details"(
            "Details_ID" INT IDENTITY(1,1) PRIMARY KEY,
            "Order_ID" INT NOT NULL,
            "Product_ID" INT NOT NULL,
            "Quantity" INT NOT NULL,
            FOREIGN KEY ("Product_ID") REFERENCES "Products"("Product_ID"),
            FOREIGN KEY ("Order_ID") REFERENCES "Orders"("Order_ID"),
            CONSTRAINT order_product UNIQUE ("Order_ID", "Product_ID")
        );
END;

select * from Order_Details

select * from orders 
-- Check and create "Club_Items" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Club_Items')
BEGIN
    CREATE TABLE "Club_Items"(
        "Item_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Item_Name" VARCHAR(255) NOT NULL,
        "Storage" INT NOT NULL,
        FOREIGN KEY ("Storage") REFERENCES "Locations"("Location_ID")
    );
END;

-- Check and create "Responsibility" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Responsibility')
BEGIN
    CREATE TABLE "Responsibility"(
        "Responsibilty_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Item_ID" INT NOT NULL,
        "Person_Responsible" INT NOT NULL,
        "StartDate" DATE NOT NULL,
        "EndDate" DATE NULL,
        FOREIGN KEY ("Person_Responsible") REFERENCES "Users" ("User_ID"),
        FOREIGN KEY ("Item_ID") REFERENCES "Club_Items" ("Item_ID"),
        CONSTRAINT item_person UNIQUE ("Item_ID", "Person_Responsible")
    );
END;

-- Check and create "Tags" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Tags')
BEGIN
    CREATE TABLE "Tags"(
        "Tag_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Tag_Name" NVARCHAR(255) NOT NULL
    );
END;

-- Check and create "Blogs" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Blogs')
BEGIN
    CREATE TABLE "Blogs"(
        "Post_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Title" VARCHAR(255) NOT NULL,
        "Date_Created" DATE NOT NULL,
        "Content" NVARCHAR(255) NOT NULL,
        "User_ID" INT NOT NULL,
        "Tag_ID" INT NOT NULL,
        FOREIGN KEY ("User_ID") REFERENCES "Users"("User_ID"),
        FOREIGN KEY ("Tag_ID") REFERENCES "Tags"("Tag_ID")
    );
END;


select CAST(GETDATE() AS DATE);
select CAST(DATEADD(yy, 1, GETDATE()) AS DATE );

-- Check and create "Transaction_Types" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Transaction_Types')
BEGIN
    CREATE TABLE "Transaction_Types"(
        "Type_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Type_Name" VARCHAR(255) NOT NULL
    );
END;

-- Check and create "Finances" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Finances')
BEGIN
    CREATE TABLE "Finances"(
        "Transaction_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Responsible_Officer" INT NOT NULL,
        "User_ID" INT NOT NULL,
        "Transaction_Type" INT NOT NULL,
        "Date" DATE NOT NULL,
        "Description" NVARCHAR(255) NOT NULL,
        "Amount" INT NOT NULL,
        FOREIGN KEY ("Responsible_Officer") REFERENCES "Users" ("User_ID"),
        FOREIGN KEY ("User_ID") REFERENCES "Users" ("User_ID"),
        FOREIGN KEY ("Transaction_Type") REFERENCES "Transaction_Types" ("Type_ID")
    );
END;


-- Check and create "Elections" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Elections')
BEGIN
    CREATE TABLE "Elections"(
        "Election_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Start_Date" DATE NOT NULL,
        "End_Date" DATE NOT NULL
    );
END;

-- Check and create "Role_Types" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Role_Types')
BEGIN
    CREATE TABLE "Role_Types"(
        "Role_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Role_Name" VARCHAR(255) NOT NULL
    );
END;

select * from role_types
-- Check and create "Candidates" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Candidates')
BEGIN
    CREATE TABLE "Candidates"(
        "Candidate_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "User_ID" INT NOT NULL,
        "Role_ID" INT NOT NULL,
        "Election_ID" INT NOT NULL,
        FOREIGN KEY ("Election_ID") REFERENCES "Elections" ("Election_ID"),
        FOREIGN KEY ("Role_ID") REFERENCES "Role_Types" ("Role_ID"),
        FOREIGN KEY ("User_ID") REFERENCES "Users" ("User_ID")
    );
END;


-- Check and create "Leadership" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Leadership')
BEGIN
    CREATE TABLE "Leadership"(
        "Leader_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "User_ID" INT NOT NULL,
        "Role_ID" INT NOT NULL,
        "Start_Date" DATE NOT NULL,
        "End_Date" DATE NOT NULL,
        FOREIGN KEY ("Role_ID") REFERENCES "Role_Types" ("Role_ID"),
        FOREIGN KEY ("User_ID") REFERENCES "Candidates" ("Candidate_ID"),
        CONSTRAINT user_role_date UNIQUE ("User_ID", "Role_ID", "Start_Date")        
    );
END;


-- Check and create "Voting" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Voting')
BEGIN
    CREATE TABLE "Voting"(
        "Vote_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Voter_ID" INT NOT NULL,
        "Candidate_ID" INT NOT NULL,
        FOREIGN KEY ("Voter_ID") REFERENCES "Users"("User_ID"),
        FOREIGN KEY ("Candidate_ID") REFERENCES "Candidates"("Candidate_ID"),
        CONSTRAINT voter_candidate UNIQUE ("Voter_ID", "Candidate_ID")
    );
END;

------------------------------------------------------------------------------
-- Populating Majors table
INSERT INTO Majors (Name) VALUES
('Computer Science'),
('Electrical Engineering'),
('Mechanical Engineering');

-- Populating Users table
INSERT INTO Users (Name, Reg_Date, Contact_Number, Password, Privilege, Address, CNIC, Year, Major, HUID) VALUES
('Admin', '2024-01-01', '3001234567', 'password123', 1, '123 Admin Street', '12345-6789012-3', NULL, NULL, 1001),
('User1', '2024-01-02', '3007654321', 'user123', 2, '456 User Lane', '98765-4321098-7', 1, 1, 2001),
('User2', '2024-01-03', '3009988776', 'user456', 2, '789 Common Road', '56789-1234567-9', 2, 2, 2002);

-- Populating Teams table
INSERT INTO Teams (Team_Name, Team_Lead, Date_Created) VALUES
('Development', 1, '2024-02-01'),
('Marketing', 2, '2024-02-05');

-- Populating Team_Roles table
INSERT INTO Team_Roles (Role_Name, Role_Description) VALUES
('Team Lead', 'Leader of the team'),
('Member', 'Regular team member');

-- Populating Team_Members table
INSERT INTO Team_Members (User_ID, Team_ID, Role, Date_Started, Date_Ended) VALUES
(2, 1, 2, '2024-02-01', '2024-06-30'),
(3, 1, 2, '2024-02-01', NULL);

-- Populating Locations table
INSERT INTO Locations (Location_Name) VALUES
('Auditorium A'),
('Hall B'),
('Open Ground');

-- Populating Events table
INSERT INTO Events (Event_Lead, Event_Name, Start_Date, End_Date, Location, Scale, Description) VALUES
(1, 'Tech Conference 2024', '2024-03-15', '2024-03-17', 1, 3, 'Annual technology conference'),
(2, 'Sports Gala', '2024-04-10', '2024-04-12', 3, 5, 'Inter-departmental sports event');

-- Populating Attendee_Type table
INSERT INTO Attendee_Type (Type_Name) VALUES
('Student'),
('Faculty'),
('Visitor');

-- Populating Attendees table
INSERT INTO Attendees (Event_ID, Attendee, Type_ID) VALUES
(1, 2, 1),
(1, 3, 2),
(2, 1, 1);

-- Populating Event_Teams table
INSERT INTO Event_Teams (Event_ID, Team_ID) VALUES
(1, 1),
(2, 2);

-- Populating Products table
INSERT INTO Products (Product_Name, Price, Items_In_Stock) VALUES
('T-shirt', 500, 100),
('Mug', 300, 200),
('Notebook', 200, 150);

-- Populating Orders table
INSERT INTO Orders (Customer_ID, Order_Date, Delivery_Date) VALUES
(2, '2024-03-01', '2024-03-05'),
(3, '2024-03-02', '2024-03-06');

-- Populating Order_Details table
INSERT INTO Order_Details (Order_ID, Product_ID, Quantity) VALUES
(1, 1, 2),
(1, 2, 1),
(2, 3, 3);

-- Populating Club_Items table
INSERT INTO Club_Items (Item_Name, Storage) VALUES
('Projector', 1),
('Sound System', 2);

-- Populating Responsibility table
INSERT INTO Responsibility (Item_ID, Person_Responsible, StartDate, EndDate) VALUES
(1, 1, '2024-02-01', '2024-06-30'),
(2, 2, '2024-02-05', NULL);

-- Populating Tags table
INSERT INTO Tags (Tag_Name) VALUES
('Announcement'),
('Event'),
('General');

-- Populating Blogs table
INSERT INTO Blogs (Title, Date_Created, Content, User_ID, Tag_ID) VALUES
('Welcome to the Club', '2024-01-15', 'dummy text',1,1),
('Upcoming Events', '2024-02-20', 'dummy text lorem epsum',2,2);


-- Populating Transaction_Types table
INSERT INTO Transaction_Types (Type_Name) VALUES
('Income'),
('Expense');

-- Populating Finances table
INSERT INTO Finances (Responsible_Officer, User_ID, Transaction_Type, Date, Description, Amount) VALUES
(1, 2, 1, '2024-01-10', 'Membership Fee', 50000),
(2, 3, 2, '2024-01-20', 'Event Expense', 60000);

-- Populating Elections table
INSERT INTO Elections (Start_Date, End_Date) VALUES
('2024-05-01', '2024-05-10');

-- Populating Role_Types table
INSERT INTO Role_Types (Role_Name) VALUES
('President'),
('Secretary');

-- Populating Candidates table
INSERT INTO Candidates (User_ID, Role_ID, Election_ID) VALUES
(1, 1, 1),
(2, 2, 1);

-- Populating Leadership table
INSERT INTO Leadership (User_ID, Role_ID, Start_Date, End_Date) VALUES
(1, 1, '2024-05-11', '2025-05-11'),
(2, 2, '2024-05-11', '2025-05-11');

-- Populating Voting table
INSERT INTO Voting (Voter_ID, Candidate_ID) VALUES
(2, 1),
(3, 2);



