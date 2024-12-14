from utils import file_handler, markdown_styler
from leetcode.leetcode_service import LeetCodeService
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    cookie = os.getenv("LEETCODE_COOKIE")
    study_plan = LeetCodeService(cookie).get_study_plan("top-sql-50")
    study_plan = LeetCodeService(cookie).get_study_plan("top-sql-50")
    markdown = markdown_styler.MarkdownStyler()

    with open("test.md", "w") as file:
        file.write(markdown.heading(study_plan["name"]))
        file.write(markdown.paragraph(study_plan["highlight"]))
        file.write(markdown.paragraph(study_plan["description"]))
        file.write(markdown.paragraph(study_plan["staticCoverPicture"]))

        for i, group in enumerate(study_plan["planSubGroups"]):
            file.write(markdown.heading(f"{i + 1}. {group['name']}", level=3))
            for j, question in enumerate(group["questions"]):

                file.write(
                    markdown.paragraph(
                        f"{i + 1}.{j + 1} {question['titleSlug']}\n"

                    )
                )

        file.write(markdown.paragraph(study_plan["staticCoverPicture"]))

    print("Done")

    return

if __name__ == "__main__":
    main()
    