# reference: week 5 course note
# https://henryiii.github.io/se-for-sci/content/week05/task_runners.html
import nox


@nox.session
def tests(session):
    session.install("-e.[test]")
    session.run("pytest")


@nox.session
def docs(session):
    session.install("-e.[docs]")
    session.chdir("docs")
    session.run("make", "html", external=True)
    session.run("open", "_build/html/index.html", external=True)
