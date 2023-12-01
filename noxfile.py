# reference: week 5 course note
# https://henryiii.github.io/se-for-sci/content/week05/task_runners.html
import nox


@nox.session
def tests(session):
    session.install("-e.[test]")
    session.run("pytest")
