"""
Revision Planner Prompt Builder
"""


class PlannerPromptBuilder:

    @staticmethod
    def build(

        exam,

        subject,

        topics,

        exam_date,

        hours,

        difficulty,

        goal,

        plan_type

    ):

        return f"""
You are an expert study planner.

Create a {plan_type.lower()} revision plan.

Exam:
{exam}

Subject:
{subject}

Topics:
{topics}

Exam Date:
{exam_date}

Available Study Hours:
{hours} hours/day

Difficulty:
{difficulty}

Goal:
{goal}

Generate:

1. Study Schedule
2. Daily Tasks
3. Weekly Milestones
4. Important Topics
5. Revision Strategy
6. Practice Plan
7. Mock Test Plan
8. Final Week Strategy

Format using Markdown headings and bullet points.
"""