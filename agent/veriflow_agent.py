from browser_use.agent.service import Agent

from agent.browser.chrome import build_chrome_browser
from agent.llm.azure_llm import AzureLLM


class VeriFlowAgent:

    @staticmethod
    def create(task: str,
               use_vision: bool = True,
               initial_actions: list = None):
        browser = build_chrome_browser()
        llm = AzureLLM().create()

        agent = Agent(
            task=task,
            llm=llm,
            browser=browser,
            use_vision=use_vision
        )

        return agent
