from bs4 import BeautifulSoup
#requests is like a person asking for info from their computer
import requests, csv
#this is a url from searching for the next set of all books sorted by popularity: https://www.gutenberg.org/ebooks/search/?query=&submit_search=Go%21&start_index=5000
#An example of a ebook link: /ebooks/18184
#75744 books total
#this converts everything on the html of this url into text i also made the mistake of trying to use title as an index number but title has a string value so thats why it doesnt work
def Gutenburg(): 
    bookUrl = []
    bookTitle = []
    bookAuthor = []
    count = 0
    for page in range(1, 21):
        url = requests.get(f'https://www.gutenberg.org/ebooks/{page}').text
        soup = BeautifulSoup(url, 'lxml')
        bookUrl.append(f'https://www.gutenberg.org/ebooks/{page}')
        bookTitle.append(soup.find("h1").text.split('by ')[0])
        try:
            bookAuthor.append(soup.find("h1").text.split('by')[1])
        except:
            bookAuthor.append("No author found")
        #print(bookTitle[count])
        #print(bookUrl[count])
        #print(bookAuthor[count]+'\n\n')
        count += 1

    fileOfBooks = open("BooksFromGutenberg.csv", "w", newline='', encoding='utf-8')
    writer = csv.writer(fileOfBooks)
    writer.writerow(["Title", "Author", "Link"])
    for i in range(len(bookAuthor)):
        writer.writerow([bookTitle[i], bookAuthor[i], bookUrl[i]])
    fileOfBooks.close()
    return bookAuthor, bookUrl, bookTitle
    print("All done!")
        

