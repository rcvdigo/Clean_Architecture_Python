import requests
import os
from dotenv import load_dotenv
from pprint import pprint


def make_github_graphql_request(query_def, variables_def):
    load_dotenv()

    # Defina o token de acesso do GitHub
    token = os.getenv("GIT_TOKEN")

    # Defina o cabeçalho da requisição com o token de acesso
    headers = {
        'Authorization': f'Bearer {token}',
    }

    # Defina os dados da requisição GraphQL, incluindo a consulta e as variáveis
    data = {
        'query': query_def,
        'variables': variables_def
    }

    # Faça a requisição POST para o endpoint GraphQL do GitHub
    response = requests.post(
        'https://api.github.com/graphql',
        json=data, headers=headers,
        timeout=10
        )

    # Verifique o código de status da resposta
    if response.status_code == 200:
        return response.json()

    # Se a requisição falhar, imprima o código de status e a mensagem de erro
    print(f'Erro ao fazer a requisição: {response.status_code}')
    print(response.text)
    return None

# Consulta GraphQL e variáveis
QUERY = """
      query($username: String!) {
        user(login: $username) { 
          name
          bio
          avatarUrl
          location
          repositoriesContributedTo(first: 5, contributionTypes: [COMMIT, ISSUE, PULL_REQUEST], includeUserRepositories: false) {
            totalCount
            nodes {
              name
              description
              forkCount
              stargazerCount
              url
              id
              diskUsage
              primaryLanguage {
                name
                color
              }
            }
          }
          pinnedItems(first: 6, types: [REPOSITORY]) {
            edges {
              node {
                ... on Repository {
                  name
                  description
                  forkCount
                  stargazers {
                    totalCount
                  }
                  url
                  id
                  diskUsage
                  primaryLanguage {
                    name
                    color
                  }
                }
              }
            }
          }
        }
      }
"""

variables = {
    "username": os.getenv("GIT_NAME")
}

# Faz a requisição GraphQL
result = make_github_graphql_request(QUERY, variables)
pprint(result)

# if result:
#     print("Dados do usuário:")
#     print("Nome:", result['data']['user']['name'])
#     print("Bio:", result['data']['user']['bio'])
#     print("Localização:", result['data']['user']['location'])
#     print("Avatar URL:", result['data']['user']['avatarUrl'])
#     print("Repositórios contribuídos:")
#     for repo in result['data']['user']['repositoriesContributedTo']['nodes']:
#         print("- Nome:", repo['name'])
#         print("  Descrição:", repo['description'])
#         print("  Forks:", repo['forkCount'])
#         print("  Estrelas:", repo['stargazerCount'])
#         print("  URL:", repo['url'])
#         print(
# "  Linguagem primária:", repo['primaryLanguage']['name'], repo['primaryLanguage']['color'])
#     print("Repositórios fixados:")
#     for edge in result['data']['user']['pinnedItems']['edges']:
#         repo = edge['node']
#         print("- Nome:", repo['name'])
#         print("  Descrição:", repo['description'])
#         print("  Forks:", repo['forkCount'])
#         print("  Estrelas:", repo['stargazers']['totalCount'])
#         print("  URL:", repo['url'])
#         print("
#  Linguagem primária:", repo['primaryLanguage']['name'], repo['primaryLanguage']['color'])

