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

        try:
            response = self.client.send_query(payload)
            return response["studyPlanV2Detail"]
        except Exception as e:
            print(f"Error fetching study plan for {plan_slug}: {e}")
            return None

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

        try:
            response = self.client.send_query(payload)
            return response["question"]
        except Exception as e:
            print(f"Error fetching question for {question_slug}: {e}")
            return None

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
        try:
            response = self.client.send_query(payload)
            submissions = response.get("questionSubmissionList", {}).get(
                "submissions", []
            )

            if not submissions:
                # print(f"No submissions found for question: {question_slug}")
                return None

            return submissions[0]["id"]
        except Exception as e:
            # print(
            #     f"An error occurred while fetching submission ID for {question_slug}: {e}"
            # )
            return None

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
        try:
            response = self.client.send_query(payload)
            submission_details = response.get("submissionDetails")

            if not submission_details:
                # print(f"No submission details found for submission ID: {submission_id}")
                return None

            return submission_details

        except Exception as e:
            # print(
            #     f"An error occurred while fetching submission details for {submission_id}: {e}"
            # )
            return None

    def get_question_submission(self, question_slug):
        try:
            id = self.get_last_submission_id(question_slug)
            if id is None:
                # print(f"No submission ID found for question: {question_slug}")
                return None

            submission = self.get_submission(id)
            if submission is None:
                # print(f"No submission details for submission ID: {id}")
                return None

            return submission

        except Exception as e:
            # print(
            #     f"An error occurred while fetching the submission for question: {question_slug}: {e}"
            # )
            return None
