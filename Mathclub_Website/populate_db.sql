CREATE TABLE "Event"(
    "Event_ID" INT NOT NULL,
    "Event_Lead" INT NOT NULL,
    "Event_Name" VARCHAR(255) NOT NULL,
    "Start_Date" DATETIME2 NOT NULL,
    "End_Date" DATETIME2 NOT NULL,
    "Location" BIGINT NOT NULL,
    "Scale" BIGINT NOT NULL,
    "Description" BIGINT NOT NULL
);
ALTER TABLE
    "Event" ADD CONSTRAINT "event_event_id_primary" PRIMARY KEY("Event_ID");
ALTER TABLE
    "Event" ADD CONSTRAINT "event_event_lead_primary" PRIMARY KEY("Event_Lead");
CREATE TABLE "Responsibility"(
    "Item_ID" BIGINT NOT NULL,
    "Person_Responsible" BIGINT NOT NULL,
    "StartDate" DATE NOT NULL,
    "EndDate" DATE NOT NULL
);
ALTER TABLE
    "Responsibility" ADD CONSTRAINT "responsibility_item_id_primary" PRIMARY KEY("Item_ID");
ALTER TABLE
    "Responsibility" ADD CONSTRAINT "responsibility_person_responsible_primary" PRIMARY KEY("Person_Responsible");
CREATE TABLE "Blog_Content"(
    "Post_ID" INT NOT NULL,
    "File" BIGINT NOT NULL,
    "File_Type" NCHAR(255) NOT NULL
);
ALTER TABLE
    "Blog_Content" ADD CONSTRAINT "blog_content_post_id_primary" PRIMARY KEY("Post_ID");
CREATE TABLE "Order_Details"(
    "Order_ID" INT NOT NULL,
    "Product_ID" INT NOT NULL,
    "Quantity" INT NOT NULL
);
ALTER TABLE
    "Order_Details" ADD CONSTRAINT "order_details_order_id_primary" PRIMARY KEY("Order_ID");
ALTER TABLE
    "Order_Details" ADD CONSTRAINT "order_details_product_id_primary" PRIMARY KEY("Product_ID");
CREATE TABLE "Event_Teams"(
    "Event_ID" INT NOT NULL,
    "Team_ID" INT NOT NULL
);
ALTER TABLE
    "Event_Teams" ADD CONSTRAINT "event_teams_event_id_primary" PRIMARY KEY("Event_ID");
ALTER TABLE
    "Event_Teams" ADD CONSTRAINT "event_teams_team_id_primary" PRIMARY KEY("Team_ID");
CREATE TABLE "Locations"(
    "Location_ID" BIGINT NOT NULL,
    "Location_Name" BIGINT NOT NULL
);
ALTER TABLE
    "Locations" ADD CONSTRAINT "locations_location_id_primary" PRIMARY KEY("Location_ID");
CREATE TABLE "Blog"(
    "Post_ID" INT NOT NULL,
    "Title" VARCHAR(255) NOT NULL,
    "Date_Created" DATETIME2 NOT NULL,
    "User_ID" INT NOT NULL
);
ALTER TABLE
    "Blog" ADD CONSTRAINT "blog_post_id_primary" PRIMARY KEY("Post_ID");
ALTER TABLE
    "Blog" ADD CONSTRAINT "blog_user_id_primary" PRIMARY KEY("User_ID");
CREATE TABLE "Product"(
    "Product_ID" INT NOT NULL,
    "Product_Name" VARCHAR(255) NOT NULL,
    "Price" INT NOT NULL,
    "Items_In_Stock" INT NOT NULL
);
ALTER TABLE
    "Product" ADD CONSTRAINT "product_product_id_primary" PRIMARY KEY("Product_ID");
CREATE TABLE "Team"(
    "Team_ID" INT NOT NULL,
    "Team_Name" VARCHAR(255) NOT NULL,
    "Team_Lead" INT NOT NULL,
    "Date_Created" DATETIME2 NOT NULL
);
ALTER TABLE
    "Team" ADD CONSTRAINT "team_team_id_primary" PRIMARY KEY("Team_ID");
CREATE TABLE "Event_Participation"(
    "Event_ID" INT NOT NULL,
    "Attendee" INT NOT NULL
);
ALTER TABLE
    "Event_Participation" ADD CONSTRAINT "event_participation_event_id_primary" PRIMARY KEY("Event_ID");
ALTER TABLE
    "Event_Participation" ADD CONSTRAINT "event_participation_attendee_primary" PRIMARY KEY("Attendee");
CREATE TABLE "Tags"(
    "Tag_ID" INT NOT NULL,
    "Tag_Name" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Tags" ADD CONSTRAINT "tags_tag_id_primary" PRIMARY KEY("Tag_ID");
CREATE TABLE "Orders"(
    "Order_ID" INT NOT NULL,
    "Customer_ID" INT NOT NULL,
    "Order_Date" DATE NOT NULL,
    "Delivery_Date" DATE NOT NULL,
    "Delivery_Date" DATE NOT NULL
);
ALTER TABLE
    "Orders" ADD CONSTRAINT "orders_order_id_primary" PRIMARY KEY("Order_ID");
ALTER TABLE
    "Orders" ADD CONSTRAINT "orders_customer_id_primary" PRIMARY KEY("Customer_ID");
CREATE TABLE "Club_Items"(
    "Item_ID" INT NOT NULL,
    "Item_Name" VARCHAR(255) NOT NULL,
    "Storage" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Club_Items" ADD CONSTRAINT "club_items_item_id_primary" PRIMARY KEY("Item_ID");
CREATE TABLE "Blog_Tags"(
    "Post_ID" INT NOT NULL,
    "Tag_ID" INT NOT NULL
);

CREATE TABLE "Attendee_type"(
    "type_id" BIGINT NOT NULL,
    "attendee_type" BIGINT NOT NULL
);
ALTER TABLE
    "Attendee_type" ADD CONSTRAINT "attendee_type_type_id_primary" PRIMARY KEY("type_id");
CREATE TABLE "Election"(
    "Election_ID" INT NOT NULL,
    "Start_Date" DATETIME2 NOT NULL,
    "End_Date" DATETIME2 NOT NULL
);
ALTER TABLE
    "Election" ADD CONSTRAINT "election_election_id_primary" PRIMARY KEY("Election_ID");
CREATE TABLE "Majors"(
    "Major_ID" BIGINT NOT NULL,
    "StartDate" DATE NOT NULL,
    "Name" BIGINT NOT NULL,
    "EndDate" DATE NOT NULL
);
ALTER TABLE
    "Majors" ADD CONSTRAINT "majors_major_id_primary" PRIMARY KEY("Major_ID");
ALTER TABLE
    "Majors" ADD CONSTRAINT "majors_startdate_primary" PRIMARY KEY("StartDate");
CREATE TABLE "Voting"(
    "Voter_ID" INT NOT NULL,
    "Candidate_ID" INT NOT NULL
);
ALTER TABLE
    "Voting" ADD CONSTRAINT "voting_voter_id_primary" PRIMARY KEY("Voter_ID");
ALTER TABLE
    "Voting" ADD CONSTRAINT "voting_candidate_id_primary" PRIMARY KEY("Candidate_ID");
CREATE TABLE "Team_Roles"(
    "role_id" BIGINT NOT NULL,
    "role_name" BIGINT NOT NULL,
    "role_description" BIGINT NOT NULL
);
ALTER TABLE
    "Team_Roles" ADD CONSTRAINT "team_roles_role_id_primary" PRIMARY KEY("role_id");
CREATE TABLE "Role_types"(
    "Role_Id" BIGINT NOT NULL,
    "Role_Name" BIGINT NOT NULL
);
ALTER TABLE
    "Role_types" ADD CONSTRAINT "role_types_role_id_primary" PRIMARY KEY("Role_Id");
CREATE TABLE "Privileges"(
    "User_ID" BIGINT NOT NULL,
    "StartDate" DATE NOT NULL,
    "Privilege" BIGINT NOT NULL,
    "EndDate" DATE NOT NULL
);
ALTER TABLE
    "Privileges" ADD CONSTRAINT "privileges_user_id_primary" PRIMARY KEY("User_ID");
ALTER TABLE
    "Privileges" ADD CONSTRAINT "privileges_startdate_primary" PRIMARY KEY("StartDate");
CREATE TABLE "Candidates"(
    "Candidate_ID" BIGINT NOT NULL,
    "User_ID" BIGINT NOT NULL,
    "Role_ID" INT NOT NULL,
    "Election_ID" INT NOT NULL
);
ALTER TABLE
    "Candidates" ADD CONSTRAINT "candidates_candidate_id_primary" PRIMARY KEY("Candidate_ID");
ALTER TABLE
    "Candidates" ADD CONSTRAINT "candidates_user_id_primary" PRIMARY KEY("User_ID");
ALTER TABLE
    "Candidates" ADD CONSTRAINT "candidates_role_id_primary" PRIMARY KEY("Role_ID");
ALTER TABLE
    "Candidates" ADD CONSTRAINT "candidates_election_id_primary" PRIMARY KEY("Election_ID");
CREATE TABLE "Attendees"(
    "User_ID" INT NOT NULL,
    "Event_ID" INT NOT NULL,
    "type_id" INT NOT NULL
);
ALTER TABLE
    "Attendees" ADD CONSTRAINT "attendees_user_id_primary" PRIMARY KEY("User_ID");
ALTER TABLE
    "Attendees" ADD CONSTRAINT "attendees_event_id_primary" PRIMARY KEY("Event_ID");
CREATE TABLE "Team_Members"(
    "User_ID" INT NOT NULL,
    "Team_ID" INT NOT NULL,
    "Role" INT NOT NULL,
    "Date_Ended" DATE NULL,
    "Date_Started" DATE NOT NULL,
    "isLeader" BIGINT NOT NULL
);
ALTER TABLE
    "Team_Members" ADD CONSTRAINT "team_members_user_id_primary" PRIMARY KEY("User_ID");
ALTER TABLE
    "Team_Members" ADD CONSTRAINT "team_members_team_id_primary" PRIMARY KEY("Team_ID");
CREATE TABLE "Leadership"(
    "User_ID" BIGINT NOT NULL,
    "Role_ID" BIGINT NOT NULL,
    "StartDate" BIGINT NOT NULL,
    "EndDate" BIGINT NOT NULL
);
ALTER TABLE
    "Leadership" ADD CONSTRAINT "leadership_user_id_primary" PRIMARY KEY("User_ID");
ALTER TABLE
    "Leadership" ADD CONSTRAINT "leadership_role_id_primary" PRIMARY KEY("Role_ID");
ALTER TABLE
    "Leadership" ADD CONSTRAINT "leadership_startdate_primary" PRIMARY KEY("StartDate");
CREATE TABLE "TransactionType"(
    "Type_ID" INT NOT NULL,
    "Type_Name" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "TransactionType" ADD CONSTRAINT "transactiontype_type_id_primary" PRIMARY KEY("Type_ID");
CREATE TABLE "User"(
    "User_ID" INT NOT NULL,
    "Name" VARCHAR(255) NOT NULL,
    "RegDate" DATETIME2 NOT NULL,
    "Contact_Number" INT NOT NULL,
    "Privelege" INT NOT NULL,
    "Password" NVARCHAR(255) NOT NULL,
    "Address" VARCHAR(255) NULL,
    "CNIC" VARCHAR(255) NULL,
    "Year" BIGINT NULL,
    "Major" BIGINT NULL,
    "HUID" BIGINT NULL
);
ALTER TABLE
    "User" ADD CONSTRAINT "user_user_id_primary" PRIMARY KEY("User_ID");
CREATE TABLE "Finances"(
    "Transaction_ID" INT NOT NULL,
    "Responsible_Officer" BIGINT NOT NULL,
    "User_ID" INT NOT NULL,
    "Amount" INT NOT NULL,
    "Transaction_Type" INT NOT NULL,
    "Date" DATETIME2 NOT NULL,
    "Description" VARCHAR(1000) NOT NULL
);
ALTER TABLE
    "Finances" ADD CONSTRAINT "finances_transaction_id_primary" PRIMARY KEY("Transaction_ID");
ALTER TABLE
    "Finances" ADD CONSTRAINT "finances_responsible_officer_primary" PRIMARY KEY("Responsible_Officer");
ALTER TABLE
    "Finances" ADD CONSTRAINT "finances_user_id_primary" PRIMARY KEY("User_ID");
ALTER TABLE
    "User" ADD CONSTRAINT "user_user_id_foreign" FOREIGN KEY("User_ID") REFERENCES "Voting"("Voter_ID");
ALTER TABLE
    "Privileges" ADD CONSTRAINT "privileges_user_id_foreign" FOREIGN KEY("User_ID") REFERENCES "User"("User_ID");
ALTER TABLE
    "Role_types" ADD CONSTRAINT "role_types_role_id_foreign" FOREIGN KEY("Role_Id") REFERENCES "Candidates"("Role_ID");
ALTER TABLE
    "Leadership" ADD CONSTRAINT "leadership_role_id_foreign" FOREIGN KEY("Role_ID") REFERENCES "Candidates"("Role_ID");
ALTER TABLE
    "Election" ADD CONSTRAINT "election_election_id_foreign" FOREIGN KEY("Election_ID") REFERENCES "Candidates"("Election_ID");
ALTER TABLE
    "Team_Members" ADD CONSTRAINT "team_members_role_foreign" FOREIGN KEY("Role") REFERENCES "Team_Roles"("role_id");
ALTER TABLE
    "Finances" ADD CONSTRAINT "finances_transaction_type_foreign" FOREIGN KEY("Transaction_Type") REFERENCES "TransactionType"("Type_ID");
ALTER TABLE
    "Voting" ADD CONSTRAINT "voting_candidate_id_foreign" FOREIGN KEY("Candidate_ID") REFERENCES "Candidates"("Candidate_ID");
ALTER TABLE
    "Candidates" ADD CONSTRAINT "candidates_user_id_foreign" FOREIGN KEY("User_ID") REFERENCES "User"("User_ID");
ALTER TABLE
    "User" ADD CONSTRAINT "user_major_foreign" FOREIGN KEY("Major") REFERENCES "Majors"("Major_ID");
ALTER TABLE
    "Team" ADD CONSTRAINT "team_team_id_foreign" FOREIGN KEY("Team_ID") REFERENCES "Team_Members"("Team_ID");
ALTER TABLE
    "Leadership" ADD CONSTRAINT "leadership_user_id_foreign" FOREIGN KEY("User_ID") REFERENCES "Candidates"("Candidate_ID");
ALTER TABLE
    "User" ADD CONSTRAINT "user_user_id_foreign" FOREIGN KEY("User_ID") REFERENCES "Attendees"("User_ID");
ALTER TABLE
    "Attendees" ADD CONSTRAINT "attendees_type_id_foreign" FOREIGN KEY("type_id") REFERENCES "Attendee_type"("attendee_type");
ALTER TABLE
    "User" ADD CONSTRAINT "user_user_id_foreign" FOREIGN KEY("User_ID") REFERENCES "Finances"("User_ID");
ALTER TABLE
    "User" ADD CONSTRAINT "user_user_id_foreign" FOREIGN KEY("User_ID") REFERENCES "Team_Members"("User_ID");
ALTER TABLE
    "Team" ADD CONSTRAINT "team_user_id_foreign" FOREIGN KEY("User_ID") REFERENCES "User"("User_ID");
ALTER TABLE
    "Finances" ADD CONSTRAINT "finances_responsible_officer_foreign" FOREIGN KEY("Responsible_Officer") REFERENCES "Team_Members"("User_ID");







ALTER TABLE
    "Blog_Tags" ADD CONSTRAINT "blog_tags_post_id_primary" PRIMARY KEY("Post_ID");
ALTER TABLE
    "Blog_Tags" ADD CONSTRAINT "blog_tags_tag_id_primary" PRIMARY KEY("Tag_ID");
ALTER TABLE
    "Event_Teams" ADD CONSTRAINT "event_teams_event_id_foreign" FOREIGN KEY("Event_ID") REFERENCES "Event"("Event_ID");
ALTER TABLE
    "Orders" ADD CONSTRAINT "orders_order_id_foreign" FOREIGN KEY("Order_ID") REFERENCES "Order_Details"("Order_ID");
ALTER TABLE
    "User" ADD CONSTRAINT "user_user_id_foreign" FOREIGN KEY("User_ID") REFERENCES "Blog"("User_ID");
ALTER TABLE
    "Product" ADD CONSTRAINT "product_product_id_foreign" FOREIGN KEY("Product_ID") REFERENCES "Order_Details"("Product_ID");
ALTER TABLE
    "Team" ADD CONSTRAINT "team_team_lead_foreign" FOREIGN KEY("Team_Lead") REFERENCES "User"("User_ID");
ALTER TABLE
    "Blog" ADD CONSTRAINT "blog_post_id_foreign" FOREIGN KEY("Post_ID") REFERENCES "Blog_Content"("Post_ID");
ALTER TABLE
    "Event_Teams" ADD CONSTRAINT "event_teams_team_id_foreign" FOREIGN KEY("Team_ID") REFERENCES "Team"("Team_ID");
ALTER TABLE
    "Responsibility" ADD CONSTRAINT "responsibility_item_id_foreign" FOREIGN KEY("Item_ID") REFERENCES "Club_Items"("Item_ID");
ALTER TABLE
    "Blog_Tags" ADD CONSTRAINT "blog_tags_tag_id_foreign" FOREIGN KEY("Tag_ID") REFERENCES "Tags"("Tag_ID");
ALTER TABLE
    "User" ADD CONSTRAINT "user_user_id_foreign" FOREIGN KEY("User_ID") REFERENCES "Event"("Event_Lead");
ALTER TABLE
    "User" ADD CONSTRAINT "user_user_id_foreign" FOREIGN KEY("User_ID") REFERENCES "Responsibility"("Person_Responsible");
ALTER TABLE
    "Event" ADD CONSTRAINT "event_location_foreign" FOREIGN KEY("Location") REFERENCES "Locations"("Location_ID");
ALTER TABLE
    "Blog" ADD CONSTRAINT "blog_post_id_foreign" FOREIGN KEY("Post_ID") REFERENCES "Blog_Tags"("Post_ID");
ALTER TABLE
    "User" ADD CONSTRAINT "user_user_id_foreign" FOREIGN KEY("User_ID") REFERENCES "Event_Participation"("Attendee");
ALTER TABLE
    "User" ADD CONSTRAINT "user_user_id_foreign" FOREIGN KEY("User_ID") REFERENCES "Orders"("Customer_ID");
ALTER TABLE
    "Event_Participation" ADD CONSTRAINT "event_participation_event_id_foreign" FOREIGN KEY("Event_ID") REFERENCES "Event"("Event_ID");
