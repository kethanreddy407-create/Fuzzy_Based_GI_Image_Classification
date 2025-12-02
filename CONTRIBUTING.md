# Contributing to Fuzzy-Based GI Image Classification

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Report issues responsibly
- Follow best practices for code quality

## How to Contribute

### 1. Fork and Clone

```bash
git clone https://github.com/YOUR_USERNAME/Fuzzy_Based_GI_Image_Classification.git
cd Fuzzy_Based_GI_Image_Classification
```

### 2. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-number
```

### 3. Set Up Development Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Make Your Changes

- Follow PEP 8 style guidelines
- Add comments for complex logic
- Maintain consistent code formatting
- Test your changes thoroughly

### 5. Commit Your Changes

```bash
git add .
git commit -m "feat: Add your feature description"
```

#### Commit Message Format

- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation
- `test:` for test additions
- `refactor:` for code refactoring
- `perf:` for performance improvements
- `chore:` for maintenance tasks

### 6. Push and Create a Pull Request

```bash
git push origin feature/your-feature-name
```

Then open a Pull Request on GitHub with a clear description of changes.

## Pull Request Guidelines

### PR Description Should Include:

- Clear description of changes
- Motivation and context
- Type of change (feature, fix, documentation, etc.)
- Related issues (e.g., "Closes #123")
- Testing performed
- Screenshots (if UI changes)

### PR Checklist:

- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests added/updated
- [ ] Tests pass locally
- [ ] Changes don't break existing functionality

## Development Guidelines

### Code Style

- Use meaningful variable and function names
- Maximum line length: 100 characters
- Use type hints where applicable
- Add docstrings to functions and classes

### Testing

- Add unit tests for new features
- Ensure all tests pass before submitting PR
- Test with different input variations
- Include edge cases

### Documentation

- Update README if adding features
- Add docstrings in Google format
- Include examples for new functionality
- Update API documentation if needed

## Areas for Contribution

### High Priority
- [ ] Performance optimizations for inference
- [ ] Additional medical image datasets
- [ ] Deployment scripts (Docker, AWS, GCP)
- [ ] Web API implementation
- [ ] Real-time prediction interface

### Medium Priority
- [ ] Extended documentation
- [ ] Additional evaluation metrics
- [ ] Visualization improvements
- [ ] Configuration file support
- [ ] Batch processing capabilities

### Nice to Have
- [ ] GUI for predictions
- [ ] Model explainability tools (Grad-CAM)
- [ ] Comparison with other methods
- [ ] Benchmark scripts
- [ ] Mobile app integration

## Reporting Issues

### Bug Reports

Include:
- Clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Python version, GPU)
- Error logs/traceback
- Minimal reproducible example

### Feature Requests

Include:
- Clear description of desired feature
- Use cases and motivation
- Possible implementation approach
- Any related research papers or references

## Review Process

1. Automated checks must pass
2. Code review by maintainers
3. Address requested changes
4. Final approval and merge

## Questions?

- Open an issue for discussions
- Email maintainers for specific questions
- Check existing issues before asking

## Recognition

Contributors will be acknowledged in:
- README contributors section
- Release notes
- GitHub contributors page

Thank you for contributing! 🎉
