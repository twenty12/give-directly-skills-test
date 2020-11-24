# Decisions

## Database Choice

In thinking about what database to use I considered using either Mongo or Postgres. Given how very simple this data is and how much support there is for SQLAlchemy I chose Postgres.

## Docker Choice

I know Docker is slight overkill for such a simple project, but I knew the setup would only be slightly more labour intensive then a virtual environment and that benefit of having it easily deployable on another machine could be helpful for the developers who are going to asses this project.


# To dos
    - add more sophisticated email validation 