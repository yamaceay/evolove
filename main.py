from selenium import webdriver
import json
from tqdm import tqdm
driver = webdriver.Chrome(executable_path="chromedriver.exe")

links = [f"http://www.projectevolove.com/forums/topic/{i}" for i in range(1, 520)]

list_data = []
for i in tqdm(range(len(links))):
    data = {}
    link = links[i]
    driver.get(link)
    texts = driver.find_elements_by_css_selector("li.forum_boxarea_body > div.advforum_boxarea_postcontent > p")
    texts = [text.get_attribute("innerText") for text in texts]
    labels = driver.find_elements_by_css_selector("#global_content > div.advforum_post_detail > div.advforum_post_header > div.advforum_post_header_left > span > a")
    labels = [label.get_attribute("innerText") for label in labels[1:]]
    labels = list(set(labels))
    forum = "NaN"
    if len(labels) > 0:
        forum = labels[-1]
    titles = driver.find_elements_by_css_selector("div.forum_topic_title > h3")
    if len(titles) > 0:
        title = titles[0].get_attribute("innerText")
        data.update({"id": i, "title": title, "texts": texts, "labels": labels, "forum": forum})
        list_data.append(data)

jsonified = json.dumps(list_data, indent=4)
with open("users.json", "w") as file:
    file.write(jsonified)