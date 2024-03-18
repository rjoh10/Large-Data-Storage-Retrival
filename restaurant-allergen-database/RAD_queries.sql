-- Rhea Johnson and Richa Juvekar
-- RAD Sample Queries
-- Retrieve all restaurants.
SELECT * FROM Restaurants;

-- Retrieve restaurants with that practice cross contamination prevention.
SELECT RestaurantName
FROM Restaurants
WHERE CrossContaminationPrevention = TRUE;

-- Retrieve all users and their allergies
SELECT u.UserName, a.AllergenName
FROM UserProfile u
JOIN UserAllergens ua ON u.UserID = ua.UserID
JOIN Allergens a ON ua.AllergenID = a.AllergenID;

-- Retrieve all users who posted a community forum post reviewing a restaurant
-- during August 2022
SELECT CommentID, UserName, RestaurantName, Comment, Datetime
FROM CommunityForumPost c
JOIN UserProfile u ON c.UserID = u.UserID
JOIN Restaurants r ON c.RestaurantID = r.RestaurantID
WHERE MONTH(c.Datetime) = 8 AND YEAR(c.Datetime) = 2022;

-- Retrieve all restaurants that accommodate for tree nuts allergies
SELECT RestaurantName
FROM Restaurants r
JOIN RestaurantAllergenAccomodation ra ON r.RestaurantID = ra.RestaurantID
JOIN Allergens a ON ra.AllergenID = a.AllergenID
WHERE a.AllergenName = 'Tree Nuts';