IF EXISTS (SELECT * FROM sys.databases WHERE name = 'CLUBS_DATABASE')
    USE MASTER 
    DROP DATABASE CLUBS_DATABASE
GO

CREATE DATABASE CLUBS_DATABASE;
USE CLUBS_DATABASE;
GO

CREATE TABLE "Event"(
    "Event_ID" INT IDENTITY(1,1) NOT NULL,
    "Event_Name" VARCHAR(255) NOT NULL,
    "Start_Date" DATETIME2 NOT NULL,
    "End_Date" DATETIME2 NOT NULL,
    "Location" INT NOT NULL,
    "Scale" INT NOT NULL,
    "Description" INT NOT NULL,
    PRIMARY KEY ("Event_ID")
);

CREATE TABLE "Products"(
    "Product_ID" INT IDENTITY(1,1) PRIMARY KEY,
    "Product_Name" VARCHAR(255) NOT NULL,
    "Price" INT NOT NULL
);

CREATE TABLE "Majors"(
    "Major_ID" INT IDENTITY(1,1) PRIMARY KEY,
    "Name" VARCHAR(255) NOT NULL  -- Major name
);

CREATE TABLE "TransactionType"(
    "Type_ID" INT IDENTITY(1,1) PRIMARY KEY,
    "Type_Name" VARCHAR(255) NOT NULL
);

CREATE TABLE "Team_Roles"(
    "role_id" INT IDENTITY(1,1) PRIMARY KEY,
    "role_name" VARCHAR(255) NOT NULL,  -- Corrected column type for name
    "role_description" TEXT NOT NULL  -- Corrected column type for description
);

CREATE TABLE "Role_types"(
    "Role_Id" INT IDENTITY(1,1) PRIMARY KEY,
    "Role_Name" VARCHAR(255) NOT NULL  -- Corrected column type for Role_Name
);

CREATE TABLE "Tags"(
    "Tag_ID" INT IDENTITY(1,1) PRIMARY KEY,
    "Tag_Name" VARCHAR(255) NOT NULL
);

CREATE TABLE "Attendee_type"(
    "type_id" INT IDENTITY(1,1) PRIMARY KEY,
    "attendee_type" VARCHAR(255) NOT NULL
);

CREATE TABLE "Responsibility"(
    "Item_ID" INT IDENTITY(1,1) PRIMARY KEY,
    "Person_Responsible" INT NOT NULL,
    "StartDate" DATE NOT NULL,
    "EndDate" DATE NOT NULL
);

CREATE TABLE "Blog_Content"(
    "Post_ID" INT IDENTITY(1,1) PRIMARY KEY,
    "File" INT NOT NULL,
    "File_Type" NCHAR(255) NOT NULL
);

CREATE TABLE "Election"(
    "Election_ID" INT IDENTITY(1,1) PRIMARY KEY,
    "Start_Date" DATETIME2 NOT NULL,
    "End_Date" DATETIME2 NOT NULL
);

CREATE TABLE "Club_Items"(
    "Item_ID" INT IDENTITY(1,1) PRIMARY KEY,
    "Item_Name" VARCHAR(255) NOT NULL,
    "Storage" VARCHAR(255) NOT NULL
);

CREATE TABLE "Order_Details"(
    "Order_ID" INT IDENTITY(1,1) PRIMARY KEY,
    "Product_ID" INT NOT NULL,
    "Quantity" INT NOT NULL
);

CREATE TABLE "Event_Teams"(
    "Event_ID" INT NOT NULL,
    "Team_ID" INT NOT NULL,
    PRIMARY KEY ("Event_ID", "Team_ID")
);

CREATE TABLE "Locations"(
    "Location_ID" INT IDENTITY(1,1) PRIMARY KEY,
    "Location_Name" VARCHAR(255) NOT NULL  -- Corrected column type for name
);

CREATE TABLE "Product"(
    "Product_ID" INT IDENTITY(1,1) PRIMARY KEY,
    "Product_Name" VARCHAR(255) NOT NULL,
    "Price" INT NOT NULL,
    "Items_In_Stock" INT NOT NULL
);

CREATE TABLE "User"(
    "User_ID" INT IDENTITY(1,1) PRIMARY KEY,
    "Name" VARCHAR(255) NOT NULL,
    "RegDate" DATETIME2 NOT NULL,
    "Contact_Number" INT NOT NULL,  
    "Privilege" INT NOT NULL,
    "Password" NVARCHAR(255) NOT NULL,
    "Address" VARCHAR(255) NULL,
    "CNIC" VARCHAR(255) NULL,
    "Year" INT NULL,
    "HUID" INT NULL
);

CREATE TABLE "Event_Leaders"(
    "Event_ID" INT NOT NULL,
    "Event_Lead" INT NOT NULL,
    PRIMARY KEY ("Event_ID", "Event_Lead"),
    FOREIGN KEY ("Event_ID") REFERENCES "Event"("Event_ID"),
    FOREIGN KEY ("Event_Lead") REFERENCES "User"("User_ID")
);

CREATE TABLE "Event_Participation"(
    "Event_ID" INT NOT NULL,
    "Attendee" INT NOT NULL,
    PRIMARY KEY ("Event_ID", "Attendee"),
    FOREIGN KEY ("Event_ID") REFERENCES "Event"("Event_ID"),
    FOREIGN KEY ("Attendee") REFERENCES "User"("User_ID")
);

CREATE TABLE "User_Majors"(
    "User_ID" INT NOT NULL,
    "Major_ID" INT NOT NULL,
    "StartDate" DATE NOT NULL,
    "EndDate" DATE NOT NULL,
    PRIMARY KEY ("User_ID", "Major_ID", "StartDate"),
    FOREIGN KEY ("User_ID") REFERENCES "User"("User_ID"),
    FOREIGN KEY ("Major_ID") REFERENCES "Majors"("Major_ID")
);

CREATE TABLE "Blog"(
    "Post_ID" INT IDENTITY(1,1) PRIMARY KEY,
    "Title" VARCHAR(255) NOT NULL,
    "Date_Created" DATETIME2 NOT NULL,
    "User_ID" INT NOT NULL,
    FOREIGN KEY ("User_ID") REFERENCES "User"("User_ID")
);

CREATE TABLE "Team"(
    "Team_ID" INT IDENTITY(1,1) PRIMARY KEY,
    "Team_Name" VARCHAR(255) NOT NULL,
    "Team_Lead" INT NOT NULL,
    "Date_Created" DATETIME2 NOT NULL,
    FOREIGN KEY ("Team_Lead") REFERENCES "User"("User_ID")
);

CREATE TABLE "Orders"(
    "Order_ID" INT IDENTITY(1,1) PRIMARY KEY,
    "Customer_ID" INT NOT NULL,
    "Order_Date" DATE NOT NULL,
    "Delivery_Date" DATE NOT NULL,
    FOREIGN KEY ("Customer_ID") REFERENCES "User"("User_ID")
);

CREATE TABLE "Blog_Tags"(
    "Post_ID" INT NOT NULL,
    "Tag_ID" INT NOT NULL,
    PRIMARY KEY ("Post_ID", "Tag_ID"),
    FOREIGN KEY ("Post_ID") REFERENCES "Blog"("Post_ID"),
    FOREIGN KEY ("Tag_ID") REFERENCES "Tags"("Tag_ID")
);

CREATE TABLE "Privileges"(
    "User_ID" INT NOT NULL,
    "StartDate" DATE NOT NULL,
    "Privilege" VARCHAR(255) NOT NULL,  -- Corrected column type for Privilege
    "EndDate" DATE NOT NULL,
    PRIMARY KEY("User_ID", "StartDate"),
    FOREIGN KEY ("User_ID") REFERENCES "User"("User_ID")
);

CREATE TABLE "Candidates"(
    "Candidate_ID" INT IDENTITY(1,1) PRIMARY KEY,
    "User_ID" INT NOT NULL,
    "Role_ID" INT NOT NULL,
    "Election_ID" INT NOT NULL,
    FOREIGN KEY ("User_ID") REFERENCES "User"("User_ID"),
    FOREIGN KEY ("Role_ID") REFERENCES "Role_types"("Role_Id"),
    FOREIGN KEY ("Election_ID") REFERENCES "Election"("Election_ID")
);

CREATE TABLE "Voting"(
    "Voter_ID" INT IDENTITY(1,1) PRIMARY KEY,
    "Candidate_ID" INT NOT NULL,
    "User_ID" INT NOT NULL,
    "Role_ID" INT NOT NULL,
    "Election_ID" INT NOT NULL,
    FOREIGN KEY ("Candidate_ID", "User_ID", "Role_ID", "Election_ID") REFERENCES "Candidates"("Candidate_ID", "User_ID", "Role_ID", "Election_ID")
);

CREATE TABLE "Attendees"(
    "User_ID" INT NOT NULL,
    "Event_ID" INT NOT NULL,
    "type_id" INT NOT NULL,
    PRIMARY KEY("User_ID", "Event_ID"),
    FOREIGN KEY ("User_ID") REFERENCES "User"("User_ID"),
    FOREIGN KEY ("Event_ID") REFERENCES "Event"("Event_ID"),
    FOREIGN KEY ("type_id") REFERENCES "Attendee_type"("type_id")
);

CREATE TABLE "Team_Members"(
    "User_ID" INT NOT NULL,
    "Team_ID" INT NOT NULL,
    "Role" INT NOT NULL,
    "Date_Ended" DATE NULL,
    "Date_Started" DATE NOT NULL,
    "isLeader" BIT NOT NULL,  -- Changed to BIT for Boolean values
    PRIMARY KEY("User_ID", "Team_ID"),
    FOREIGN KEY ("User_ID") REFERENCES "User"("User_ID"),
    FOREIGN KEY ("Team_ID") REFERENCES "Team"("Team_ID"),
    FOREIGN KEY ("Role") REFERENCES "Team_Roles"("role_id")
);

CREATE TABLE "Leadership"(
    "User_ID" INT NOT NULL,
    "Role_ID" INT NOT NULL,
    "StartDate" DATETIME2 NOT NULL,
    "EndDate" DATETIME2 NOT NULL,
    PRIMARY KEY("User_ID", "Role_ID", "StartDate"),
    FOREIGN KEY ("User_ID") REFERENCES "User"("User_ID"),
    FOREIGN KEY ("Role_ID") REFERENCES "Role_types"("Role_Id")
);

CREATE TABLE "Sales"(
    "Product_ID" INT NOT NULL,
    "Quantity" INT NOT NULL,
    "Sale_Date" DATETIME2 NOT NULL,
    PRIMARY KEY("Product_ID", "Sale_Date"),
    FOREIGN KEY ("Product_ID") REFERENCES "Products"("Product_ID")
);

CREATE TABLE "Inventory"(
    "Product_ID" INT NOT NULL,
    "Quantity_In_Stock" INT NOT NULL,
    "Location_ID" INT NOT NULL,
    PRIMARY KEY("Product_ID", "Location_ID"),
    FOREIGN KEY ("Product_ID") REFERENCES "Products"("Product_ID"),
    FOREIGN KEY ("Location_ID") REFERENCES "Locations"("Location_ID")
);
