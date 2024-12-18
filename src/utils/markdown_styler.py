class MarkdownStyler:
    def __init__(self):
        pass

    def bold(self, text):
        return f"**{text}**"
    
    def italic(self, text):
        return f"*{text}*"
    
    def underline(self, text):
        return f"__{text}__"
    
    def strikethrough(self, text):
        return f"~~{text}~~"
    
    def link(self, text, url):
        return f"[{text}]({url})"
    
    def image(self, url, alt_text):
        return f"![{alt_text}]({url})"
    
    def hr(self):
        return "\n---\n\n"
    
    def ordered_list(self, items):
        return "\n".join(f"{i+1}. {item}" for i, item in enumerate(items))
    
    def unordered_list(self, items):
        return "\n".join(f"- {item}" for item in items)
    
    def heading(self, text, level):
        return f"{'#' * level} {text}\n\n"
    
    def paragraph(self, text):
        return f"{text}\n"
    
    def blockquote(self, text):
        return f"> {text}\n"
    
    def inline_code(self, text):
        return f"`{text}`"
    
    def table(self, headers, rows):
        table = "| " + " | ".join(headers) + " |\n"
        table += "| " + " | ".join(["---"] * len(headers)) + " |\n"
        table += "\n".join("| " + " | ".join(row) + " |" for row in rows)
        table += "\n"
        return table
    
    def code_block(self, code):
        return f"```\n{code}\n```\n"
    
    def newline(self):
        return "\n"
    