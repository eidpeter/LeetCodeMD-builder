OOP Style, command-line args
validate submissions, study plan link
progress bar when executing
1. Reorg reqs
2. Try browser cookie 3 instead of manual cookie entry in .env file
3. Optimize GraphQL queries in 2 (study plan, question detials, lastSubmissionId) then (submissionId)
4. path exists create a new path with path-1 path-2 ...
5. display stats in readme
6. when i complete it I want to display the medal

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


