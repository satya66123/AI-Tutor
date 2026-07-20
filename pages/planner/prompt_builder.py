"""
Study Plan Prompt Builder
"""


class PromptBuilder:

    @staticmethod
    def build(
        subject,
        level,
        goal,
        hours,
        duration
    ):

        return f"""
You are an expert tutor.

Create a personalized study plan.

Subject:
{subject}

Current Level:
{level}

Goal:
{goal}

Study Hours Per Day:
{hours}

Duration:
{duration}

Return:

1. Weekly roadmap

2. Daily schedule

3. Important topics

4. Practice tasks

5. Resources

6. Revision strategy

Use markdown formatting.
"""