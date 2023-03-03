Working through another flask login project to see if this can help me understand what went wrong in my previous repo. 
Will see what we can learn from this one.
https://www.freecodecamp.org/news/how-to-authenticate-users-in-flask/

The article writer's github repo is:
https://github.com/ondiekelijah/User-Authentication-in-Flask

Completed items:
1. Create better User model for db that would include a number of different features for a user.
2. Created database_baseline.db with a default user and password. 

Current TODO list:

3. Create an Admin panel that will allow admins to administrate users. (On deck after item 6)
    - Create user link need removed from sign in page and moved here.
4. Improve default page with name of application.
5. Do some UX work to make this look more unique for a login page.
6. Create a user page. This will be a landing page for a logged in user. (in progress)
    - Have created a page on login that has a link to logout or go to admin page. 
    - Need to cleanup the register user page.

7. Implement logging for this. 
    - Make sure log rotation is a thing.
    - Make sure implementation is secure and not logging details we should not.


Spikes TODO list:
1. Lets figure out if flask logging is built in. (RESEARCH)
2. Lets figure out logging for non-flask code. (RESEARCH)
