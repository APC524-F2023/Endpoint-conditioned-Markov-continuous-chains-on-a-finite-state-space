# reference: week 5 course note
# https://henryiii.github.io/se-for-sci/content/week05/task_runners.html
import nox


@nox.session
def tests(session):
    session.install("-e.[test]")
    session.run("pytest")


@nox.session
def build_api_docs(session: nox.Session) -> None:
    """
    Build (regenerate) API docs.
    """

    session.install("sphinx")
    session.chdir("docs")
    session.run(
        "sphinx-apidoc",
        "-o",
        "api/",
        "--module-first",
        "--no-toc",
        "--force",
        "../src/ECMC",
    )
