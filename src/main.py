from leetcode.leetcode_service import LeetCodeService
from utils.file_handler import FileHandler
from utils.markdown_styler import MarkdownStyler
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    cookie = os.getenv("LEETCODE_COOKIE")

    leetcode_service = LeetCodeService(cookie)
    file_handler = FileHandler()
    markdown_styler = MarkdownStyler()

    study_plan_url = "https://leetcode.com/studyplan/top-sql-50/"
    study_plan = study_plan_url.split("https://leetcode.com/studyplan/")[1].split("/")[
        0
    ]

    study_plan_data = leetcode_service.get_study_plan(study_plan)

    folder_path = file_handler.create_folder(".", study_plan)
    # for every subgroup in study plan create a folder
    for i, subgroup in enumerate(study_plan_data["planSubGroups"], 1):
        subgroup_path = file_handler.create_folder(
            folder_path, f"{i} {subgroup['name']}"
        )
        for j, question in enumerate(subgroup["questions"], 1):
            file_path =file_handler.create_file(
                subgroup_path, f"{i}-{j}_{question['titleSlug']}.md"
            )
            question_data = leetcode_service.get_question(question["titleSlug"])
            submission_data = leetcode_service.get_question_submission(question["titleSlug"])

            with open(file_path, "w") as f:
                f.write(markdown_styler.heading(f"{question_data['questionFrontendId']}. {question_data['title']}", 2))
                f.write(question_data["content"])
                f.write(markdown_styler.hr())
                f.write(markdown_styler.heading("Solution", 3))
                f.write(markdown_styler.code_block(submission_data["code"], "sql"))

    return


if __name__ == "__main__":
    main()
