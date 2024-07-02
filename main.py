


import pandas as pd
from recommender import get_recommendations
from styling import color_genre
from tabulate import tabulate
from colorama import Fore, Style, Back






def main():
    try:
        movie_data = pd.read_csv('filmtv_movies.csv')
    except FileNotFoundError:
        print(Fore.RED + "File not found." + Style.RESET_ALL)
        return
    


    while True:
        try:
            movie_title = input(Back.LIGHTWHITE_EX + "\n Enter a movie title (or type 'exit' to quit): " + Style.RESET_ALL + "\t")
            if movie_title.lower() == 'exit':
                print(Back.CYAN + "Thanks 🙏" + Style.RESET_ALL)
                break



            filtered_movies = movie_data[movie_data['title'].str.contains(movie_title, case= False, na= False)]


            if filtered_movies.empty:
                print("⚠️ No movies found with that title ⚠️" + Style.RESET_ALL)
                continue



            if len(filtered_movies) > 1:
                while True:
                    print(Fore.LIGHTGREEN_EX + "\n Multiple movies found with that title. Please choose one: \n" + Style.RESET_ALL)
                    # for index, row in filtered_movies.iterrows():
                    #     print(f"{index}: Title: {row['title']},\t Genre: {row['genre']},\t Country: {row['country']},\t Released in: {row['year']}")

                    # movie_list = filtered_movies[['title', 'genre', 'country', 'year']]
                    # movie_list.insert(0, 'index', filtered_movies.index, allow_duplicates= False)
                    # print(tabulate(movie_list, headers="keys", tablefmt="grid", showindex= False))

                    #print(tabulate(movie_list, headers=["index", "title", "genre", "country", "year"], tablefmt="grid"))


                    filtered_movies = filtered_movies.sort_values(by= 'year', ascending= False)
                    movie_list = filtered_movies[['title', 'genre', 'country', 'year']]
                    # New col with idx
                    movie_list.insert(0, 'index', filtered_movies.index, allow_duplicates= False)
                    # Coloring
                    #movie_list['genre'] = movie_list['genre'].apply(color_genre)
                    movie_list.loc[:, 'genre'] = movie_list['genre'].apply(color_genre)

                    print(tabulate(movie_list, headers=["index", "title", "genre", "country", "year"], tablefmt= "grid", showindex= False))

                    choice = input(Back.LIGHTWHITE_EX + "\n Enter the index of the movie you are interested in: " + Style.RESET_ALL + "\t")

                    if not choice.isdigit() or int(choice) not in filtered_movies.index:
                        print(Back.RED + "\n Invalid choice" + Style.RESET_ALL)
                        continue

                    chosen_movie = filtered_movies.loc[int(choice)]
                    break


            else:
                chosen_movie = filtered_movies.iloc[0]

            print(Fore.LIGHTGREEN_EX + f"\n Selected Movie: {chosen_movie['title']},\t Genre: {chosen_movie['genre']},\t Country: {chosen_movie['country']},\t Released in: {chosen_movie['year']}" + Style.RESET_ALL)




            if pd.isna(chosen_movie['description']):
                print(Fore.RED + "\n The selected movie does not have a description available for recommendation." + Style.RESET_ALL)
                continue



        #     recommendations = get_recommendations(chosen_movie, movie_data)
        #     if recommendations:
        #         # print("Recommendations:")
        #         # for rec in recommendations:
        #         #     print(f"Title: {rec['title']},\t Genre: {rec['genre']},\t Country: {rec['country']},\t Released in: {rec['year']}")
        #         print("Recommendations:")
        #         print(tabulate(recommendations, headers="keys", tablefmt="rounded_grid"))
        #     else:
        #         print("No recommendations found.")
        # except Exception as e:
        #     print(f"An error occurred: {e}")

            recommendations = get_recommendations(chosen_movie, movie_data)
            if recommendations:
                print(Style.BRIGHT + "\n\n\n Recommendations:" + Style.RESET_ALL)

                # Apply color to genre cells in recommendations
                for rec in recommendations:
                    rec['genre'] = color_genre(rec['genre'])

                # Convert recommendations to a DataFrame for tabulate
                rec_df = pd.DataFrame(recommendations)
                rec_df.sort_values(by='year', ascending= False, inplace= True)
                
                # Print the recommendations in a table format
                print(tabulate(rec_df, headers=["title", "genre", "country", "year"], tablefmt="rounded_grid", showindex= False))

            else:
                print(Fore.CYAN + "No recommendations found 🥲" + Style.RESET_ALL)




            # Keep or stop
            user_choice = input(Back.LIGHTWHITE_EX + "\n Do you want to search for another movie? (yes to continue, no to quit): " + Style.RESET_ALL + "\t")
            print()

            if user_choice.lower() != 'yes':
                print(Back.CYAN + "Thanks 🙏" + Style.RESET_ALL)
                break


        except ValueError:
            print(Back.RED + "Invalid input. Please enter a valid index." + Style.RESET_ALL)
        except IndexError:
            print(Back.RED + "Index out of range. Please select a valid index." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)



if __name__ == '__main__':
    main()