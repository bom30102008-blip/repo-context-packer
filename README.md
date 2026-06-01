# Repo Context Packer

A lightning-fast CLI utility that aggregates your entire codebase into a single, LLM-digestible Markdown file. 

Built to eliminate the copy-paste friction when feeding repository context to AI models like Claude 3 or GPT-4.

## Features
* **Smart Filtering:** Automatically respects your `.gitignore` rules.
* **Binary Safe:** Skips images, compiled binaries, and non-text files to prevent context pollution.
* **Zero Config:** Runs out of the box with sensible defaults.

## Installation

Clone the repository and install the minimal dependencies:

```bash
git clone [https://github.com/bom30102008-blip/repo-context-packer.git](https://github.com/bom30102008-blip/repo-context-packer.git)
cd repo-context-packer
pip install -r requirements.txt