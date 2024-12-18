TODO:

- [x] validate submissions
- [x] progress bar when executing
- [x] Reorg reqs
- [ ] command-line args
- [ ] path exists create a new path with path-1 path-2 ...
- [ ] display stats in readme
- [ ] when i complete it I want to display the medal
- [ ] Try browser cookie 3 instead of manual cookie entry in .env file
- [ ] parallelize file writing
- [ ] Optimize GraphQL queries in 2 (study plan, question details, lastSubmissionId) then (submissionId)

---

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


