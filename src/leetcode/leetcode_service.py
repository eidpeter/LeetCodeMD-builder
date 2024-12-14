import requests
import json
import os
from dotenv import load_dotenv
from leetcode.api_client import LeetCodeAPIClient


class LeetCodeService:
    def __init__(self, cookie):
        self.client = LeetCodeAPIClient(cookie)

    def get_study_plan(self, plan_slug):

        payload = {
            "query": """
                query GetSQL50StudyPlan($planSlug: String!) {
                    studyPlanV2Detail(planSlug: $planSlug) {
                        name
                        highlight
                        description
                        staticCoverPicture
                        planSubGroups {
                            slug
                            name
                            questions {
                                titleSlug
                                title
                                questionFrontendId
                                difficulty
                                status
                            }
                        }
                    }
                }
            """,
            "variables": {"planSlug": plan_slug},
        }

        response = self.client.send_query(payload)

        return response["studyPlanV2Detail"]


load_dotenv()
cookie = os.getenv("LEETCODE_COOKIE")
study_plan = LeetCodeService(cookie).get_study_plan("top-sql-50")
print(study_plan["name"])
print(study_plan["highlight"])
print(study_plan["description"])
print(study_plan["staticCoverPicture"])


for i, group in enumerate(study_plan["planSubGroups"]):
    print(f"{i + 1}. {group['name']}")
    for j, question in enumerate(group["questions"]):
        print(f"  {i+1}.{j + 1} {question['titleSlug']}")
