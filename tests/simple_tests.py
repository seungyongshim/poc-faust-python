import pytest
from unittest.mock import Mock, patch
from simple import app, foo, bar


@pytest.fixture()
def test_app(event_loop):
    app.finalize()
    app.conf.store = "memory://"
    app.flow_control.resume()
    return app


@pytest.mark.asyncio()
async def test_foo(test_app):
    with patch(__name__ + ".bar") as mocked_bar:
        mocked_bar.send = mock_coro()
        async with foo.test_context() as agent:
            await agent.put("hey")
            mocked_bar.send.assert_called_with("hey")
