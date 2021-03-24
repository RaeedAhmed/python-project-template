import nox

locs = "src", "noxfile.py"


@nox.session(python=False)
def lint(session):
    session.run("poetry", "shell")
    session.run("poetry", "install")
    session.run("black", *locs)
    session.run("isort", *locs)
    session.run("flake8", *locs)
