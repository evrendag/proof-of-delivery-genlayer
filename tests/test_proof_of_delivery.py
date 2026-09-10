PASS = (
    '{"verdict":"PASS","score":92,"primary_gap":"NONE",'
    '"rationale":"The delivery satisfies every stated requirement with supporting evidence."}'
)
FAIL = (
    '{"verdict":"FAIL","score":35,"primary_gap":"COMPLETENESS",'
    '"rationale":"The delivery omits the required comparison and source list."}'
)
REVIEW = (
    '{"verdict":"REVIEW","score":68,"primary_gap":"EVIDENCE",'
    '"rationale":"The work appears complete but the supplied evidence cannot establish accuracy."}'
)
REQ = (
    "Compare three agent-payment protocols. Include architecture, public fee "
    "information, differentiators, limitations, and links to official sources."
)
DELIVERY = (
    "The report compares three named protocols across architecture, fees, "
    "differentiators, and limitations, with a source list for every section."
)


def create_and_submit(contract, direct_vm, worker):
    contract.create_work(type(contract.owner)(worker), REQ, 2)
    with direct_vm.prank(worker):
        contract.submit_delivery(0, DELIVERY, "Official documentation links are included.")


def test_create_work(direct_deploy, direct_bob):
    contract = direct_deploy("contract.py", sdk_version="v0.2.12")
    contract.create_work(type(contract.owner)(direct_bob), REQ, 2)
    item = contract.get_work(0)
    assert item.status == "OPEN"
    assert item.max_attempts == 2
    assert contract.get_work_count() == 1


def test_only_worker_can_submit(direct_vm, direct_deploy, direct_bob):
    contract = direct_deploy("contract.py", sdk_version="v0.2.12")
    contract.create_work(type(contract.owner)(direct_bob), REQ, 2)
    with direct_vm.expect_revert("Only the assigned worker"):
        contract.submit_delivery(0, DELIVERY, "Official sources")


def test_pass_becomes_accepted(direct_vm, direct_deploy, direct_bob):
    direct_vm.mock_llm(r".*", PASS)
    contract = direct_deploy("contract.py", sdk_version="v0.2.12")
    create_and_submit(contract, direct_vm, direct_bob)
    contract.evaluate_delivery(0)
    assert contract.get_work(0).status == "ACCEPTED"
    assert direct_vm.run_validator() is True


def test_fail_requests_revision(direct_vm, direct_deploy, direct_bob):
    direct_vm.mock_llm(r".*", FAIL)
    contract = direct_deploy("contract.py", sdk_version="v0.2.12")
    create_and_submit(contract, direct_vm, direct_bob)
    contract.evaluate_delivery(0)
    assert contract.get_work(0).status == "REVISION_REQUIRED"


def test_review_requires_client_resolution(direct_vm, direct_deploy, direct_bob):
    direct_vm.mock_llm(r".*", REVIEW)
    contract = direct_deploy("contract.py", sdk_version="v0.2.12")
    create_and_submit(contract, direct_vm, direct_bob)
    contract.evaluate_delivery(0)
    assert contract.get_work(0).status == "MANUAL_REVIEW"
    contract.resolve_manual_review(0, True)
    assert contract.get_work(0).status == "ACCEPTED"


def test_validator_rejects_different_gap(direct_vm, direct_deploy, direct_bob):
    direct_vm.mock_llm(r".*", PASS)
    contract = direct_deploy("contract.py", sdk_version="v0.2.12")
    create_and_submit(contract, direct_vm, direct_bob)
    contract.evaluate_delivery(0)
    direct_vm.clear_mocks()
    direct_vm.mock_llm(r".*", REVIEW)
    assert direct_vm.run_validator() is False
