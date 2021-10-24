def print_book_info(title, author=None, year=None):
    total_str = '"' + title + '"'
    if author is not None or year is not None:
        total_str += ' was written'
    if author is not None:
        total_str += ' by ' + author
    if year is not None:
        total_str += ' in ' + year
    print(total_str)

    # ---- other variant I
    # written_info = " was written" if author or year else ""
    # info_author = f" by {author}" if author else ""
    # year_info = f" in {year}" if year else ""
    # print(f'"{title}"{written_info}{info_author}{year_info}')

    # ---- other variant II
    # written = " was written" * bool(author or year)
    # by_author = f" by {author}" * bool(author)
    # in_year = f" in {year}" * bool(year)
    # print(f'"{title}"{written}{by_author}{in_year}')

# print_book_info("Huut")
