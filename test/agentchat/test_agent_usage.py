from autogen.agent_utils import gather_usage_summary
from autogen import AssistantAgent, UserProxyAgent
from test_assistant_agent import KEY_LOC, OAI_CONFIG_LIST
import pytest
from conftest import skip_openai

try:
    import openai
except ImportError:
    skip = True
else:
    skip = False or skip_openai


def test_gathering():
    assistant1 = AssistantAgent(
        "assistant",
        system_message="You are a helpful assistant.",
        llm_config={
            "config_list": OAI_CONFIG_LIST,
        },
    )
    assistant2 = AssistantAgent(
        "assistant",
        system_message="You are a helpful assistant.",
        llm_config={
            "config_list": OAI_CONFIG_LIST,
        },
    )
    assistant3 = AssistantAgent(
        "assistant",
        system_message="You are a helpful assistant.",
        llm_config={
            "config_list": OAI_CONFIG_LIST,
        },
    )

    assistant1.client.total_usage_summary = {
        "total_cost": 0.1,
        "gpt-35-turbo": {"cost": 0.1, "prompt_tokens": 100, "completion_tokens": 200, "total_tokens": 300},
    }
    assistant2.client.total_usage_summary = {
        "total_cost": 0.2,
        "gpt-35-turbo": {"cost": 0.2, "prompt_tokens": 100, "completion_tokens": 200, "total_tokens": 300},
    }
    assistant3.client.total_usage_summary = {
        "total_cost": 0.3,
        "gpt-4": {"cost": 0.3, "prompt_tokens": 100, "completion_tokens": 200, "total_tokens": 300},
    }

    total_usage, _ = gather_usage_summary([assistant1, assistant2, assistant3])

    assert round(total_usage["total_cost"], 8) == 0.6
    assert round(total_usage["gpt-35-turbo"]["cost"], 8) == 0.3
    assert round(total_usage["gpt-4"]["cost"], 8) == 0.3

    # test when agent doesn't have client
    user_proxy = UserProxyAgent(
        name="ai_user",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=2,
        code_execution_config=False,
        default_auto_reply="That's all. Thank you.",
    )

    total_usage, acutal_usage = gather_usage_summary([user_proxy])


@pytest.mark.skipif(skip, reason="openai not installed OR requested to skip")
def test_agent_usage():
    assistant = AssistantAgent(
        "assistant",
        system_message="You are a helpful assistant.",
        llm_config={
            "timeout": 600,
            "cache_seed": None,
            "config_list": OAI_CONFIG_LIST,
        },
    )

    ai_user_proxy = UserProxyAgent(
        name="ai_user",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=1,
        code_execution_config=False,
        llm_config={
            "config_list": OAI_CONFIG_LIST,
        },
        # In the system message the "user" always refers to the other agent.
        system_message="You ask a user for help. You check the answer from the user and provide feedback.",
    )

    math_problem = "$x^3=125$. What is x?"
    ai_user_proxy.initiate_chat(
        assistant,
        message=math_problem,
    )

    # test print
    ai_user_proxy.print_usage_summary()
    print()
    assistant.print_usage_summary()

    # test get
    print("Actual usage summary (excluding completion from cache):", assistant.get_actual_usage())
    print("Total usage summary (including completion from cache):", assistant.get_total_usage())

    print("Actual usage summary (excluding completion from cache):", ai_user_proxy.get_actual_usage())
    print("Total usage summary (including completion from cache):", ai_user_proxy.get_total_usage())


if __name__ == "__main__":
    test_gathering()
    test_agent_usage()
