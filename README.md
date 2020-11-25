# Getting Started

1.  Clone this repo and navigate to the projects root directory 
2.  Run `docker-compose build`
3.  Run `docker-compose up`
4.  Check out the site at [http://localhost:5000/request](http://localhost:5000/request)

# Decisions

## Integration Tests

I chose to write this app in a test driven manner to both ensure the specs were met and to guide my coding processing.

## Database Choice

In thinking about what database to use I considered using either Mongo or Postgres. Given how very simple this data is and how much support there is for SQLAlchemy I chose Postgres.

## Docker Choice

I know Docker is slight overkill for such a simple project, but I knew the setup would only be slightly more labour intensive then a virtual environment and that benefit of having it easily deployable on another machine could be helpful for the developers who are going to assess this project.

## Regarding Email Validation

I did see that the project description asked I validate the email address of the requesting user and I found that slightly confusing as any user would have had already had their email address validated upon creating their account. The instructions also specified that this was a theoretical addition endpoint and not intended to be a full service. Thus I only included email validation on the user model and assumed all users had valid emails when making requests.

I could have made the app such that any email address could request a book, but that seemed like a very flawed API decision decision.

# TO DO (if time allowed)

There were a number of things I would have liked to done had I not already used the allotted 3 hours.

- Add more sophisticated email validation
- Add a create user endpoint
- Write tests such that they don't use the endpoints to do the data setup and cleanup

# My Steps

- Read instructions
- Create ERD
- Setup Docker
- Code Models
- Code tests and endpoints simultaneously
- Test and check requirements met
