OOP Style, command-line args
1. Reorg reqs
2. Try browser cookie 3 instead of manual cookie entry in .env file
3. Optimize GraphQL queries in 2 (study plan, question detials, lastSubmissionId) then (submissionId)
4. path exists create a new path with path-1 path-2 ...
5. when i complete it I want to display the medal

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


