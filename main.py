from fasthtml.common import *
from monsterui.all import *
import random
from menu_data import categories, items  # Importing menu data from external file

# Using the "slate" theme with Highlight.js enabled
hdrs = Theme.slate.headers(
    highlightjs=True,
    extra_css=["https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css"],
    extra_js=["https://cdnjs.cloudflare.com/ajax/libs/alpinejs/3.10.5/cdn.min.js"]
)
app, rt = fast_app(hdrs=hdrs, live=True)

################################
### Example Data and Content ###
################################
def ex_sliders_2(): 
    def _card(i): return Card(H3(f'Card {i}'), P(f'Card {i} content'))
    return Div(Slider(*[_card(i) for i in range(10)], cls="w-full max-w-lg mx-auto"))  # ✅ Ensure FastHTML integration

def display_menu():
    menu_section = Div(cls="p-4 bg-gray-100 rounded-lg")
    for category, item_list in categories.items():
        category_title = H2(category, cls="text-2xl font-bold mt-4 text-blue-600")
        items_list = Div(cls="space-y-2")
        for item in item_list:
            details = items.get(item, {})
            price = details.get("price", "N/A")
            size = details.get("size", "N/A")
            item_display = P(f"{item}: ${price} ({size})", cls="text-lg text-gray-700")
            items_list.append(item_display)
        menu_section.append(category_title, items_list)
    return menu_section

@rt("/")
def index():
    return Page(
        H1("Welcome to the Menu", cls="text-3xl font-bold text-center text-gray-800"),
        Div(display_menu(), cls="max-w-2xl mx-auto p-6 bg-white shadow-lg rounded-lg"),
        ex_sliders_2()
    )

if __name__ == "__main__":
    app.run()
