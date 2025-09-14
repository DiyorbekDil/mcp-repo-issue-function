# GitHub Issue Creator MCP Tool

A powerful Model Context Protocol (MCP) tool that enables automated GitHub issue creation through AI assistants like Claude. Built with Python and the PyGithub library.

## 🚀 Features

- **Automated Issue Creation**: Create GitHub issues programmatically through MCP
- **Environment Configuration**: Secure token and repository management
- **FastMCP Integration**: Built on the FastMCP framework for easy deployment
- **AI Assistant Compatible**: Works seamlessly with Claude and other MCP-supported AI tools

## 🛠️ Technologies Used

- **Python 3.x** - Core programming language
- **PyGithub** - GitHub API integration
- **FastMCP** - Model Context Protocol server framework
- **python-dotenv** - Environment variable management
- **GitHub API** - Repository and issue management

## 📋 Prerequisites

- Python 3.7+
- GitHub Personal Access Token with Issues write permissions
- Git repository access

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/github-issue-creator.git
   cd github-issue-creator
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```
   *if you use pip:*
   ```bash
   pip install pygithub python-dotenv fastmcp
   ```

4. **Configure environment variables**
   Create a `.env` file in the project root:
   ```env
   ACCESS_TOKEN=your_github_personal_access_token
   REPO_NAME=your-username/your-repository-name
   ```

5. **Run the MCP server**
   ```bash
   python main.py
   ```

## 🔧 Configuration

### GitHub Token Setup
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate a fine-grained token with **Issues: Write** permission
3. Add the token to your `.env` file

### Repository Configuration
Update the `REPO_NAME` in your `.env` file with your target repository in the format: `username/repository-name`

## 💡 Usage

Once configured, the tool exposes a `create_issue` function that can be called by MCP-compatible AI assistants:

```python
create_issue(
    issue_title="Your Issue Title",
    issue_text="Detailed issue description with markdown support"
)
```
