from mcp.server.fastmcp import FastMCP

# Inicialização do servidor MCP
mcp = FastMCP("Tool Generator MCP")


@mcp.tool(
    name="generate_mcp_tool",
    description="Gera código fonte para uma nova tool FastMCP em Python ou JavaScript, exibindo o resultado em preview code."
)
def generate_mcp_tool(
    language: str,
    tool_name: str,
    tool_description: str,
    parameters: str,
    function_body: str
) -> str:
    """
    Gera código fonte para uma nova tool FastMCP em Python ou JavaScript,
    encapsulando o resultado em um bloco de preview code.

    Args:
        language: 'python' ou 'javascript'.
        tool_name: Nome da nova tool.
        tool_description: Descrição da nova tool.
        parameters: Lista de parâmetros da função, por exemplo: "x: int, y: int".
        function_body: Corpo da função com indentação adequada (ex.: 4 espaços por nível).
    
    Returns:
        str: Código fonte da nova tool encapsulado em um bloco de preview code.
    
    Raises:
        ValueError: Se a linguagem não for suportada.
    """
    language = language.lower().strip()
    
    if language == "python":
        code = f'''from mcp.server.fastmcp import FastMCP

mcp = FastMCP("{tool_name} Generator")

@mcp.tool(
    name="{tool_name}",
    description="{tool_description}"
)
def {tool_name}({parameters}):
{function_body}

if __name__ == "__main__":
    mcp.run(transport="stdio")
'''
        preview = f"```python\n{code}\n```"
    
    elif language == "javascript":
        code = f'''// Exemplo de uma tool FastMCP em JavaScript
const {{ FastMCP }} = require('mcp.server.fastmcp');

const mcp = new FastMCP("{tool_name} Generator");

/**
 * {tool_description}
 */
mcp.tool("{tool_name}", ({parameters}) => {{
{function_body}
}});

mcp.run({{ transport: "stdio" }});
'''
        preview = f"```javascript\n{code}\n```"
    
    else:
        raise ValueError("Linguagem não suportada. Escolha 'python' ou 'javascript'.")

    return preview

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="stdio")