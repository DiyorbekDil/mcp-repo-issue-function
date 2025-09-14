import os

from github import Github
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

mcp = FastMCP()

@mcp.tool()
def create_issue(issue_title: str, issue_text: str) -> str:
    try:
        g = Github(os.getenv('ACCESS_TOKEN'))
        repo = g.get_repo(os.getenv('REPO_NAME'))
        issue = repo.create_issue(title=issue_title, body=issue_text)

        return "Success"
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == '__main__':
    mcp.run(transport='stdio')