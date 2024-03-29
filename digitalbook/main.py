# ブックシェルフ初期化
book_shelf=[]

#本の追加　関数
def add(title,read_status):
    book_id = len(book_shelf) + 1
    book={"id":book_id,"title":title,"read_status":read_status}
    book_shelf.append(book)
    print(f"Book name :'{title}' is added")

#本の編集　関数
def edit(book_id,new_title,new_readstatus):
    for book in book_shelf:
        if book["id"] == book_id:
            book["title"] = new_title
            book["read_status"] = new_readstatus
            return
    print("This book id is not registered")

#本の検索　関数
def search(keyword):
    search_books_group=[]
    for book in book_shelf:
        if keyword.lower() in book["title"].lower():
            search_books_group.append(book)
    
    if len(search_books_group) ==0 :
        print("Not found the book.Please try again with another word.")
    else:
        print("Search result:")
        for book in search_books_group:
            print(f"ID:{book['id']},Title:{book['title']},Read status:{'Yes' if book['read_status']=='1' else 'No'}")

#本の削除　関数
def delete(book_id):
    for i, book in enumerate(book_shelf):
        if book["id"] == book_id:
            del book_shelf[i]
            print(f"Delete the book which has the ID: {book['id']} and the title: {book['title']}.")
            return
    
    print("Not found the book id. Please make confirmation and try again.")

#ブックシェルフの統計情報の表示　関数
def stats():
    num_books = len(book_shelf)
    read_books_group=[]
    for book in book_shelf:
        if book['read_status']=="1":
            read_books_group.append(book)
    read_books = len(read_books_group)
    unread_books = num_books - read_books
    
    print(f"Number of all books: {num_books}")
    print(f"Number of read book: {read_books}")
    print(f"Number of unread book: {unread_books} ")
    
#メニューを表示する関数
def menu():
    print(
    "=================================================\n"+
    "Welcome to your personal books digital library!\n"+
    "=================================================\n"+
    "1: Add a Book\n"+
    "2: Edit a Book\n"+
    "3: Search for Books\n"+
    "4: Delete a Book\n"+
    "5: View Library Stats\n"+
    "6: Exit app"
    )

#ユーザーインプットに応じた処理を関数を使って行う
def user_input():
    while True:
        menu()
        user_choice =input("Please select from 1 to 6:")
        
        if user_choice == "1" :
            title = input("Please input book title:")
            read_status = input("Please input read status. Read:'1', Unread:'2':")
            add(title,read_status)
        elif user_choice == "2" :
            book_id = int(input("Please input book id:"))
            new_title = input("Please input new title for this book:")
            new_readstatus = input("Please input new read status for this book:")
            edit(book_id,new_title,new_readstatus)
        elif user_choice == "3" :
            keyword = input("Please input keyword of the book:")
            search(keyword)
        elif user_choice == "4" :
            book_id = int(input("Please input book id:"))
            delete(book_id)
        elif user_choice == "5" :
            stats()
        elif user_choice == "6" :
            print("Exit from this app")
            break
        else :
            print ("Invalid input. Please select from 1 to 6.")

user_input()
