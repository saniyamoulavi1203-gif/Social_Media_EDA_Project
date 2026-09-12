-- Social Media Engagement Analysis: Social Media Engagement Analysis

-- 1. Count total posts
SELECT COUNT(*) AS total_posts
FROM social_media_engagement;


-- 2. Average likes per post
SELECT AVG(Likes) AS average_likes
FROM social_media_engagement;


-- 3. Top 10 most engaged posts
SELECT
    Post_ID,
    Platform,
    Content_Type,
    Likes,
    Comments,
    Shares,
    Saves,
    (Likes + Comments + Shares + Saves) AS Total_Engagement
FROM social_media_engagement
ORDER BY Total_Engagement DESC
LIMIT 10;


-- 4. Engagement by platform
SELECT
    Platform,
    COUNT(*) AS total_posts,
    AVG(Likes + Comments + Shares + Saves)
        AS average_engagement
FROM social_media_engagement
GROUP BY Platform
ORDER BY average_engagement DESC;


-- 5. Monthly posting trend
SELECT
    DATE_FORMAT(Timestamp, '%Y-%m') AS month,
    COUNT(*) AS total_posts
FROM social_media_engagement
GROUP BY DATE_FORMAT(Timestamp, '%Y-%m')
ORDER BY month;


-- 6. Average comments
SELECT AVG(Comments) AS average_comments
FROM social_media_engagement;


-- 7. Posts with highest views
SELECT
    Post_ID,
    Platform,
    Content_Type,
    Views
FROM social_media_engagement
ORDER BY Views DESC
LIMIT 10;


-- 8. Rank posts based on engagement
SELECT
    Post_ID,
    Platform,
    (Likes + Comments + Shares + Saves) AS Total_Engagement,
    RANK() OVER (
        ORDER BY (Likes + Comments + Shares + Saves) DESC
    ) AS Engagement_Rank
FROM social_media_engagement;


-- 9. Hashtag usage
SELECT
    Hashtag_Count,
    COUNT(*) AS total_posts,
    AVG(Likes + Comments + Shares + Saves)
        AS average_engagement
FROM social_media_engagement
GROUP BY Hashtag_Count
ORDER BY Hashtag_Count;


-- 10. Engagement rate
SELECT
    Post_ID,
    Platform,
    Engagement_Rate
FROM social_media_engagement
ORDER BY Engagement_Rate DESC;
