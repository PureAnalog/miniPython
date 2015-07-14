import media
import fresh_tomatoes


toy_story = media.Movie("Toy Story",
                        "A story of a boy and his torys that",
                        "http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

wit = media.Movie("Wit",
                        "Professor Vivian Bearing (Emma Thompson), an expert on the work of 17th-century British poet John Donne, has spent her adult life contemplating religion and death as literary motifs. Diagnosed with advanced ovarian cancer, she consents to an aggressive andexperimental form of chemotherapy administered by Dr. Kelekian (Christopher Lloyd) and his assistant, Dr. Posner (Jonathan M. Woodward), her former student. Facing death on a personal level, she reflects on her life and work.",
                        "http://1.bp.blogspot.com/-8xWlW2_VUGo/TndWPI0qojI/AAAAAAAAAXk/ARO_XqoxIIo/s1600/Wit+cover.png",
                        "https://www.youtube.com/watch?v=u0PPvYlGqL8")

#toy_story.show_trailer()

movies = [toy_story, wit]

#fresh_tomatoes.open_movies_page(movies)

#print( media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)

