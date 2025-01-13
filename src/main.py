import os
import argparse
from dotenv import load_dotenv
from leetcode.leetcode_service import LeetCodeService
from utils.file_handler import FileHandler
from utils.markdown_styler import MarkdownStyler
from tqdm import tqdm


def main():
    parser = argparse.ArgumentParser(
        description="Download leetcode study plan questions and solutions to markdown files."
    )
    parser.add_argument(
        "-u",
        "--url",
        type=str,
        required=True,
        help="The URL of the Leetcode study plan (e.g., https://leetcode.com/studyplan/top-sql-50/)",
    )
    parser.add_argument(
        "-o",
        "--output_folder",
        type=str,
        required=True,
        help="The output folder path to save the markdown files.",
    )
    args = parser.parse_args()

    load_dotenv()
    cookie = os.getenv("LEETCODE_COOKIE")

    leetcode_service = LeetCodeService(cookie)
    file_handler = FileHandler()
    markdown_styler = MarkdownStyler()

    study_plan_url = args.url
    study_plan = study_plan_url.split("https://leetcode.com/studyplan/")[1].split("/")[
        0
    ]

    study_plan_data = leetcode_service.get_study_plan(study_plan)

    folder_path = file_handler.create_folder(
        args.output_folder, "leetcode-" + study_plan
    )

    readme_path = file_handler.create_file(folder_path, "README.md")

    with open(readme_path, "a", encoding="utf-8") as f:
        f.write(
            markdown_styler.heading(
                markdown_styler.link(
                    f"LeetCode {study_plan_data['name']}", study_plan_url
                ),
                1,
            )
        )

        f.write(
            markdown_styler.blockquote(
                f"This whole repository is auto-generated using {markdown_styler.link('eidpeter/LeetCodeMD-builder', 'https://github.com/eidpeter/LeetCodeMD-builder')}. Only version control is done manually.\n"
            )
        )

        f.write(markdown_styler.paragraph(study_plan_data["description"]))

        f.write(markdown_styler.hr())

    for i, subgroup in enumerate(
        tqdm(study_plan_data["planSubGroups"], desc="Subgroups"), 1
    ):
        subgroup_path = file_handler.create_folder(
            folder_path, f"{i} {subgroup['name']}"
        )

        with open(readme_path, "a", encoding="utf-8") as f:
            f.write(markdown_styler.bold(f"{subgroup['name']}:"))
            f.write("\n\n")

        for j, question in enumerate(
            tqdm(subgroup["questions"], desc=f"Questions", leave=False), 1
        ):
            file_path = file_handler.create_file(
                subgroup_path, f"{i}-{j}_{question['titleSlug']}.md"
            )
            question_data = leetcode_service.get_question(question["titleSlug"])
            submission_data = leetcode_service.get_question_submission(
                question["titleSlug"]
            )

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(
                    markdown_styler.heading(
                        f"{question_data['questionFrontendId']}. {question_data['title']}",
                        2,
                    )
                )
                if question_data["difficulty"] == "Easy":
                    f.write("🟢 ")
                elif question_data["difficulty"] == "Medium":
                    f.write("🟠 ")
                elif question_data["difficulty"] == "Hard":
                    f.write("🔴 ")
                f.write(question_data["difficulty"])
                f.write("\n")
                f.write(markdown_styler.hr())
                f.write(question_data["content"])
                f.write(markdown_styler.hr())
                if submission_data is not None:
                    f.write(markdown_styler.heading("Solution", 3))
                    f.write(markdown_styler.code_block(submission_data["code"]))

            with open(readme_path, "a", encoding="utf-8") as f:
                f.write(markdown_styler.checkbox(checked=submission_data is not None))
                f.write(
                    markdown_styler.link(
                        f"{question['title']}",
                        "<"
                        + f"{i} {subgroup['name']}"
                        + "/"
                        + f"{i}-{j}_{question['titleSlug']}.md"
                        + ">",
                    )
                )
                f.write(f" ({question_data['difficulty']})")
                f.write("\n\n")

    return


if __name__ == "__main__":
    main()
