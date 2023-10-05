import re

# Change this boi.
NOTES = "e0e1e3a0a2a3a5d2d3d5d7d9d10d12g9g10g12g14g16g17g19g17g16g14d17d15d14d12d10d9d7a10a8a7a5a3a2a0e3e1e0"

STRING_MAP = {"e": 3, "a": 2, "d": 1, "g": 0}


def generate_tabs(notes: str) -> list[str]:
    """
    Genrates tabs given data.

    Form of data is:
        e1e3a1a3d1d3g1g3g2g4d2d4a2a4e2e4
    """
    notes_split = [note.strip() for note in re.findall(r"[eadg]\d+", notes)]
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


html = generate_tabs(notes=NOTES)
for i in html:
    print(i)
