-- Rhea Johson and Richa Juvekar
-- RAD database setup file
DROP DATABASE IF EXISTS rad;
CREATE DATABASE IF NOT EXISTS rad;
USE rad;

-- Step 1: Create Tables
CREATE TABLE IF NOT EXISTS UserProfile (
    UserID INT PRIMARY KEY,
    UserName VARCHAR(25)
);

CREATE TABLE IF NOT EXISTS Allergens (
    AllergenID INT PRIMARY KEY,
    AllergenName VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS UserAllergens (
    UserID INT,
    AllergenID INT,
    PRIMARY KEY (UserID, AllergenID),
    FOREIGN KEY (UserID) REFERENCES UserProfile(UserID),
    FOREIGN KEY (AllergenID) REFERENCES Allergens(AllergenID)
);

CREATE TABLE IF NOT EXISTS Restaurants (
	RestaurantID INT PRIMARY KEY AUTO_INCREMENT,
    RestaurantName VARCHAR(255) NOT NULL,
    PhoneNumber VARCHAR(255),
	Street VARCHAR(100),
    City VARCHAR(100),
    State CHAR(2),
    CrossContaminationPrevention BOOLEAN DEFAULT NULL,
    SpecialDietaryAccommodation BOOLEAN DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS RestaurantAllergenAccomodation (
    RestaurantID INT,
    AllergenID INT,
    PRIMARY KEY (RestaurantID, AllergenID),
    FOREIGN KEY (RestaurantID) REFERENCES Restaurants(RestaurantID),
    FOREIGN KEY (AllergenID) REFERENCES Allergens(AllergenID)
);

CREATE TABLE IF NOT EXISTS CommunityForumPost (
    CommentID INT PRIMARY KEY AUTO_INCREMENT,
    UserID INT,
	RestaurantID INT,
	FOREIGN KEY (UserID) REFERENCES UserProfile(UserID),
	FOREIGN KEY (RestaurantID) REFERENCES Restaurants(RestaurantID),
    Comment VARCHAR(1000),
    Datetime DATETIME
);

-- Step 2: Insert Sample Data
INSERT INTO UserProfile (UserID, UserName) VALUES
(1, 'jcharlesw01'),
(2, 'jreagan6'),
(3, 'Kleeraden'),
(4, 'cheryldelo'),
(5, 'Supernova');

INSERT INTO Allergens (AllergenID, AllergenName) VALUES
(1, 'Gluten'),
(2, 'Dairy'),
(3, 'Tree Nuts'),
(4, 'Soy'),
(5, 'Shellfish'),
(6, 'Sesame'),
(7, 'Peanuts'),
(8, 'Eggs');

INSERT INTO UserAllergens (UserID, AllergenID) VALUES
(1,3),
(1,7),
(2,7),
(2,3),
(2,6),
(3,5),
(3,3),
(4,6),
(4,7),
(5,7),
(5,3),
(5,8),
(5,6);

INSERT INTO Restaurants (RestaurantID, RestaurantName, PhoneNumber, Street, City, State, CrossContaminationPrevention, SpecialDietaryAccommodation)
VALUES
(1, 'Tresca', '(617) 742-8240', '233 Hanover St', 'Boston', 'MA', TRUE, TRUE),
(2, 'Joes American Bar & Grill', '(617) 367-8700', '100 Atlantic Ave', 'Boston', 'MA', FALSE, TRUE),
(3, 'Jennifer Lees Gourmet Bakery', '(978) 675-5116', '100 Hanover St', 'Boston', 'MA', FALSE, TRUE),
(4, '110 Grill', '(781) 305-4355','373 Washington St', 'Woburn', 'MA', FALSE, TRUE);

INSERT INTO RestaurantAllergenAccomodation(RestaurantID, AllergenID) VALUES
(1,3),
(1,1),
(1,4),
(2,1),
(3,3),
(3,7),
(3,6),
(4,6),
(4,7),
(4,3);

INSERT INTO CommunityForumPost (CommentID, UserID, RestaurantID, Comment, Datetime) VALUES 
(1,1,1,'My daughter has a TN/PN allergy and ordered linguini and clams and ate the bread at the table. We stayed away from the desserts as a precaution since those tend to be trickier with nut cross contamination. But the waiter and staff seemed knowledgeable about food allergies.', '2022-08-18'),
(2,2,2,'I have a sesame allergy and was able to eat the burger roll which was pretty exciting (for me anyway) along with French fries. My daughter (PN/TN) was able to safely have the Mac & cheese with lobster. She also was able to have the chocolate cake but it’s not made in-house so dessert really depends on your own comfort level', '2022-11-19'),
(3,3,3,'Such a joyous visit here! My son couldn’t believe that every item there was safe for him to eat. Everything we got was delicious as well.', '2022-08-22'),
(4,4,4,'Very knowledgeable and my son was able to enjoy a meal without any issues including chicken tenders which are usually a no-go with sesame allergy', '2020-01-07'),
(5,5,4,'Oh boy. The 110 Grill in Worcester is excellent allergy-wise, but at this one, they served me the wrong kind of bun that had egg in it. They swore up and down that it was fine, but I could tell it was a gluten-free bun (which usually have egg) from seeing my celiac family members meal and insisted they check again. Without saying a word, the server came back and replaced my burger with a different one. I could MAYBE get over the mistake if they had handled it well, but they never said a WORD about it. No apology, no explanation, and somehow most insulting, they took a side off the bill that got sent back from a different party member for a different reason, but not mine. It was insanely unprofessional and I will never go back to the Woburn location unless they overhaul their allergen procedure.', "2021-06-01");
