from langchain.tools import tool
from pydantic import BaseModel, Field


class MultiplyInput(BaseModel):
    a: int = Field(default=1, description="The first number")
    b: int = Field(default=1, description="The second number")


@tool("multiply_numbers", description="Calculate the product of two numbers. Always use result_formatter tool while returning the result.", infer_schema=True)
def multiply_numbers(input: MultiplyInput) -> int:

    print(f"Tool Called: Multiply calculator")

    return input.a * input.b


@tool("add_numbers", description="Calculate the addition of two numbers. Always use result_formatter tool while returning the result.", infer_schema=True)
def add_numbers(input: MultiplyInput) -> int:

    print(f"Tool Called: Add calculator")

    return input.a + input.b


@tool("result_formatter", description="Format the result in a specific way before sending it back to the user.")
def result_formatter(result: int) -> str:

    print(f"Tool Called: Result formatter")

    return "Result is coming from Bangalore: " + str(result)