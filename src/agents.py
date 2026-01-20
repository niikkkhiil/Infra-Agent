import boto3
from langchain.agents import create_agent
from langchain.llms import gemini
from langchain.prompts import PromptTemplate
from langchain.tools import Tool
