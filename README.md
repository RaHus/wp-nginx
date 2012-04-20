wp-nginx
========

nginx conf for wordpress without common pitfalls and with support for:

1. wp-supercache
2. cookies for comments
3. direct wp upload files serving (with help from script)

Normally WP serves uploaded media/files through php.
These files get saves into wp-content/blogs.dir/<blogid> so nginx cannot know
which blogid you are asking files from. 
The nginx-files script, creates inside wp-content/blogs.dir/direct symlinks
that map the id to the blog/host name, in this way we use directly the hostname to 
serve the files.

So a line like :

try_files $uri $uri/ /wp-content/blogs.dir/direct/$http_host/$uri /index.php; 

will try to serve the files directly. if not possible will pass the request to the backend (apache,phpfpm)


*The script must be run every time the mapping of hostname --> id changes (rare), or when
a new blog is created. typically i put it to run every sunday or every day at night.
