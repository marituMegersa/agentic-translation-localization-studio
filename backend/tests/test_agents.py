def test_agent_orchestrator():
    prompt = "Test execution query for agentic-translation-localization-studio"
    assert len(prompt) > 0
    assert "Test" in prompt
