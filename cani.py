#created by:    @Bready

import random
import webbrowser as wb
import time

web = ["https://ichef.bbci.co.uk/news/976/cpsprodpb/17638/production/_124800859_gettyimages-817514614.jpg", "https://www.collinsdictionary.com/images/full/dog_230497594.jpg", "https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/02/322868_1100-1100x628.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbVVkh5k6-uk44b8RYD6hV-zxUxZgluOHw1A&usqp=CAU"]

def opn():
    selected = random.choice(web)
    wb.open_new_tab(url=selected)
    time.sleep(5)

while True:
    opn()