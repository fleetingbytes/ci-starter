from pytest import FixtureRequest, fixture

from ci_starter import generate_reusable_workflow


@fixture(scope="session")
def workflow(request: FixtureRequest) -> dict:
    path = request.param
    wf: dict = generate_reusable_workflow(path)
    return wf
