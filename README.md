OOP Style, command-line args
1. take slug from study plan link `https://leetcode.com/studyplan/top-sql-50`
2. GraphQL query the study plan to create folders and files (with id, title, difficulty)
3. GraphQL query the questions using the titleSlug of questionss from previous query, fill the markdown files
4. Go to list of submissions (see `submissions.json`) 
5. ? get the accepted solution with the fastest runtime > latest date
6. Use the id to get code and runtime
7. Reorg reqs
8. Try browser cookie 3 instead of manual cookie entry in .env file

```
query GetSubmission {
submissionDetails(submissionId:1458151796){
    memory
    runtimeDisplay
    code
  }
}

```


get study plan progress

{"query":"
    query studyPlanProgress($slug: String!, $historyId: ID) {
        studyPlanV2ProgressDetail(planSlug: $slug, id: $historyId) {
              id
            status
            weeklyTaskScheduleResettable
            finishedQuestionNum
            studyPlanDetail {
                questionNum
              planSubGroups {
                  slug
                questions {
                    titleSlug
                  status
                }
              }
            }
          }
        }
            ","variables":{"slug":"top-sql-50"},"operationName":"studyPlanProgress"}


when i complete it I want to display the medal