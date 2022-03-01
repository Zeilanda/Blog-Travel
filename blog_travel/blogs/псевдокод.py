from typing import Optional


def insert_post() -> int:
    """вставляет в таблицу "post" новую строку и возвращает значение из колонки "id" новой строки`"""


def insert_tag(new_name: str) -> int:

    """вставляет в таблицу "tag" новую строку со значением колонки "name", равным значению аргумента new_name, и
возвращает значение из колонки "id" новой строки"""


def insert_post_tag(new_post_id: int, new_tag_id: int) -> None:

    """вставляет в таблицу "post_tag" новую строку со значением колонки "post_id", равным значению аргумента
    new_post_id, значением колонки "tag_id", равным значению аргумента new_tag_id, и ничего не возвращает"""


def select_tag(target_name: str) -> Optional[int]:
    """выбирает строку из таблицы "tag", где значение колонки "name" равно значению аргумента target_name.
    Возвращает значение из колонки "id" полученной строки, если она была получена, иначе None"""


new_post_tags = ["tc"]
new_tag_id = select_tag(''.join(new_post_tags))

insert_post_tag(insert_post(), new_tag_id)


# Добавление поста с одним несуществующим тегом

new_post_tags = ["td"]
new_tag_id = insert_tag(''.join(new_post_tags))
insert_post_tag(insert_post(), new_tag_id)

# Добавление поста с несколькими существующими тегами

new_post_tags = ["ta", 'tc']
post_id = insert_post()
tags_id = [select_tag(tag) for tag in new_post_tags]
for tag_id in tags_id:
    insert_post_tag(post_id, tag_id)

# Добавление поста с несколькими несуществующими тегами

new_post_tags = ["td", 'te']
post_id = insert_post()
tags_id = [insert_tag(tag) for tag in new_post_tags]
for tag_id in tags_id:
    insert_post_tag(post_id, tag_id)

# Добавление поста с 2 тегами, где 1 есть, а 2 нет

new_post_tags = ['tc', 'td']
post_id = insert_post()
new_tags_id = [insert_tag(new_tag) if new_tag not in Tag else select_tag(new_tag)for new_tag in new_post_tags]

new_tags_id = []
for new_tag in new_post_tags:
    if select_tag(new_tag) is None:
        new_tags_id.append(insert_tag(new_tag))
    else:
        new_tags_id.append(select_tag(new_tag))


a = [i for i in range(3)]
a = []
for i in range(3):
    a.append(i)


for new_tag_id in new_tags_id:
    insert_post_tag(post_id, new_tag_id)
