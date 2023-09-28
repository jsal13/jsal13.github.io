# Change this boi.
notes = "e1,e3,a1,a3,d1,d3,g1,g3,g2,g4,d2,d4,a2,a4,e2,e4,e3,e5,a3,a5,d3,d5,g3,g5,g4,g6,d4,d6,a4,a6,e4,e6"

STRING_MAP = {"e": 3, "a": 2, "d": 1, "g": 0}


def generate_tabs(notes: str) -> list[str]:
    """
    Genrates tabs given data.

    Form of data is:
        e1,e3,a1,a3,d1,d3,g1,g3,g2,g4,d2,d4,a2,a4,e2,e4
    """
    notes_split = [note.strip() for note in notes.split(",")]
    tabs = [["-"] * (2 * len(notes_split)) for _ in range(4)]

    for idx, note in enumerate(notes_split):
        string_idx = STRING_MAP[note[0]]
        value = note[1:]
        tabs[string_idx][2 * idx] = value

    chunk_val = 16
    tabs_chunked = [
        [
            tabs[string][idx : idx + chunk_val]
            for idx in range(0, len(tabs[0]), chunk_val)
        ]
        for string in range(4)
    ]

    num_chunks = len(tabs_chunked[0])

    tabs_joined = []
    for chunk_idx in range(num_chunks):
        chunk_phrase = []
        for string_idx in range(4):
            chunk_phrase.append("".join(tabs_chunked[string_idx][chunk_idx]))
        tabs_joined.append(chunk_phrase)

    stacked_html = ["<div class='d-flex flex-wrap'>"]
    for measure in range(num_chunks):
        stacked_html.append(
            f"""
            <pre>
            {tabs_joined[measure][0]}
            {tabs_joined[measure][1]}
            {tabs_joined[measure][2]}
            {tabs_joined[measure][3]}
            </pre>
            """.replace(
                " ", ""
            ).strip()
        )
    stacked_html.append("</div>")

    return stacked_html


html = generate_tabs(notes=notes)
for i in html:
    print(i)
