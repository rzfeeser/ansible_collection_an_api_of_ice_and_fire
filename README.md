# Ansible Collection - An API of Ice and Fire

An Ansible collection providing automations and utilities for interacting with the [An API of Ice and Fire REST API](https://anapioficeandfire.com). This collection includes playbooks and roles for querying and processing data about books, characters, and other resources from the Game of Thrones/A Song of Ice and Fire universe.

## About

- **Collection Name:** `rzfeeser.an_api_of_ice_and_fire`
- **Version:** 1.0.0
- **Author:** RZFeeser
- **License:** GPL-2.0-or-later
- **Repository:** https://github.com/rzfeeser/ansible_collection_an_api_of_ice_and_fire

## Description

Automations against An API Of Ice And Fire - a free REST API providing information about books, characters, houses, and other entities from the world of A Song of Ice and Fire.

## Requirements

- Ansible >= 2.9.10
- Python 3.x
- Network access to https://anapioficeandfire.com/api/

## Collection Contents

### Playbooks

The collection includes four primary playbooks demonstrating different approaches to API interaction:

- **playbook01_uri_module_only.yml** - Basic example using the uri module to make direct API calls to the root endpoint
- **playbook02_uri_module_only_explore_book_by_var.yml** - Explores specific book endpoints using variables
- **playbook03_with_loops.yml** - Advanced playbook using loops to iterate over multiple API endpoints
- **playbook03_with_loops_include_tasks.yml** - Loop-based approach with included task files for better modularity
- **playbook04_role_rzfeeser_an_api_of_ice_and_fire_resource_getter.yml** - Demonstrates using the included role for resource fetching

### Roles

#### `resource_getter`

A reusable role for querying the API and processing responses.

**Role Tasks:**
- Queries the root API endpoint (https://anapioficeandfire.com/api/)
- Registers the JSON response containing available resources (books, characters, houses, etc.)
- Loops through available resources using included tasks for modular processing

**Usage in a playbook:**
```yaml
- hosts: localhost
  gather_facts: false
  roles:
    - rzfeeser.an_api_of_ice_and_fire.resource_getter
```

### Plugins

Currently contains plugin documentation and can be extended with additional custom plugins as needed.

## Getting Started

### Installation

Install the collection from GitHub:

```bash
ansible-galaxy collection install git+https://github.com/rzfeeser/ansible_collection_an_api_of_ice_and_fire.git
```

Or from Galaxy (when published):

```bash
ansible-galaxy collection install rzfeeser.an_api_of_ice_and_fire
```

### Running Playbooks

Run any of the included playbooks:

```bash
ansible-playbook playbooks/playbook01_uri_module_only.yml
ansible-playbook playbooks/playbook04_role_rzfeeser_an_api_of_ice_and_fire_resource_getter.yml
```

## API Information

This collection interacts with [An API of Ice and Fire](https://anapioficeandfire.com), a free REST API providing:

- Books from A Song of Ice and Fire series
- Characters from the series
- Houses and their histories
- Additional metadata

All endpoints return JSON data with no authentication required.

## Use Cases

- Automated data collection from the API for analysis or reporting
- Creating dynamic inventories based on API data
- Learning Ansible automation patterns with a public, reliable API
- Building workflows that consume Game of Thrones/ASOIAF data

## Contributing

Contributions are welcome! Please open an issue or pull request on the GitHub repository.

## License

This collection is licensed under GPL-2.0-or-later. See LICENSE file for details.

## Author

**RZFeeser** - rzfeeser@users.noreply.github.com

For issues, questions, or contributions, please visit the [https://iris7.com](https://iris7.com)


