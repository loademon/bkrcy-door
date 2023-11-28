from app import render_template, get_flashed_messages, Markup
from db import rd


def create_flash_messages():
    flash_messages_html = render_template("flash.html")
    flash_messages_html += "".join(
        [
            f'<div class="alert">{message}<span class="closebtn" onclick="closeFlashMessage(event)">&times;</span></div>'
            for message in get_flashed_messages()
        ]
    )
    return flash_messages_html


def create_page(search: list[str], type: str = "door_access") -> Markup:
    page = ""
    for item in search:
        if type == "user":
            text = f"{rd.hget(item, 'school_number')} : {rd.hget(item, 'name')}"
        if type == "door_access":
            text = item
        page += (
            f'<div class="checkbox-container">'
            f'<label for="{item}">'
            f'<input type="checkbox" name="{type}" value="{item}">{text}'
            f"</label>"
            f"</div>\n"
        )
    flash = create_flash_messages()
    return flash , Markup(page)
