import asyncio
import os
import sys

from dotenv import load_dotenv

from agent.veriflow_agent import VeriFlowAgent

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv()


# Entrypoint of the application
async def main():
    task = """
    1. Navigate to https://rahulshettyacademy.com/loginpagePractise/
    2. Login with username and password. login details are available in the page
    3. after login, select first 2 products and add them to cart
    4. then checkout and store the total value you see in the screen
    5. increase the quantity of any product and check if total value updates accordingly
    6. checkout and select country, agree terms and purchase
    7. verify thank you message is displayed
    """

    agent = VeriFlowAgent.create(task=task)
    history = await agent.run()
    test_result = history.final_result()
    print(test_result)


asyncio.run(main())
