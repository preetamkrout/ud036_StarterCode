import fresh_tomatoes
import media


def add_movies():
    '''This method adds all the movies to final list and generates the html'''
    # creating tiles for all dc movies
    watchmen = media.Movie(
        "Watchmen",
        "A vigilante sets out to investigate the murder of one of his colleagu"
        "es. In the process of doing so,he discovers some murky truths.",
        "https://upload.wikimedia.org/wikipedia/en/b/bc/Watchmen_film_poster.jpg",  # nopep8 # Url not be disected pylint: disable=line-too-long
        "https://www.youtube.com/watch?v=NUjMO_k9IF8")

    batman_begins = media.Movie(
        "Batman Begins",
        "After witnessing his parents' death, Bruce learns the art of fighting"
        " to confront injustice."
        " When he returns to Gotham as Batman,"
        " he must stop a secret society that intends to destroy the city.",
        "https://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg",  # nopep8 # Url not be disected pylint: disable=line-too-long
        "https://www.youtube.com/watch?v=vak9ZLfhGnQ")

    the_dark_knight = media.Movie(
        "The Dark Knight", "After Gordon, Dent and "
        "Batman begin an assault on Gotham's organised crime"
        ", the mobs hire the Joker, a psychopathic criminal mastermind,"
        " who wants to bring all the heroes down to his level.",
        "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
        "https://www.youtube.com/watch?v=yQ5U8suTUw0")

    the_dark_knight_rises = media.Movie(
        "The Dark Knight Rises",
        "Bane, an imposing terrorist, "
        "attacks Gotham City and disrupts its eight-year-long period of peace."
        " This forces Bruce Wayne to come out of hiding and "
        "don the cape and cowl of Batman again.",
        "https://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg",  # nopep8 # Url not be disected pylint: disable=line-too-long
        "https://www.youtube.com/watch?v=g8evyE9TuYk")

    green_lantern = media.Movie(
        "Green Lantern",
        "An arrogant test pilot, Hal Jordan, acquires superhuman powers, "
        "after being chosen by the Ring, "
        "which is the willpower-fed source of power of the "
        "Green Lantern Intergalactic Corps.",
        "https://upload.wikimedia.org/wikipedia/en/6/6b/Green_Lantern_poster.jpg",  # nopep8 # Url not be disected pylint: disable=line-too-long
        "https://www.youtube.com/watch?v=f8ZPg8uaoR0")

    man_of_steel = media.Movie(
        "Man of Steel",
        "When a young boy discovers that he has extraordinary powers, "
        "he decides to find out about his origin. He then learns to fight"
        " for Earth when it gets attacked by members of his own race.",
        "https://upload.wikimedia.org/wikipedia/en/8/85/ManofSteelFinalPoster.jpg",  # nopep8 # Url not be disected pylint: disable=line-too-long
        "https://www.youtube.com/watch?v=OAVuKPFKrNo")

    batman_vs_superman = media.Movie(
        "Batman v Superman: Dawn of Justice",
        "Fearing the actions of a god-like super hero left unchecked, "
        "Gotham City’s own formidable, "
        "forceful vigilante takes on Metropolis’s most revered, "
        "modern-day savior, while the world wrestles with "
        "what sort of hero it really needs. "
        "And with Batman and Superman at war with one another, "
        "a new threat quickly arises, "
        "putting mankind in greater danger than it’s ever known before.",
        "https://upload.wikimedia.org/wikipedia/en/2/20/Batman_v_Superman_poster.jpg",  # nopep8 # Url not be disected pylint: disable=line-too-long
        "https://www.youtube.com/watch?v=U652-BpXVQY")

    suicide_squad = media.Movie(
        "Suicide Squad",
        "An intelligence officer assembles a team of imprisoned super-villains"
        " to execute dangerous black ops missions."
        " Meanwhile, the homicidal Joker"
        " launches a diabolical agenda of his own.",
        "https://upload.wikimedia.org/wikipedia/en/5/50/Suicide_Squad_(film)_Poster.png",  # nopep8 # Url not be disected pylint: disable=line-too-long
        "https://www.youtube.com/watch?v=CmRih_VtVAs")

    wonder_woman = media.Movie(
        "Wonder Woman",
        "Before she was Wonder Woman (Gal Gadot), she was Diana,"
        " princess of the Amazons, trained to be an unconquerable warrior."
        " Raised on a sheltered island paradise, Diana meets an American pilot"
        " (Chris Pine) who tells her about the massive conflict"
        " that's raging in the outside world."
        " Convinced that she can stop the threat,"
        " Diana leaves her home for the first time."
        " Fighting alongside men in a war to end all wars,"
        " she finally discovers her full powers and true destiny.",
        "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_(2017_film).jpg",  # nopep8 # Url not be disected pylint: disable=line-too-long
        "https://www.youtube.com/watch?v=VSB4wGIdDwo")

    # create the movie list
    movies = [
        watchmen, batman_begins, the_dark_knight, the_dark_knight_rises,
        green_lantern, man_of_steel, batman_vs_superman, suicide_squad,
        wonder_woman
    ]

    # generate html using fresh_tomatoes module provided by Udacity team
    fresh_tomatoes.open_movies_page(movies)


add_movies()
