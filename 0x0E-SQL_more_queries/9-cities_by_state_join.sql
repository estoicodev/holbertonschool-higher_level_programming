-- lists all cities contained in the database hbtn_0d_usa.
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
SELECT c.id, c.name, s.name FROM `cities` AS c, `states` AS s WHERE c.state_id = s.id;