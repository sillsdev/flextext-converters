def make_flextext_tagline(tag_name, modifiers_dict):
    modifiers = ""
    if modifiers_dict is not None:
        for mod_key in modifiers_dict.keys():
            mod_string = f'{mod_key}="{modifiers_dict[mod_key]}"'
            modifiers += f" {mod_string}"

    tagline = f"<{tag_name}{modifiers}>"
    return tagline


def make_ft_line(marker, toolbox_content):
    pass


def make_ge_line(marker, toolbox_content):
    pass


def make_tx_line(marker, toolbox_content):
    modifiers = {"type": "txt"}
    if marker.keys().__contains__("lng"):
        modifiers["lang"] = marker["lng"]

    return (
        f"{make_flextext_tagline('item', modifiers)}"
        f"{toolbox_content}"
        f"{make_flextext_tagline('/item', None)}"
    )
