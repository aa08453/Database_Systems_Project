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

-- Check and create "User" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'User')
BEGIN
    CREATE TABLE "User"(
        "User_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Name" VARCHAR(255) NOT NULL,
        "Reg_Date" DATE NOT NULL,
        "Contact_Number" INT NOT NULL, 
        "Password" NVARCHAR(255) NOT NULL,
        "Address" VARCHAR(255) NULL,
        "CNIC" VARCHAR(255) NULL,
        "Year" INT NULL,
        "Major" INT NULL,
        "HUID" INT NULL,
        FOREIGN KEY ("Major") REFERENCES "Majors" ("Major_ID")
    );
END;

-- Check and create "Teams" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Teams')
BEGIN
    CREATE TABLE "Teams"(
        "Team_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Team_Name" NVARCHAR(255) NOT NULL,
        "Team_Lead" INT NOT NULL,
        "Date_Created" DATE NOT NULL,
        FOREIGN KEY ("Team_Lead") REFERENCES "User"("User_ID")
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
        "User_ID" INT NOT NULL,
        "Team_ID" INT NOT NULL,
        "Role" INT NOT NULL,
        "Date_Started" DATE NOT NULL,
        "Date_Ended" DATE NOT NULL,
        PRIMARY KEY ("User_ID", "Team_ID"),
        FOREIGN KEY ("User_ID") REFERENCES "User"("User_ID"),
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
        FOREIGN KEY ("Event_Lead") REFERENCES "User"("User_ID"),
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
        "Event_ID" INT NOT NULL,
        "Attendee" INT NOT NULL,
        "Type_ID" INT NOT NULL
        PRIMARY KEY ("Event_ID", "Attendee"),
        FOREIGN KEY ("Type_ID") REFERENCES "Attendee_Type" ("Type_ID"),
        FOREIGN KEY ("Event_ID") REFERENCES "Events"("Event_ID"),
        FOREIGN KEY ("Attendee") REFERENCES "User"("User_ID")
    );
END;

-- Check and create "Event_Teams" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Event_Teams')
BEGIN
    CREATE TABLE "Event_Teams"(
        "Event_ID" INT NOT NULL,
        "Team_ID" INT NOT NULL,
        PRIMARY KEY ("Event_ID", "Team_ID"),
        FOREIGN KEY ("Team_ID") REFERENCES "Teams"("Team_ID"),
        FOREIGN KEY ("Event_ID") REFERENCES "Events"("Event_ID")
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
        FOREIGN KEY ("Customer_ID") REFERENCES "User"("User_ID")
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
        "Order_ID" INT NOT NULL,
        "Product_ID" INT NOT NULL,
        "Quantity" INT NOT NULL,
        PRIMARY KEY ("Order_ID", "Product_ID"),
        FOREIGN KEY ("Order_ID") REFERENCES "Orders"("Order_ID"),
        FOREIGN KEY ("Product_ID") REFERENCES "Products"("Product_ID")
    );
END;

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
        "Item_ID" INT NOT NULL,
        "Person_Responsible" INT NOT NULL,
        "StartDate" DATE NOT NULL,
        "EndDate" DATE NOT NULL,
        PRIMARY KEY ("Item_ID", "Person_Responsible"),
        FOREIGN KEY ("Person_Responsible") REFERENCES "User" ("User_ID"),
        FOREIGN KEY ("Item_ID") REFERENCES "Club_Items" ("Item_ID")
    );
END;

-- Check and create "Blog" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Blog')
BEGIN
    CREATE TABLE "Blog"(
        "Post_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Title" VARCHAR(255) NOT NULL,
        "Date_Created" DATE NOT NULL,
        "User_ID" INT NOT NULL,
        FOREIGN KEY ("User_ID") REFERENCES "User"("User_ID")
    );
END;

-- Check and create "Blog_Content" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Blog_Content')
BEGIN
    CREATE TABLE "Blog_Content"(
        "Post_ID" INT NOT NULL,
        "File_ID" INT NOT NULL,
        "File" NCHAR(255) NOT NULL,
        PRIMARY KEY ("Post_ID", "File_ID"),
        FOREIGN KEY ("Post_ID") REFERENCES "Blog"("Post_ID")        
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

-- Check and create "Blog_Tags" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Blog_Tags')
BEGIN
    CREATE TABLE "Blog_Tags"(
        "Post_ID" INT NOT NULL,
        "Tag_ID" INT NOT NULL,
        PRIMARY KEY ("Post_ID", "Tag_ID"),
        FOREIGN KEY ("Post_ID") REFERENCES "Blog"("Post_ID"),
        FOREIGN KEY ("Tag_ID") REFERENCES "Tags"("Tag_ID")
    );
END;

-- Check and create "Privileges" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Privileges')
BEGIN
    CREATE TABLE "Privileges"(
        "User_ID" INT NOT NULL,
        "Privilege" INT NOT NULL,
        "Start_Date" DATE NOT NULL,
        "End_Date" DATE NOT NULL,
        PRIMARY KEY ("User_ID", "Start_Date"),
        FOREIGN KEY ("User_ID") REFERENCES "User"("User_ID")
    );
END;

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
        "Transaction_ID" INT NOT NULL,
        "Responsible_Officer" INT NOT NULL,
        "User_ID" INT NOT NULL,
        "Transaction_Type" INT NOT NULL,
        "Date" DATE NOT NULL,
        "Description" NVARCHAR(255) NOT NULL,
        PRIMARY KEY ("Transaction_ID", "Responsible_Officer", "User_ID"),
        FOREIGN KEY ("Responsible_Officer") REFERENCES "User" ("User_ID"),
        FOREIGN KEY ("User_ID") REFERENCES "User" ("User_ID"),
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

-- Check and create "Leadership" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Leadership')
BEGIN
    CREATE TABLE "Leadership"(
        "User_ID" INT NOT NULL,
        "Role_ID" INT NOT NULL,
        "Start_Date" DATE NOT NULL,
        "End_Date" DATE NOT NULL,
        PRIMARY KEY ("User_ID", "Role_ID", "Start_Date"),
        FOREIGN KEY ("Role_ID") REFERENCES "Role_Types" ("Role_ID"),
        FOREIGN KEY ("User_ID") REFERENCES "Candidates" ("Candidate_ID")
    );
END;

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
        FOREIGN KEY ("User_ID") REFERENCES "User" ("User_ID")
    );
END;

-- Check and create "Voting" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Voting')
BEGIN
    CREATE TABLE "Voting"(
        "Voter_ID" INT NOT NULL,
        "Candidate_ID" INT NOT NULL,
        PRIMARY KEY ("Voter_ID", "Candidate_ID"),
        FOREIGN KEY ("Voter_ID") REFERENCES "User"("User_ID"),
        FOREIGN KEY ("Candidate_ID") REFERENCES "Candidates"("Candidate_ID")
    );
END;