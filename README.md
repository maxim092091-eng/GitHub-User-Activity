# GitHub User Activity
GitHub User Activity is a command-line interface (CLI) for fetching and displaying a user's GitHub activity.

## Project URL

https://github.com/maxim092091-eng/GitHub-User-Activity

## Roadmap Project

https://roadmap.sh/projects/github-user-activity

## Features
- **Username** - Display activity for the selected user
- **Username + Type** - Display user activity filtered by event type

## Installation

Clone the repository:

```bash
git clone https://github.com/maxim092091-eng/GitHub-User-Activity
```

Go to the project directory:

```bash
cd GitHub-User-Activity
```

Install the project:

```bash
pip install -e .
```

## Usage

### Show user activity

```bash
github-activity <username>
```

Example:

```bash
github-activity rasam
```

Output:

```text
Pushed 5 commits to rasam/GitHub-User-Activity
Opened a new issue in rasam/GitHub-User-Activity
```

### Show user activity filtered by event type

```bash
github-activity <username> <type>
```
The event type can be specified using the beginning of the event name in lowercase.

Example:

```bash
github-activity rasam push
```

Output:

```text
Pushed 5 commits to rasam/GitHub-User-Activity
```

## Technologies

- Python 3
- JSON
- Argparse
- Requests

## License

This project is licensed under the MIT License.