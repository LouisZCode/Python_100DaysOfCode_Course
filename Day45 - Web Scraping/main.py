from bs4 import BeautifulSoup
#sometimes you need to use the lxml parser
import lxml  #different parsing of the webpage.


#lets first open the contents of the html file:
with open("Day45 - Web Scraping\website.html") as website:
    content = website.read()
    #now that we have the contents, we can use beautiful soup!

#if we tap into the object with a parser (Obj=HTML)
# we can work with that object as if it was a python one!
soup = BeautifulSoup(content, "html.parser")

#lets try...
print(soup.title)

#or
print(soup.title.name)

#or...!
print(soup.title.string)



#what if we want to find all the X things? for example all the anchor tags:
anchor_tags = soup.find_all(name="a")

#we get hold of ALL anchor tags
print(anchor_tags)
#[<a href="https://www.appbrewery.co/">The App Brewery</a>,
# <a href="https://angelabauer.github.io/cv/hobbies.html">My Hobbies</a>,
# <a href="https://angelabauer.github.io/cv/contact-me.html">Contact Me</a>]


#or only the text?
for tag in anchor_tags:
    print(tag.get_text())
#The App Brewery
#My Hobbies
#Contact Me

#what if we want the link?
for tag in anchor_tags:
    print(tag.get('href'))
#this gives me all of the link in the href!

#we can also get things by the attribute name, by id.
heading = soup.find(name="h1", id="name")   #it will search the element with name AND id
print(heading)
#we get:   <h1 id="name">Angela Yu</h1>

#same with class attribute
section_heading = soup.find(name="h3", class_='heading') #this is a special Class word, only for creating classes
print(section_heading)
#we get    <h3 class="heading">Books and Teaching</h3>     and we can use   .name   


#NOTE sometimes this do not work... so we can narrow hierarchy or steps

company_url = soup.select_one(selector='p a') #the first matching item    we add the 'selector' as a string
#company_url_v2 = soup.select() #all amtching items
print(company_url)