import db
import article
import category
import author

def show_menu():
    menu = """
    What would you like to do?
    1. Create new articles
    2. Modify existing articles
    3. Deactivate articles
    4. Get the list of all articles
    5. Get article details
    6. Get articles from a category
    7. Get active/published articles
    8. Get articles from an author
    9. Create a new author
    10. Modify existing author's information
    11. Get author's details
    12. Create a new category
    13. Modify existing category's information
    14. Get a list of categories
    0. Exit
    """
    print(menu.strip())


while True:
    show_menu()
    option = input("please select an option")

    if option == "1":
        print(" 1. Create new articles please, follow the intructions below: ")
        tittle = input("Please insert the tittle") 
        content = input("Please insert the content")
        author = input("Please insert the author_id")
        category = input("Please insert the category_id")
        article.create(tittle,content,author,category)

    elif option == "2":
        print(" 2. Modify existing articles, please follow the intructions below: ")
        id = input("Please insert the id to modify")
        tittle = input("Please insert the tittle") 
        content = input("Please insert the content")
        author = input("Please insert the author_id")
        category = input("Please insert the category_id")
        article.update(id,tittle,content,author,category)

    elif option == "3":
        id = input(" 3. Deactivate articles, please select the id to deactivate: ")
        article.deactivate(id)

    elif option == "4":
        print(" 4. Get the list of all articles, please follow the intructions below: ") 
        article.get()

    elif option == "5":
        cat= input(" 5. Get article details, please select the category: ")  
        article.et_by_category(cat)
    

    #elif option == "6":
     #   category = input(" 6. Get articles from a category, please select the category: ") 
      #  article.get_article_detail(category)
    
    elif option == "7":
        print(" 7. Get active/published articles, the active articles are shown below")  
        article.get_active()

    elif option == "8":
        autor = input(" 8. Get articles from an author, please select the author to get info ")
        article.get_by_autho(autor)

    elif option == "9":
        print(" 9. Create a new author, please follow the intructions below: ")
        firt_name = input("Please insert the first_name")
        last_name = input("Please insert the last_name") 
        email = input("Please insert the email")
        password = input("Please insert the password")
        author.create(firt_name,last_name,email,password)

    elif option == "10":
        print(" 10. Modify existing author's information, please follow the intructions below: ")
        id = input("Please insert the id to modify")
        first_name = input("Please insert the first name") 
        last_name = input("Please insert the last name")
        email = input("Please insert the email")
        password =input("Please insert the password")
        author.update(id,firt_name,last_name,email,password)


    elif option == "11":
        author_id = input(" 11. Get author's details, please select the author_id: ")
        author.get(author_id)

    elif option == "12":
        print(" 12. Create a new category, please follow the intructions below: ")
        name = input("Please insert the name of category")
        description = input("Please insert the description") 
        category.create(name,description)

    elif option == "13":
        print(" 13. Modify existing category's information, please follow the intructions below: ")
        category_id = input("Please select the category_id to modify") 
        name = input("Please insert the new name of category")
        description = input("Please insert the new description")
        category.update(category_id,name,description)

    elif option == "14":
        print(" 4. Get a list of categories, please follow the intructions below: ") 
        category.get()

    elif option == "0":
        print("See you later!")
        break
    else:
        print("Invalid option. Please choose a valid option.")