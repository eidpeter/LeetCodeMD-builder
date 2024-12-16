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
    study_plan = study_plan_url.split("https://leetcode.com/studyplan/")[1].split("/")[0]
    print(study_plan)

    study_plan_data = leetcode_service.get_study_plan(study_plan)
    print(study_plan_data)

    

    return


if __name__ == "__main__":
    main()
