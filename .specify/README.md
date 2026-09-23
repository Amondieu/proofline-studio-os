# Proofline lightweight Spec-Kit workflow

This is a project-local, dependency-free adaptation of the workflow described
by GitHub Spec Kit. It is not a second build system and does not override
`AGENTS.md` or Proofline's human authority model.

For a feature or research integration, keep these artifacts together:

1. `.specify/memory/constitution.md`
2. `specs/<number>-<slug>/spec.md`
3. `specs/<number>-<slug>/plan.md`
4. `specs/<number>-<slug>/tasks.md`
5. `specs/<number>-<slug>/converge.md`

The normal sequence is:

`Constitution → Specify → Plan → Tasks → Implement → Converge/Verify`

The files are reviewable Markdown, not a permission to skip human decisions.
