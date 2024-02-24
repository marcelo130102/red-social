-- SQLite
INSERT INTO post (content, user_id, post_img, date_posted)
VALUES ("Ut neque massa, ultrices nec faucibus quis, dapibus non leo. Suspendisse sed neque eget elit laoreet interdum nec non arcu. Phasellus tempus mi libero, ac vulputate massa consequat at. Quisque orci ipsum, luctus id semper eget, venenatis ac dolor.", 2, "https://cdn.domestika.org/c_fill,dpr_auto,f_auto,q_auto/v1680866854/content-items/013/518/425/image-73-5-original.jpeg?1680866854", "2023-02-15"), 
("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer velit orci, consectetur vel tellus ac, auctor pulvinar mauris. Curabitur et diam ac velit malesuada euismod.", 1, "https://i.blogs.es/0ca9a6/aa/1366_2000.jpeg", "2024-01-10"), 
("Etiam fermentum tortor tortor, quis auctor nisi fringilla et. Quisque sit amet lorem quis velit viverra auctor vel a nunc. Aenean ut imperdiet augue. Aenean quis nibh sed tortor dapibus auctor.", 1, "https://media.es.wired.com/photos/6501e7429fa9000811a95fe8/16:9/w_1920,c_limit/Adobe%20Firefly.jpeg", "2024-02-20");


DROP TABLE IF EXISTS post;

CREATE TABLE post (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT,
    user_id INTEGER,
    post_img TEXT,
    FOREIGN KEY (user_id) REFERENCES user(id)
);