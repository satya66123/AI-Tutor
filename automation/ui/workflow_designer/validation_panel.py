import streamlit as st


class ValidationPanel:

    @staticmethod
    def render(workflow):

        st.subheader("Workflow Validation")

        if workflow is None:

            st.error("Workflow not found.")

            return

        errors = []
        warnings = []

        # ----------------------------------------
        # Workflow Name
        # ----------------------------------------

        if not workflow.workflow_name.strip():

            errors.append(
                "Workflow name cannot be empty."
            )

        # ----------------------------------------
        # Steps
        # ----------------------------------------

        if len(workflow.steps) == 0:

            errors.append(
                "Workflow contains no steps."
            )

        # ----------------------------------------
        # Duplicate IDs
        # ----------------------------------------

        ids = [step.id for step in workflow.steps]

        duplicates = []

        for step_id in ids:

            if ids.count(step_id) > 1 and step_id not in duplicates:

                duplicates.append(step_id)

        if duplicates:

            errors.append(
                f"Duplicate Step IDs: {', '.join(duplicates)}"
            )

        # ----------------------------------------
        # Dependency Validation
        # ----------------------------------------

        valid_ids = set(ids)

        for step in workflow.steps:

            for dependency in step.depends_on:

                if dependency not in valid_ids:

                    errors.append(

                        f"{step.id} depends on missing step '{dependency}'."

                    )

        # ----------------------------------------
        # Disabled Steps
        # ----------------------------------------

        disabled = [

            step.id

            for step in workflow.steps

            if not step.enabled

        ]

        if disabled:

            warnings.append(

                "Disabled Steps: "

                + ", ".join(disabled)

            )

        # ----------------------------------------
        # Missing Task Name
        # ----------------------------------------

        for step in workflow.steps:

            task = step.task.task

            if not task.task_name.strip():

                warnings.append(

                    f"{step.id} has empty task name."

                )

        # ----------------------------------------
        # Missing Input
        # ----------------------------------------

        for step in workflow.steps:

            task = step.task.task

            if task.input_data in (None, "", {}):

                warnings.append(

                    f"{step.id} has no input."

                )

        # ----------------------------------------
        # Circular Dependency
        # ----------------------------------------

        graph = {}

        for step in workflow.steps:

            graph[step.id] = step.depends_on

        visited = set()
        stack = set()

        def dfs(node):

            if node in stack:

                return True

            if node in visited:

                return False

            visited.add(node)

            stack.add(node)

            for nxt in graph.get(node, []):

                if dfs(nxt):

                    return True

            stack.remove(node)

            return False

        circular = False

        for node in graph:

            if dfs(node):

                circular = True

                break

        if circular:

            errors.append(

                "Circular dependency detected."

            )

        # ----------------------------------------
        # Results
        # ----------------------------------------

        if len(errors) == 0:

            st.success(

                "Workflow validation passed."

            )

        else:

            st.error(

                f"{len(errors)} Error(s) Found"

            )

            for error in errors:

                st.error(error)

        if warnings:

            st.warning(

                f"{len(warnings)} Warning(s)"

            )

            for warning in warnings:

                st.warning(warning)

        st.divider()

        st.subheader("Validation Summary")

        c1, c2, c3 = st.columns(3)

        c1.metric(

            "Steps",

            len(workflow.steps)

        )

        c2.metric(

            "Errors",

            len(errors)

        )

        c3.metric(

            "Warnings",

            len(warnings)

        )