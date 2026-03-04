from langchain.tools import tool
from pydantic import BaseModel, Field


class MultiplyInput(BaseModel):
    a: int = Field(default=1, description="The first number")
    b: int = Field(default=1, description="The second number")


@tool("multiply_numbers", description="Calculate the product of two numbers", infer_schema=True)
def multiply_numbers(input: MultiplyInput) -> int:

    print(f"Tool Called: Multiply calculator")

    return input.a * input.b