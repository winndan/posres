# app.py

from fasthtml.common import *
from monsterui.all import *
from data.categories import categories
from data.menu_items import menu_items

# Using the "slate" theme with Highlight.js enabled
hdrs = Theme.slate.headers(highlightjs=True)
app, rt = fast_app(hdrs=hdrs, live=True)

@rt("/")
def test():
    return Html(
        Head(
            Meta(charset='UTF-8'),
            Meta(name='viewport', content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no'),
            Title('Food Ordering App'),
            Link(rel='stylesheet', href='styles/menu.css')
        ),
        Body(
            Header(
                H1('Quick Bites'),
                P('Fast & Delicious')
            ),
            Div(
                Div(
                    Div(
                        *[Div(
                            Div(
                                Img(src=cat["icon"], alt=f'{cat["name"]} icon', cls='category-icon'),
                                Span(cat["name"], cls='category-name'),
                                data_category=cat["data_category"],
                                cls=cat["cls"]
                            )
                        ) for cat in categories],  # Fixed the closing brackets here
                        cls='categories'
                    ),
                    cls='categories-container'
                ),
                *[Div(
                    Div(
                        H2(cat_name.capitalize(), cls='category-title'),
                        Div(
                            *[Div(
                                Img(src=item["image"], alt=item["name"], cls='menu-image'),
                                Div(
                                    H3(item["name"], cls='menu-name'),
                                    P(item["description"], cls='menu-description'),
                                    P(item["price"], cls='menu-price'),
                                    Button('Add', cls='add-to-cart'),
                                    cls='menu-info'
                                ),
                                cls='menu-item'
                            ) for item in items],
                            cls='menu-items'
                        ),
                        cls='menu-section'
                    ),
                    id=cat_name,
                    cls='food-category' + (' active' if cat_name == 'all' else '')
                ) for cat_name, items in menu_items.items()],
                cls='container'
            ),
            Script(src='styles/menu.js')
        ),
        lang='en'
    )

if __name__ == "__main__":
    serve()