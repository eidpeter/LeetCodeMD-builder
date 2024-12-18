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

    def get_question(self, question_slug):
        payload = {
            "query": """
                query GetQuestion($titleSlug: String!) {
                    question(titleSlug: $titleSlug) {
                        questionId
                        questionFrontendId
                        title
                        titleSlug
                        difficulty
                        content
                    }
                }
            """,
            "variables": {"titleSlug": question_slug},
        }

        response = self.client.send_query(payload)

        return response["question"]

    def get_last_submission_id(self, question_slug):
        payload = {
            "query": """
                query GetSubmissionList($questionSlug: String!) {
                    questionSubmissionList(questionSlug: $questionSlug, status: 10, offset: 0, limit: 1) {
                        submissions{
                            id
                        }
                      }
                }
            """,
            "variables": {"questionSlug": question_slug},
        }
        response = self.client.send_query(payload)

        id = response["questionSubmissionList"]["submissions"][0]["id"]

        return id

    def get_submission(self, submission_id):
        payload = {
            "query": """
                query GetSubmission($submissionId: Int!) {
                    submissionDetails(submissionId: $submissionId) {
                        code
                        memory
                        runtimeDisplay
                    }
                }
            """,
            "variables": {"submissionId": submission_id},
        }
        response = self.client.send_query(payload)

        return response["submissionDetails"]

    def get_question_submission(self, question_slug):
        id = self.get_last_submission_id(question_slug)
        submission = self.get_submission(id)
        return submission
