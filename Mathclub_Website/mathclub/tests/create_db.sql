-- Check and create "Event" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Event')
BEGIN
    CREATE TABLE "Event"(
        "Event_ID" INT IDENTITY(1,1) NOT NULL,
        "Event_Name" VARCHAR(255) NOT NULL,
        "Start_Date" DATETIME2 NOT NULL,
        "End_Date" DATETIME2 NOT NULL,
        "Location" INT NOT NULL,
        "Scale" INT NOT NULL,
        "Description" VARCHAR(255) NOT NULL,
        PRIMARY KEY ("Event_ID")
    );
END;

-- Check and create "Products" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Products')
BEGIN
    CREATE TABLE "Products"(
        "Product_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Product_Name" VARCHAR(255) NOT NULL,
        "Price" INT NOT NULL
    );
END;

-- Check and create "Majors" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Majors')
BEGIN
    CREATE TABLE "Majors"(
        "Major_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Name" VARCHAR(255) NOT NULL
    );
END;

-- Check and create "TransactionType" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'TransactionType')
BEGIN
    CREATE TABLE "TransactionType"(
        "Type_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Type_Name" VARCHAR(255) NOT NULL
    );
END;

-- Check and create "Team_Roles" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Team_Roles')
BEGIN
    CREATE TABLE "Team_Roles"(
        "role_id" INT IDENTITY(1,1) PRIMARY KEY,
        "role_name" VARCHAR(255) NOT NULL,
        "role_description" TEXT NOT NULL
    );
END;

-- Check and create "Role_types" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Role_types')
BEGIN
    CREATE TABLE "Role_types"(
        "Role_Id" INT IDENTITY(1,1) PRIMARY KEY,
        "Role_Name" VARCHAR(255) NOT NULL
    );
END;

-- Check and create "Tags" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Tags')
BEGIN
    CREATE TABLE "Tags"(
        "Tag_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Tag_Name" VARCHAR(255) NOT NULL
    );
END;

-- Check and create "Attendee_type" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Attendee_type')
BEGIN
    CREATE TABLE "Attendee_type"(
        "type_id" INT IDENTITY(1,1) PRIMARY KEY,
        "attendee_type" VARCHAR(255) NOT NULL
    );
END;

-- Check and create "Responsibility" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Responsibility')
BEGIN
    CREATE TABLE "Responsibility"(
        "Item_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Person_Responsible" INT NOT NULL,
        "StartDate" DATE NOT NULL,
        "EndDate" DATE NOT NULL
    );
END;

-- Check and create "Blog_Content" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Blog_Content')
BEGIN
    CREATE TABLE "Blog_Content"(
        "Post_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "File" INT NOT NULL,
        "File_Type" NCHAR(255) NOT NULL
    );
END;

-- Check and create "Election" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Election')
BEGIN
    CREATE TABLE "Election"(
        "Election_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Start_Date" DATETIME2 NOT NULL,
        "End_Date" DATETIME2 NOT NULL
    );
END;

-- Check and create "Club_Items" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Club_Items')
BEGIN
    CREATE TABLE "Club_Items"(
        "Item_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Item_Name" VARCHAR(255) NOT NULL,
        "Storage" VARCHAR(255) NOT NULL
    );
END;

-- Check and create "Order_Details" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Order_Details')
BEGIN
    CREATE TABLE "Order_Details"(
        "Order_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Product_ID" INT NOT NULL,
        "Quantity" INT NOT NULL
    );
END;

-- Check and create "Event_Teams" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Event_Teams')
BEGIN
    CREATE TABLE "Event_Teams"(
        "Event_ID" INT NOT NULL,
        "Team_ID" INT NOT NULL,
        PRIMARY KEY ("Event_ID", "Team_ID")
    );
END;

-- Check and create "Locations" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Locations')
BEGIN
    CREATE TABLE "Locations"(
        "Location_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Location_Name" VARCHAR(255) NOT NULL
    );
END;

-- Check and create "Product" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Product')
BEGIN
    CREATE TABLE "Product"(
        "Product_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Product_Name" VARCHAR(255) NOT NULL,
        "Price" INT NOT NULL,
        "Items_In_Stock" INT NOT NULL
    );
END;

-- Check and create "User" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'User')
BEGIN
    CREATE TABLE "User"(
        "User_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Name" VARCHAR(255) NOT NULL,
        "RegDate" DATETIME2 NOT NULL,
        "Contact_Number" VARCHAR(10) NOT NULL,  
        "Privilege" INT NOT NULL,
        "Password" NVARCHAR(255) NOT NULL,
        "Address" VARCHAR(255) NULL,
        "CNIC" VARCHAR(255) NULL,
        "Year" INT NULL,
        "HUID" INT NULL
    );
END;

-- Check and create "Event_Leaders" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Event_Leaders')
BEGIN
    CREATE TABLE "Event_Leaders"(
        "Event_ID" INT NOT NULL,
        "Event_Lead" INT NOT NULL,
        PRIMARY KEY ("Event_ID", "Event_Lead"),
        FOREIGN KEY ("Event_ID") REFERENCES "Event"("Event_ID"),
        FOREIGN KEY ("Event_Lead") REFERENCES "User"("User_ID")
    );
END;

-- Check and create "Event_Participation" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Event_Participation')
BEGIN
    CREATE TABLE "Event_Participation"(
        "Event_ID" INT NOT NULL,
        "Attendee" INT NOT NULL,
        PRIMARY KEY ("Event_ID", "Attendee"),
        FOREIGN KEY ("Event_ID") REFERENCES "Event"("Event_ID"),
        FOREIGN KEY ("Attendee") REFERENCES "User"("User_ID")
    );
END;

-- Check and create "User_Majors" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'User_Majors')
BEGIN
    CREATE TABLE "User_Majors"(
        "User_ID" INT NOT NULL,
        "Major_ID" INT NOT NULL,
        "StartDate" DATE NOT NULL,
        "EndDate" DATE NOT NULL,
        PRIMARY KEY ("User_ID", "Major_ID", "StartDate"),
        FOREIGN KEY ("User_ID") REFERENCES "User"("User_ID"),
        FOREIGN KEY ("Major_ID") REFERENCES "Majors"("Major_ID")
    );
END;

-- Check and create "Blog" table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Blog')
BEGIN
    CREATE TABLE "Blog"(
        "Post_ID" INT IDENTITY(1,1) PRIMARY KEY,
        "Title" VARCHAR(255) NOT NULL,
        "Date_Created" DATETIME2 NOT NULL,
        "User_ID" INT NOT NULL,
        FOREIGN KEY ("User_ID") REFERENCES "User"("User_ID")
    );
END;



-- Populate "Event" table if empty
IF NOT EXISTS (SELECT * FROM "Event")
BEGIN
    INSERT INTO "Event" ("Event_Name", "Start_Date", "End_Date", "Location", "Scale", "Description")
    VALUES 
        ('Tech Conference', '2024-01-10', '2024-01-12', 1, 100, 'Annual Tech Event'),
        ('Hackathon', '2024-02-15', '2024-02-16', 2, 50, 'Coding Competition');
END;

-- Populate "Products" table if empty
IF NOT EXISTS (SELECT * FROM "Products")
BEGIN
    INSERT INTO "Products" ("Product_Name", "Price")
    VALUES 
        ('T-Shirt', 500),
        ('Notebook', 200);
END;

-- Populate "Majors" table if empty
IF NOT EXISTS (SELECT * FROM "Majors")
BEGIN
    INSERT INTO "Majors" ("Name")
    VALUES 
        ('Computer Science'),
        ('Electrical Engineering');
END;

-- Populate "TransactionType" table if empty
IF NOT EXISTS (SELECT * FROM "TransactionType")
BEGIN
    INSERT INTO "TransactionType" ("Type_Name")
    VALUES 
        ('Purchase'),
        ('Donation');
END;

-- Populate "Team_Roles" table if empty
IF NOT EXISTS (SELECT * FROM "Team_Roles")
BEGIN
    INSERT INTO "Team_Roles" ("role_name", "role_description")
    VALUES 
        ('Leader', 'Responsible for team management'),
        ('Member', 'Assist in team activities');
END;

-- Populate "Role_types" table if empty
IF NOT EXISTS (SELECT * FROM "Role_types")
BEGIN
    INSERT INTO "Role_types" ("Role_Name")
    VALUES 
        ('Admin'),
        ('User');
END;

-- Populate "Tags" table if empty
IF NOT EXISTS (SELECT * FROM "Tags")
BEGIN
    INSERT INTO "Tags" ("Tag_Name")
    VALUES 
        ('Technology'),
        ('Education');
END;

-- Populate "Attendee_type" table if empty
IF NOT EXISTS (SELECT * FROM "Attendee_type")
BEGIN
    INSERT INTO "Attendee_type" ("attendee_type")
    VALUES 
        ('Student'),
        ('Professional');
END;

-- Populate "Responsibility" table if empty
IF NOT EXISTS (SELECT * FROM "Responsibility")
BEGIN
    INSERT INTO "Responsibility" ("Person_Responsible", "StartDate", "EndDate")
    VALUES 
        (1, '2024-01-01', '2024-06-01'),
        (2, '2024-02-01', '2024-07-01');
END;

-- Populate "Blog_Content" table if empty
IF NOT EXISTS (SELECT * FROM "Blog_Content")
BEGIN
    INSERT INTO "Blog_Content" ("File", "File_Type")
    VALUES 
        (1, 'Text'),
        (2, 'Image');
END;

-- Populate "Election" table if empty
IF NOT EXISTS (SELECT * FROM "Election")
BEGIN
    INSERT INTO "Election" ("Start_Date", "End_Date")
    VALUES 
        ('2024-03-01', '2024-03-15'),
        ('2024-09-01', '2024-09-15');
END;

-- Populate "Club_Items" table if empty
IF NOT EXISTS (SELECT * FROM "Club_Items")
BEGIN
    INSERT INTO "Club_Items" ("Item_Name", "Storage")
    VALUES 
        ('Projector', 'Main Office'),
        ('Chairs', 'Event Hall');
END;

-- Populate "Order_Details" table if empty
IF NOT EXISTS (SELECT * FROM "Order_Details")
BEGIN
    INSERT INTO "Order_Details" ("Product_ID", "Quantity")
    VALUES 
        (1, 50),
        (2, 100);
END;

-- Populate "Event_Teams" table if empty
IF NOT EXISTS (SELECT * FROM "Event_Teams")
BEGIN
    INSERT INTO "Event_Teams" ("Event_ID", "Team_ID")
    VALUES 
        (1, 1),
        (2, 2);
END;

-- Populate "Locations" table if empty
IF NOT EXISTS (SELECT * FROM "Locations")
BEGIN
    INSERT INTO "Locations" ("Location_Name")
    VALUES 
        ('Conference Room A'),
        ('Main Hall');
END;

-- Populate "Product" table if empty
IF NOT EXISTS (SELECT * FROM "Product")
BEGIN
    INSERT INTO "Product" ("Product_Name", "Price", "Items_In_Stock")
    VALUES 
        ('T-Shirt', 500, 100),
        ('Notebook', 200, 50);
END;

-- Populate "User" table if empty
IF NOT EXISTS (SELECT * FROM "User")
BEGIN
    INSERT INTO "User" ("Name", "RegDate", "Contact_Number", "Privilege", "Password", "Address", "CNIC", "Year", "HUID")
    VALUES 
        ('John Doe', '2024-01-01', '1234567890', 1, 'password123', '123 Street', '12345-6789012-3', 2024, 1001),
        ('Jane Smith', '2024-01-15', '9876543210', 2, 'password456', '456 Avenue', '23456-7890123-4', 2024, 1002);
END;

-- Populate "Event_Leaders" table if empty
IF NOT EXISTS (SELECT * FROM "Event_Leaders")
BEGIN
    INSERT INTO "Event_Leaders" ("Event_ID", "Event_Lead")
    VALUES 
        (1, 1),
        (2, 2);
END;

-- Populate "Event_Participation" table if empty
IF NOT EXISTS (SELECT * FROM "Event_Participation")
BEGIN
    INSERT INTO "Event_Participation" ("Event_ID", "Attendee")
    VALUES 
        (1, 1),
        (2, 2);
END;

-- Populate "User_Majors" table if empty
IF NOT EXISTS (SELECT * FROM "User_Majors")
BEGIN
    INSERT INTO "User_Majors" ("User_ID", "Major_ID", "StartDate", "EndDate")
    VALUES 
        (1, 1, '2024-01-01', '2024-12-31'),
        (2, 2, '2024-01-01', '2024-12-31');
END;

-- Populate "Blog" table if empty
IF NOT EXISTS (SELECT * FROM "Blog")
BEGIN
    INSERT INTO "Blog" ("Title", "Date_Created", "User_ID")
    VALUES 
        ('First Post', '2024-01-01', 1),
        ('Second Post', '2024-01-02', 2);
END;




