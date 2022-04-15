**Setup**

-   [x] github repo
-   [x] virtual environment
-   [x] django project

**Templates**

steph:

edit_game,
add_game,
add_loan,
game_loans (where all your loans are listed, with return date and return loan button)
return_game, (will list a form), only has datefield with return button?

add restricted access,

more specific bootstrap styling ?

-   opinion on styling :)

gabes:

index,
base,
games,
game_info,
edit_loan,
login,
logout,
register

**Models**

-   [ ] board game (like Book in bcb)
-   [ ] game loan

**Views**

-   [x] log in
-   [x] log out
-   [x] register

-   [x] board games (like books in cbc)
    -   listing all available games
-   [ ] board game (like book/reviews in cbc)
    -   listing loans etc
-   [ ] create game (like new_book in cbc)
    -   adding a new game
-   [x] edit game (like edit_review/edit_book in cbc)
    -   editing you own games
-   [ ] loan game
    -   loaning a game that is free
-   [ ] edit loan
    -   editing a made loan

**Forms**

-   [ ] Game form (like BookForm in cbc)
    -   name
    -   genre
    -   year
    -   (stars)
-   [ ] Loan form
    -   name of the loaner
    -   game
    -   date loaned
    -   date to return

The minimum requirement for an accepted teamwork is 12 points. To earn that it is expected that

-   [ ] the web site is implemented for an accepted subject, (required)
-   [ ] the implemented web site functions, (2 points)
-   [x] MVT architecture is obeyed, (2 points)
-   [x] there must be more than 1 model, (2 points)
-   [x] users [board gamers] can view a list of all [available board games] entities of one kind, (2 points)
-   [x] a user [a board gamer] can add an entity [a board game], (2 points)
-   [x] a user can do something for an entity [a board gamer can borrow a board game]. (2 points)
-   the web site and its source code are presented online to the instructor in agreed time (required)

    More points can be earned by fulfilling the following requests:

-   [x] a user [a board gamer] can edit instances to at least 2 models [(not only a board game)], (2 points)
-   [x] template inheritance is used, (2 points)
-   [x] user accounts have been set up (2 points)
