IF EXISTS (SELECT * FROM sys.databases WHERE name = 'CLUBS_DATABASE')
BEGIN
    USE master;
    DROP DATABASE CLUBS_DATABASE;
    -- Optionally, wait for a short time before recreating the database
    WAITFOR DELAY '00:00:05'; -- Wait for 5 seconds
END

CREATE DATABASE CLUBS_DATABASE;
USE CLUBS_DATABASE;

-- Check and create "Events" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Events')
BEGIN
    CREATE TABLE Events(
        Event_ID INT IDENTITY(1,1) NOT NULL,
        Event_Name VARCHAR(255) NOT NULL,
        Start_Date DATETIME2 NOT NULL,
        End_Date DATETIME2 NOT NULL,
        Location INT NOT NULL,
        Scale INT NOT NULL,
        Description VARCHAR(255) NOT NULL,
        PRIMARY KEY (Event_ID)
    );
END;

-- Check and create "Products" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Products')
BEGIN
    CREATE TABLE Products(
        Product_ID INT IDENTITY(1,1) PRIMARY KEY,
        Product_Name VARCHAR(255) NOT NULL,
        Price INT NOT NULL
    );
END;

-- Check and create "Majors" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Majors')
BEGIN
    CREATE TABLE Majors(
        Major_ID INT IDENTITY(1,1) PRIMARY KEY,
        Name VARCHAR(255) NOT NULL
    );
END;

-- Check and create "TransactionTypes" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'TransactionTypes')
BEGIN
    CREATE TABLE TransactionTypes(
        Type_ID INT IDENTITY(1,1) PRIMARY KEY,
        Type_Name VARCHAR(255) NOT NULL
    );
END;

-- Check and create "Team_Roles" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Team_Roles')
BEGIN
    CREATE TABLE Team_Roles(
        role_id INT IDENTITY(1,1) PRIMARY KEY,
        role_name VARCHAR(255) NOT NULL,
        role_description TEXT NOT NULL
    );
END;

-- Check and create "Role_Types" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Role_Types')
BEGIN
    CREATE TABLE Role_Types(
        Role_Id INT IDENTITY(1,1) PRIMARY KEY,
        Role_Name VARCHAR(255) NOT NULL
    );
END;

-- Check and create "Tags" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Tags')
BEGIN
    CREATE TABLE Tags(
        Tag_ID INT IDENTITY(1,1) PRIMARY KEY,
        Tag_Name VARCHAR(255) NOT NULL
    );
END;

-- Check and create "Attendee_Types" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Attendee_Types')
BEGIN
    CREATE TABLE Attendee_Types(
        type_id INT IDENTITY(1,1) PRIMARY KEY,
        attendee_type VARCHAR(255) NOT NULL
    );
END;

-- Check and create "Responsibilities" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Responsibilities')
BEGIN
    CREATE TABLE Responsibilities(
        Item_ID INT IDENTITY(1,1) PRIMARY KEY,
        Person_Responsible INT NOT NULL,
        StartDate DATE NOT NULL,
        EndDate DATE NOT NULL
    );
END;

-- Check and create "Blog_Contents" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Blog_Contents')
BEGIN
    CREATE TABLE Blog_Contents(
        Post_ID INT IDENTITY(1,1) PRIMARY KEY,
        File_Path VARCHAR(255) NULL,
        File_Type NCHAR(255) NOT NULL
    );
END;

-- Check and create "Elections" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Elections')
BEGIN
    CREATE TABLE Elections(
        Election_ID INT IDENTITY(1,1) PRIMARY KEY,
        Start_Date DATETIME2 NOT NULL,
        End_Date DATETIME2 NOT NULL
    );
END;

-- Check and create "Club_Items" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Club_Items')
BEGIN
    CREATE TABLE Club_Items(
        Item_ID INT IDENTITY(1,1) PRIMARY KEY,
        Item_Name VARCHAR(255) NOT NULL,
        Storage VARCHAR(255) NOT NULL
    );
END;

-- Check and create "Order_Details" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Order_Details')
BEGIN
    CREATE TABLE Order_Details(
        Order_ID INT IDENTITY(1,1) PRIMARY KEY,
        Product_ID INT NOT NULL,
        Quantity INT NOT NULL
    );
END;

-- Check and create "Event_Teams" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Event_Teams')
BEGIN
    CREATE TABLE Event_Teams(
        Event_ID INT NOT NULL,
        Team_ID INT NOT NULL,
        PRIMARY KEY (Event_ID, Team_ID)
    );
END;

-- Check and create "Locations" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Locations')
BEGIN
    CREATE TABLE Locations(
        Location_ID INT IDENTITY(1,1) PRIMARY KEY,
        Location_Name VARCHAR(255) NOT NULL
    );
END;

-- Check and create "Users" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Users')
BEGIN
    CREATE TABLE Users(
        User_ID INT IDENTITY(1,1) PRIMARY KEY,
        Name VARCHAR(255) NOT NULL,
        RegDate DATETIME2 NOT NULL,
        Contact_Number VARCHAR(10) NOT NULL,  
        Privilege INT NOT NULL,
        Password NVARCHAR(255) NOT NULL,
        Address VARCHAR(255) NULL,
        CNIC VARCHAR(255) NULL,
        Year INT NULL,
        HUID INT NULL
    );
END;

-- Check and create "Event_Leaders" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Event_Leaders')
BEGIN
    CREATE TABLE Event_Leaders(
        Event_ID INT NOT NULL,
        Event_Lead INT NOT NULL,
        PRIMARY KEY (Event_ID, Event_Lead),
        FOREIGN KEY (Event_ID) REFERENCES Events(Event_ID),
        FOREIGN KEY (Event_Lead) REFERENCES Users(User_ID)
    );
END;

-- Check and create "Event_Participations" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Event_Participations')
BEGIN
    CREATE TABLE Event_Participations(
        Event_ID INT NOT NULL,
        Attendee INT NOT NULL,
        PRIMARY KEY (Event_ID, Attendee),
        FOREIGN KEY (Event_ID) REFERENCES Events(Event_ID),
        FOREIGN KEY (Attendee) REFERENCES Users(User_ID)
    );
END;

-- Check and create "User_Majors" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'User_Majors')
BEGIN
    CREATE TABLE User_Majors(
        User_ID INT NOT NULL,
        Major_ID INT NOT NULL,
        StartDate DATE NOT NULL,
        EndDate DATE NOT NULL,
        PRIMARY KEY (User_ID, Major_ID, StartDate),
        FOREIGN KEY (User_ID) REFERENCES Users(User_ID),
        FOREIGN KEY (Major_ID) REFERENCES Majors(Major_ID)
    );
END;

-- Check and create "Blogs" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Blogs')
BEGIN
    CREATE TABLE Blogs(
        Post_ID INT IDENTITY(1,1) PRIMARY KEY,
        Title VARCHAR(255) NOT NULL,
        Date_Created DATETIME2 NOT NULL,
        User_ID INT NOT NULL,
        FOREIGN KEY (User_ID) REFERENCES Users(User_ID)
    );
END;


IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Roles')
BEGIN
    CREATE TABLE Blogs(
        Role_ID INT IDENTITY(1,1) PRIMARY KEY,
        Role_Name VARCHAR(20) NOT NULL,
    );
END;




-- Check and create "Blogs" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Candidates')
BEGIN
    CREATE TABLE Blogs(
        Candidate_ID INT IDENTITY(1,1) PRIMARY KEY,
        Role_ID INT NOT NULL,
        Election_ID INT NOT NULL,
        User_ID INT NOT NULL,
        FOREIGN KEY (User_ID) REFERENCES Users(User_ID)
        FOREIGN KEY (Role_ID) REFERENCES Roles(Role_ID)
        FOREIGN KEY (Election_ID) REFERENCES Elections(Election_ID)
    );
END;



-- Populate "Events" table if empty
IF NOT EXISTS (SELECT * FROM Events)
BEGIN
    INSERT INTO Events (Event_Name, Start_Date, End_Date, Location, Scale, Description)
    VALUES 
        ('Tech Conference', '2024-01-10', '2024-01-12', 1, 5, 'A conference about technology innovations'),
        ('Hackathon', '2024-02-20', '2024-02-22', 2, 4, 'A 48-hour coding competition');
END;


-- Populate "Products" table if empty
IF NOT EXISTS (SELECT * FROM Products)
BEGIN
    INSERT INTO Products (Product_Name, Price)
    VALUES 
        ('T-Shirt', 500),
        ('Notebook', 200);
END;

-- Populate "Majors" table if empty
IF NOT EXISTS (SELECT * FROM Majors)
BEGIN
    INSERT INTO Majors (Name)
    VALUES 
        ('Computer Science'),
        ('Electrical Engineering');
END;

-- Populate "TransactionType" table if empty
IF NOT EXISTS (SELECT * FROM TransactionType)
BEGIN
    INSERT INTO TransactionType (Type_Name)
    VALUES 
        ('Purchase'),
        ('Donation');
END;

-- Populate "Team_Roles" table if empty
IF NOT EXISTS (SELECT * FROM Team_Roles)
BEGIN
    INSERT INTO Team_Roles (role_name, role_description)
    VALUES 
        ('Leader', 'Responsible for team management'),
        ('Member', 'Assist in team activities');
END;

-- Populate "Role_types" table if empty
IF NOT EXISTS (SELECT * FROM Role_types)
BEGIN
    INSERT INTO Role_types (Role_Name)
    VALUES 
        ('Admin'),
        ('User');
END;

-- Populate "Tags" table if empty
IF NOT EXISTS (SELECT * FROM Tags)
BEGIN
    INSERT INTO Tags (Tag_Name)
    VALUES 
        ('Technology'),
        ('Education');
END;

-- Populate "Attendee_type" table if empty
IF NOT EXISTS (SELECT * FROM Attendee_type)
BEGIN
    INSERT INTO Attendee_type (attendee_type)
    VALUES 
        ('Student'),
        ('Professional');
END;

-- Populate "Responsibility" table if empty
IF NOT EXISTS (SELECT * FROM Responsibility)
BEGIN
    INSERT INTO Responsibility (Person_Responsible, StartDate, EndDate)
    VALUES 
        (1, '2024-01-01', '2024-06-01'),
        (2, '2024-02-01', '2024-07-01');
END;

-- Populate "Blog_Content" table if empty
IF NOT EXISTS (SELECT * FROM Blog_Content)
BEGIN
    INSERT INTO Blog_Content (File_Path, File_Type)
    VALUES 
        (1, 'Text'),
        (2, 'Image');
END;

-- Populate "Election" table if empty
IF NOT EXISTS (SELECT * FROM Election)
BEGIN
    INSERT INTO Election (Start_Date, End_Date)
    VALUES 
        ('2024-03-01', '2024-03-15'),
        ('2024-09-01', '2024-09-15');
END;

-- Populate "Club_Items" table if empty
IF NOT EXISTS (SELECT * FROM Club_Items)
BEGIN
    INSERT INTO Club_Items (Item_Name, Storage)
    VALUES 
        ('Projector', 'Main Office'),
        ('Chairs', 'Event Hall');
END;

-- Populate "Order_Details" table if empty
IF NOT EXISTS (SELECT * FROM Order_Details)
BEGIN
    INSERT INTO Order_Details (Product_ID, Quantity)
    VALUES 
        (1, 50),
        (2, 100);
END;

-- Populate "Event_Teams" table if empty
IF NOT EXISTS (SELECT * FROM Event_Teams)
BEGIN
    INSERT INTO Event_Teams (Event_ID, Team_ID)
    VALUES 
        (1, 1),
        (2, 2);
END;

-- Populate "Locations" table if empty
IF NOT EXISTS (SELECT * FROM Locations)
BEGIN
    INSERT INTO Locations (Location_Name)
    VALUES 
        ('Conference Room A'),
        ('Main Hall');
END;
-- Populate "Users" table if empty
IF NOT EXISTS (SELECT * FROM Users)
BEGIN
    INSERT INTO Users (Name, RegDate, Contact_Number, Privilege, Password)
    VALUES 
        ('admin', '2024-01-01', '3001234567', 1, '123'),
        ('user', '2024-01-02', '3007654321', 2, '123');
END;

-- Populate "Blog_Contents" table if empty
IF NOT EXISTS (SELECT * FROM Blog_Contents)
BEGIN
    INSERT INTO Blog_Contents (File_Path, File_Type)
    VALUES 
        ('/files/blog1.pdf', 'application/pdf'),
        ('/files/blog2.docx', 'application/msword');
END;
